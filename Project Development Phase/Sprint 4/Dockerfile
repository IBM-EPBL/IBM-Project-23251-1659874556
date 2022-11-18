FROM python:3.7

COPY requirements.txt /opt/python/requirements.txt
RUN pip install -r /opt/python/requirements.txt \
 && rm -rf /opt/python && pip install gunicorn==20.1.0

COPY app /opt/app

EXPOSE 8000

WORKDIR /opt/app
CMD gunicorn --bind 0.0.0.0:8000 --access-logfile - --error-logfile - run:app