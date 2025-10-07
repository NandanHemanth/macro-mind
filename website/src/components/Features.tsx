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
    <section className="py-20 bg-black/30 backdrop-blur-sm">
      <div className="max-w-4xl mx-auto px-4">
        <div ref={titleRef} className={`text-center mb-16 fade-in ${titleVisible ? 'visible' : ''}`}>
          <h2 className="text-5xl md:text-6xl font-bold text-white mb-6 text-center">
            What is <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">MacroMind</span>?
          </h2>
        </div>

        <div ref={featuresRef} className={`text-center slide-in-left ${featuresVisible ? 'visible' : ''}`}>
          <div className={`bg-gradient-to-br ${features[activeFeature].color} rounded-3xl p-12 text-white mx-auto max-w-2xl`}>
            <div className="text-8xl mb-8 text-center">{features[activeFeature].icon}</div>
            <h3 className="text-4xl font-bold mb-4 text-center">{features[activeFeature].title}</h3>
            <h4 className="text-2xl font-semibold mb-6 text-center text-white/80">
              {features[activeFeature].subtitle}
            </h4>
            <p className="text-xl leading-relaxed text-center text-white/90 mb-8">
              {features[activeFeature].description}
            </p>
          </div>

          <div className="flex justify-center items-center mt-12 space-x-8">
            <button
              onClick={() => setActiveFeature(activeFeature > 0 ? activeFeature - 1 : features.length - 1)}
              className="p-4 bg-white/20 backdrop-blur-lg rounded-full hover:bg-white/30 transition-all duration-300 text-white"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
            </button>

            <div className="flex space-x-2">
              {features.map((_, index) => (
                <button
                  key={index}
                  className={`w-3 h-3 rounded-full transition-all duration-300 ${
                    activeFeature === index ? 'bg-blue-400' : 'bg-white/30'
                  }`}
                  onClick={() => setActiveFeature(index)}
                />
              ))}
            </div>

            <button
              onClick={() => setActiveFeature(activeFeature < features.length - 1 ? activeFeature + 1 : 0)}
              className="p-4 bg-white/20 backdrop-blur-lg rounded-full hover:bg-white/30 transition-all duration-300 text-white"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}