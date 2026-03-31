#!/usr/bin/env node
/**
 * generate-og-images.js
 * Generates 1200×630 PNG Open Graph images for each article.
 *
 * Usage:
 *   cd scripts
 *   npm install          # installs sharp
 *   node generate-og-images.js
 *
 * Output: ../og-<slug>.png for each article.
 */

'use strict';

const sharp = require('sharp');
const path  = require('path');
const fs    = require('fs');

// ── Article definitions ─────────────────────────────────────────────────────
const articles = [
  {
    slug:   'behavioral-contracts-human-autonomy-teaming',
    title:  'Behavioral Contracts for\nHuman-Autonomy Teaming',
  },
  {
    slug:   'agentic-ai-regulated-infrastructure',
    title:  'Agentic AI in\nRegulated Infrastructure:\nGuardrails, Evidence, and\nthe Accountability Gap',
  },
  {
    slug:   'it-operations-architecture',
    title:  'Reference Architecture:\nMaximum-Autonomy IT Operations',
  },
  {
    slug:   'enforceable-boundary-contracts',
    title:  'Enforceable Boundary Contracts\nfor EU-Regulated Infrastructure',
  },
];

// ── Colour palette (matches style.css dark theme) ───────────────────────────
const BG          = '#0a0e13';
const BG_SURFACE  = '#0f1319';
const FG_STRONG   = '#edf0f4';
const MUTED       = '#6b7a8d';
const ACCENT      = '#0d9488';
const BORDER_RAW  = 'rgba(255,255,255,0.08)';
const BORDER_ACC  = 'rgba(13,148,136,0.35)';

const W = 1200;
const H = 630;

// ── Helpers ──────────────────────────────────────────────────────────────────

/** Escape XML special characters for SVG text content. */
function xmlEsc(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/**
 * Build the SVG string for one OG image.
 *
 * Design:
 *  - Dark background with subtle dot-grid overlay
 *  - 4 px left accent bar in teal
 *  - Article title in large bold sans-serif (white)
 *  - "Roman Mednitzer" in monospace teal (bottom-left)
 *  - "rmednitzer.github.io" in small monospace muted (bottom-right)
 */
function buildSvg(title) {
  const lines      = title.split('\n');
  // Reduce font size for titles with 4+ lines to keep them comfortably within the card
  const titleFontSize = lines.length >= 4 ? 58 : 68;
  const lineHeight    = lines.length >= 4 ? 74 : 82;
  const titleX        = 100;

  // Vertical centre the title block
  const blockH  = lines.length * lineHeight;
  const titleY0 = Math.round((H - blockH) / 2) - 20; // nudge slightly above centre

  const titleLines = lines.map((line, i) => {
    const y = titleY0 + i * lineHeight + titleFontSize; // baseline
    return `<text x="${titleX}" y="${y}" font-family="ui-sans-serif, system-ui, sans-serif" font-size="${titleFontSize}" font-weight="600" fill="${FG_STRONG}" letter-spacing="-1">${xmlEsc(line)}</text>`;
  }).join('\n    ');

  // Subtle grid pattern (60 px pitch, very faint)
  // We render a few horizontal & vertical guide lines
  const gridLines = [];
  for (let gx = 60; gx < W; gx += 60) {
    gridLines.push(`<line x1="${gx}" y1="0" x2="${gx}" y2="${H}" stroke="${BORDER_RAW}" stroke-width="1"/>`);
  }
  for (let gy = 60; gy < H; gy += 60) {
    gridLines.push(`<line x1="0" y1="${gy}" x2="${W}" y2="${gy}" stroke="${BORDER_RAW}" stroke-width="1"/>`);
  }

  return `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="${W}" height="${H}" fill="${BG}"/>

  <!-- Subtle grid overlay -->
  <g opacity="0.35">
    ${gridLines.join('\n    ')}
  </g>

  <!-- Left accent bar -->
  <rect x="0" y="0" width="5" height="${H}" fill="${ACCENT}"/>

  <!-- Inner surface card -->
  <rect x="60" y="60" width="${W - 120}" height="${H - 120}" rx="12" fill="${BG_SURFACE}" opacity="0.5"/>
  <rect x="60" y="60" width="${W - 120}" height="${H - 120}" rx="12" fill="none" stroke="${BORDER_ACC}" stroke-width="1"/>

  <!-- Title -->
  ${titleLines}

  <!-- Author -->
  <text x="${titleX}" y="${H - 68}" font-family="ui-monospace, 'Cascadia Code', monospace" font-size="26" font-weight="500" fill="${ACCENT}" letter-spacing="0.5">${xmlEsc('Roman Mednitzer')}</text>

  <!-- Domain -->
  <text x="${W - 100}" y="${H - 68}" font-family="ui-monospace, 'Cascadia Code', monospace" font-size="22" fill="${MUTED}" text-anchor="end">${xmlEsc('rmednitzer.github.io')}</text>
</svg>`;
}

// ── Main ─────────────────────────────────────────────────────────────────────
const outDir = path.resolve(__dirname, '..');

(async () => {
  for (const article of articles) {
    const svg     = buildSvg(article.title);
    const outPath = path.join(outDir, `og-${article.slug}.png`);

    await sharp(Buffer.from(svg))
      .png({ compressionLevel: 9, palette: false })
      .toFile(outPath);

    console.log(`✓  ${path.basename(outPath)}`);
  }
  console.log('Done.');
})().catch(err => {
  console.error(err);
  process.exit(1);
});
