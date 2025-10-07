# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the MacroMind project - a fitness and lifestyle superapp landing page. The main development is in the `website/` directory, which is a Next.js application built for launching in January 2026.

**Project Purpose**: A landing page for MacroMind, an AI-powered fitness platform that uses computer vision for real-time posture analysis, rep counting, personalized nutrition, and meal planning.

## Common Commands

All commands should be run from the `website/` directory:

```bash
# Development
npm run dev          # Start development server with Turbopack
npm run build        # Build for production with Turbopack
npm start           # Start production server
npm run lint        # Run ESLint

# Navigate to website directory first
cd website
```

The development server runs on `http://localhost:3000` with Turbopack enabled for faster builds.

## Architecture & Key Components

### Tech Stack
- **Next.js 15** with App Router and Turbopack
- **React 19** with TypeScript
- **Tailwind CSS 4** for styling
- **Vanta.js + Three.js** for interactive 3D wave background
- **Intersection Observer API** for scroll animations

### Component Architecture

The application follows a single-page landing structure with these main sections:

1. **Global Vanta.js Background**: Applied to entire site via `#vanta-background` div in `src/app/page.tsx`
2. **Component Sections**: Hero, CountdownTimer, Features, About, Footer
3. **Custom Hook**: `useScrollAnimation` for intersection observer-based animations

### Key Design Patterns

**Vanta.js Integration**:
- Scripts are dynamically loaded in the main page component
- Background applied globally with specific settings: black waves (color: 0x0), shininess: 30, waveHeight: 15
- All sections use backdrop-blur and transparency to show background

**Features Carousel**:
- Centered design with arrow navigation (left/right)
- No side panel - single large card display
- Features data defined as array with icons, colors, and descriptions

**Email Integration**:
- All "Get Early Access" buttons link to `mailto:nhemanth@stevens.edu`
- Found in Navbar, CountdownTimer, and Footer components

**Scroll Animations**:
- Custom `useScrollAnimation` hook uses Intersection Observer
- CSS classes: `.fade-in`, `.slide-in-left`, `.slide-in-right`, `.scale-in`
- Animations trigger once and stay visible (observer unobserves after trigger)

### Content & Styling Guidelines

**Countdown Timer**: Targets January 1, 2026 launch date
**Social Links**: Resume download, LinkedIn, and GitHub links are in Footer only
**Color Scheme**: Dark theme with blue/purple gradients and white text
**Layout**: All content is centered - headings, buttons, text, and sections

### File Structure Notes

- Resume PDF is stored in `public/NandanHemanth_Resume.pdf`
- Global styles include custom animation keyframes in `src/app/globals.css`
- Component files are self-contained with their own state management
- TypeScript declarations for Vanta.js are included inline where needed

### Important Implementation Details

- Turbopack is enabled for both dev and build commands
- Smooth scrolling navigation with section IDs: #countdown, #features, #about
- Mobile-responsive design with hamburger menu
- Glass-morphism effects using backdrop-blur throughout