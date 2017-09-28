FROM parity/parity:v1.7.2
MAINTAINER Ondrej Sika <ondrej@ondrejsika.com>
COPY . /app
ENTRYPOINT ["/app/entrypoint.sh"]

