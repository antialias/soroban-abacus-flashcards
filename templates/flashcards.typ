#let draw-soroban(value, columns: auto, show-empty: false, hide-inactive: false, bead-shape: "diamond", color-scheme: "monochrome") = {
  // Parse the value into digits
  let digits = if type(value) == int {
    str(value).clusters().map(d => int(d))
  } else {
    panic("Value must be an integer")
  }
  
  // Determine number of columns
  let num-columns = if columns == auto {
    digits.len()
  } else {
    columns
  }
  
  // Pad with leading zeros if needed
  let padded-digits = if digits.len() < num-columns {
    (0,) * (num-columns - digits.len()) + digits
  } else {
    digits.slice(calc.max(0, digits.len() - num-columns))
  }
  
  // Skip leading zeros if show-empty is false
  let start-idx = if not show-empty {
    let first-nonzero = padded-digits.position(d => d != 0)
    if first-nonzero == none { 0 } else { first-nonzero }
  } else { 0 }
  
  let display-digits = padded-digits.slice(start-idx)
  if display-digits.len() == 0 { display-digits = (0,) }
  
  // Drawing parameters
  let rod-width = 3pt
  let bead-size = 12pt
  let bead-spacing = 4pt
  let column-spacing = 25pt
  let heaven-earth-gap = 20pt
  let bar-thickness = 2pt
  
  // Color schemes
  let place-value-colors = (
    rgb("#2E86AB"),  // ones - blue
    rgb("#A23B72"),  // tens - magenta
    rgb("#F18F01"),  // hundreds - orange
    rgb("#6A994E"),  // thousands - green
    rgb("#BC4B51"),  // ten-thousands - red
  )
  
  let get-column-color(col-idx, total-cols, scheme) = {
    if scheme == "place-value" {
      // Right-to-left: rightmost is ones
      let place-idx = total-cols - col-idx - 1
      let color-idx = calc.rem(place-idx, place-value-colors.len())
      place-value-colors.at(color-idx)
    } else if scheme == "alternating" {
      if calc.rem(col-idx, 2) == 0 { rgb("#1E88E5") } else { rgb("#43A047") }
    } else if scheme == "heaven-earth" {
      black  // Will be overridden per bead type
    } else {
      black  // monochrome
    }
  }
  
  let inactive-color = gray.lighten(70%)
  let active-color = black
  
  // Function to draw a bead based on shape
  // y parameter represents the CENTER of where the bead should be
  let draw-bead(x, y, shape, fill-color) = {
    if shape == "diamond" {
      // Horizontally elongated diamond (rhombus)
      place(
        dx: x - bead-size * 0.7,
        dy: y - bead-size / 2,
        polygon(
          (bead-size * 0.7, 0pt),           // left point
          (bead-size * 1.4, bead-size / 2), // top point
          (bead-size * 0.7, bead-size),      // right point
          (0pt, bead-size / 2),              // bottom point
          fill: fill-color,
          stroke: 0.5pt + black
        )
      )
    } else if shape == "square" {
      // Square bead
      place(
        dx: x - bead-size / 2,
        dy: y - bead-size / 2,
        rect(
          width: bead-size,
          height: bead-size,
          fill: fill-color,
          stroke: 0.5pt + black,
          radius: 1pt  // Slight rounding
        )
      )
    } else {
      // Circle (traditional option)
      // Use a box to position the circle from top-left like other shapes
      place(
        dx: x - bead-size / 2,
        dy: y - bead-size / 2,
        box(
          width: bead-size,
          height: bead-size,
          align(center + horizon, circle(
            radius: bead-size / 2,
            fill: fill-color,
            stroke: 0.5pt + black
          ))
        )
      )
    }
  }
  
  // Calculate total width and height
  let total-width = display-digits.len() * column-spacing
  let total-height = heaven-earth-gap + 5 * (bead-size + bead-spacing) + 10pt
  
  box(width: total-width, height: total-height)[
    #place(top + left)[
      #for (idx, digit) in display-digits.enumerate() [
        #let x-offset = idx * column-spacing + column-spacing / 2
        
        // Decompose digit into heaven (5s) and earth (1s) beads
        #let heaven-active = if digit >= 5 { 1 } else { 0 }
        #let earth-active = calc.rem(digit, 5)
        
        // Draw rod
        #place(
          dx: x-offset - rod-width / 2,
          dy: 0pt,
          rect(
            width: rod-width,
            height: total-height,
            fill: gray.lighten(80%),
            stroke: none
          )
        )
        
        // Draw heaven bead
        #let heaven-y = if heaven-active == 1 {
          heaven-earth-gap - bead-size / 2 - 2pt  // Active (center just above bar)
        } else {
          5pt + bead-size / 2  // Inactive (center near top)
        }
        
        #let bead-color = if heaven-active == 1 {
          if color-scheme == "heaven-earth" {
            rgb("#F18F01")  // Orange for heaven beads
          } else {
            get-column-color(idx, display-digits.len(), color-scheme)
          }
        } else {
          inactive-color
        }
        
        #if heaven-active == 1 or not hide-inactive [
          #draw-bead(
            x-offset,
            heaven-y,
            bead-shape,
            bead-color
          )
        ]
        
        // Draw earth beads
        #for i in range(4) [
          #let is-active = i < earth-active
          #let earth-y = if is-active {
            heaven-earth-gap + bar-thickness + 2pt + bead-size / 2 + i * (bead-size + bead-spacing)
          } else {
            total-height - (4 - i) * (bead-size + bead-spacing) - 5pt + bead-size / 2
          }
          
          #let earth-bead-color = if is-active {
            if color-scheme == "heaven-earth" {
              rgb("#2E86AB")  // Blue for earth beads
            } else {
              get-column-color(idx, display-digits.len(), color-scheme)
            }
          } else {
            inactive-color
          }
          
          #if is-active or not hide-inactive [
            #draw-bead(
              x-offset,
              earth-y,
              bead-shape,
              earth-bead-color
            )
          ]
        ]
      ]
      
      // Draw reckoning bar
      #place(
        dx: 0pt,
        dy: heaven-earth-gap,
        rect(
          width: total-width,
          height: bar-thickness,
          fill: black,
          stroke: none
        )
      )
    ]
  ]
}

