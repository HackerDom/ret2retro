all: build

build:
	cd web && docker build . -f Dockerfile -t ructf.ru/ret2retro-web:latest
