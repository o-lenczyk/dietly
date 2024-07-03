FROM python:3.12.4-slim-bookworm

ADD dietly /dietly
ADD keys/client-cert.pem keys/client-cert.pem
ADD keys/server-ca.pem keys/server-ca.pem

ADD dietly/requirements.txt requirements.txt

RUN pip install -r requirements.txt 

EXPOSE 8080

CMD python /dietly/manage.py runserver 0.0.0.0:8080 --noreload
