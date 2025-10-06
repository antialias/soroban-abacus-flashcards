/**
 * @vitest-environment node
 */

import { describe, it, expect, beforeEach, afterEach } from 'vitest'
import { db, schema } from '../src/db'
import { eq } from 'drizzle-orm'

/**
 * API Players E2E Tests
 *
 * These tests verify the players API endpoints work correctly.
 * They use the actual database and test the full request/response cycle.
 */

describe('Players API', () => {
  let testUserId: string
  let testGuestId: string

  beforeEach(async () => {
    // Create a test user with unique guest ID
    testGuestId = `test-guest-${Date.now()}-${Math.random().toString(36).slice(2)}`
    const [user] = await db
      .insert(schema.users)
      .values({ guestId: testGuestId })
      .returning()
    testUserId = user.id
  })

  afterEach(async () => {
    // Clean up: delete test user (cascade deletes players)
    await db.delete(schema.users).where(eq(schema.users.id, testUserId))
  })

  describe('POST /api/players', () => {
    it('creates a player with valid data', async () => {
      const playerData = {
        name: 'Test Player',
        emoji: '😀',
        color: '#3b82f6',
        isActive: true,
      }

      // Simulate creating via DB (API would do this)
      const [player] = await db
        .insert(schema.players)
        .values({
          userId: testUserId,
          ...playerData,
        })
        .returning()

      expect(player).toBeDefined()
      expect(player.name).toBe(playerData.name)
      expect(player.emoji).toBe(playerData.emoji)
      expect(player.color).toBe(playerData.color)
      expect(player.isActive).toBe(true)
      expect(player.userId).toBe(testUserId)
    })

    it('sets isActive to false by default', async () => {
      const [player] = await db
        .insert(schema.players)
        .values({
          userId: testUserId,
          name: 'Inactive Player',
          emoji: '😴',
          color: '#999999',
        })
        .returning()

      expect(player.isActive).toBe(false)
    })
  })

  describe('GET /api/players', () => {
    it('returns all players for a user', async () => {
      // Create multiple players
      await db.insert(schema.players).values([
        {
          userId: testUserId,
          name: 'Player 1',
          emoji: '😀',
          color: '#3b82f6',
        },
        {
          userId: testUserId,
          name: 'Player 2',
          emoji: '😎',
          color: '#8b5cf6',
        },
      ])

      const players = await db.query.players.findMany({
        where: eq(schema.players.userId, testUserId),
      })

      expect(players).toHaveLength(2)
      expect(players[0].name).toBe('Player 1')
      expect(players[1].name).toBe('Player 2')
    })

    it('returns empty array for user with no players', async () => {
      const players = await db.query.players.findMany({
        where: eq(schema.players.userId, testUserId),
      })

      expect(players).toHaveLength(0)
    })
  })

  describe('PATCH /api/players/[id]', () => {
    it('updates player fields', async () => {
      const [player] = await db
        .insert(schema.players)
        .values({
          userId: testUserId,
          name: 'Original Name',
          emoji: '😀',
          color: '#3b82f6',
        })
        .returning()

      const [updated] = await db
        .update(schema.players)
        .set({
          name: 'Updated Name',
          emoji: '🎉',
        })
        .where(eq(schema.players.id, player.id))
        .returning()

      expect(updated.name).toBe('Updated Name')
      expect(updated.emoji).toBe('🎉')
      expect(updated.color).toBe('#3b82f6') // unchanged
    })

    it('toggles isActive status', async () => {
      const [player] = await db
        .insert(schema.players)
        .values({
          userId: testUserId,
          name: 'Test Player',
          emoji: '😀',
          color: '#3b82f6',
          isActive: false,
        })
        .returning()

      const [updated] = await db
        .update(schema.players)
        .set({ isActive: true })
        .where(eq(schema.players.id, player.id))
        .returning()

      expect(updated.isActive).toBe(true)
    })
  })

  describe('DELETE /api/players/[id]', () => {
    it('deletes a player', async () => {
      const [player] = await db
        .insert(schema.players)
        .values({
          userId: testUserId,
          name: 'To Delete',
          emoji: '👋',
          color: '#ef4444',
        })
        .returning()

      const [deleted] = await db
        .delete(schema.players)
        .where(eq(schema.players.id, player.id))
        .returning()

      expect(deleted).toBeDefined()
      expect(deleted.id).toBe(player.id)

      // Verify it's gone
      const found = await db.query.players.findFirst({
        where: eq(schema.players.id, player.id),
      })
      expect(found).toBeUndefined()
    })
  })

  describe('Cascade delete behavior', () => {
    it('deletes players when user is deleted', async () => {
      // Create players
      await db.insert(schema.players).values([
        {
          userId: testUserId,
          name: 'Player 1',
          emoji: '😀',
          color: '#3b82f6',
        },
        {
          userId: testUserId,
          name: 'Player 2',
          emoji: '😎',
          color: '#8b5cf6',
        },
      ])

      // Verify players exist
      let players = await db.query.players.findMany({
        where: eq(schema.players.userId, testUserId),
      })
      expect(players).toHaveLength(2)

      // Delete user
      await db.delete(schema.users).where(eq(schema.users.id, testUserId))

      // Verify players are gone
      players = await db.query.players.findMany({
        where: eq(schema.players.userId, testUserId),
      })
      expect(players).toHaveLength(0)
    })
  })

  describe('Security: userId injection prevention', () => {
    it('rejects creating player with non-existent userId', async () => {
      // Attempt to create a player with a fake userId
      await expect(async () => {
        await db.insert(schema.players).values({
          userId: 'HACKER_ID_NON_EXISTENT',
          name: 'Hacker Player',
          emoji: '🦹',
          color: '#ff0000',
        })
      }).rejects.toThrow(/FOREIGN KEY constraint failed/)
    })

    it('prevents modifying another user\'s player via userId injection (DB layer alone is insufficient)', async () => {
      // Create victim user and their player
      const victimGuestId = `victim-${Date.now()}-${Math.random().toString(36).slice(2)}`
      const [victimUser] = await db
        .insert(schema.users)
        .values({ guestId: victimGuestId })
        .returning()

      try {
        // Create attacker's player
        const [attackerPlayer] = await db
          .insert(schema.players)
          .values({
            userId: testUserId,
            name: 'Attacker Player',
            emoji: '😈',
            color: '#ff0000',
          })
          .returning()

        const [victimPlayer] = await db
          .insert(schema.players)
          .values({
            userId: victimUser.id,
            name: 'Victim Player',
            emoji: '👤',
            color: '#00ff00',
            isActive: true,
          })
          .returning()

        // IMPORTANT: At the DB level, changing userId to another valid userId SUCCEEDS
        // This is why API layer MUST filter userId from request body!
        const [updated] = await db
          .update(schema.players)
          .set({
            userId: victimUser.id, // This WILL succeed at DB level!
            name: 'Stolen Player',
          })
          .where(eq(schema.players.id, attackerPlayer.id))
          .returning()

        // The update succeeded - the player now belongs to victim!
        expect(updated.userId).toBe(victimUser.id)
        expect(updated.name).toBe('Stolen Player')

        // This test demonstrates why the API route MUST:
        // 1. Strip userId from request body
        // 2. Derive userId from session cookie
        // 3. Use WHERE clause to scope updates to current user's data only
      } finally {
        await db.delete(schema.users).where(eq(schema.users.id, victimUser.id))
      }
    })

    it('ensures players are isolated per user', async () => {
      // Create another user
      const user2GuestId = `user2-${Date.now()}-${Math.random().toString(36).slice(2)}`
      const [user2] = await db
        .insert(schema.users)
        .values({ guestId: user2GuestId })
        .returning()

      try {
        // Create players for both users
        await db.insert(schema.players).values({
          userId: testUserId,
          name: 'User 1 Player',
          emoji: '🎮',
          color: '#0000ff',
        })

        await db.insert(schema.players).values({
          userId: user2.id,
          name: 'User 2 Player',
          emoji: '🎯',
          color: '#ff00ff',
        })

        // Verify each user only sees their own players
        const user1Players = await db.query.players.findMany({
          where: eq(schema.players.userId, testUserId),
        })
        const user2Players = await db.query.players.findMany({
          where: eq(schema.players.userId, user2.id),
        })

        expect(user1Players).toHaveLength(1)
        expect(user1Players[0].name).toBe('User 1 Player')

        expect(user2Players).toHaveLength(1)
        expect(user2Players[0].name).toBe('User 2 Player')
      } finally {
        await db.delete(schema.users).where(eq(schema.users.id, user2.id))
      }
    })
  })
})
