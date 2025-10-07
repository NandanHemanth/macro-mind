'use client';

export default function About() {
  return (
    <section className="py-32 bg-black/30 backdrop-blur-sm">
      <div className="max-w-5xl mx-auto px-4 flex flex-col items-center">
        <div className="mb-[100px] w-full">
          <h2 className="text-5xl md:text-6xl font-bold text-white mb-[60px] text-center">
            About the <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">Founder</span>
          </h2>
        </div>

        <div className="bg-white/10 backdrop-blur-lg rounded-3xl p-16 border border-white/20 max-w-4xl w-full">
          <h3 className="text-4xl md:text-5xl font-bold text-white mb-[80px] text-center">Nandan Hemanth</h3>

          <div className="space-y-12 text-gray-300 text-center mb-[80px]">
            <p className="text-xl md:text-2xl leading-relaxed">
              Passionate innovator combining cutting-edge technology with health and wellness solutions
            </p>
            <p className="text-xl md:text-2xl leading-relaxed">
              Expert in AI, computer vision, and mobile application development
            </p>
            <p className="text-xl md:text-2xl leading-relaxed">
              Dedicated to making fitness accessible, engaging, and scientifically-backed for everyone
            </p>
          </div>

          <div className="pt-[80px] border-t border-white/20 center">
            <p className="text-gray-300 text-xl md:text-2xl leading-relaxed text-center italic mb-[600px]">
              "My vision is to revolutionize how people approach fitness and nutrition by leveraging
              the power of AI and computer vision. MacroMind isn't just an app – it's a comprehensive
              ecosystem designed to make healthy living intuitive, personalized, and sustainable."
            </p>
            <div className="text-center">
              <span className="text-blue-400 font-semibold text-xl">— Nandan Hemanth</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}