import { useMemo } from 'react'
import { useSpring, useSprings } from '@react-spring/web'
import type { RailroadTrackGenerator } from '../lib/RailroadTrackGenerator'

interface TrainTransform {
  x: number
  y: number
  rotation: number
}

interface TrainCarTransform extends TrainTransform {
  position: number
  opacity: number
}

interface UseTrainTransformsParams {
  trainPosition: number
  trackGenerator: RailroadTrackGenerator
  pathRef: React.RefObject<SVGPathElement>
  maxCars: number
  carSpacing: number
}

export function useTrainTransforms({
  trainPosition,
  trackGenerator,
  pathRef,
  maxCars,
  carSpacing,
}: UseTrainTransformsParams) {
  // Calculate target locomotive transform
  const locomotiveTarget = useMemo<TrainTransform>(() => {
    if (!pathRef.current) {
      return { x: 50, y: 300, rotation: 0 }
    }
    return trackGenerator.getTrainTransform(pathRef.current, trainPosition)
  }, [trainPosition, trackGenerator, pathRef])

  // Animated spring for smooth locomotive movement
  const trainTransform = useSpring({
    x: locomotiveTarget.x,
    y: locomotiveTarget.y,
    rotation: locomotiveTarget.rotation,
    config: { tension: 600, friction: 35 }, // Fast/responsive to avoid lag
  })

  // Calculate target transforms for train cars (each car follows behind the locomotive)
  const carTargets = useMemo((): TrainCarTransform[] => {
    if (!pathRef.current) {
      return Array.from({ length: maxCars }, () => ({
        x: 0,
        y: 0,
        rotation: 0,
        position: 0,
        opacity: 0,
      }))
    }

    return Array.from({ length: maxCars }).map((_, carIndex) => {
      // Calculate position for this car (behind the locomotive)
      const carPosition = Math.max(0, trainPosition - (carIndex + 1) * carSpacing)

      // Calculate opacity: fade in at left tunnel (3-8%), fade out at right tunnel (92-97%)
      const fadeInStart = 3
      const fadeInEnd = 8
      const fadeOutStart = 92
      const fadeOutEnd = 97

      let opacity = 1 // Default to fully visible

      // Fade in from left tunnel
      if (carPosition <= fadeInStart) {
        opacity = 0
      } else if (carPosition < fadeInEnd) {
        opacity = (carPosition - fadeInStart) / (fadeInEnd - fadeInStart)
      }
      // Fade out into right tunnel
      else if (carPosition >= fadeOutEnd) {
        opacity = 0
      } else if (carPosition > fadeOutStart) {
        opacity = 1 - (carPosition - fadeOutStart) / (fadeOutEnd - fadeOutStart)
      }

      return {
        ...trackGenerator.getTrainTransform(pathRef.current!, carPosition),
        position: carPosition,
        opacity,
      }
    })
  }, [trainPosition, trackGenerator, pathRef, maxCars, carSpacing])

  // Animated springs for smooth car movement
  const trainCars = useSprings(
    carTargets.length,
    carTargets.map((target) => ({
      x: target.x,
      y: target.y,
      rotation: target.rotation,
      opacity: target.opacity,
      position: target.position,
      config: { tension: 600, friction: 35 }, // Fast/responsive to avoid lag
    }))
  )

  // Calculate target locomotive opacity (fade in/out through tunnels)
  const locomotiveOpacityTarget = useMemo(() => {
    const fadeInStart = 3
    const fadeInEnd = 8
    const fadeOutStart = 92
    const fadeOutEnd = 97

    // Fade in from left tunnel
    if (trainPosition <= fadeInStart) {
      return 0
    } else if (trainPosition < fadeInEnd) {
      return (trainPosition - fadeInStart) / (fadeInEnd - fadeInStart)
    }
    // Fade out into right tunnel
    else if (trainPosition >= fadeOutEnd) {
      return 0
    } else if (trainPosition > fadeOutStart) {
      return 1 - (trainPosition - fadeOutStart) / (fadeOutEnd - fadeOutStart)
    }

    return 1 // Default to fully visible
  }, [trainPosition])

  // Animated spring for smooth locomotive opacity
  const locomotiveOpacity = useSpring({
    opacity: locomotiveOpacityTarget,
    config: { tension: 600, friction: 35 }, // Fast/responsive to avoid lag
  })

  return {
    trainTransform,
    trainCars,
    locomotiveOpacity: locomotiveOpacity.opacity,
  }
}
