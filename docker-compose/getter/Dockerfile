# Version: 1

# FROM python_uni_image:latest
FROM crenom/python_uni_image:latest

RUN mkdir app && \
    mkdir app/engine

COPY getter.py /app
COPY engine/*.py /app/engine/
COPY docker-compose/getter/boot.sh /app

WORKDIR /app

RUN chmod 777 boot.sh

EXPOSE 5000

# CMD ["python", "availability_service.py"]
ENTRYPOINT ["./boot.sh"]

# docker build . -t av_service
# docker run --rm -d --name av_service -p 5000:5000 -e DBNAME=test_db -e HOST=10.1.7.192 -e PORT=5432 -e USER=testu -e PASSWORD=admin av_service



