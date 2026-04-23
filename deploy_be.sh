#!/bin/bash

set -e

echo "🔄 Pulling latest backend code..."
git pull

echo "🛑 Stopping backend container..."
docker compose stop harry_backend

echo "🐳 Rebuilding backend..."
docker compose build harry_backend

echo "🚀 Starting backend..."
docker compose up -d harry_backend

echo "🧹 Cleaning unused images..."
docker image prune -f

echo "✅ Backend deploy complete!"