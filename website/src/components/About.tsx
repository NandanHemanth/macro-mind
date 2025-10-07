'use client';

export default function About() {
  return (
    <section className="py-20 bg-black/30 backdrop-blur-sm">
      <div className="max-w-4xl mx-auto px-4 text-center">
        <div className="mb-16">
          <h2 className="text-5xl md:text-6xl font-bold text-white mb-6 text-center">
            About the <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">Founder</span>
          </h2>
        </div>

        <div className="bg-white/10 backdrop-blur-lg rounded-3xl p-12 border border-white/20 max-w-3xl mx-auto">
          <h3 className="text-4xl font-bold text-white mb-8 text-center">Nandan Hemanth</h3>

          <div className="space-y-6 text-gray-300 text-center">
            <p className="text-xl leading-relaxed">
              Passionate innovator combining cutting-edge technology with health and wellness solutions
            </p>
            <p className="text-xl leading-relaxed">
              Expert in AI, computer vision, and mobile application development
            </p>
            <p className="text-xl leading-relaxed">
              Dedicated to making fitness accessible, engaging, and scientifically-backed for everyone
            </p>
          </div>

          <div className="mt-12 pt-8 border-t border-white/20">
            <p className="text-gray-300 text-xl leading-relaxed text-center italic">
              "My vision is to revolutionize how people approach fitness and nutrition by leveraging
              the power of AI and computer vision. MacroMind isn't just an app – it's a comprehensive
              ecosystem designed to make healthy living intuitive, personalized, and sustainable."
            </p>
            <div className="mt-6 text-center">
              <span className="text-blue-400 font-semibold text-lg">— Nandan Hemanth</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}