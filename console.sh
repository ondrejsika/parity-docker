#!/bin/sh

PORT_SHIFT=${1:-0}

docker exec -ti parity-$PORT_SHIFT /app/geth attach http://127.0.0.1:8545

