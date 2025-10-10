/**
 * Player Ownership Utilities
 *
 * Centralized module for determining player ownership across the codebase.
 * Provides consistent utilities for both server-side (DB-based) and client-side
 * (RoomData-based) player ownership checking.
 *
 * This module solves the problem of scattered player ownership logic that
 * previously existed in 4+ locations with different implementations.
 */

import { eq } from 'drizzle-orm'
import { db, schema } from '@/db'
import type { RoomData } from '@/hooks/useRoomData'

/**
 * Player ownership mapping: playerId -> userId
 *
 * This is the canonical representation of player ownership used throughout
 * the application. Both server-side and client-side utilities return this type.
 */
export type PlayerOwnershipMap = Record<string, string>

/**
 * Player metadata with ownership information
 *
 * Used when building player metadata for game state that needs to be
 * shared across room members.
 */
export interface PlayerMetadata {
  id: string
  name: string
  emoji: string
  userId: string // Owner's user ID
  color: string
}

/**
 * SERVER-SIDE: Build player ownership map from database
 *
 * Queries the database to get all players and their owner userIds.
 * Used by session-manager and validators for authorization checks.
 *
 * @param roomId - Optional room ID to filter players (currently unused, fetches all)
 * @returns Promise resolving to playerOwnership map
 *
 * @example
 * const ownership = await buildPlayerOwnershipMap()
 * // { "player-uuid-1": "user-uuid-1", "player-uuid-2": "user-uuid-2" }
 */
export async function buildPlayerOwnershipMap(roomId?: string): Promise<PlayerOwnershipMap> {
  // Fetch all players with their userId ownership
  const players = await db.query.players.findMany({
    columns: {
      id: true,
      userId: true,
    },
  })

  // Convert to ownership map: playerId -> userId
  return Object.fromEntries(players.map((p) => [p.id, p.userId]))
}

/**
 * CLIENT-SIDE: Build player ownership map from RoomData
 *
 * Constructs ownership map from the memberPlayers structure in RoomData.
 * Used by React components and providers for client-side ownership checks.
 *
 * @param roomData - Room data containing memberPlayers mapping
 * @returns PlayerOwnershipMap
 *
 * @example
 * const ownership = buildPlayerOwnershipFromRoomData(roomData)
 * // { "player-uuid-1": "user-uuid-1", "player-uuid-2": "user-uuid-2" }
 */
export function buildPlayerOwnershipFromRoomData(
  roomData: RoomData | null | undefined
): PlayerOwnershipMap {
  if (!roomData?.memberPlayers) {
    return {}
  }

  const ownershipMap: PlayerOwnershipMap = {}

  // memberPlayers is Record<userId, RoomPlayer[]>
  // We need to invert it to Record<playerId, userId>
  for (const [userId, userPlayers] of Object.entries(roomData.memberPlayers)) {
    for (const player of userPlayers) {
      ownershipMap[player.id] = userId
    }
  }

  return ownershipMap
}

/**
 * Check if a player is owned by a specific user
 *
 * @param playerId - The player ID to check
 * @param userId - The user ID to check ownership against
 * @param ownershipMap - Player ownership mapping
 * @returns true if the player belongs to the user
 *
 * @example
 * const isOwned = isPlayerOwnedByUser(playerId, currentUserId, ownershipMap)
 * if (!isOwned) {
 *   return { valid: false, error: 'Not your player' }
 * }
 */
export function isPlayerOwnedByUser(
  playerId: string,
  userId: string,
  ownershipMap: PlayerOwnershipMap
): boolean {
  return ownershipMap[playerId] === userId
}

/**
 * Get the owner userId for a player
 *
 * @param playerId - The player ID to look up
 * @param ownershipMap - Player ownership mapping
 * @returns The owner's userId, or undefined if not found
 *
 * @example
 * const owner = getPlayerOwner(playerId, ownershipMap)
 * if (owner !== currentUserId) {
 *   console.log('This player belongs to another user')
 * }
 */
export function getPlayerOwner(
  playerId: string,
  ownershipMap: PlayerOwnershipMap
): string | undefined {
  return ownershipMap[playerId]
}

/**
 * Build player metadata with correct ownership information
 *
 * Combines player data with ownership information to create complete
 * metadata objects. This is used when starting games or sending player
 * info across the network.
 *
 * @param playerIds - Array of player IDs to include
 * @param ownershipMap - Player ownership mapping
 * @param playersMap - Map of player ID to player data (from GameModeContext)
 * @param fallbackUserId - UserId to use if player not found in ownership map
 * @returns Record of playerId to PlayerMetadata
 *
 * @example
 * const metadata = buildPlayerMetadata(
 *   activePlayers,
 *   ownershipMap,
 *   players,
 *   viewerId
 * )
 * // Send metadata with game state
 */
export function buildPlayerMetadata(
  playerIds: string[],
  ownershipMap: PlayerOwnershipMap,
  playersMap: Map<string, { name: string; emoji: string; color: string }>,
  fallbackUserId?: string
): Record<string, PlayerMetadata> {
  const metadata: Record<string, PlayerMetadata> = {}

  for (const playerId of playerIds) {
    const playerData = playersMap.get(playerId)
    if (!playerData) continue

    // Get the actual owner userId from ownership map, or use fallback
    const ownerUserId = ownershipMap[playerId] || fallbackUserId || ''

    metadata[playerId] = {
      id: playerId,
      name: playerData.name,
      emoji: playerData.emoji,
      userId: ownerUserId,
      color: playerData.color,
    }
  }

  return metadata
}

/**
 * Check if it's a specific user's turn in a game
 *
 * Convenience function that combines current player check with ownership check.
 *
 * @param currentPlayerId - The ID of the player whose turn it is
 * @param userId - The user ID to check
 * @param ownershipMap - Player ownership mapping
 * @returns true if it's this user's turn
 *
 * @example
 * const isMyTurn = isUsersTurn(state.currentPlayer, viewerId, ownershipMap)
 * const label = isMyTurn ? 'Your turn' : 'Their turn'
 */
export function isUsersTurn(
  currentPlayerId: string,
  userId: string,
  ownershipMap: PlayerOwnershipMap
): boolean {
  return isPlayerOwnedByUser(currentPlayerId, userId, ownershipMap)
}

/**
 * SERVER-SIDE: Convert guestId to internal userId
 *
 * Helper to convert the guestId (from cookies) to the internal database userId.
 * This is needed because the database uses internal user.id as foreign keys.
 *
 * @param guestId - The guest ID from the cookie
 * @returns The internal user ID, or undefined if not found
 */
export async function getUserIdFromGuestId(guestId: string): Promise<string | undefined> {
  const user = await db.query.users.findFirst({
    where: eq(schema.users.guestId, guestId),
    columns: { id: true },
  })
  return user?.id
}
