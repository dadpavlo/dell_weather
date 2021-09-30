FROM python:3.9

RUN mkdir -p /usr/src/server/
WORKDIR /usr/src/server/

COPY . /usr/src/server/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "server.py"]