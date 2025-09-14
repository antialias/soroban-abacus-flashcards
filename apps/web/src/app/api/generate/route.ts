import { NextRequest, NextResponse } from 'next/server'
import { SorobanGenerator } from '@soroban/core'
import { assetStore } from '@/lib/asset-store'
import path from 'path'
import crypto from 'crypto'

// Global generator instance for better performance
let generator: SorobanGenerator | null = null

async function getGenerator() {
  if (!generator) {
    // Point to the core package in our monorepo
    const corePackagePath = path.join(process.cwd(), '../../packages/core')
    generator = new SorobanGenerator(corePackagePath)

    // Note: SorobanGenerator from @soroban/core doesn't have initialize method
    // It uses one-shot mode by default
  }
  return generator
}

export async function POST(request: NextRequest) {
  try {
    const config = await request.json()

    // Debug: log the received config
    console.log('📥 Received config:', JSON.stringify(config, null, 2))

    // Ensure range is set with a default
    if (!config.range) {
      console.log('⚠️ No range provided, using default: 0-99')
      config.range = '0-99'
    }

    // Get generator instance
    const gen = await getGenerator()

    // Check dependencies before generating
    const deps = await gen.checkDependencies?.()
    if (deps && (!deps.python || !deps.typst)) {
      return NextResponse.json({
        error: 'Missing system dependencies',
        details: {
          python: deps.python ? '✅ Available' : '❌ Missing Python 3',
          typst: deps.typst ? '✅ Available' : '❌ Missing Typst',
          qpdf: deps.qpdf ? '✅ Available' : '⚠️ Missing qpdf (optional)'
        }
      }, { status: 500 })
    }

    // Generate flashcards using Python via TypeScript bindings
    console.log('🚀 Generating flashcards with config:', JSON.stringify(config, null, 2))
    const pdfBuffer = await gen.generate(config)

    // Create unique ID for this generated asset
    const assetId = crypto.randomUUID()

    // For now, only PDF format is supported by the core generator
    const format = 'pdf'
    const mimeType = 'application/pdf'
    const filename = `soroban-flashcards-${config.range || 'cards'}.pdf`

    // Store the generated asset temporarily
    assetStore.set(assetId, {
      data: pdfBuffer,
      filename,
      mimeType,
      createdAt: new Date()
    })

    // Calculate metadata from config
    const cardCount = calculateCardCount(config.range || '0', config.step || 1)
    const numbers = generateNumbersFromRange(config.range || '0', config.step || 1)

    // Return metadata and download URL
    return NextResponse.json({
      id: assetId,
      downloadUrl: `/api/download/${assetId}`,
      metadata: {
        cardCount,
        numbers: numbers.slice(0, 20), // Show first 20 numbers for preview
        format,
        filename,
        fileSize: pdfBuffer.length
      },
      success: true
    })

  } catch (error) {
    console.error('❌ Generation failed:', error)

    return NextResponse.json({
      error: 'Failed to generate flashcards',
      details: error instanceof Error ? error.message : 'Unknown error',
      success: false
    }, { status: 500 })
  }
}

// Helper functions to calculate metadata
function calculateCardCount(range: string, step: number): number {
  if (range.includes('-')) {
    const [start, end] = range.split('-').map(n => parseInt(n) || 0)
    return Math.floor((end - start + 1) / step)
  }

  if (range.includes(',')) {
    return range.split(',').length
  }

  return 1
}

function generateNumbersFromRange(range: string, step: number): number[] {
  if (range.includes('-')) {
    const [start, end] = range.split('-').map(n => parseInt(n) || 0)
    const numbers: number[] = []
    for (let i = start; i <= end; i += step) {
      numbers.push(i)
      if (numbers.length >= 100) break // Limit to prevent huge arrays
    }
    return numbers
  }

  if (range.includes(',')) {
    return range.split(',').map(n => parseInt(n.trim()) || 0)
  }

  return [parseInt(range) || 0]
}

// Health check endpoint
export async function GET() {
  try {
    const gen = await getGenerator()
    const deps = await gen.checkDependencies?.() || { python: true, typst: true, qpdf: true }

    return NextResponse.json({
      status: 'healthy',
      dependencies: deps,
      assetsInMemory: assetStore.size
    })
  } catch (error) {
    return NextResponse.json({
      status: 'unhealthy',
      error: error instanceof Error ? error.message : 'Unknown error'
    }, { status: 500 })
  }
}