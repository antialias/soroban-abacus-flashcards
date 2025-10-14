import { eq } from 'drizzle-orm'
import { type NextRequest, NextResponse } from 'next/server'
import { db, schema } from '@/db'
import { getRoomMembers } from '@/lib/arcade/room-membership'
import { denyJoinRequest } from '@/lib/arcade/room-join-requests'
import { getViewerId } from '@/lib/viewer'
import { getSocketIO } from '@/lib/socket-io'

type RouteContext = {
  params: Promise<{ roomId: string; requestId: string }>
}

/**
 * POST /api/arcade/rooms/:roomId/join-requests/:requestId/deny
 * Deny a join request (host only)
 */
export async function POST(req: NextRequest, context: RouteContext) {
  try {
    const { roomId, requestId } = await context.params
    const viewerId = await getViewerId()

    // Check if user is the host
    const members = await getRoomMembers(roomId)
    const currentMember = members.find((m) => m.userId === viewerId)

    if (!currentMember) {
      return NextResponse.json({ error: 'You are not in this room' }, { status: 403 })
    }

    if (!currentMember.isCreator) {
      return NextResponse.json({ error: 'Only the host can deny join requests' }, { status: 403 })
    }

    // Get the request
    const [request] = await db
      .select()
      .from(schema.roomJoinRequests)
      .where(eq(schema.roomJoinRequests.id, requestId))
      .limit(1)

    if (!request) {
      return NextResponse.json({ error: 'Join request not found' }, { status: 404 })
    }

    if (request.status !== 'pending') {
      return NextResponse.json({ error: 'Join request is not pending' }, { status: 400 })
    }

    // Deny the request
    const deniedRequest = await denyJoinRequest(requestId, viewerId, currentMember.displayName)

    // Notify the requesting user via socket
    const io = await getSocketIO()
    if (io) {
      try {
        io.to(`user:${request.userId}`).emit('join-request-denied', {
          roomId,
          requestId,
          deniedBy: currentMember.displayName,
        })

        console.log(
          `[Deny Join Request API] Request ${requestId} denied for user ${request.userId} to join room ${roomId}`
        )
      } catch (socketError) {
        console.error('[Deny Join Request API] Failed to broadcast denial:', socketError)
      }
    }

    return NextResponse.json({ request: deniedRequest }, { status: 200 })
  } catch (error: any) {
    console.error('Failed to deny join request:', error)
    return NextResponse.json({ error: 'Failed to deny join request' }, { status: 500 })
  }
}
