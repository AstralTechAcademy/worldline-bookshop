// @ts-check
import { defineConfig } from 'astro/config';

import node from '@astrojs/node';

import tailwindcss from '@tailwindcss/vite';
import { serverHelpers } from 'astro/runtime/client/dev-toolbar/helpers.js';

// https://astro.build/config
export default defineConfig({
  output: 'server',
  site: 'https://bookshop.worldline.astraltech.es',
  adapter: node({
    mode: 'standalone'
  }),

  vite: {
    plugins: [tailwindcss()]
  }
});