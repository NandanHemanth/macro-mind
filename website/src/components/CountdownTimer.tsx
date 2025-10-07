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
    <section className="py-48 bg-black/30 backdrop-blur-sm">
      <div className="max-w-7xl mx-auto px-4 text-center flex flex-col items-center">
        <div className="mb-[200px]">
          <h2 className="text-5xl md:text-7xl font-bold text-white mb-[80px] text-center">
            Launch Countdown
          </h2>
          <p className="text-xl md:text-2xl text-gray-300 text-center">
            The future of fitness is coming January 2026
          </p>
        </div>

        <div className="flex justify-center items-center gap-8 flex-wrap max-w-5xl pb-16 pt-[100px]">
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-10 border border-white/20 min-w-[160px]">
            <div className="text-5xl md:text-7xl font-bold text-white mb-4">
              {timeLeft.weeks}
            </div>
            <div className="text-base md:text-lg text-gray-300 uppercase tracking-wider font-semibold">
              Weeks
            </div>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-10 border border-white/20 min-w-[160px]">
            <div className="text-5xl md:text-7xl font-bold text-white mb-4">
              {timeLeft.days}
            </div>
            <div className="text-base md:text-lg text-gray-300 uppercase tracking-wider font-semibold">
              Days
            </div>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-10 border border-white/20 min-w-[160px]">
            <div className="text-5xl md:text-7xl font-bold text-white mb-4">
              {timeLeft.hours}
            </div>
            <div className="text-base md:text-lg text-gray-300 uppercase tracking-wider font-semibold">
              Hours
            </div>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-10 border border-white/20 min-w-[160px]">
            <div className="text-5xl md:text-7xl font-bold text-white mb-4">
              {timeLeft.minutes}
            </div>
            <div className="text-base md:text-lg text-gray-300 uppercase tracking-wider font-semibold">
              Minutes
            </div>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-10 border border-white/20 min-w-[160px]">
            <div className="text-5xl md:text-7xl font-bold text-white mb-4">
              {timeLeft.seconds}
            </div>
            <div className="text-base md:text-lg text-gray-300 uppercase tracking-wider font-semibold">
              Seconds
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}