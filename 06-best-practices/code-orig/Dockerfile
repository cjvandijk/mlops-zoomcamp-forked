FROM public.ecr.aws/lambda/python:3.9
# FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

WORKDIR /home/ubuntu/code

RUN pip install pipenv

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY [ "lambda_function.py", "model.py", "./" ]

CMD [ "lambda_function.lambda_handler" ]
