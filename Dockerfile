FROM parity/parity:v1.7.10
MAINTAINER Ondrej Sika <ondrej@ondrejsika.com>
COPY . /app
VOLUME /ethereum
ENTRYPOINT ["/app/entrypoint.sh"]

