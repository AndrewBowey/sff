FROM python:3.8-slim-buster

WORKDIR /plansmart
COPY . /plansmart

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5555

ENTRYPOINT ["python3"]
CMD ["app.py"]
