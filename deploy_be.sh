#!/bin/bash

echo "🔄 Pulling latest backend code..."
git pull

echo "🛑 Stopping backend container..."
docker compose stop backend

echo "🐳 Rebuilding backend..."
docker compose build backend

echo "🚀 Starting backend..."
docker compose up -d backend

echo "✅ Backend deploy complete!"
