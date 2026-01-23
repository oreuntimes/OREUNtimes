# CLAUDE.md - AI Assistant Guide for OREUN TIMES

## Project Overview

**OREUN TIMES** is a Bloomberg Terminal-inspired, single-page financial market intelligence dashboard. It provides comprehensive market analysis for Korean investors with coverage of US markets, commodities, cryptocurrencies, and key market influencers.

- **Website**: https://www.oreun.co.kr
- **Related Platform**: https://www.daily-m.tv/
- **Language**: Korean (KR) with English market terminology
- **Target Audience**: Korean investors tracking global markets

## Repository Structure

```
OREUNtimes/
├── index.html      # Single-page React application (all code in one file)
├── CLAUDE.md       # This file - AI assistant guidelines
└── .git/           # Git repository
```

This is a **single-file application** where all HTML, CSS, and JavaScript/React code is contained within `index.html` (~3700 lines).

## Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| React | 17 (CDN) | UI component library |
| Tailwind CSS | Latest (CDN) | Utility-first CSS framework |
| Babel | Latest (CDN) | JSX transpilation in browser |
| Lucide Icons | Latest (CDN) | Icon library |

### Fonts Used
- **IBM Plex Sans Condensed** - Bloomberg-style headers
- **Noto Sans KR** - Korean text
- **JetBrains Mono** - Monospace/terminal styling
- **Space Grotesk** - Headlines and section titles
- **Pretendard** - Fallback Korean font

## File Structure Within index.html

The single HTML file is organized into these sections:

1. **Lines 1-75**: HTML head, CDN imports, CSS styles
2. **Lines 76-130**: Lucide icon shim and icon definitions
3. **Lines 132-200**: Helper functions (getDirection, getColorClass, etc.)
4. **Lines 200-450**: Constants (VOICE_TAG_LABELS, TICKER_NAME_MAP, etc.)
5. **Lines 454-1900+**: `MARKET_DATA` - JSON data object with all market data
6. **Lines 1900-2810**: React components (SectionHeader, IndexCard, etc.)
7. **Lines 2810-3730**: Main `App()` component
8. **Lines 3733-3745**: React mounting and error handling

## Key React Components

| Component | Purpose |
|-----------|---------|
| `App` | Main application container |
| `SectionHeader` | Collapsible section wrapper with styling |
| `IndexCard` | Market index/commodity display card |
| `M7DeepDiveRow` | Magnificent 7 stock analysis row |
| `MoverFeedItem` | Market mover display item |
| `VoiceCard` | Market influencer quote card |
| `CircularGauge` | Circular progress indicator |
| `HorizontalBar` | Horizontal progress bar |
| `FlagKR` / `FlagUS` | Country flag SVG components |
| `CornerBrackets` | Decorative corner bracket styling |
| `Sparkline` | Mini sparkline chart component |

## MARKET_DATA Structure

The `MARKET_DATA` constant contains all dashboard data:

```javascript
const MARKET_DATA = {
  // Metadata
  date: "YYYY.MM.DD",
  generationTime: "HH:MM:SS",
  targetDateUS: "YYYY-MM-DD (US CLOSE)",
  publishKST: "YYYY-MM-DD HH:MM KST",
  dstStatus: "ON" | "OFF",  // Daylight saving time

  // Headlines
  headline: "Main headline text",

  // Key Indicators (shown in header)
  keyIndicators: {
    nasdaq: { val, chg, class: "up"|"down"|"flat" },
    vix: { val, chg, class },
    fearGreed: { val, label, class }
  },

  // Market Data Arrays
  indices: [...],       // Market indices (DJI, NDX, SPX, etc.)
  commodities: [...],   // Commodities (Gold, Oil, etc.)
  crypto: [...],        // Cryptocurrencies (BTC, ETH, etc.)

  // Analysis Sections
  m7deep: [...],        // Magnificent 7 deep dive analysis
  movers: [...],        // Market movers (up/down)
  marketVoices: [...],  // Key influencer quotes
  riskAlerts: [...],    // Risk alerts/warnings
  schedule: [...],      // Daily market schedule
  events: [...],        // Upcoming economic events

  // Final Strategy
  finalAction: "Strategy text",
  finalDecision: "HOLD" | "BUY" | "SELL",
  threatLevel: "LOW" | "MID" | "HIGH",
  marketBias: "BULLISH" | "NEUTRAL" | "DEFENSIVE"
}
```

