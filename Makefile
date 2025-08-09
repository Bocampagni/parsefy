APP_NAME := fastapi-template
CMD_DIR := app/main.py

.PHONY: all help install dev lint format docker-build docker-run docker-stop clean

all: dev

help:
	@echo "Available commands:"
	@echo "  install      - Install dependencies with uv"
	@echo "  dev          - Run FastAPI development server"
	@echo "  lint         - Run ruff linter"
	@echo "  format       - Format code with ruff"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run   - Run Docker container"
	@echo "  docker-stop  - Stop running Docker container"
	@echo "  clean        - Clean up Docker images and containers"

install:
	uv sync

dev:
	uv run fastapi dev ${CMD_DIR} --reload

lint:
	uv run ruff check .

format:
	uv run ruff format .
	uv run ruff check --fix .
	uv run ruff check --select I --fix .

docker-build:
	docker build -t ${APP_NAME} .

docker-run:
	docker run -d --name ${APP_NAME} -p 80:80 ${APP_NAME}

docker-stop:
	docker stop ${APP_NAME} || true
	docker rm ${APP_NAME} || true

clean: docker-stop
	docker rmi ${APP} || true
	docker system prune -f
