'use client';

import { useEffect } from 'react';
import Navbar from '@/components/Navbar';
import Hero from '@/components/Hero';
import Features from '@/components/Features';
import About from '@/components/About';
import CountdownTimer from '@/components/CountdownTimer';
import Footer from '@/components/Footer';

export default function Home() {
  useEffect(() => {
    const threeScript = document.createElement('script');
    threeScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js';
    threeScript.onload = () => {
      const vantaScript = document.createElement('script');
      vantaScript.src = 'https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.waves.min.js';
      vantaScript.onload = () => {
        if (window.VANTA) {
          window.VANTA.WAVES({
            el: "#vanta-background",
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x0,
            shininess: 30,
            waveHeight: 15,
            waveSpeed: 1,
            zoom: 1
          });
        }
      };
      document.head.appendChild(vantaScript);
    };
    document.head.appendChild(threeScript);
  }, []);

  return (
    <div id="vanta-background" className="min-h-screen">
      <main className="relative z-10">
        <Navbar />
        <Hero />
        <section id="countdown" className="scroll-mt-16">
          <CountdownTimer />
        </section>
        <section id="features" className="scroll-mt-16">
          <Features />
        </section>
        <section id="about" className="scroll-mt-16">
          <About />
        </section>
        <Footer />
      </main>
    </div>
  );
}