#let flashcard(
  front-content,
  back-content,
  card-width: 3.5in,
  card-height: 2.5in,
  safe-margin: 5mm,
  show-cut-marks: false,
  show-registration: false
) = {
  let card = rect(
    width: card-width,
    height: card-height,
    stroke: if show-cut-marks { 0.25pt + gray } else { none },
    radius: 0pt
  )[
    #box(
      width: card-width - 2 * safe-margin,
      height: card-height - 2 * safe-margin,
      inset: safe-margin
    )[
      #align(center + horizon)[
        #front-content
      ]
    ]
    
    // Registration mark
    #if show-registration {
      place(
        bottom + right,
        dx: -2mm,
        dy: -2mm,
        circle(radius: 0.5mm, fill: gray.lighten(70%))
      )
    }
  ]
  
  (
    front: card,
    back: rect(
      width: card-width,
      height: card-height,
      stroke: if show-cut-marks { 0.25pt + gray } else { none },
      radius: 0pt
    )[
      #box(
        width: card-width - 2 * safe-margin,
        height: card-height - 2 * safe-margin,
        inset: safe-margin
      )[
        #align(center + horizon)[
          #back-content
        ]
      ]
      
      // Registration mark
      #if show-registration {
        place(
          bottom + left,
          dx: 2mm,
          dy: -2mm,
          circle(radius: 0.5mm, fill: gray.lighten(70%))
        )
      }
    ]
  )
}

