FROM python:3.12.1

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt --no-cache-dir --disable-pip-version-check

COPY ./ ./

EXPOSE 8000