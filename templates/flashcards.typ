#let draw-soroban(value, columns: auto, show-empty: false, hide-inactive: false, bead-shape: "diamond") = {
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
  let inactive-color = gray.lighten(70%)
  let active-color = black
  let bar-thickness = 2pt
  
  // Function to draw a bead based on shape
  // Note: y parameter represents the TOP edge of the bead for all shapes
  let draw-bead(x, y, shape, fill-color) = {
    if shape == "diamond" {
      // Horizontally elongated diamond (rhombus)
      place(
        dx: x - bead-size * 0.7,
        dy: y,
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
        dy: y,
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
      // For circles, y already represents where the center should be
      place(
        dx: x - bead-size / 2,
        dy: y,
        circle(
          radius: bead-size / 2,
          fill: fill-color,
          stroke: 0.5pt + black
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
          heaven-earth-gap - bead-size - 2pt  // Active (touching bar)
        } else {
          5pt  // Inactive (at top)
        }
        
        // Adjust y for circles (which use center positioning)
        #let adjusted-y = if bead-shape == "circle" {
          heaven-y + bead-size / 2
        } else {
          heaven-y
        }
        
        #if heaven-active == 1 or not hide-inactive [
          #draw-bead(
            x-offset,
            adjusted-y,
            bead-shape,
            if heaven-active == 1 { active-color } else { inactive-color }
          )
        ]
        
        // Draw earth beads
        #for i in range(4) [
          #let is-active = i < earth-active
          #let earth-y = if is-active {
            heaven-earth-gap + bar-thickness + 2pt + i * (bead-size + bead-spacing)
          } else {
            total-height - (4 - i) * (bead-size + bead-spacing) - 5pt
          }
          
          // Adjust y for circles (which use center positioning)
          #let adjusted-earth-y = if bead-shape == "circle" {
            earth-y + bead-size / 2
          } else {
            earth-y
          }
          
          #if is-active or not hide-inactive [
            #draw-bead(
              x-offset,
              adjusted-earth-y,
              bead-shape,
              if is-active { active-color } else { inactive-color }
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
  bead-shape: "diamond"
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
  let (cols, rows) = if cards-per-page == 6 {
    (2, 3)
  } else if cards-per-page == 4 {
    (2, 2)
  } else if cards-per-page == 8 {
    (2, 4)
  } else if cards-per-page == 9 {
    (3, 3)
  } else {
    panic("Unsupported cards-per-page value")
  }
  
  let card-width = (usable-width - gutter * (cols - 1)) / cols
  let card-height = (usable-height - gutter * (rows - 1)) / rows
  
  // Generate cards
  let cards = numbers.map(num => {
    flashcard(
      draw-soroban(num, columns: columns, show-empty: show-empty-columns, hide-inactive: hide-inactive-beads, bead-shape: bead-shape),
      text(size: font-size)[#num],
      card-width: card-width,
      card-height: card-height,
      show-cut-marks: show-cut-marks,
      show-registration: show-registration
    )
  })
  
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
    grid(
      columns: (card-width,) * cols,
      rows: (card-height,) * rows,
      column-gutter: gutter,
      row-gutter: gutter,
      ..page-cards.map(c => c.front)
    )
    
    // Always add page break after front side
    pagebreak()
    
    // BACK SIDE (even page numbers: 2, 4, 6...)
    // This will be the numeral side
    // Mirrored horizontally for long-edge duplex binding
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
    
    // Add page break except after the last page
    if page-idx < total-pages - 1 {
      pagebreak()
    }
  }
}