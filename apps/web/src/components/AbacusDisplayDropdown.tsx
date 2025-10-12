'use client'

import * as DropdownMenu from '@radix-ui/react-dropdown-menu'
import * as Label from '@radix-ui/react-label'
import * as RadioGroup from '@radix-ui/react-radio-group'
import * as Switch from '@radix-ui/react-switch'
import { type BeadShape, type ColorScheme, useAbacusDisplay } from '@soroban/abacus-react'
import { useState } from 'react'
import { css } from '../../styled-system/css'
import { hstack, stack } from '../../styled-system/patterns'

interface AbacusDisplayDropdownProps {
  isFullscreen?: boolean
}

export function AbacusDisplayDropdown({ isFullscreen = false }: AbacusDisplayDropdownProps) {
  const [open, setOpen] = useState(false)
  const { config, updateConfig, resetToDefaults } = useAbacusDisplay()

  const handleOpenChange = (isOpen: boolean) => {
    console.log('Dropdown open change:', isOpen)
    setOpen(isOpen)
  }

  return (
    <DropdownMenu.Root open={open} onOpenChange={handleOpenChange}>
      <DropdownMenu.Trigger asChild>
        <button
          onClick={(e) => e.stopPropagation()} // Prevent parent dropdown from closing
          className={css({
            display: 'flex',
            alignItems: 'center',
            gap: '2',
            px: '3',
            py: '2',
            fontSize: 'sm',
            fontWeight: 'medium',
            color: isFullscreen ? 'white' : 'gray.600',
            bg: isFullscreen ? 'rgba(0, 0, 0, 0.85)' : 'white',
            border: '1px solid',
            borderColor: isFullscreen ? 'rgba(255, 255, 255, 0.1)' : 'gray.200',
            rounded: 'lg',
            shadow: 'lg',
            backdropFilter: isFullscreen ? 'blur(15px)' : 'none',
            transition: 'all',
            cursor: 'pointer',
            _hover: {
              bg: isFullscreen ? 'rgba(0, 0, 0, 0.9)' : 'gray.50',
              borderColor: isFullscreen ? 'rgba(255, 255, 255, 0.2)' : 'gray.300',
            },
            _focus: {
              outline: 'none',
              ring: '2px',
              ringColor: isFullscreen ? 'blue.400' : 'brand.500',
              ringOffset: '1px',
            },
          })}
        >
          <span className={css({ fontSize: 'lg' })}>🧮</span>
          <span>Style</span>
          <svg
            className={css({
              w: '4',
              h: '4',
              transition: 'transform',
              transform: open ? 'rotate(180deg)' : 'rotate(0deg)',
            })}
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>
      </DropdownMenu.Trigger>

      <DropdownMenu.Portal>
        <DropdownMenu.Content
          onClick={(e) => e.stopPropagation()} // Prevent clicks inside from closing parent
          className={css({
            bg: isFullscreen ? 'rgba(0, 0, 0, 0.85)' : 'white',
            rounded: 'xl',
            shadow: 'lg',
            border: '1px solid',
            borderColor: isFullscreen ? 'rgba(255, 255, 255, 0.1)' : 'gray.200',
            backdropFilter: isFullscreen ? 'blur(15px)' : 'none',
            p: '6',
            minW: '320px',
            maxW: '400px',
            maxH: '80vh',
            overflowY: 'auto',
            position: 'relative',
            zIndex: 50,
          })}
          sideOffset={8}
          align="end"
        >
          <div className={stack({ gap: '6' })}>
            {/* Header */}
            <div className={stack({ gap: '1' })}>
              <div
                className={hstack({
                  justify: 'space-between',
                  alignItems: 'center',
                })}
              >
                <h3
                  className={css({
                    fontSize: 'lg',
                    fontWeight: 'semibold',
                    color: isFullscreen ? 'white' : 'gray.900',
                  })}
                >
                  🎨 Abacus Style
                </h3>
                <button
                  onClick={resetToDefaults}
                  className={css({
                    fontSize: 'xs',
                    color: isFullscreen ? 'gray.300' : 'gray.500',
                    _hover: { color: isFullscreen ? 'white' : 'gray.700' },
                  })}
                >
                  Reset
                </button>
              </div>
              <p
                className={css({
                  fontSize: 'sm',
                  color: isFullscreen ? 'gray.300' : 'gray.600',
                })}
              >
                Configure display across the entire app
              </p>
            </div>

            {/* Color Scheme */}
            <FormField label="Color Scheme" isFullscreen={isFullscreen}>
              <RadioGroupField
                value={config.colorScheme}
                onValueChange={(value) => updateConfig({ colorScheme: value as ColorScheme })}
                options={[
                  { value: 'monochrome', label: 'Monochrome' },
                  { value: 'place-value', label: 'Place Value' },
                  { value: 'heaven-earth', label: 'Heaven-Earth' },
                  { value: 'alternating', label: 'Alternating' },
                ]}
                isFullscreen={isFullscreen}
              />
            </FormField>

            {/* Bead Shape */}
            <FormField label="Bead Shape" isFullscreen={isFullscreen}>
              <RadioGroupField
                value={config.beadShape}
                onValueChange={(value) => updateConfig({ beadShape: value as BeadShape })}
                options={[
                  { value: 'diamond', label: '💎 Diamond' },
                  { value: 'circle', label: '⭕ Circle' },
                  { value: 'square', label: '⬜ Square' },
                ]}
                isFullscreen={isFullscreen}
              />
            </FormField>

            {/* Toggle Options */}
            <div className={stack({ gap: '4' })}>
              <FormField label="Hide Inactive Beads" isFullscreen={isFullscreen}>
                <SwitchField
                  checked={config.hideInactiveBeads}
                  onCheckedChange={(checked) => updateConfig({ hideInactiveBeads: checked })}
                  isFullscreen={isFullscreen}
                />
              </FormField>

              <FormField label="Colored Numerals" isFullscreen={isFullscreen}>
                <SwitchField
                  checked={config.coloredNumerals}
                  onCheckedChange={(checked) => updateConfig({ coloredNumerals: checked })}
                  isFullscreen={isFullscreen}
                />
              </FormField>

              <FormField label="Sound Effects" isFullscreen={isFullscreen}>
                <SwitchField
                  checked={config.soundEnabled}
                  onCheckedChange={(checked) => updateConfig({ soundEnabled: checked })}
                  isFullscreen={isFullscreen}
                />
              </FormField>

              {config.soundEnabled && (
                <FormField
                  label={`Volume: ${Math.round(config.soundVolume * 100)}%`}
                  isFullscreen={isFullscreen}
                >
                  <input
                    type="range"
                    min="0"
                    max="1"
                    step="0.1"
                    value={config.soundVolume}
                    onChange={(e) => updateConfig({ soundVolume: parseFloat(e.target.value) })}
                    className={css({
                      w: 'full',
                      h: '2',
                      bg: isFullscreen ? 'rgba(255, 255, 255, 0.2)' : 'gray.200',
                      rounded: 'full',
                      appearance: 'none',
                      cursor: 'pointer',
                      _focusVisible: {
                        outline: 'none',
                        ring: '2px',
                        ringColor: isFullscreen ? 'blue.400' : 'brand.500',
                      },
                      '&::-webkit-slider-thumb': {
                        appearance: 'none',
                        w: '4',
                        h: '4',
                        bg: isFullscreen ? 'blue.400' : 'brand.600',
                        rounded: 'full',
                        cursor: 'pointer',
                        transition: 'all',
                        _hover: {
                          bg: isFullscreen ? 'blue.500' : 'brand.700',
                          transform: 'scale(1.1)',
                        },
                      },
                      '&::-moz-range-thumb': {
                        w: '4',
                        h: '4',
                        bg: isFullscreen ? 'blue.400' : 'brand.600',
                        rounded: 'full',
                        border: 'none',
                        cursor: 'pointer',
                      },
                    })}
                    onClick={(e) => e.stopPropagation()} // Prevent dropdown close
                  />
                </FormField>
              )}
            </div>
          </div>
        </DropdownMenu.Content>
      </DropdownMenu.Portal>
    </DropdownMenu.Root>
  )
}

