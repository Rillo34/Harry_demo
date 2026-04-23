#!/bin/bash

set -e

echo "🔄 Pulling latest code..."
git pull

echo "🐳 Rebuilding frontend..."
docker compose up -d --build harry_frontend

echo "🧹 Cleaning old images..."
docker image prune -f

echo "✅ Frontend deploy complete!"