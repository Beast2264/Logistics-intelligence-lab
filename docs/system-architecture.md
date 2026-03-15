# Logistics Intelligence Lab — System Architecture

## Overview

The Logistics Intelligence Lab is a fleet operations intelligence environment designed to explore dispatch monitoring, telemetry pipelines, and AI-assisted logistics analysis.

The system is currently focused on fleet operations intelligence and is structured around four core layers:

1. Fleet Data Modeling
2. Dispatch Monitoring
3. Telemetry Pipeline
4. AI Decision Support

---

## High-Level Architecture

```text
Fleet Data Models
(drivers, trucks, trailers, routes, assignments)
            │
            ▼
Dispatch Dashboard
(Python + Flask + HTML/CSS)
            │
            ▼
Fleet Monitoring Interface
(status, assignments, live summary, auto refresh)
            │
            ├──────────────► AI Route Risk Analyzer
            │                  (route risk scoring)
            │
            ▼
Telemetry Pipeline
(MQTT → Telegraf → InfluxDB → Grafana)

