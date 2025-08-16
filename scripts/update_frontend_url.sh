#!/usr/bin/env bash
set -euo pipefail

# Updates FRONTEND_URL in .env with current ngrok web tunnel URL and restarts the bot.
# Requirements: jq, running ngrok container with API exposed on localhost:4040
# Usage: bash scripts/update_frontend_url.sh

NGROK_API="${NGROK_API:-http://localhost:4040/api/tunnels}"
ENV_FILE=".env"
TARGET_ADDR="app:5173"

if ! command -v jq >/dev/null 2>&1; then
  echo "[ERROR] 'jq' is required. Install with: brew install jq" >&2
  exit 1
fi

# Wait up to 20s for ngrok API
for i in $(seq 1 20); do
  if curl -s "$NGROK_API" >/dev/null 2>&1; then
    break
  fi
  sleep 1
  if [ "$i" = 20 ]; then
    echo "[ERROR] ngrok API not reachable at $NGROK_API" >&2
    exit 1
  fi
done

json=$(curl -s "$NGROK_API")
web_url=$(echo "$json" | jq -r --arg addr "$TARGET_ADDR" '.tunnels[] | select(.config.addr==$addr) | .public_url' | head -n1)
if [ -z "$web_url" ] || [ "$web_url" = "null" ]; then
  echo "[ERROR] Could not extract web tunnel public URL for $TARGET_ADDR" >&2
  echo "$json" | jq '.tunnels[] | {name: .name, addr: .config.addr, public_url: .public_url}' >&2
  exit 1
fi

# Ensure HTTPS (Telegram requirement)
if [[ "$web_url" != https:* ]]; then
  # Replace http with https (ngrok usually provides both http/https)
  web_url="${web_url/http:/https:}"
fi

echo "[INFO] Detected web tunnel URL: $web_url"

if [ ! -f "$ENV_FILE" ]; then
  echo "[ERROR] $ENV_FILE not found" >&2
  exit 1
fi

# Replace FRONTEND_URL line (macOS/BSD sed compatible)
if grep -q '^FRONTEND_URL=' "$ENV_FILE"; then
  sed -i '' -E "s|^FRONTEND_URL=.*|FRONTEND_URL=$web_url|" "$ENV_FILE"
else
  echo "FRONTEND_URL=$web_url" >> "$ENV_FILE"
fi

echo "[INFO] Updated FRONTEND_URL in $ENV_FILE"

docker-compose restart bot >/dev/null

echo "[INFO] Bot restarted. You can now open the bot and use the WebApp buttons."
