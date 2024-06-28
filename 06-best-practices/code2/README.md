## Code snippets

### Building and running Docker images

```bash
docker build -t stream-model-duration:v2 .
```

```bash
docker run -it --rm \
    -v ~/.aws:/root/.aws \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e RUN_ID="da8a85f0cfc94022891e42f77ed37298" \
    -e TEST_RUN="True" \
    -e AWS_DEFAULT_REGION="us-east-1" \
    stream-model-duration:v2
```
    -v $HOME/.aws/credentials:/home/app/.aws/credentials:ro \