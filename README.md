# Digital-Twin-for-Sustainable-Micro-Factories
### Hack For Green Bharat – Pathway Track

---

## Team Members
- Divyadharshini V  
- Athina K A  
- Adhirasree  

---

##  Problem Statement

Micro and MSME factories face:

- High energy consumption  
- Rising carbon emissions  
- Unplanned machine downtime  
- Lack of real-time intelligence  
- Expensive Industry 4.0 adoption  

We built a **low-cost, real-time AI-powered Digital Twin** system to optimize operations and improve sustainability.

---

#  Project Overview

This project simulates a **live Digital Twin of a micro-factory** using streaming data and real-time AI processing.

### Key Features

-  Real-time energy monitoring  
-  Overheating detection  
-  Production overload alerts  
-  Sustainability scoring (0–100)  
-  Live monitoring dashboard  

---

#  What is a Digital Twin?

A **Digital Twin** is a live virtual replica of a physical system that continuously receives data and optimizes operations.

In this project:


---

# System Architecture

## Factory Simulation Layer
Simulates IoT sensors generating:

- Temperature  
- Energy usage  
- Carbon emission  
- Production load  

Streaming source
Simulated Machines → Live Data Stream → Pathway AI Engine → Optimization Insights

---

##  Real-Time Streaming Engine (Pathway)

Built using the Pathway Framework.

Capabilities:

- Real-time ingestion  
- Stateful aggregation  
- Continuous recomputation  
- AI-based alert classification  
- Sustainability score calculation  

Outputs:

- `live_alerts.csv`  
- `live_sustainability.csv`  
- `live_energy_stats.csv`  

---

## AI Reasoning Layer

Alert Rules:

-  Temperature > 90 → CRITICAL TEMP  
-  Energy > 150 → HIGH ENERGY  
-  Load > 95 → OVERLOAD  

Sustainability Score Formula:
Score = 100 - (
(energy_usage / 200) * 30 +
(carbon_emission / 100) * 70
)

---

##  Real-Time Dashboard (Streamlit)

Displays:

-  Energy statistics  
-  Machine alerts  
-  Sustainability metrics  

---

#  Tech Stack

- Python  
- Pathway Framework  
- Streamlit  
- Pandas  
- CSV Streaming  
- WSL Environment  

---

#  Project Structure

---

# ⚙️ How to Run

##  Install Dependencies

```bash
pip install pathway streamlit pandas
python data_generator.py
python Digital_twin_engine.py
streamlit run Dashboard.py
