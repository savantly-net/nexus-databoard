#!/bin/bash

RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${RED}Be sure to login to Heroku first: heroku container:login${NC}"

# Exit on any error
set -e

docker buildx build --platform linux/amd64 -t registry.heroku.com/stellar-data-tools/web . --push
heroku container:release web -a stellar-data-tools