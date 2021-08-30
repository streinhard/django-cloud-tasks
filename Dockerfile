FROM alpine:3.14

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /app

COPY /tests/requirements.txt .

RUN apk update &&\
    apk add --no-cache py3-pip py3-gunicorn &&\
    pip3 install --no-cache-dir -r requirements.txt &&\
    pip3 uninstall -y pip &&\
    find /usr/lib/python* | grep '__pycache__' | xargs -n1 rm -rf &&\
    find /usr/lib/python*/ -type d | grep '/locale/' | grep -v 'LC_MESSAGES$' | grep -v '/en' | xargs -n1 rm -rf &&\
    find /usr/lib/python*/ -type d | grep '/static/' | xargs -n1 rm -rf

COPY tests/ /app/
COPY django_cloud_tasks/ /app/django_cloud_tasks/
RUN ./manage.py migrate

CMD gunicorn --bind :8080 --workers 1 --threads 4 testapp.wsgi:application