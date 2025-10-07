'use client';

import { useState, useEffect } from 'react';

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
    setIsMobileMenuOpen(false);
  };

  return (
    <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${isScrolled ? 'bg-black/80 backdrop-blur-lg border-b border-white/10' : 'bg-transparent'
      }`}>
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-3">
            <img
              src="/MacroMind_T.png"
              alt="MacroMind Logo"
              className="w-10 h-10 object-contain"
            />
            <div className="text-2xl font-bold text-white">
              Macro<span className="text-blue-400">Mind</span>
            </div>
          </div>

          <div className="hidden md:flex items-center gap-8">
            <button
              onClick={() => scrollToSection('features')}
              className="text-white hover:text-blue-400 transition-colors duration-300 font-medium text-lg px-4"
            >
              Features
            </button>
            <button
              onClick={() => scrollToSection('countdown')}
              className="text-white hover:text-blue-400 transition-colors duration-300 font-medium text-lg px-4"
            >
              Launch
            </button>
            <button
              onClick={() => scrollToSection('about')}
              className="text-white hover:text-blue-400 transition-colors duration-300 font-medium text-lg px-4"
            >
              About
            </button>
            <div className="w-px h-6 bg-white/20 mx-2"></div>
            <a
              href="mailto:nhemanth@stevens.edu"
              className="px-8 py-2.5 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full font-semibold text-white hover:from-blue-600 hover:to-purple-700 transition-all duration-300 transform hover:scale-105 text-center whitespace-nowrap"
            >
              Get Early Access
            </a>
          </div>

          <button
            className="md:hidden text-white"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d={isMobileMenuOpen ? "M6 18L18 6M6 6l12 12" : "M4 6h16M4 12h16M4 18h16"} />
            </svg>
          </button>
        </div>

        {isMobileMenuOpen && (
          <div className="md:hidden bg-black/90 backdrop-blur-lg border-t border-white/10">
            <div className="px-2 pt-2 pb-3 space-y-1">
              <button
                onClick={() => scrollToSection('features')}
                className="block w-full text-left px-3 py-2 text-white hover:text-blue-400 transition-colors duration-300 font-medium"
              >
                Features
              </button>
              <button
                onClick={() => scrollToSection('countdown')}
                className="block w-full text-left px-3 py-2 text-white hover:text-blue-400 transition-colors duration-300 font-medium"
              >
                Launch
              </button>
              <button
                onClick={() => scrollToSection('about')}
                className="block w-full text-left px-3 py-2 text-white hover:text-blue-400 transition-colors duration-300 font-medium"
              >
                About
              </button>
              <a
                href="mailto:nhemanth@stevens.edu"
                className="w-full mt-2 px-6 py-2 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full font-semibold text-white hover:from-blue-600 hover:to-purple-700 transition-all duration-300 text-center block"
              >
                Get Early Access
              </a>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}