// Helper Components (simplified versions of StyleControls components)
function FormField({
  label,
  children,
  isFullscreen = false,
}: {
  label: string
  children: React.ReactNode
  isFullscreen?: boolean
}) {
  return (
    <div className={stack({ gap: '2' })}>
      <Label.Root
        className={css({
          fontSize: 'sm',
          fontWeight: 'medium',
          color: isFullscreen ? 'white' : 'gray.900',
        })}
      >
        {label}
      </Label.Root>
      {children}
    </div>
  )
}

function SwitchField({
  checked,
  onCheckedChange,
  isFullscreen = false,
}: {
  checked: boolean
  onCheckedChange: (checked: boolean) => void
  isFullscreen?: boolean
}) {
  return (
    <Switch.Root
      checked={checked}
      onCheckedChange={onCheckedChange}
      className={css({
        w: '11',
        h: '6',
        bg: checked
          ? isFullscreen
            ? 'blue.500'
            : 'brand.600'
          : isFullscreen
            ? 'rgba(255, 255, 255, 0.2)'
            : 'gray.300',
        rounded: 'full',
        position: 'relative',
        transition: 'all',
        cursor: 'pointer',
        _hover: {
          bg: checked
            ? isFullscreen
              ? 'blue.600'
              : 'brand.700'
            : isFullscreen
              ? 'rgba(255, 255, 255, 0.3)'
              : 'gray.400',
        },
      })}
      onClick={(e) => e.stopPropagation()} // Prevent dropdown close only on the switch itself
    >
      <Switch.Thumb
        className={css({
          display: 'block',
          w: '5',
          h: '5',
          bg: 'white',
          rounded: 'full',
          shadow: 'sm',
          transition: 'transform 0.2s',
          transform: checked ? 'translateX(20px)' : 'translateX(0px)',
          willChange: 'transform',
        })}
      />
    </Switch.Root>
  )
}

