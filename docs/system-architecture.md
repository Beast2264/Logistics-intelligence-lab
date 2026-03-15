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

---

## Core Components

### 1. Fleet Data Models
Structured JSON files represent the operational state of the fleet.

Entities include:

- Drivers
- Trucks
- Trailers
- Routes
- Assignments

These datasets are used to simulate fleet operations and dispatch workflows.

---

### 2. Dispatch Dashboard
The dispatch dashboard is built using Python and Flask.

Current functionality includes:

- Fleet status visibility
- Driver, truck, and trailer monitoring
- Active assignment display
- Status color coding
- Auto-refresh every 10 seconds
- Fleet summary metrics

---

### 3. Telemetry Pipeline
The telemetry pipeline simulates real-time fleet monitoring.

Architecture:

- MQTT broker for telemetry messaging
- Telegraf for metric ingestion
- InfluxDB for time-series storage
- Grafana for telemetry visualization

---

### 4. AI Route Risk Analyzer
The AI Route Risk Analyzer evaluates dispatch routes and estimates operational risk.

Example factors include:

- Number of stops
- Distance
- Driver hours remaining
- Operational complexity

---

## Purpose

The purpose of this project is to explore how transportation operations can be improved through:

- better fleet visibility
- dispatch monitoring
- telemetry analytics
- AI-assisted logistics decision support

---

## Future Expansion

Possible future enhancements:

- interactive dispatch controls
- route assignment from the UI
- route risk scoring displayed in dashboard
- shipment-level visibility
- facility and warehouse nodes
- broader supply chain analytics
