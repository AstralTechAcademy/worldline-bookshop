# Create project

```sh
npm create astro@latest
```

# Add aditional tools

## Add tailwind css

```sh
npx astro add tailwind
```

## NodeJS adapter


```sh
npx astro add node
```

After run the above commands, your file astro.config.mjs must contains

```js
// @ts-check
import { defineConfig } from 'astro/config';

import node from '@astrojs/node';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  adapter: node({
    mode: 'standalone'
  }),

  vite: {
    plugins: [tailwindcss()]
  }
});
```

# Writing code

## Layout

Layouts are Astro components used to provide a reusable UI structure, such as a page template.

We conventionally use the term “layout” for Astro components that provide common UI elements shared across pages such as headers, navigation bars, and footers. 

A typical Astro layout component provides Astro, Markdown or MDX pages with:

a page shell (<html>, <head> and <body> tags)
a <slot /> to specify where individual page content should be injected.

## Header Component

## Body

>[!WARNING]
TODO

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

# Deployment

## Docker container

>[!Warning]
> Might you must run docker command as sudo

### Build image

```docker
docker build -t worldline-bookshop .
```

### Run container

```docker
docker run -p 8081:4321 --name worldline-bookshop worldline-bookshop
```

# Test

- Open a web browser
- http://localhost:8081