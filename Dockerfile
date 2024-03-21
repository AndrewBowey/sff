from alpine:latest
RUN apk add --no-cache py3-pip \
    && pip3 install --upgrade pip

WORKDIR /plansmart
COPY . /plansmart

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5555

ENTRYPOINT ["python3"]
CMD ["app.py"]
