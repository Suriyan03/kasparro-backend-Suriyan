# Makefile for Kasparro Backend

.PHONY: build up down test clean logs

# Build the Docker image
build:
	docker-compose build

# Start the application
up:
	docker-compose up -d

# Stop the application
down:
	docker-compose down

# Run the test suite
test:
	docker-compose run backend pytest

# View logs
logs:
	docker-compose logs -f

# Clean up docker artifacts
clean:
	docker-compose down -v
	docker system prune -f