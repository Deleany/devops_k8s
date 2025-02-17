FROM golang:latest AS builder
LABEL maintainer="michaelhall.dev@gmail.com"
WORKDIR /app
COPY main.go /app
RUN app install gcc
RUN go build -o /app/server

FROM alpine
COPY --from=builder /app/server /app/server
ENV SERVER_BIND_ADDR ":8080"
EXPOSE 8080/tcp

ENTRYPOINT [ "/app/server" ]
CMD [ "executable" ]
