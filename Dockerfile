FROM python:3.9

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

WORKDIR /app
COPY ./ ./

RUN pip install --no-cache-dir -r requirements/prod.txt

CMD ["make", "app"]