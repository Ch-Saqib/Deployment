# Deploying a Docker Container from GitHub Actions

This repository is configured to automatically build and deploy a Docker container using GitHub Actions. Follow the steps below to set up and customize the deployment process.

## Prerequisites

- Ensure you have a Docker Hub account or access to a container registry.
- Store your Docker credentials (username, password, and email) as GitHub secrets:
  - `DOCKER_HUB_USERNAME`
  - `DOCKER_HUB_ACCESS_TOKEN`
  - `AZURE_CREDENTIALS`

## Workflow Overview

The GitHub Actions workflow is configured to trigger on a `push` or `pull_request` event to the `main` branch. It performs the following steps:

1. **Checkout the Code**: Pulls the code from the repository.
2. **Set Up Docker**: Installs Docker and logs into the Docker registry.
3. **Build the Docker Image**: Builds the Docker image using the `Dockerfile` in the root directory.
4. **Push the Docker Image**: Pushes the built image to Docker Hub or your specified container registry.

## Example GitHub Actions Workflow

Here's an example of a GitHub Actions workflow (`.github/workflows/deploy.yml`) that deploys a Docker container:

```yaml
name: Deploy to Azure Container Apps

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1

      - name: Log in to Docker Hub
        run: |
          echo ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }} | docker login -u ${{ secrets.DOCKER_HUB_USERNAME }} --password-stdin

      - name: Build and push Docker image
        run: |
          docker build -t ${{ secrets.DOCKER_HUB_USERNAME }}/your docker hub image name:latest ./your code directory name
          docker push ${{ secrets.DOCKER_HUB_USERNAME }}/your docker hub image name:latest
   

      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Deploy to Azure Container Apps
        run: |
          az containerapp update \
            --name your azure container name \
            --resource-group your azure resource group name \
            --image ${{ secrets.DOCKER_HUB_USERNAME }}/your docker hub image name:latest

```
## After This You can create a Image with the following Command ##
```bash
docker buildx build --platform linux/amd64 -t $DOCKERHUB_USERNAME/IMAGE_NAME:latest --push .
```
  - This Command Creates a Image and also Push This Image to Docker Hub
  - After This When Its Creates Image or Pushed To Docker Hub
  - Then You Can Copy Docker Hub Username and Docker Hub Access Token


## References ##
 - Github Action : <a>https://docs.github.com/en/actions/about-github-actions/understanding-github-actions</a>

