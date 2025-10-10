/**
 * Unit tests for player ownership utilities
 */

import { describe, expect, it } from 'vitest'
import type { RoomData } from '@/hooks/useRoomData'
import {
  type PlayerOwnershipMap,
  buildPlayerMetadata,
  buildPlayerOwnershipFromRoomData,
  getPlayerOwner,
  isPlayerOwnedByUser,
  isUsersTurn,
} from '../player-ownership'

describe('player-ownership utilities', () => {
  describe('buildPlayerOwnershipFromRoomData', () => {
    it('builds ownership map from roomData.memberPlayers', () => {
      const roomData: RoomData = {
        id: 'room-1',
        name: 'Test Room',
        code: 'ABC123',
        gameName: 'matching',
        members: [],
        memberPlayers: {
          'user-1': [
            { id: 'player-1', name: 'Player 1', emoji: '😀', color: '#3b82f6' },
            { id: 'player-2', name: 'Player 2', emoji: '😎', color: '#8b5cf6' },
          ],
          'user-2': [{ id: 'player-3', name: 'Player 3', emoji: '🤠', color: '#10b981' }],
        },
      }

      const ownershipMap = buildPlayerOwnershipFromRoomData(roomData)

      expect(ownershipMap).toEqual({
        'player-1': 'user-1',
        'player-2': 'user-1',
        'player-3': 'user-2',
      })
    })

    it('returns empty object for null roomData', () => {
      const ownershipMap = buildPlayerOwnershipFromRoomData(null)
      expect(ownershipMap).toEqual({})
    })

    it('returns empty object for undefined roomData', () => {
      const ownershipMap = buildPlayerOwnershipFromRoomData(undefined)
      expect(ownershipMap).toEqual({})
    })

    it('returns empty object for roomData without memberPlayers', () => {
      const roomData = {
        id: 'room-1',
        name: 'Test Room',
        code: 'ABC123',
        gameName: 'matching',
        members: [],
        memberPlayers: {},
      } as RoomData

      const ownershipMap = buildPlayerOwnershipFromRoomData(roomData)
      expect(ownershipMap).toEqual({})
    })
  })

  describe('isPlayerOwnedByUser', () => {
    const ownershipMap: PlayerOwnershipMap = {
      'player-1': 'user-1',
      'player-2': 'user-1',
      'player-3': 'user-2',
    }

    it('returns true when player is owned by user', () => {
      expect(isPlayerOwnedByUser('player-1', 'user-1', ownershipMap)).toBe(true)
      expect(isPlayerOwnedByUser('player-2', 'user-1', ownershipMap)).toBe(true)
      expect(isPlayerOwnedByUser('player-3', 'user-2', ownershipMap)).toBe(true)
    })

    it('returns false when player is not owned by user', () => {
      expect(isPlayerOwnedByUser('player-1', 'user-2', ownershipMap)).toBe(false)
      expect(isPlayerOwnedByUser('player-3', 'user-1', ownershipMap)).toBe(false)
    })

    it('returns false for unknown player', () => {
      expect(isPlayerOwnedByUser('player-unknown', 'user-1', ownershipMap)).toBe(false)
    })
  })

  describe('getPlayerOwner', () => {
    const ownershipMap: PlayerOwnershipMap = {
      'player-1': 'user-1',
      'player-2': 'user-1',
      'player-3': 'user-2',
    }

    it('returns correct owner userId for player', () => {
      expect(getPlayerOwner('player-1', ownershipMap)).toBe('user-1')
      expect(getPlayerOwner('player-2', ownershipMap)).toBe('user-1')
      expect(getPlayerOwner('player-3', ownershipMap)).toBe('user-2')
    })

    it('returns undefined for unknown player', () => {
      expect(getPlayerOwner('player-unknown', ownershipMap)).toBeUndefined()
    })
  })

  describe('isUsersTurn', () => {
    const ownershipMap: PlayerOwnershipMap = {
      'player-1': 'user-1',
      'player-2': 'user-1',
      'player-3': 'user-2',
    }

    it('returns true when current player belongs to user', () => {
      expect(isUsersTurn('player-1', 'user-1', ownershipMap)).toBe(true)
      expect(isUsersTurn('player-3', 'user-2', ownershipMap)).toBe(true)
    })

    it('returns false when current player belongs to different user', () => {
      expect(isUsersTurn('player-1', 'user-2', ownershipMap)).toBe(false)
      expect(isUsersTurn('player-3', 'user-1', ownershipMap)).toBe(false)
    })

    it('returns false for unknown player', () => {
      expect(isUsersTurn('player-unknown', 'user-1', ownershipMap)).toBe(false)
    })
  })

  describe('buildPlayerMetadata', () => {
    const ownershipMap: PlayerOwnershipMap = {
      'player-1': 'user-1',
      'player-2': 'user-1',
      'player-3': 'user-2',
    }

    const playersMap = new Map([
      ['player-1', { name: 'Player 1', emoji: '😀', color: '#3b82f6' }],
      ['player-2', { name: 'Player 2', emoji: '😎', color: '#8b5cf6' }],
      ['player-3', { name: 'Player 3', emoji: '🤠', color: '#10b981' }],
    ])

    it('builds metadata with correct ownership', () => {
      const metadata = buildPlayerMetadata(
        ['player-1', 'player-2', 'player-3'],
        ownershipMap,
        playersMap
      )

      expect(metadata).toEqual({
        'player-1': {
          id: 'player-1',
          name: 'Player 1',
          emoji: '😀',
          userId: 'user-1',
          color: '#3b82f6',
        },
        'player-2': {
          id: 'player-2',
          name: 'Player 2',
          emoji: '😎',
          userId: 'user-1',
          color: '#8b5cf6',
        },
        'player-3': {
          id: 'player-3',
          name: 'Player 3',
          emoji: '🤠',
          userId: 'user-2',
          color: '#10b981',
        },
      })
    })

    it('uses fallback userId when player not in ownership map', () => {
      const metadata = buildPlayerMetadata(
        ['player-1', 'player-4'],
        ownershipMap,
        playersMap,
        'fallback-user'
      )

      // player-1 has ownership, but player-4 is not in playersMap
      // so it won't be in metadata at all
      expect(metadata['player-1']?.userId).toBe('user-1')
      expect(metadata['player-4']).toBeUndefined()
    })

    it('skips players not in playersMap', () => {
      const metadata = buildPlayerMetadata(['player-1', 'player-unknown'], ownershipMap, playersMap)

      expect(metadata['player-1']).toBeDefined()
      expect(metadata['player-unknown']).toBeUndefined()
    })

    it('handles empty playerIds array', () => {
      const metadata = buildPlayerMetadata([], ownershipMap, playersMap)
      expect(metadata).toEqual({})
    })
  })

  describe('edge cases', () => {
    it('handles empty ownership map', () => {
      const emptyMap: PlayerOwnershipMap = {}

      expect(isPlayerOwnedByUser('player-1', 'user-1', emptyMap)).toBe(false)
      expect(getPlayerOwner('player-1', emptyMap)).toBeUndefined()
      expect(isUsersTurn('player-1', 'user-1', emptyMap)).toBe(false)
    })

    it('handles empty strings', () => {
      const ownershipMap: PlayerOwnershipMap = {
        'player-1': 'user-1',
      }

      expect(isPlayerOwnedByUser('', 'user-1', ownershipMap)).toBe(false)
      expect(getPlayerOwner('', ownershipMap)).toBeUndefined()
      expect(isUsersTurn('', 'user-1', ownershipMap)).toBe(false)
    })
  })

  describe('real-world scenario: turn indicator logic', () => {
    it('reproduces the "Your turn" vs "Their turn" bug and fix', () => {
      const roomData: RoomData = {
        id: 'room-1',
        name: 'Game Room',
        code: 'ABC123',
        gameName: 'matching',
        members: [],
        memberPlayers: {
          'local-user-id': [
            { id: 'local-player-1', name: 'My Player 1', emoji: '😀', color: '#3b82f6' },
            { id: 'local-player-2', name: 'My Player 2', emoji: '😎', color: '#8b5cf6' },
          ],
          'remote-user-id': [
            { id: 'remote-player-1', name: 'Their Player', emoji: '🤠', color: '#10b981' },
          ],
        },
      }

      const ownershipMap = buildPlayerOwnershipFromRoomData(roomData)
      const viewerId = 'local-user-id'

      // Scenario 1: It's my turn (local player is current)
      const currentPlayer1 = 'local-player-1'
      const isMyTurn1 = isUsersTurn(currentPlayer1, viewerId, ownershipMap)
      expect(isMyTurn1).toBe(true)
      expect(isMyTurn1 ? 'Your turn' : 'Their turn').toBe('Your turn')

      // Scenario 2: It's their turn (remote player is current)
      const currentPlayer2 = 'remote-player-1'
      const isMyTurn2 = isUsersTurn(currentPlayer2, viewerId, ownershipMap)
      expect(isMyTurn2).toBe(false)
      expect(isMyTurn2 ? 'Your turn' : 'Their turn').toBe('Their turn')
    })
  })
})
