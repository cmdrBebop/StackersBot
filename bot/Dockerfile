FROM python:3.10-alpine
ENV BOT_NAME=$BOT_NAME
ENV PIPENV_VENV_IN_PROJECT=1
ENV PYTHONUNBUFFERED=1

COPY Pipfile .
COPY Pipfile.lock .
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --deploy

COPY . .
