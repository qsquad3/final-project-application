FROM python:3.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/

ENV DB_HOST=10.0.3.14
ENV DB_NAME=user
ENV DB_USER=user
ENV DB_PASSWD=password

RUN pip install  --no-cache-dir -r src/requirements.txt

CMD ["python","/usr/src/app/app.py"]
