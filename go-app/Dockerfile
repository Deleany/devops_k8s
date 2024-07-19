FROM golang:latest AS builder
LABEL maintainer="michaelhall.dev@gmail.com"
WORKDIR /app
COPY main.go /app
RUN app install gcc

ENV SERVER_BIND_ADDR ":8080"
EXPOSE 8080/tcp

ENTRYPOINT [ "executable" ]
CMD [ "executable" ]