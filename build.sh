#!/bin/bash

REPOSITORY="registry.hpc.ut.ee/sander"
TAG="latest"

docker compose --parallel 12 build

IMAGES=$(cat docker-compose.yaml | yq '.services | keys | .[]')

for IMAGE in $IMAGES; do
    docker tag "localhost/ds-practice-2024_${IMAGE}" "${REPOSITORY}/${IMAGE}:${TAG}"
    docker push "${REPOSITORY}/${IMAGE}:${TAG}"
done