function RadioGroupField({
  value,
  onValueChange,
  options,
  isFullscreen = false,
}: {
  value: string
  onValueChange: (value: string) => void
  options: Array<{ value: string; label: string }>
  isFullscreen?: boolean
}) {
  return (
    <RadioGroup.Root value={value} onValueChange={onValueChange} className={stack({ gap: '2' })}>
      {options.map((option) => (
        <div key={option.value} className={hstack({ gap: '3', alignItems: 'center' })}>
          <RadioGroup.Item
            value={option.value}
            className={css({
              w: '4',
              h: '4',
              rounded: 'full',
              border: '2px solid',
              borderColor: isFullscreen ? 'rgba(255, 255, 255, 0.3)' : 'gray.300',
              bg: isFullscreen ? 'rgba(255, 255, 255, 0.1)' : 'white',
              cursor: 'pointer',
              transition: 'all',
              _hover: { borderColor: isFullscreen ? 'blue.400' : 'brand.400' },
              '&[data-state=checked]': {
                borderColor: isFullscreen ? 'blue.500' : 'brand.600',
              },
            })}
            onClick={(e) => e.stopPropagation()} // Prevent dropdown close only on radio button
          >
            <RadioGroup.Indicator
              className={css({
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                w: 'full',
                h: 'full',
                position: 'relative',
                _after: {
                  content: '""',
                  display: 'block',
                  w: '1.5',
                  h: '1.5',
                  rounded: 'full',
                  bg: isFullscreen ? 'blue.400' : 'brand.600',
                },
              })}
            />
          </RadioGroup.Item>
          <label
            className={css({
              fontSize: 'sm',
              color: isFullscreen ? 'white' : 'gray.900',
              cursor: 'pointer',
              flex: 1,
            })}
            onClick={(e) => e.stopPropagation()} // Prevent dropdown close on label click too
          >
            {option.label}
          </label>
        </div>
      ))}
    </RadioGroup.Root>
  )
}
