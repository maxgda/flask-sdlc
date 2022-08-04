# syntax=docker/dockerfile:1

FROM arm32v6/python:3.9-alpine as base

# gcc needed for python GPIO library
RUN apk update
RUN apk add python3-dev \
            gcc \
            libc-dev \
            libffi-dev

WORKDIR /app

# flask app env variable
ENV FLASK_APP=flaskr

COPY flaskr ./flaskr
COPY requirements/base.txt ./requirements/base.txt

FROM base as test

COPY requirements/test.txt ./requirements/test.txt
# only needed in test image
COPY pytest.ini ./pytest.ini
COPY .coveragerc ./.coveragerc
COPY tests ./tests

RUN pip3 install -r requirements/test.txt

# run linting
RUN ["flake8", "flaskr/"]
RUN ["flake8", "tests/"]
# run unit tests first, then integration tests
RUN ["coverage", "run", "-m", "pytest", "-m", "unit"]
RUN ["coverage", "run", "-m", "pytest", "-m", "integration"]
# of test covergae is under 80% the build will fail
RUN ["coverage", "report", "--fail-under", "80"]

FROM base as development

COPY requirements/dev.txt ./requirements/dev.txt

RUN pip3 install -r requirements/dev.txt

# flask startup command with debug
CMD ["flask", "--debug", "run", "--host=0.0.0.0"]

# this is not a valid production setup, just a demonstration
# use a production grade server for production
FROM base as production

COPY requirements/prod.txt ./requirements/prod.txt

RUN pip3 install -r requirements/prod.txt

# flask startup command
CMD ["flask", "run", "--host=0.0.0.0"]