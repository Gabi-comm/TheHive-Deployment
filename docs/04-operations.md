# 4. Operations

## 4.1 Start the stack

Start Docker Desktop, then from a Command Prompt:

```cmd
wsl
```

```bash
cd ~/hive/strangebee-docker/prod1-thehive
docker compose up -d
```

Open <http://localhost:9000/login>.

## 4.2 Check status

```bash
docker compose ps
```

All services should report `Up`. TheHive depends on Cassandra, Elasticsearch, and MinIO — if
TheHive is restarting, check those first.

## 4.3 Logs

```bash
docker compose logs -f thehive
docker compose logs --tail=100 cassandra
```

## 4.4 Stop the stack

Stop the containers but keep all data:

```bash
docker compose stop
```

Remove the containers, keeping the named volumes:

```bash
docker compose down
```

## 4.5 Teardown

> **Destructive.** This deletes every case, observable, and attachment in the deployment.

```bash
docker compose down -v
```

## 4.6 Redeploy from scratch

```bash
cd ~/hive
rm -rf strangebee-docker
python3 deploy.py
```

The deployer re-clones the bundle, regenerates secrets via `init.sh`, and brings a clean stack
up.

## 4.7 Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| `permission denied` on `./scripts/init.sh` | Scripts not executable after clone | `chmod +x scripts/*.sh` |
| Files owned by `root` in `strangebee-docker/` | Clone created by a root process | `sudo chown -R "$USER:$USER" ~/hive/strangebee-docker` |
| `503` or blank page on port 9000 | Cassandra/Elasticsearch still starting | Wait ~60s, then `docker compose logs -f thehive` |
| `Cannot connect to the Docker daemon` in WSL | Docker Desktop not running, or WSL integration off | Start Docker Desktop → Settings → Resources → WSL Integration |
| Port 9000 already in use | Another service bound to it | Stop it, or remap the published port in the compose file |
