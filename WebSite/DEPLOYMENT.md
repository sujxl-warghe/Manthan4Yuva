Deployment guide — Frontend (Railway / Netlify) and Backend (Render)

Overview
- Frontend: Next.js app located in WebSite/frontend.
  - Railway: run as a Node web service (next start)
  - Netlify: supported via @netlify/plugin-nextjs
- Backend: FastAPI app located in WebSite/backend
  - Render: deploy as a Python web service using uvicorn

Frontend — Railway (recommended for full Next.js behavior)
1. In the WebSite/frontend folder, ensure Node version matches your environment (set in Railway dashboard).
2. Build & start commands (Railway):
   - Build Command: npm install && npm run build
   - Start Command: npm start
   Railway will provide PORT via the $PORT environment variable. The package.json start script is already set to: "next start -p $PORT".
3. Environment variables
   - Set any API_BASE or similar env vars to point to your backend service URL (https://your-backend.on.render.com).
   - Update backend CORS_ORIGINS to include the frontend URL.

Frontend — Netlify
1. Netlify uses the @netlify/plugin-nextjs plugin included in devDependencies and a netlify.toml at the project root of the frontend.
2. In Netlify, set the Build command: npm run build and publish directory: leave default (the plugin will handle server functions and pages).
3. Environment variables
   - Set any API_BASE or similar env vars in the Netlify site settings.
   - Ensure backend CORS_ORIGINS includes the Netlify site URL.

Backend — Render
1. Create a new Web Service on Render and connect your repository (or use the render.yaml included at WebSite/backend/render.yaml for IaC).
2. Environment: select "Python" environment.
3. Build Command: pip install -r requirements.txt
4. Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   - Uvicorn is included in requirements.txt; this command is suitable for small/medium workloads on Render. For higher throughput, consider adding gunicorn + uvicorn workers.
5. Environment variables
   - Set DATABASE_URL for a managed Postgres service (recommended). If omitted, app falls back to local SQLite which may not be persistent.
   - Set JWT_SECRET, CORS_ORIGINS (comma-separated list including the frontend domain), and other secrets as needed.

CORS and Environment notes
- The backend reads CORS_ORIGINS from the CORS_ORIGINS env var. Example:
  CORS_ORIGINS=https://your-frontend.netlify.app,https://your-frontend.railway.app
- For production databases use a managed Postgres (e.g., Render's Postgres or Neon). Provide the DATABASE_URL env var.

No Docker
- These instructions use platform-native deployment for Render and Railway/Netlify and do not require Docker.

Troubleshooting
- If you see connection errors to the database, verify DATABASE_URL and network access.
- If the frontend cannot call the backend, confirm CORS_ORIGINS includes the frontend origin and that the backend URL is reachable and configured in frontend environment variables.

Files added/updated
- WebSite/frontend/package.json: start script updated to use $PORT; added @netlify/plugin-nextjs devDependency
- WebSite/frontend/netlify.toml: Netlify config to enable Next.js plugin
- WebSite/backend/render.yaml: Render service config
- WebSite/DEPLOYMENT.md: this guide

If you want, the next steps can automate Render/Netlify settings (example YAML for Render is added). If preferred, create a render service spec for the frontend for Railway deployment or CI/CD pipeline notes.
