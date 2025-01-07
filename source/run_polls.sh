#!/bin/bash

# Step 1: Open Docker Desktop
echo "Starting Docker Desktop..."
open -a "Docker"
MAX_RETRIES=30  # Maximum number of retries
RETRY_DELAY=2   # Seconds to wait between retries
RETRIES=0

while ! docker info > /dev/null 2>&1; do
  if [ $RETRIES -ge $MAX_RETRIES ]; then
    echo "Docker did not become ready in time. Exiting."
    exit 1
  fi
  RETRIES=$((RETRIES + 1))
  echo "Retrying... ($RETRIES/$MAX_RETRIES)"
  sleep $RETRY_DELAY
done

echo "Docker is ready!"

# Step 2: Start WAHA with docker-compose
echo "Starting WAHA with docker-compose..."
cd ~/Projects/VballPolling
docker-compose up -d
if [ $? -ne 0 ]; then
  echo "Failed to start WAHA using docker-compose."
  exit 1
fi

# Step 3: Wait for WAHA to initialize
echo "Waiting for WAHA to initialize..."
MAX_RETRIES=30  # Number of retries
RETRY_DELAY=2   # Delay in seconds between retries
RETRIES=0

while ! curl -sf http://localhost:3000/api/sessions > /dev/null; do
  if [ $RETRIES -ge $MAX_RETRIES ]; then
    echo "WAHA API did not become ready in time. Exiting."
    exit 1
  fi
  RETRIES=$((RETRIES + 1))
  echo "Retrying... ($RETRIES/$MAX_RETRIES)"
  sleep $RETRY_DELAY
done
echo "WAHA is ready!"

# Step 4: Start a new WAHA session
echo "Starting WAHA session..."
curl -X POST "http://localhost:3000/api/sessions/default/start" -H "Content-Type: application/json" -H "accept: application/json"
if [ $? -ne 0 ]; then
  echo "Failed to start WAHA session."
  exit 1
fi

# Step 5: Run Python script
echo "Running Python script..."
python3 ~/Projects/VballPolling/source/main.py
if [ $? -ne 0 ]; then
  echo "Python script failed."
  exit 1
fi

# Step 6: Stop Docker containers
echo "Stopping Docker containers..."
docker-compose down
if [ $? -ne 0 ]; then
  echo "Failed to stop Docker containers."
  exit 1
fi

# Step 7: Close Docker Desktop
echo "Closing Docker Desktop on macOS..."
osascript -e 'quit app "Docker"'

# Step 8: Confirm Docker has stopped
echo "Waiting for Docker to stop..."
while docker info > /dev/null 2>&1; do
  sleep 1
done

echo "Docker Desktop has been closed."
