# Version: 1

FROM python:buster

RUN mkdir app && \
    mkdir app/engine

COPY generator/random_generator.py /app
COPY engine/*.py /app/engine/

WORKDIR /app

RUN pip install requests

CMD ["python", "random_generator.py"]

