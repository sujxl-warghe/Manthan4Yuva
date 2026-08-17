#!/usr/bin/env bash
set -euo pipefail

# Navigate to the frontend folder and run install, build, and start.
cd WebSite/frontend

# Use CI install for reproducible builds in CI environments.
npm ci

# Build the Next.js app
npm run build

# Start the app; next start reads $PORT
npm start