#let generate-flashcards(
  numbers,
  cards-per-page: 6,
  paper-size: "us-letter",
  orientation: "portrait",
  margins: (top: 0.5in, bottom: 0.5in, left: 0.5in, right: 0.5in),
  gutter: 5mm,
  show-cut-marks: false,
  show-registration: false,
  font-family: "DejaVu Sans",
  font-size: 48pt,
  columns: auto,
  show-empty-columns: false,
  hide-inactive-beads: false,
  bead-shape: "diamond",
  color-scheme: "monochrome"
) = {
  // Set document properties
  set document(
    title: "Soroban Flashcards", 
    author: "Soroban Flashcard Generator",
    keywords: ("soroban", "abacus", "flashcards", "education", "math"),
    date: auto
  )
  set page(
    paper: paper-size,
    margin: margins,
    flipped: orientation == "landscape"
  )
  
  set text(font: font-family, size: font-size, fallback: true)
  
  // Calculate card dimensions
  let page-width = if orientation == "portrait" { 8.5in } else { 11in }
  let page-height = if orientation == "portrait" { 11in } else { 8.5in }
  
  let usable-width = page-width - margins.left - margins.right
  let usable-height = page-height - margins.top - margins.bottom
  
  // Determine grid layout
  let (cols, rows) = if cards-per-page == 1 {
    (1, 1)
  } else if cards-per-page == 2 {
    (1, 2)
  } else if cards-per-page == 3 {
    (1, 3)
  } else if cards-per-page == 4 {
    (2, 2)
  } else if cards-per-page == 6 {
    (2, 3)
  } else if cards-per-page == 8 {
    (2, 4)
  } else if cards-per-page == 9 {
    (3, 3)
  } else if cards-per-page == 10 {
    (2, 5)
  } else if cards-per-page == 12 {
    (3, 4)
  } else if cards-per-page == 15 {
    (3, 5)
  } else if cards-per-page == 16 {
    (4, 4)
  } else if cards-per-page == 18 {
    (3, 6)
  } else if cards-per-page == 20 {
    (4, 5)
  } else if cards-per-page == 24 {
    (4, 6)
  } else if cards-per-page == 25 {
    (5, 5)
  } else if cards-per-page == 30 {
    (5, 6)
  } else {
    // Try to find a reasonable grid for other values
    let sqrt-cards = calc.sqrt(cards-per-page)
    let cols-guess = calc.ceil(sqrt-cards)
    let rows-guess = calc.ceil(cards-per-page / cols-guess)
    (cols-guess, rows-guess)
  }
  
  let card-width = (usable-width - gutter * (cols - 1)) / cols
  let card-height = (usable-height - gutter * (rows - 1)) / rows
  
  // Generate cards
  let cards = numbers.map(num => {
    flashcard(
      draw-soroban(num, columns: columns, show-empty: show-empty-columns, hide-inactive: hide-inactive-beads, bead-shape: bead-shape, color-scheme: color-scheme),
      text(size: font-size)[#num],
      card-width: card-width,
      card-height: card-height,
      show-cut-marks: show-cut-marks,
      show-registration: show-registration
    )
  })
  
  // Function to draw cutting guides
  let draw-cutting-guides(cols, rows, card-width, card-height, gutter, usable-width, usable-height) = {
    // Use subtle gray lines that won't be too distracting if cut is slightly off
    let guide-color = gray.lighten(50%)
    let guide-stroke = 0.25pt + guide-color
    
    // Draw horizontal cutting guides
    for row in range(rows - 1) {
      let y-pos = (row + 1) * card-height + row * gutter + gutter / 2
      place(
        dx: -margins.left,  // Extend to page edge
        dy: y-pos,
        line(
          start: (0pt, 0pt),
          end: (usable-width + margins.left + margins.right, 0pt),
          stroke: guide-stroke
        )
      )
    }
    
    // Draw vertical cutting guides
    for col in range(cols - 1) {
      let x-pos = (col + 1) * card-width + col * gutter + gutter / 2
      place(
        dx: x-pos,
        dy: -margins.top,  // Extend to page edge
        line(
          start: (0pt, 0pt),
          end: (0pt, usable-height + margins.top + margins.bottom),
          stroke: guide-stroke
        )
      )
    }
  }
  
  // Layout pages - alternating front and back for duplex printing
  let total-cards = cards.len()
  let total-pages = calc.ceil(total-cards / cards-per-page)
  
  // Generate all pages in front/back pairs for proper duplex printing
  for page-idx in range(total-pages) {
    let start-idx = page-idx * cards-per-page
    let end-idx = calc.min(start-idx + cards-per-page, total-cards)
    let page-cards = cards.slice(start-idx, end-idx)
    
    // FRONT SIDE (odd page numbers: 1, 3, 5...)
    // This will be the soroban bead side
    place(
      grid(
        columns: (card-width,) * cols,
        rows: (card-height,) * rows,
        column-gutter: gutter,
        row-gutter: gutter,
        ..page-cards.map(c => c.front)
      )
    )
    
    // Draw cutting guides on top if enabled
    if show-cut-marks {
      draw-cutting-guides(cols, rows, card-width, card-height, gutter, usable-width, usable-height)
    }
    
    // Always add page break after front side
    pagebreak()
    
    // BACK SIDE (even page numbers: 2, 4, 6...)
    // This will be the numeral side
    // Mirrored horizontally for long-edge duplex binding
    place(
      grid(
        columns: (card-width,) * cols,
        rows: (card-height,) * rows,
        column-gutter: gutter,
        row-gutter: gutter,
        ..range(rows).map(r => {
          // Reverse columns for proper back-side alignment
          range(cols).rev().map(c => {
            let idx = r * cols + c
            if idx < page-cards.len() {
              page-cards.at(idx).back
            } else {
              // Empty space for incomplete grids
              rect(width: card-width, height: card-height, stroke: none)[]
            }
          })
        }).flatten()
      )
    )
    
    // Draw cutting guides on back side too
    if show-cut-marks {
      draw-cutting-guides(cols, rows, card-width, card-height, gutter, usable-width, usable-height)
    }
    
    // Add page break except after the last page
    if page-idx < total-pages - 1 {
      pagebreak()
    }
  }
}