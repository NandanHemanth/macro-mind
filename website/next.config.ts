import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'export',
  basePath: '/macromind',
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
