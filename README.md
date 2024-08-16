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
name: Deploy Docker Container

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Log in to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Set up QEMU
      uses: docker/setup-qemu-action@v2

    - name: Build and Push Docker Image
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ secrets.DOCKER_USERNAME }}/my-container:${{ github.sha }}

    - name: Log out of Docker Hub
      run: docker logout
```
## After This You can create a Image with the following Command ##
```bash
docker buildx build --platform linux/amd64 -t $DOCKERHUB_USERNAME/IMAGE_NAME:latest --push .
```
  - This Command Creates a Image and also Push This Image to Docker Hub
  - After This When Its Creates Image or Pushed To Docker Hub
  - Then You Can Copy Docker Hub Username and Docker Hub Access Token

