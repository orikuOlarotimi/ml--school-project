IMAGE_NAME = plant-disease-api
# Replace with your actual Docker Hub username or registry URL
REGISTRY_USER = codepraycode 
TAG = latest

.PHONY: build run push all

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME):$(TAG) .

# Run the Docker container locally
run:
	docker run -p 5000:5000 $(IMAGE_NAME):$(TAG)

# Tag the image for the registry
tag:
	docker tag $(IMAGE_NAME):$(TAG) $(REGISTRY_USER)/$(IMAGE_NAME):$(TAG)

# Push the image to the registry
push: tag
	docker push $(REGISTRY_USER)/$(IMAGE_NAME):$(TAG)

# One-shot command to build and push
all: build push
