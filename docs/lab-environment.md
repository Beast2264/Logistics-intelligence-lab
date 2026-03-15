# Lab Environment

The Logistics Intelligence Lab runs inside a virtualized infrastructure hosted on **Proxmox VE**.

This environment simulates a small-scale enterprise infrastructure used to support fleet telemetry, analytics, and security testing.

---

## Virtualization Platform

**Proxmox Virtual Environment**

The Proxmox host manages all virtual machines used in the lab.

Capabilities include:

- Virtual machine orchestration
- Network segmentation
- Storage management
- Snapshot and rollback testing
- Security lab isolation

---

## Virtual Machines

The lab currently includes the following systems:

### Infrastructure

| VM ID | System | Purpose |
|------|--------|---------|
| 200 | FLEET-CORE | Core services and fleet simulation |
| 201 | fleet-telemetry01 | Telemetry pipeline services |

### Security & Network Lab

| VM ID | System | Purpose |
|------|--------|---------|
| 100 | security-ubuntu | Security monitoring and testing |
| 101 | kali | Penetration testing toolkit |
| 102 | pfsense | Firewall and network routing |
| 103 | metasploitable | Vulnerable system for security testing |
| 104 | ubuntu-vuln-server01 | Vulnerability analysis environment |

---

## Network Design

The virtual machines communicate through segmented virtual networks managed by Proxmox and pfSense.

This allows simulation of:

- fleet telemetry traffic
- internal service communication
- security testing scenarios
- monitoring pipelines

---

## Lab Purpose

The environment is designed to explore the intersection of:

- logistics technology
- fleet telemetry systems
- infrastructure observability
- cybersecurity testing
- AI-assisted logistics operations

This setup allows experimentation with real-world system architecture patterns used by modern logistics technology platforms.



