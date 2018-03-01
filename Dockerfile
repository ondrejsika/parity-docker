FROM parity/parity:v1.9.4
MAINTAINER Ondrej Sika <ondrej@ondrejsika.com>
COPY . /app
VOLUME /ethereum
ENTRYPOINT ["/app/entrypoint.sh"]

