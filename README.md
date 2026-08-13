```text
# Canonical Logic System (CLS)
> An axiomatic 32-bit nested closed-loop logic framework for AI reasoning calibration, data protocol design, and biological homeostasis modeling.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## Overview

The **Canonical Logic System (CLS)** defines the geometry, mechanics, and operational rules of a Nested Closed-Loop System. It uses integer boundaries (2³² - 1), N - 0.5 floating-point friction gates (G₁ = G₂ = 0.5), and forced substrate energy conservation (ΔE_sub = 0) to drive deterministic, recursive state transitions (U_{k+4} ≡ U₀).

This repository provides a non-ordinary, scale-invariant mathematical framework intended for computer scientists, systems engineers, research teams, logic artists, and multi-disciplinary developers evaluating closed-loop physical, biological, or digital systems.

---

## Key Architecture: Executable Deterministic Middleware

The core implementation of CLS operates as an **executable middleware script** (`cls_engine.py`), offloading discrete state logic, energy conservation tracking, and path classification directly to the CPU.

```text
Incoming Data / Visitor Payload
               │
               ▼
      [ cls_engine.py ]  <-- Deterministic CPU Layer (Python / C)
               │  • Phase Index Tracking: k (mod 4)
               │  • Substrate Energy Balance: ΔE_sub = 0
               │  • Sub-millisecond Path & Safety Classification
               │  • Invariant Enforcement
               ▼
[ Downstream LLM / Agent / Protocol ] <-- Generative / Display Layer
                  • Ingests pre-conditioned CLS state metrics
                  • Executes output generation or routing

```

### Note on `canonical_logic_system.txt`

The raw specification file (`system_prompt/canonical_logic_system.txt`) is preserved in this repository solely as an **archival reference document**. Because `cls_engine.py` executes the entire 32-bit state machine, friction calculations, and phase transformations directly in Python code, inserting the full text prompt into LLM context windows is **functionally redundant** and no longer required.

---

## Target Applications & Use Cases

* **AI Reasoning Calibration & Guardrails:** Enforces deterministic state transitions, path routing, and zero-hallucination bounds in local or cloud LLM agentic pipelines.
* **Data & Communication Protocols:** Offers a zero-loss, 32-bit state-machine architecture for low-latency packet routing, loss-free data transmission, and clock synchronization.
* **Cellular & Cognitive Equilibrium Medicine:** Serves as a mathematical reference model for studying metabolic homeostasis, local energy containment, phase lag recovery, and neural stability in biological systems.
* **Physics & Complex Systems Analysis:** Provides a discrete geometric lens for examining closed-loop thermodynamic engines, macro drag (τ_macro), and scale-invariant substrate systems.

---

## Repository Structure

```text
├── LICENSE
├── README.md
├── system_prompt/
│   └── canonical_logic_system.txt   # Archival specification (Redundant; replaced by cls_engine.py)
├── engine/
│   └── cls_engine.py               # Executable Python middleware (sub-ms CPU state machine)
├── examples/
│   ├── python_orchestrator.py      # Sample: Standalone CLI/Agent pipeline integrating CLS
│   └── flask_warmup_app.py         # Sample: Web app/API server integrating CLS state middleware

```

---

## Integration Samples

This repository includes two sample integration scripts demonstrating how to activate `cls_engine.py` within your own workflows:

1. **`examples/python_orchestrator.py`**
A generic command-line and agent orchestrator showing how to initialize `CLSEngine`, step the 4-stroke cycle (k mod 4), capture metrics, and pass pre-conditioned context payloads to an LLM or decision backend.
2. **`examples/flask_warmup_app.py`**
A lightweight Web/API server sample showing how to wrap `cls_engine.py` in a HTTP or WebSocket pipeline to dynamically calibrate state per request or user session.

---

## Quick Start (Python)

```python
from engine.cls_engine import CLSEngine

# Initialize the 32-bit CLS State Engine
cls = CLSEngine()

# Step the state machine with an incoming payload
payload = "Evaluate closed-loop system state."
metrics, conditioned_context = cls.step(payload)

print(f"Current Phase: σ_{metrics['phase']}")
print(f"Path Mode:     {metrics['path']}")
print(f"Injected Payload:\n{conditioned_context}")

```

---

## 🤝 Open Source & License

This framework is open-source software made available under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You are free to share, adapt, and build upon this architecture for academic, personal, or commercial use with attribution.

```

```
