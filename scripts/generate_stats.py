import datetime

# Get current UTC date
today_str = datetime.datetime.utcnow().strftime("%B %d, %Y")

# Generate SVG content dynamically
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="400" height="60" viewBox="0 0 400 60">
  <rect width="100%" height="100%" fill="#0d1117" rx="10" />
  <text x="20" y="35" font-family="Segoe UI, Ubuntu, sans-serif" font-size="14" fill="#58a6ff" font-weight="bold">
    ⚡ Profile Last Updated: <tspan fill="#c9d1d9">{today_str}</tspan>
  </text>
</svg>
"""

# Save to an SVG file
with open("status.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Status SVG updated successfully.")
