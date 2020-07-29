# Version: 1

FROM python:buster

RUN mkdir app && \
    mkdir app/engine

COPY getter.py /app
COPY engine/*.py /app/engine/
COPY docker-compose/getter/boot.sh /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN chmod 777 boot.sh

EXPOSE 5000

# CMD ["python", "getter.py"]
ENTRYPOINT ["./boot.sh"]

