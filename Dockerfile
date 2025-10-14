FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev build-essential

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

# collect static if any (skip if not configured)
# RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "community.wsgi:application", "--bind", "0.0.0.0:8000"]
