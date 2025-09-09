// Single card template for PNG export
// Renders one card at a time with optional transparent background

#import "flashcards.typ": draw-soroban

// Local definition of create-colored-numeral since it's not exported
#let create-colored-numeral(num, scheme, use-colors, font-size) = {
  // Use the exact same colors as the beads
  let place-value-colors = (
    rgb("#2E86AB"),  // ones - blue (same as beads)
    rgb("#A23B72"),  // tens - magenta (same as beads)
    rgb("#F18F01"),  // hundreds - orange (same as beads)
    rgb("#6A994E"),  // thousands - green (same as beads)
    rgb("#BC4B51"),  // ten-thousands - red (same as beads)
  )
  
  if not use-colors or scheme == "monochrome" {
    // Plain black text
    text(size: font-size)[#num]
  } else if scheme == "place-value" {
    // Color each digit according to its place value
    let digits = str(num).clusters()
    let num-digits = digits.len()
    let colored-digits = ()
    
    for (idx, digit) in digits.enumerate() {
      let place-idx = num-digits - idx - 1  // 0 = ones, 1 = tens, etc.
      let color-idx = calc.rem(place-idx, place-value-colors.len())
      let digit-color = place-value-colors.at(color-idx)
      colored-digits += (text(fill: digit-color, size: font-size)[#digit],)
    }
    
    colored-digits.join()
  } else if scheme == "heaven-earth" {
    // For heaven-earth, use orange (heaven bead color)
    text(size: font-size, fill: rgb("#F18F01"))[#num]
  } else if scheme == "alternating" {
    // For alternating, we could alternate digit colors
    let digits = str(num).clusters()
    let colored-digits = ()
    
    for (idx, digit) in digits.enumerate() {
      let digit-color = if calc.rem(idx, 2) == 0 { rgb("#1E88E5") } else { rgb("#43A047") }
      colored-digits += (text(fill: digit-color, size: font-size)[#digit],)
    }
    
    colored-digits.join()
  } else {
    // Fallback to plain text
    text(size: font-size)[#num]
  }
}

#let generate-single-card(
  number,
  side: "front",  // "front" or "back"
  bead-shape: "diamond",
  color-scheme: "monochrome",
  colored-numerals: false,
  hide-inactive-beads: false,
  show-empty-columns: false,
  columns: auto,
  transparent: false,
  width: 3.5in,
  height: 2.5in,
  font-size: 48pt,
  font-family: "DejaVu Sans",
  scale-factor: 1.0,
) = {
  // Set page size to exact card dimensions
  set page(
    width: width,
    height: height,
    margin: 0pt,
    fill: if transparent { none } else { white }
  )
  
  // Set font
  set text(font: font-family, size: font-size, fallback: true)
  
  // Calculate padding for content
  let padding = width * 0.05
  
  // Render the appropriate side
  if side == "front" {
    // Soroban side
    align(center + horizon)[
      #box(
        width: width - 2 * padding,
        height: height - 2 * padding
      )[
        #align(center + horizon)[
          #scale(x: scale-factor * 100%, y: scale-factor * 100%)[
            #draw-soroban(
              number,
              columns: columns,
              show-empty: show-empty-columns,
              hide-inactive: hide-inactive-beads,
              bead-shape: bead-shape,
              color-scheme: color-scheme,
              base-size: 1.0
            )
          ]
        ]
      ]
    ]
  } else {
    // Numeral side
    align(center + horizon)[
      #create-colored-numeral(number, color-scheme, colored-numerals, font-size * scale-factor)
    ]
  }
}