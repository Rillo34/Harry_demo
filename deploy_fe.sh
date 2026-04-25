#!/bin/bash
set -e

echo "🔄 Pull frontend..."
git pull

echo "🧨 Recreating frontend (forces env reload)..."
docker compose up -d --build --force-recreate harry_frontend

echo "🧹 Cleanup..."
docker image prune -f

echo "✅ Frontend deployed"