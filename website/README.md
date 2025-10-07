# MacroMind Website

A modern, interactive landing page for MacroMind - the revolutionary fitness and lifestyle superapp.

## 🚀 Features

- **Interactive Hero Section** with Vanta.js animated waves background
- **Countdown Timer** to January 2026 launch date
- **Responsive Design** optimized for all device sizes
- **Smooth Scrolling Navigation** with animated transitions
- **Interactive Feature Showcase** with clickable cards
- **About the Founder** section with downloadable resume
- **Modern UI/UX** with gradients, animations, and hover effects

## 🛠️ Tech Stack

- **Next.js 15** with App Router
- **React 18** with TypeScript
- **Tailwind CSS** for styling
- **Vanta.js** for interactive 3D background
- **Three.js** for 3D graphics support

## 📱 Sections

1. **Hero** - "Every Rep Counts!" tagline with interactive background
2. **Countdown** - Real-time countdown to January 2026 launch
3. **Features** - Interactive showcase of MacroMind capabilities:
   - AI-Powered Computer Vision
   - Personalized Nutrition
   - AI Personal Chef
   - Science-Based Training
   - Comprehensive Tracking
   - Holistic Wellness
4. **About** - Founder information with social links and resume download
5. **Footer** - Additional links and contact information

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ installed
- npm or yarn package manager

### Installation

1. Navigate to the website directory:
```bash
cd website
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and visit: http://localhost:3000

### Build for Production

```bash
npm run build
npm start
```

## 📁 Project Structure

```
website/
├── src/
│   ├── app/
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/
│   │   ├── About.tsx
│   │   ├── CountdownTimer.tsx
│   │   ├── Features.tsx
│   │   ├── Footer.tsx
│   │   ├── Hero.tsx
│   │   └── Navbar.tsx
│   └── hooks/
│       └── useScrollAnimation.ts
├── public/
│   └── NandanHemanth_Resume.pdf
├── package.json
└── README.md
```

## 🎨 Key Features Implemented

### Interactive Background
- Vanta.js waves animation with customizable parameters
- Responsive and touch-friendly controls

### Countdown Timer
- Real-time countdown to January 1, 2026
- Displays weeks, days, hours, minutes, and seconds
- Responsive grid layout

### Smooth Animations
- Scroll-triggered animations using Intersection Observer
- Smooth scrolling navigation
- Hover effects and transitions

### Responsive Design
- Mobile-first approach
- Responsive navigation with hamburger menu
- Optimized layouts for all screen sizes

## 🔧 Customization

### Vanta.js Background Settings
The wave background can be customized in `Hero.tsx`:
- `color`: Wave color (default: 0x0 - black)
- `shininess`: Wave shininess (default: 30)
- `waveHeight`: Wave amplitude (default: 15)
- `waveSpeed`: Animation speed (default: 1)
- `zoom`: Camera zoom level (default: 1)

### Countdown Target Date
Update the launch date in `CountdownTimer.tsx`:
```typescript
const launchDate = new Date('2026-01-01T00:00:00').getTime();
```

## 📞 Contact

For questions about this website or MacroMind:
- **Founder**: Nandan Hemanth
- **LinkedIn**: [nandan-hemanth-a784811b8](https://www.linkedin.com/in/nandan-hemanth-a784811b8/)
- **GitHub**: [NandanHemanth](https://github.com/NandanHemanth)

## 📄 License

This project is built for MacroMind. All rights reserved.

---

Built with ❤️ by Nandan Hemanth using Next.js, React, and modern web technologies.
