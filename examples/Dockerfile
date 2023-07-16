FROM python:3

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src .
COPY ./entrypoint.sh /

ENV PORT 8000
ENV HOST 0.0.0.0

CMD [ "sh", "-c", "streamlit run --server.port ${PORT} --server.address ${HOST} /app/app.py" ]
