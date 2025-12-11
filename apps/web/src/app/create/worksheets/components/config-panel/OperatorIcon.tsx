import { css } from '@styled/css'

export interface OperatorIconProps {
  operator: 'addition' | 'subtraction' | 'mixed' | 'fractions'
  size?: 'sm' | 'md' | 'lg' | 'xl'
  isDark?: boolean
  color?: 'gray' | 'green'
  className?: string
}

const sizeMap = {
  sm: '2xs',
  md: 'xs',
  lg: 'sm',
  xl: 'xl',
} as const

function getOperatorSymbol(operator: 'addition' | 'subtraction' | 'mixed' | 'fractions'): string {
  if (operator === 'fractions') return '⅟'
  if (operator === 'mixed') return '±'
  if (operator === 'subtraction') return '−'
  return '+'
}

export function OperatorIcon({
  operator,
  size = 'xl',
  isDark = false,
  color = 'gray',
  className,
}: OperatorIconProps) {
  const colorValue =
    color === 'green' ? (isDark ? 'green.400' : 'green.600') : isDark ? 'gray.300' : 'gray.700'

  return (
    <span
      className={css(
        {
          fontSize: sizeMap[size],
          fontWeight: 'bold',
          color: colorValue,
          flexShrink: 0,
        },
        className
      )}
    >
      {getOperatorSymbol(operator)}
    </span>
  )
}
