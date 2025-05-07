#!/bin/sh

# Name of the Compose project (optional, defaults to directory name)
PROJECT_NAME="skeleton_api"

# Ensure external network exists (safe to run even if it already exists)
echo "Ensuring external Docker network '${PROJECT_NAME}' exists..."
docker network inspect "$PROJECT_NAME" >/dev/null 2>&1 || \
    docker network create --driver bridge "$PROJECT_NAME"

# Step 1: Stop and remove old containers from the project
echo "Stopping and removing old containers (if any)..."
docker compose --env-file .env -p "$PROJECT_NAME" down

# Step 2: Remove old image
docker image rm skeleton_api_app 2>/dev/null || true

# Step 3: Build and start the new container
echo "Building and starting new container..."
docker compose --env-file .env -p "$PROJECT_NAME" up --build -d
