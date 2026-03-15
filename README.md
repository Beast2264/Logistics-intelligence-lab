# Logistics Intelligence Lab

Fleet telemetry, dispatch monitoring, and logistics analytics platform designed to explore how modern data systems and artificial intelligence can improve transportation operations.

This project simulates components commonly found in enterprise logistics technology platforms used by large transportation networks.

---

## Project Overview

The Logistics Intelligence Lab was created to study real-world logistics challenges such as fleet visibility, dispatch coordination, and operational monitoring.

The lab integrates several technologies used in modern logistics platforms including telemetry pipelines, monitoring dashboards, and structured fleet asset modeling.

---

## Purpose

The goal of the Logistics Intelligence Lab is to better understand how modern data infrastructure and AI technologies can improve fleet visibility, dispatch coordination, and transportation efficiency.

---

## System Architecture

The Logistics Intelligence Lab simulates a real-world fleet telemetry and dispatch monitoring environment.

Components include:

- **Fleet Telemetry Simulator** – Generates synthetic GPS and vehicle data
- **Telemetry Pipeline** – Processes incoming fleet data
- **Dispatch Dashboard** – Displays active vehicles and operational metrics
- **Grafana Telemetry Map** – Visualizes fleet movement geographically
- **Proxmox Lab Infrastructure** – Hosts the virtual lab environment including security and monitoring systems

For detailed technical architecture, see:

- [System Architecture](docs/system-architecture.md)
- [Lab Environment](docs/lab-environment.md)
- [Real World Logistics Problems](docs/real-world-logistics-problems.md)

---

## Technology Stack

This lab environment uses several technologies to simulate a real-world logistics analytics platform:

- **Python** – telemetry simulation and backend logic
- **Flask** – dispatch dashboard application
- **Grafana** – fleet visualization dashboards
- **Proxmox VE** – virtualization infrastructure
- **Linux** – service and lab operating environment
- **Networking tools** – pfSense firewall and virtual networking
- **MQTT / Telegraf / InfluxDB** – telemetry ingestion and analytics pipeline

- ## Project Structure

Key components of the repository:

| Directory | Purpose |
|----------|---------|
| ai-tools | AI experiments including route risk analysis |
| dispatch-dashboard | Flask-based fleet dispatch monitoring UI |
| telemetry-pipeline | Telemetry ingestion architecture documentation |
| fleet-data | Fleet asset data models |
| supply-chain-model | Logistics network modeling concepts |
| docs | System architecture and infrastructure documentation |
| screenshots | Visual examples of dashboards and infrastructure


---

## Key Capabilities

This lab environment demonstrates several operational intelligence capabilities commonly used in modern logistics platforms:

- fleet telemetry ingestion and monitoring
- dispatch visibility and operational dashboards
- AI-assisted route risk analysis
- infrastructure monitoring within a virtualized environment
- simulated fleet operations and asset modeling

The project is designed as a research and learning environment for transportation analytics and logistics system architecture


## System Screenshots

### Dispatch Dashboard
![Dispatch Dashboard](screenshots/Dispatch-Dashboard_.jpg)

### Fleet Telemetry Map
![Fleet Telemetry](screenshots/Grafana_telemetry.jpg)

### Lab Infrastructure
![Proxmox Lab](screenshots/Proxmox-Lab.jpg)

---

## Documentation

Additional project documentation:

- [System Architecture](docs/system-architecture.md)
- [Lab Environment](docs/lab-environment.md)
- [Real World Logistics Problems](docs/real-world-logistics-problems.md)

---

## Research Focus

The lab explores how artificial intelligence and data systems can improve logistics decision-making through:

- fleet telemetry analysis
- dispatch monitoring systems
- transportation analytics
- operational intelligence dashboards
- AI-assisted logistics operations
