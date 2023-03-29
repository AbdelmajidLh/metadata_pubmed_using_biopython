#!/bin/bash

# Build the Docker image
docker build -t pubmed_scrapper .

# Run the Docker container
docker run -it -v . /app pubmed_scrapper