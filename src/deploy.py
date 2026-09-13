import os
import subprocess
import sys
import time
import requests

REPO_URL = "https://github.com/StrangeBeeCorp/docker.git"
TARGET_DIR = "strangebee-docker"
THEHIVE_PATH = os.path.join(TARGET_DIR, "prod1-thehive")
WEB_URL = "http://localhost:9000"

def run_cmd(command, cwd=None):
    print(f"[+] Executing: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"[-] Command failed with exit code {result.returncode}")
        sys.exit(1)

if not os.path.exists(TARGET_DIR):
    print("Cloning")
    run_cmd(f"git clone {REPO_URL} {TARGET_DIR}")

print("Generating")
run_cmd("bash ./scripts/init.sh", cwd=THEHIVE_PATH)

print("Starting Docker Compose")
run_cmd("docker compose up -d", cwd=THEHIVE_PATH)

run_cmd("docker compose ps", cwd=THEHIVE_PATH)

print("\nSuccess!")