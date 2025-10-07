'use client';

import { useState } from 'react';
import { useScrollAnimation } from '@/hooks/useScrollAnimation';

const features = [
  {
    title: "AI-Powered Computer Vision",
    subtitle: "Real-Time Form Analysis",
    description: "Advanced pose detection using Google ML-kit and OpenCV for real-time posture analysis, rep counting, and form correction with instant audio feedback and motivation.",
    icon: "🤖",
    color: "from-blue-500 to-cyan-500"
  },
  {
    title: "Personalized Nutrition",
    subtitle: "Smart Meal Planning",
    description: "AI-powered meal planning with curated shopping lists, personalized nutrition tracking, and instant food analysis through photo recognition.",
    icon: "🍎",
    color: "from-green-500 to-emerald-500"
  },
  {
    title: "AI Personal Chef",
    subtitle: "Custom Recipe Generation",
    description: "Get personalized meal recipes based on available ingredients, fitness goals, dietary restrictions, and injuries for healthy, quick meal-prep solutions.",
    icon: "👨‍🍳",
    color: "from-orange-500 to-red-500"
  },
  {
    title: "Science-Based Training",
    subtitle: "Research-Backed Workouts",
    description: "Evidence-based lifting programs and quick educational reads to enhance your knowledge in nutrition, workout science, and healthy lifestyle habits.",
    icon: "🧬",
    color: "from-purple-500 to-pink-500"
  },
  {
    title: "Comprehensive Tracking",
    subtitle: "Complete Health Metrics",
    description: "Track calories, protein, carbs, fiber, fats, and water intake with a simple photo. Monitor your complete health journey in one place.",
    icon: "📊",
    color: "from-indigo-500 to-blue-500"
  },
  {
    title: "Holistic Wellness",
    subtitle: "Lifestyle Integration",
    description: "More than just fitness - a complete lifestyle platform that adapts to your goals, preferences, and daily routine for sustainable health improvements.",
    icon: "🌟",
    color: "from-yellow-500 to-orange-500"
  }
];

export default function Features() {
  const [activeFeature, setActiveFeature] = useState(0);
  const [titleRef, titleVisible] = useScrollAnimation();
  const [featuresRef, featuresVisible] = useScrollAnimation();

  return (
    <section className="py-48 bg-black/30 backdrop-blur-sm">
      <div className="max-w-7xl mx-auto px-4">
        <div ref={titleRef} className={`text-center mb-32 fade-in ${titleVisible ? 'visible' : ''}`}>
          <h2 className="text-5xl md:text-7xl font-bold text-white mb-8 text-center">
            What is <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">MacroMind</span>?
          </h2>
        </div>

        <div ref={featuresRef} className={`flex justify-center items-center slide-in-left ${featuresVisible ? 'visible' : ''}`}>
          <div className={`relative bg-gradient-to-br ${features[activeFeature].color} rounded-3xl p-16 text-white max-w-4xl w-full shadow-2xl`}>
            {/* Left Arrow Button */}
            <button
              onClick={() => setActiveFeature(activeFeature > 0 ? activeFeature - 1 : features.length - 1)}
              className="absolute left-6 top-1/2 transform -translate-y-1/2 p-4 bg-white/20 backdrop-blur-lg rounded-full hover:bg-white/30 transition-all duration-300 text-white z-10 hover:scale-110"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
            </button>

            {/* Right Arrow Button */}
            <button
              onClick={() => setActiveFeature(activeFeature < features.length - 1 ? activeFeature + 1 : 0)}
              className="absolute right-6 top-1/2 transform -translate-y-1/2 p-4 bg-white/20 backdrop-blur-lg rounded-full hover:bg-white/30 transition-all duration-300 text-white z-10 hover:scale-110"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </button>

            <div className="text-9xl mb-10 text-center">{features[activeFeature].icon}</div>
            <h3 className="text-4xl md:text-5xl font-bold mb-6 text-center">{features[activeFeature].title}</h3>
            <h4 className="text-2xl md:text-3xl font-semibold mb-8 text-center text-white/90">
              {features[activeFeature].subtitle}
            </h4>
            <p className="text-xl md:text-2xl leading-relaxed text-center text-white/90 mb-10 px-4 md:px-12">
              {features[activeFeature].description}
            </p>

            {/* Dot Indicators */}
            <div className="flex justify-center gap-3 mt-10">
              {features.map((_, index) => (
                <button
                  key={index}
                  className={`w-3 h-3 rounded-full transition-all duration-300 hover:scale-125 ${activeFeature === index ? 'bg-white w-8' : 'bg-white/40'
                    }`}
                  onClick={() => setActiveFeature(index)}
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}