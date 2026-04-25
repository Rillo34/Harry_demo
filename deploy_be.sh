#!/bin/bash
set -e

echo "🔄 Pull backend..."
git pull

echo "🛑 Stopping backend..."
docker compose stop harry_backend || true

echo "🐳 Rebuilding backend..."
docker compose up -d --build harry_backend

echo "🧹 Cleanup..."
docker image prune -f

echo "✅ Backend deployed"