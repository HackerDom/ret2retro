all: build

build:
	docker build . -f Dockerfile.web -t ructf.ru/ret2retro-web:latest
