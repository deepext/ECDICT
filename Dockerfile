FROM python:3
ARG ENV

ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

ENV ENV ${ENV}

RUN mkdir ./temp -p
EXPOSE 5000

CMD ["python", "server.py"]