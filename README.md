# TheHive SOC Deployment

A reproducible, container-based deployment of [TheHive](https://strangebee.com/thehive/) — the
open-source Security Incident Response Platform (SIRP) — built from scratch on Windows 11 /
Windows Server using **WSL 2 + Docker Desktop**, with a small Python deployer that automates
the clone → init → compose-up sequence.

The result is a working SOC case-management stack with a dedicated `SOC` organization and a
non-privileged analyst account, ready for incident intake and triage.

---

## What this repository contains

| Path | Purpose |
| --- | --- |
| `src/deploy.py` | Python deployer — clones the StrangeBee compose repo, runs `init.sh`, brings the stack up, prints container status |
| `Dockerfile` | Builds `hive-deployer`, a slim Python image that carries the deployer and the Docker CLI |
| `docs/01-prerequisites.md` | WSL 2, Virtual Machine Platform, Hyper-V and Docker Desktop setup |
| `docs/02-deployment.md` | Building the deployer image and bringing TheHive up |
| `docs/03-user-management.md` | Creating the `SOC` organization and analyst accounts |
| `docs/04-operations.md` | Day-to-day start / stop / logs / teardown |
| `docs/images/` | Annotated screenshots from each step |

## Architecture

```
Windows host
└── Docker Desktop (WSL 2 backend)
    └── WSL 2 (Ubuntu)  ~/hive
        ├── hive-deployer image ....... runs src/deploy.py
        └── strangebee-docker/prod1-thehive
            └── docker compose stack
                ├── thehive ........... SIRP web app  → http://localhost:9000
                ├── cassandra ......... case / observable store
                ├── elasticsearch ..... search index
                └── minio ............. attachment object storage
```

The deployer does not reimplement the stack — it drives StrangeBee's officially maintained
[`prod1-thehive`](https://github.com/StrangeBeeCorp/docker) compose bundle so the deployment
stays on a supported upgrade path.

## Quick start

Prerequisites: Windows with WSL 2 and Docker Desktop running (see
[`docs/01-prerequisites.md`](docs/01-prerequisites.md)).

```bash
# inside WSL 2
git clone https://github.com/<your-username>/thehive-soc-deployment.git ~/hive
cd ~/hive

docker build -t hive-deployer .
python3 src/deploy.py
```

Then open <http://localhost:9000/login>.

First-run credentials are TheHive's documented defaults — `admin@thehive.local` / `secret`.
**Change them immediately**; see [`docs/02-deployment.md`](docs/02-deployment.md#first-login).

Full walkthrough: [`docs/02-deployment.md`](docs/02-deployment.md).

## Security notes

- No credentials, certificates, or generated secrets are committed. `scripts/init.sh` in the
  StrangeBee bundle generates them locally at deploy time, and `.gitignore` keeps the cloned
  bundle and any `.env` out of version control.
- Every password shown in the documentation is a placeholder. Replace them with your own.
- This stack binds to `localhost` and is intended for a lab or an internal SOC segment. Put it
  behind a reverse proxy with TLS and real authentication before exposing it.

## Documentation

1. [Prerequisites — WSL 2 and Docker Desktop](docs/01-prerequisites.md)
2. [Deployment](docs/02-deployment.md)
3. [Organization and user management](docs/03-user-management.md)
4. [Operations](docs/04-operations.md)
