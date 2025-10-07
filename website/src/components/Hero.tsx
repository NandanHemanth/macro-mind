'use client';

export default function Hero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center text-white overflow-hidden">
      <div className="absolute inset-0 bg-black/20 z-10"></div>

      <div className="relative z-20 text-center px-4 max-w-4xl mx-auto">
        <div className="mb-8">
          <h1 className="text-6xl md:text-8xl font-bold mb-4 tracking-tight">
            macro
            <span className="text-blue-400">mind</span>
          </h1>
          <div className="w-24 h-1 bg-gradient-to-r from-blue-400 to-purple-500 mx-auto mb-8"></div>
        </div>

        <h2 className="text-3xl md:text-5xl font-bold mb-6 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-purple-500 to-pink-400">
          Every Rep Counts!
        </h2>

        <p className="text-xl md:text-2xl mb-8 text-gray-200 max-w-3xl mx-auto leading-relaxed text-center">
          Revolutionizing fitness and nutrition with AI-powered computer vision,
          personalized meal planning, and science-based training
        </p>
      </div>

      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-20">
        <button
          onClick={() => {
            const element = document.getElementById('countdown');
            if (element) element.scrollIntoView({ behavior: 'smooth' });
          }}
          className="animate-bounce hover:scale-110 transition-transform duration-300"
        >
          <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
          </svg>
        </button>
      </div>
    </section>
  );
}