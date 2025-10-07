'use client';

import { useState, useEffect } from 'react';

export default function CountdownTimer() {
  const [timeLeft, setTimeLeft] = useState({
    days: 0,
    weeks: 0,
    hours: 0,
    minutes: 0,
    seconds: 0
  });

  useEffect(() => {
    const calculateTimeLeft = () => {
      const launchDate = new Date('2026-01-01T00:00:00').getTime();
      const now = new Date().getTime();
      const difference = launchDate - now;

      if (difference > 0) {
        const days = Math.floor(difference / (1000 * 60 * 60 * 24));
        const weeks = Math.floor(days / 7);
        const remainingDays = days % 7;
        const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((difference % (1000 * 60)) / 1000);

        setTimeLeft({
          days: remainingDays,
          weeks,
          hours,
          minutes,
          seconds
        });
      }
    };

    calculateTimeLeft();
    const timer = setInterval(calculateTimeLeft, 1000);

    return () => clearInterval(timer);
  }, []);

  return (
    <section className="py-20 bg-black/30 backdrop-blur-sm">
      <div className="max-w-6xl mx-auto px-4 text-center">
        <h2 className="text-4xl md:text-6xl font-bold text-white mb-4 text-center">
          Launch Countdown
        </h2>
        <p className="text-xl text-gray-300 mb-12 text-center">
          The future of fitness is coming January 2026
        </p>

        <div className="grid grid-cols-2 md:grid-cols-5 gap-6 max-w-4xl mx-auto">
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
            <div className="text-3xl md:text-5xl font-bold text-white mb-2">
              {timeLeft.weeks}
            </div>
            <div className="text-sm md:text-base text-gray-300 uppercase tracking-wider">
              Weeks
            </div>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
            <div className="text-3xl md:text-5xl font-bold text-white mb-2">
              {timeLeft.days}
            </div>
            <div className="text-sm md:text-base text-gray-300 uppercase tracking-wider">
              Days
            </div>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
            <div className="text-3xl md:text-5xl font-bold text-white mb-2">
              {timeLeft.hours}
            </div>
            <div className="text-sm md:text-base text-gray-300 uppercase tracking-wider">
              Hours
            </div>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
            <div className="text-3xl md:text-5xl font-bold text-white mb-2">
              {timeLeft.minutes}
            </div>
            <div className="text-sm md:text-base text-gray-300 uppercase tracking-wider">
              Minutes
            </div>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
            <div className="text-3xl md:text-5xl font-bold text-white mb-2">
              {timeLeft.seconds}
            </div>
            <div className="text-sm md:text-base text-gray-300 uppercase tracking-wider">
              Seconds
            </div>
          </div>
        </div>

        <div className="mt-12 text-center">
          <a
            href="mailto:nhemanth@stevens.edu"
            className="inline-block px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full font-semibold text-lg text-white hover:from-blue-600 hover:to-purple-700 transition-all duration-300 transform hover:scale-105 shadow-lg text-center"
          >
            Get Early Access
          </a>
        </div>
      </div>
    </section>
  );
}