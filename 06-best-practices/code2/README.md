## Code snippets

### Building and running Docker images

```bash
docker build -t stream-model-duration:v2 .
```

##### Getting model from s3
```bash
docker run -it --rm \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e RUN_ID="da8a85f0cfc94022891e42f77ed37298" \
    -e TEST_RUN="True" \
    -e AWS_DEFAULT_REGION="us-west-2" \
    -v $HOME/.aws:/root/.aws \
    stream-model-duration:v2
```

##### Getting model from local, -v: mounting local downloaded model to container
```bash
docker run -it --rm \
    -v ~/.aws:/root/.aws \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e RUN_ID="da8a85f0cfc94022891e42f77ed37298" \
    -e TEST_RUN="True" \
    -e AWS_DEFAULT_REGION="us-east-1" \
    -e MODEL_LOCATION="/app/model" \
    -v $(pwd)/model:/app/model \
    stream-model-duration:v2
```

##### Testing via localstack; instead of RUN_ID above, using "Test123"
We don't want it to go to s3; we want to see an error in our test_docker.py assert.
```bash
docker run -it --rm \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e RUN_ID="Test123" \
    -e TEST_RUN="True" \
    -e MODEL_LOCATION="/app/model" \
    -e AWS_DEFAULT_REGION="us-east-1" \
    -v $(pwd)/model:/app/model \
    stream-model-duration:v2
```

Start localstack service in integration_tests directory
`docker compose up`
Localstack:s3 will be available on port 4566. Note that stopping the container with `docker-compose down` will remove all data as well.

To list all buckets on localstack:
`aws s3api list-buckets --endpoint-url=http://localhost:4566`

To show contents of specific localstack:s3 location:
`aws s3 ls --endpoint-url=http://localhost:4566 s3://model-test-bucket/model/`

To make bucket:
`aws --endpoint-url=http://localhost:4566 s3 mb s3://test-bucket`

Run test that creates a new bucket and puts model into it:
`python test_s3.py`
