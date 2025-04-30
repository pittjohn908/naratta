default: help

help:
	@echo Developer commands:
	@echo
	@echo " run				Run narrata server"
	@echo "  build              Build the project"
	@echo "  clean              Clean the docker-compose data""
	@echo "  serve              Start the docker-compose"
	@echo "  stop               Stop the docker-compose"

run:
	fastapi dev server/app/server.py

## -------------- DOCKER COMPOSE ---------

.PHONY: build serve stop clean

build:
	docker-compose build --no-cache

serve:
	docker-compose up -d --build

stop:
	docker-compose down

clean:
	docker-compose down -v