## Design System

### Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Background | `#0b0e11` | Main background |
| Orange | `#ff9d00` | Primary accent, highlights |
| Cyan | `#00e5ff` | Secondary accent, links |
| Green | `#00ff00` | Positive/Up indicators |
| Red | `#FF073A` | Negative/Down indicators |
| White | `#ffffff` | Primary text |
| Gray | `#333-#999` | Borders, secondary text |

### Direction/Status Classes

- **Up**: `text-[#00ff00]` - Positive change (> +0.5%)
- **Down**: `text-[#FF073A]` - Negative change (< -0.5%)
- **Flat**: `text-white` - Neutral change (-0.5% to +0.5%)

### Visual Effects

- Grid overlays for background texture
- Glow effects on hover states
- Terminal-style cursor animations
- Corner bracket decorations for cards

## Development Guidelines

### Updating Market Data

1. Locate the `MARKET_DATA` constant (around line 454)
2. Update the relevant fields with new data
3. Ensure date/time fields are updated accordingly
4. Test by opening `index.html` in a browser

### Adding New Indices/Assets

Add to the appropriate array in `MARKET_DATA`:

```javascript
{
  "name": "DISPLAY NAME (한글명)",
  "ticker": "SYMBOL",
  "price": "1,234.56",
  "chg": "+1.25%",
  "comment": "Brief commentary",
  "signal": "BUY" | "SELL" | "HOLD" | "WATCH"
}
```

### Adding Market Voices

```javascript
{
  "name": "SPEAKER NAME",
  "role": "Title/Position",
  "tags": ["FED", "WALLST", ...],  // See VOICE_TAG_LABELS
  "quote": "Quote text in Korean",
  "date": "YYYY-MM-DD",
  "impact": "positive" | "negative" | "neutral"
}
```

### Voice Tag Categories

| Tag | Korean Label | Description |
|-----|--------------|-------------|
| FED | 연준 | Federal Reserve officials |
| PRESIDENT | 대통령 | Presidents/heads of state |
| GOV | 정부 | Government officials |
| CEO | CEO | Corporate executives |
| BIGTECH | 빅테크 | Big tech companies |
| ANALYST | 애널리스트 | Market analysts |
| MEDIA | 언론 | Media outlets |
| WALLST | 월가 | Wall Street figures |
| BANK | 은행장 | Bank executives |
| VOLATILITY | 변동성 | Volatility-related |
| GLOBAL | 해외정상 | Foreign leaders |

## Testing

1. Open `index.html` directly in a modern browser (Chrome, Firefox, Edge)
2. Check browser console for any React or CDN loading errors
3. Verify all sections expand/collapse properly
4. Test responsive layout at different screen widths

## Common Issues

### CDN Loading Failures
If CDN resources fail to load, the app displays an error message in Korean. Check:
- Network connectivity
- CDN availability (unpkg.com, cdnjs.cloudflare.com)
- Browser console for specific errors

### Icon Display Issues
Lucide icons are initialized via `window.lucide.createIcons()` in a useEffect hook. If icons don't appear:
- Check that the Lucide CDN loaded successfully
- Verify the icon name exists in Lucide library

## Important Notes for AI Assistants

1. **Single File Architecture**: All changes happen in `index.html` - there are no separate component files
2. **Data Updates**: Most updates involve modifying the `MARKET_DATA` JSON object
3. **Korean Content**: Much of the content is in Korean - preserve Korean text when making edits
4. **CDN Dependencies**: The app relies on CDN-hosted libraries - no local npm/node setup required
5. **No Build Step**: Changes are immediate - just refresh the browser
6. **Browser-Based Babel**: JSX is transpiled in the browser, which may affect initial load time
7. **Static Report**: This is designed as a daily market report that gets updated with new data each day

## Git Workflow

- Main branch: `main`
- Commits typically involve updating `index.html` with new market data
- Commit messages reference the date of the market report

## External Links

- **OREUN Official Site**: https://www.oreun.co.kr
- **Daily M TV**: https://www.daily-m.tv/
