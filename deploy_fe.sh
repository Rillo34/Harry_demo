#!/bin/bash

echo "🔄 Pulling latest frontend code..."
git pull

echo "🛑 Stopping frontend container..."
docker compose stop frontend

echo "🐳 Rebuilding frontend..."
docker compose build frontend

echo "🚀 Starting frontend..."
docker compose up -d frontend

echo "✅ Frontend deploy complete!"
