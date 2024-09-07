## Introduction

This is a hybrid Next.js + Python app that uses Next.js as the frontend and [FastAPI](https://fastapi.tiangolo.com/) with [Socket.IO](https://python-socketio.readthedocs.io/en/stable/) as the API backend. One great use case of this is to write Next.js apps that use websocket comunication.

## How It Works

The Python/FastAPI server is mapped into to Next.js app under `/api/`.

This is implemented using [`next.config.js` rewrites](https://github.com/imcarlosguerrero/nextjs-fastapi-socketio-template/blob/main/next.config.mjs) to map any request to `/api/:path*` to the FastAPI app, which is hosted in the `/api` folder.

On localhost, the rewrite will be made to the `127.0.0.1:8000` port, which is where the Uvicorn server is running.

In production, the FastAPI server is hosted in the same dyno as the Next.js app, so works in a similar way.

## Deploy Your Own

You can clone & deploy it to Heroku with one click:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://www.heroku.com/deploy?template=https://github.com/imcarlosguerrero/nextjs-fastapi-socketio-template)

## Developing Locally

You can clone & create this repo with the following command

```bash
npx create-next-app nextjs-fastapi-socketio --example "https://github.com/imcarlosguerrero/nextjs-fastapi-socketio-template"
```

## Getting Started

First, install the dependencies:

```bash
npm install
# or
yarn
# or
pnpm install
# or
bun install
```

Then, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

The FastAPI server will be running on [http://127.0.0.1:8000](http://127.0.0.1:8000) – feel free to change the port in `package.json` (you'll also need to update it in `next.config.js`).

## Why the template doesn't use Vercel

Vercel is based in a serverless approach that doesn't support websockets, therefore, the deployment of a project using this template wouldn't work at all.

## Learn More

To learn more about Next.js and the technologies used in this template, take a look at the following resources:

-   [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
-   [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
-   [FastAPI Documentation](https://fastapi.tiangolo.com/) - learn about FastAPI features and API.
-   [Socket.IO Documentation](https://python-socketio.readthedocs.io/en/stable/) - learn about Socket.IO features and API.
-   [About Vercel and WebSockets](https://vercel.com/guides/do-vercel-serverless-functions-support-websocket-connections) - learn more about Vercel and WebSockets.