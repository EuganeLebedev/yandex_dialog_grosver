FROM laudio/pyodbc:1.0.37-sqlcmd
ENV TZ=Europe/Minsk

WORKDIR /usr/src/app
COPY app.py requirements.txt
RUN pip install -r ./requirements.txt

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["python -m flask run --host=0.0.0.0 --cert=cert.pem --key=privkey.pem "]