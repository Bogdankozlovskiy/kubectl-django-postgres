FROM gcr.io/google_appengine/python

RUN virtualenv -p python3 /env
ENV PATH /env/bin:$PATH

ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /app/requirements.txt
ADD . /app
WORKDIR /app/typical_django_project/

CMD ["sh", "-c", "python run_server.py gunicorn typical_django_project.wsgi:application -b 0.0.0.0:80"]
EXPOSE 80