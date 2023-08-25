FROM python:3.9 AS builder

WORKDIR /app/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

FROM builder AS final
WORKDIR /app/
COPY src .

CMD [ "python", "./main.py" ]