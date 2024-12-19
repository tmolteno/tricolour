docker_build:
	docker build --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) -f python312.docker --tag tmolteno/tricolour:latest .

docker_run:
	docker run -it tmolteno/tricolour:latest

push:
	docker push tmolteno/tricolour:latest
