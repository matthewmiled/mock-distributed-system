FROM python:3.10
RUN pip3 install pipenv
RUN apt-get update && apt-get install nginx
COPY Pipfile Pipfile.lock /app/
WORKDIR /app
RUN pipenv install
COPY . /app/
CMD ["pipenv", "run", "gunicorn", "-c", "python:webserver.gunicorn_config", "webserver.wsgi:app"]