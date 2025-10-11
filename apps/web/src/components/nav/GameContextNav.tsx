import React from 'react'
import { ActivePlayersList } from './ActivePlayersList'
import { AddPlayerButton } from './AddPlayerButton'
import { FullscreenPlayerSelection } from './FullscreenPlayerSelection'
import { GameModeIndicator } from './GameModeIndicator'
import { GameTitleMenu } from './GameTitleMenu'
import { NetworkPlayerIndicator } from './NetworkPlayerIndicator'
import { RoomInfo } from './RoomInfo'

type GameMode = 'none' | 'single' | 'battle' | 'tournament'

interface Player {
  id: string
  name: string
  emoji: string
}

interface NetworkPlayer {
  id: string
  emoji?: string
  name?: string
}

interface ArcadeRoomInfo {
  roomName?: string
  gameName: string
  playerCount: number
  joinCode?: string
}

interface GameContextNavProps {
  navTitle: string
  navEmoji?: string
  gameMode: GameMode
  activePlayers: Player[]
  inactivePlayers: Player[]
  shouldEmphasize: boolean
  showFullscreenSelection: boolean
  onAddPlayer: (playerId: string) => void
  onRemovePlayer: (playerId: string) => void
  onConfigurePlayer: (playerId: string) => void
  onExitSession?: () => void
  onSetup?: () => void
  onNewGame?: () => void
  canModifyPlayers?: boolean
  // Arcade session info
  networkPlayers?: NetworkPlayer[]
  roomInfo?: ArcadeRoomInfo
}

