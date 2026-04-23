#!/bin/bash

echo "🛑 Stopping frontend container..."
docker stop harry_frontend || true
docker rm harry_frontend || true

echo "🐳 Rebuilding frontend..."
docker compose build harry_frontend

echo "🚀 Starting frontend..."
docker compose up -d harry_frontend

echo "✅ Frontend deploy complete!"
