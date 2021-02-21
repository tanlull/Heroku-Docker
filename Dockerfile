FROM continuumio/anaconda3

ENV PORT 8080

WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt
CMD uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}