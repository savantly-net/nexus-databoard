# Savantly Databoard

Build a data application fast

## Quick Start

```
streamlit run src/Home.py
```

### Clone

Clone the repository

Create a virtual python environment to isolate dependency versions.  

```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### Docker Compose
Run the docker compose file to spin up the docker image.  

```shell
docker compose up --build
```


# TODO

- [x] Add POSTGRES to the docker-compose
- [ ] Seed POSTGRES from the `db/seed.sql`

