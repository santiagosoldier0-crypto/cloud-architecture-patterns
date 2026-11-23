# 08. Bastion

**ES.** `ssh_config.example` muestra un salto SSH desde un equipo administrador a una instancia privada mediante Bastion Host. La configuración es una plantilla: IPs, clave y hosts deben existir. No se crean instancias ni se abre acceso AWS en esta demostración.

**EN.** `ssh_config.example` demonstrates an SSH jump from an administrator workstation to a private instance through a Bastion Host. It is a template; the IPs, key, and hosts must exist. This demo creates no instances or AWS access rules.

```mermaid
flowchart LR
  A[Admin] -->|SSH 22| B[Bastion público]
  B -->|SSH 22 privado| P[EC2 privada]
```

For a real deployment, allow inbound port 22 to the bastion only from a trusted administrator IP; allow port 22 to the private host only from the bastion security group; keep the private host without a public IP; use a restricted key and disable password login. Copy and edit the sample as `~/.ssh/config`, then run `ssh private`. This requires provisioned AWS hosts and incurs charges; not executed here. No service to stop.

**GitHub:** [add repository URL]
