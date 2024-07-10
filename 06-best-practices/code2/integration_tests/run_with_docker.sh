#!/usr/bin/env bash

cd "$(dirname "$0")"

LOCAL_TAG=`date +"%Y-%m-%d-%H-%M"`
LOCAL_IMAGE_NAME="stream-model-duration:${LOCAL_TAG}"

docker build -t ${LOCAL_IMAGE_NAME} .

docker run -it --rm \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e RUN_ID="Test123" \
    -e TEST_RUN="True" \
    -e MODEL_LOCATION="/app/model" \
    -e AWS_DEFAULT_REGION="us-east-1" \
    -v $(pwd)/model:/app/model \
    ${LOCAL_IMAGE_NAME}

pipenv run python test_docker.py
