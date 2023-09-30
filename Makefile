
PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VERSION := $(shell cat VERSION)
TAGGED_VERSION := $(VERSION)
NEXT_VERSION := $(shell echo $(VERSION) | awk -F. '{$$NF = $$NF + 1;} 1' | sed 's/ /./g')

GIT_COMMIT := $(shell git rev-parse --short HEAD)

default : setup

.PHONY: setup
setup: 
	@echo "Setting up..."
	@echo "Creating virtual environment..."
	@python -m venv .venv
	@echo "Installing dependencies..."
	@source .venv/bin/activate && \
	pip3 install -r requirements.txt
	@echo "Done!"
	@echo "Run 'source .venv/bin/activate' to activate the virtual environment."

.PHONY: run
run:
	@echo "Running..."
	@streamlit run ./src/Home.py

.PHONY: dev
dev:
	@echo "Running in dev mode ..."
	@docker compose up --build

.PHONY: build
build:
	@echo "Cleaning dist folder..."
	@rm -rf dist
	@echo "Building..."
	@python3 -m build
	@echo "Done!"


.PHONY: docs
docs:
	@echo "Generating docs"
	docker run --rm --volume "$(PROJECT_DIR)/helm:/helm-docs:rw" jnorwood/helm-docs:latest
	git add helm/README.md

.PHONY: ensure-git-repo-pristine
ensure-git-repo-pristine:
	@echo "Ensuring git repo is pristine"
	@[[ $(shell git status --porcelain=v1 2>/dev/null | wc -l) -gt 0 ]] && echo "Git repo is not pristine" && exit 1 || echo "Git repo is pristine"

.PHONY: bump-version
bump-version:
	@echo "Bumping version to $(NEXT_VERSION)"
	@echo $(NEXT_VERSION) > VERSION
	git add VERSION


.PHONY: update-chart-yaml-with-version
update-chart-yaml-with-next-version:
	@echo "Updating Chart.yaml with version $(VERSION)"
	sed "s/version:.*/version: $(VERSION)/" ./helm/Chart.yaml > ./helm/Chart.yaml.tmp
	mv ./helm/Chart.yaml.tmp ./helm/Chart.yaml
	sed "s/appVersion:.*/appVersion: $(TAGGED_VERSION)/" ./helm/Chart.yaml > ./helm/Chart.yaml.tmp
	mv ./helm/Chart.yaml.tmp ./helm/Chart.yaml
	git add helm/Chart.yaml


.PHONY: release
release: ensure-git-repo-pristine docs bump-version update-chart-yaml-with-next-version
	@echo "Preparing release..."
	@echo "Version: $(VERSION)"
	@echo "Commit: $(GIT_COMMIT)"
	@echo "Image Tag: $(IMAGE_TAG)"
	git tag -a $(TAGGED_VERSION) -m "Release $(VERSION)"
	git push origin $(TAGGED_VERSION)
	@echo "Tag $(TAGGED_VERSION) created and pushed to origin"
	git commit -m "Released $(VERSION) and prepared for $(NEXT_VERSION)"


# https://stackoverflow.com/a/10858332/1308685
# Check that given variables are set and all have non-empty values,
# die with an error otherwise.
#
# Params:
#   1. Variable name(s) to test.
#   2. (optional) Error message to print.
check_defined = \
    $(strip $(foreach 1,$1, \
        $(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
    $(if $(value $1),, \
      $(error Undefined $1$(if $2, ($2))))