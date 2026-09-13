# 1. Prerequisites — WSL 2 and Docker Desktop

TheHive stack runs as Linux containers. On Windows that means WSL 2 plus Docker Desktop using
the WSL 2 backend.

## 1.1 Install WSL 2

In an **Administrator** PowerShell or Command Prompt:

```powershell
wsl --install
```

## 1.2 Install Docker Desktop

Download the **AMD64** installer from [docker.com](https://www.docker.com/products/docker-desktop/).

![Docker Desktop download page](images/01-docker-desktop-download.png)

During installation, tick **Use WSL 2 instead of Hyper-V**. This is what lets the containers
share the WSL 2 kernel instead of running a separate VM.

![WSL 2 backend option](images/02-wsl2-backend-option.png)

At the sign-in prompt, click **Skip** — a Docker account is not required for this deployment.

![Skip sign-in](images/03-skip-signin.png)

## 1.3 Enable the required Windows features

If WSL 2 or Docker Desktop reports that virtualization is unavailable, enable the platform
features manually. In an **Administrator** Command Prompt:

```cmd
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

![Enable Virtual Machine Platform](images/04-enable-virtual-machine-platform.png)

```cmd
bcdedit /set hypervisorlaunchtype auto
```

![Enable hypervisor launch type](images/05-enable-hypervisor-launch.png)

**Reboot the machine** — neither change takes effect until restart.

## 1.4 Verify

Start Docker Desktop and confirm the engine reports **Running** in the bottom-left status bar.

![Docker Desktop running](images/06-docker-desktop-running.png)

Confirm the Docker CLI is reachable from inside WSL:

```bash
wsl
docker version
```

If `docker version` prints both Client and Server sections, WSL integration is working and you
can continue to [deployment](02-deployment.md).
