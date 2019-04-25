#!/bin/bash

docker build -t proto .
docker run -p 5000:5000 proto