#!/bin/bash
echo "== Stopping server"
docker-compose -f bin/docker/docker-compose.dev.yml stop