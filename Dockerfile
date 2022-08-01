# syntax=docker/dockerfile:1

FROM arm32v6/python:3.9-alpine as base

WORKDIR /app

# flask app env variable
ENV FLASK_APP=flaskr

COPY flaskr ./flaskr
COPY requirements/base.txt ./requirements/base.txt

FROM base as test

COPY requirements/test.txt ./requirements/test.txt
# only needed in test image
COPY tests ./tests

RUN ["pip3", "install", "-r", "requirements/test.txt"]

# run tests
RUN ["flake8", "flaskr/"]
RUN ["pytest"]

FROM base as development

COPY requirements/dev.txt ./requirements/dev.txt

RUN pip3 install -r requirements/dev.txt

# flask startup command
CMD ["flask", "run", "--host=0.0.0.0"]

FROM base as production

COPY requirements/prod.txt ./requirements/prod.txt

RUN pip3 install -r requirements/prod.txt

# flask startup command
CMD ["flask", "run", "--host=0.0.0.0"]