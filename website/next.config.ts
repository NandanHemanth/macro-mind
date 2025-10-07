import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'export',
  basePath: '/macro-mind',
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