export function GameContextNav({
  navTitle,
  navEmoji,
  gameMode,
  activePlayers,
  inactivePlayers,
  shouldEmphasize,
  showFullscreenSelection,
  onAddPlayer,
  onRemovePlayer,
  onConfigurePlayer,
  onExitSession,
  onSetup,
  onNewGame,
  canModifyPlayers = true,
  networkPlayers = [],
  roomInfo,
}: GameContextNavProps) {
  // 2x2 grid layout for normal mode, column for fullscreen
  if (showFullscreenSelection) {
    return (
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: '16px',
          width: '100%',
        }}
      >
        <h1
          style={{
            fontSize: '32px',
            fontWeight: 'bold',
            background: 'linear-gradient(135deg, #60a5fa, #a78bfa, #f472b6)',
            backgroundClip: 'text',
            color: 'transparent',
            margin: 0,
            transition: 'font-size 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
          }}
        >
          {navEmoji && `${navEmoji} `}
          {navTitle}
        </h1>

        <GameModeIndicator
          gameMode={gameMode}
          shouldEmphasize={shouldEmphasize}
          showFullscreenSelection={showFullscreenSelection}
        />

        <FullscreenPlayerSelection
          inactivePlayers={inactivePlayers}
          onSelectPlayer={onAddPlayer}
          onConfigurePlayer={onConfigurePlayer}
          isVisible={showFullscreenSelection}
        />

        <style
          dangerouslySetInnerHTML={{
            __html: `
          @keyframes fadeIn {
            from {
              opacity: 0;
              transform: translateY(-10px);
            }
            to {
              opacity: 1;
              transform: translateY(0);
            }
          }
          @keyframes expandIn {
            from {
              opacity: 0;
              transform: scaleY(0.8);
            }
            to {
              opacity: 1;
              transform: scaleY(1);
            }
          }
        `,
          }}
        />
      </div>
    )
  }

  // Normal layout: Left side | Right side (players spanning full height)
  return (
    <div
      style={{
        display: 'flex',
        gap: '20px',
        alignItems: 'center',
        width: 'auto',
      }}
    >
      {/* Left side: Title/room info and mode */}
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '12px',
          flex: 1,
        }}
      >
        {/* Show room info pane (with unified dropdown) if in room, otherwise show title menu + mode indicator */}
        {roomInfo ? (
          <RoomInfo
            roomName={roomInfo.roomName}
            gameName={roomInfo.gameName}
            playerCount={roomInfo.playerCount}
            joinCode={roomInfo.joinCode}
            shouldEmphasize={shouldEmphasize}
            gameMode={gameMode}
            modeColor={
              gameMode === 'battle' ? '#8b5cf6' :
              gameMode === 'single' ? '#3b82f6' :
              gameMode === 'tournament' ? '#f59e0b' :
              '#6b7280'
            }
            modeEmoji={
              gameMode === 'battle' ? '⚔️' :
              gameMode === 'single' ? '🎯' :
              gameMode === 'tournament' ? '🏆' :
              '👥'
            }
            modeLabel={
              gameMode === 'battle' ? 'Battle' :
              gameMode === 'single' ? 'Solo' :
              gameMode === 'tournament' ? 'Tournament' :
              'Select Players'
            }
            navTitle={navTitle}
            navEmoji={navEmoji}
            onSetup={onSetup}
            onNewGame={onNewGame}
            onQuit={onExitSession}
          />
        ) : (
          <>
            <GameTitleMenu
              navTitle={navTitle}
              navEmoji={navEmoji}
              onSetup={onSetup}
              onNewGame={onNewGame}
              onQuit={onExitSession}
              showMenu={!canModifyPlayers}
            />
            <div style={{ marginLeft: 'auto' }}>
              <GameModeIndicator gameMode={gameMode} shouldEmphasize={shouldEmphasize} showFullscreenSelection={false} />
            </div>
          </>
        )}
      </div>

      {/* Right side: Players spanning full height */}
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: shouldEmphasize ? '16px' : '12px',
        }}
      >
        {/* Network Players */}
        {networkPlayers.length > 0 && (
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '6px 12px',
              background: 'linear-gradient(135deg, rgba(59, 130, 246, 0.12), rgba(147, 51, 234, 0.12))',
              borderRadius: '12px',
              border: '2px solid rgba(147, 51, 234, 0.25)',
              boxShadow: '0 4px 12px rgba(59, 130, 246, 0.15)',
            }}
          >
            {networkPlayers.map((player) => (
              <NetworkPlayerIndicator key={player.id} player={player} shouldEmphasize={shouldEmphasize} />
            ))}
          </div>
        )}

        {/* Active Players + Add Button */}
        {(activePlayers.length > 0 || (shouldEmphasize && inactivePlayers.length > 0 && canModifyPlayers)) && (
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: shouldEmphasize ? '12px' : '8px',
              padding: shouldEmphasize ? '12px 20px' : '6px 12px',
              background: shouldEmphasize
                ? 'linear-gradient(135deg, rgba(255, 255, 255, 0.18), rgba(255, 255, 255, 0.10))'
                : 'linear-gradient(135deg, rgba(255, 255, 255, 0.10), rgba(255, 255, 255, 0.05))',
              borderRadius: shouldEmphasize ? '16px' : '12px',
              border: shouldEmphasize ? '3px solid rgba(255, 255, 255, 0.3)' : '2px solid rgba(255, 255, 255, 0.15)',
              boxShadow: shouldEmphasize
                ? '0 8px 24px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255,255,255,0.3)'
                : '0 4px 12px rgba(0, 0, 0, 0.1)',
              transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
              transform: shouldEmphasize ? 'scale(1.05)' : 'scale(1)',
              opacity: canModifyPlayers ? 1 : 0.6,
              pointerEvents: canModifyPlayers ? 'auto' : 'none',
            }}
          >
            <ActivePlayersList
              activePlayers={activePlayers}
              shouldEmphasize={shouldEmphasize}
              onRemovePlayer={onRemovePlayer}
              onConfigurePlayer={onConfigurePlayer}
            />

            {canModifyPlayers && (
              <AddPlayerButton
                inactivePlayers={inactivePlayers}
                shouldEmphasize={shouldEmphasize}
                onAddPlayer={onAddPlayer}
              />
            )}
          </div>
        )}
      </div>

      <style
        dangerouslySetInnerHTML={{
          __html: `
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(-10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        @keyframes expandIn {
          from {
            opacity: 0;
            transform: scaleY(0.8);
          }
          to {
            opacity: 1;
            transform: scaleY(1);
          }
        }
      `,
        }}
      />
    </div>
  )
}
