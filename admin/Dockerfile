FROM python:3.10-buster
ENV PIPENV_VENV_IN_PROJECT=1

WORKDIR /app
ADD ./app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN python -m manage.py
