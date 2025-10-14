import { eq } from 'drizzle-orm'
import { type NextRequest, NextResponse } from 'next/server'
import { db, schema } from '@/db'
import { getRoomMembers } from '@/lib/arcade/room-membership'
import { getViewerId } from '@/lib/viewer'
import { getSocketIO } from '@/lib/socket-io'

type RouteContext = {
  params: Promise<{ roomId: string }>
}

/**
 * POST /api/arcade/rooms/:roomId/transfer-ownership
 * Transfer room ownership to another member (host only)
 * Body:
 *   - newOwnerId: string
 */
export async function POST(req: NextRequest, context: RouteContext) {
  try {
    const { roomId } = await context.params
    const viewerId = await getViewerId()
    const body = await req.json()

    // Validate required fields
    if (!body.newOwnerId) {
      return NextResponse.json({ error: 'Missing required field: newOwnerId' }, { status: 400 })
    }

    // Check if user is the current host
    const members = await getRoomMembers(roomId)
    const currentMember = members.find((m) => m.userId === viewerId)

    if (!currentMember) {
      return NextResponse.json({ error: 'You are not in this room' }, { status: 403 })
    }

    if (!currentMember.isCreator) {
      return NextResponse.json(
        { error: 'Only the current host can transfer ownership' },
        { status: 403 }
      )
    }

    // Can't transfer to yourself
    if (body.newOwnerId === viewerId) {
      return NextResponse.json({ error: 'You are already the owner' }, { status: 400 })
    }

    // Verify new owner is in the room
    const newOwner = members.find((m) => m.userId === body.newOwnerId)
    if (!newOwner) {
      return NextResponse.json({ error: 'New owner must be a member of the room' }, { status: 404 })
    }

    // Remove isCreator from current owner
    await db
      .update(schema.roomMembers)
      .set({ isCreator: false })
      .where(eq(schema.roomMembers.id, currentMember.id))

    // Set isCreator on new owner
    await db
      .update(schema.roomMembers)
      .set({ isCreator: true })
      .where(eq(schema.roomMembers.id, newOwner.id))

    // Update room createdBy field
    await db
      .update(schema.arcadeRooms)
      .set({
        createdBy: body.newOwnerId,
        creatorName: newOwner.displayName,
      })
      .where(eq(schema.arcadeRooms.id, roomId))

    // Broadcast ownership transfer via socket
    const io = await getSocketIO()
    if (io) {
      try {
        const updatedMembers = await getRoomMembers(roomId)

        io.to(`room:${roomId}`).emit('ownership-transferred', {
          roomId,
          oldOwnerId: viewerId,
          newOwnerId: body.newOwnerId,
          newOwnerName: newOwner.displayName,
          members: updatedMembers,
        })

        console.log(
          `[Ownership Transfer] Room ${roomId} ownership transferred from ${viewerId} to ${body.newOwnerId}`
        )
      } catch (socketError) {
        console.error('[Ownership Transfer] Failed to broadcast transfer:', socketError)
      }
    }

    return NextResponse.json({ success: true }, { status: 200 })
  } catch (error: any) {
    console.error('Failed to transfer ownership:', error)
    return NextResponse.json({ error: 'Failed to transfer ownership' }, { status: 500 })
  }
}
