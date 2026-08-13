# Canonical Logic System (CLS)
> An axiomatic 32-bit nested closed-loop logic framework for AI reasoning calibration, data protocol design, and biological homeostasis modeling.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## Overview

The **Canonical Logic System (CLS)** defines the geometry, mechanics, and operational rules of a Nested Closed-Loop System. It uses integer boundaries ($2^{32} - 1$), $N-0.5$ floating-point friction gates ($G_1, G_2 = 0.5$), and forced substrate energy conservation ($\Delta E_{\text{sub}} = 0$) to drive deterministic, recursive state transitions ($U_{k+4} \equiv U_0$).

This repository is an open-source framework intended for computer scientists, systems engineers, corporate research teams, logic artists, autistic savants, and multi-disciplinary researchers. It provides a non-ordinary, scale-invariant lens to evaluate complex, closed-loop physical, biological, and digital systems.

---

## Key Architecture: Deterministic Hybrid Middleware

While CLS can be ingested directly by Large Language Models (LLMs) as a raw system prompt specification, its highest-performing implementation is as an **executable middleware script** (`cls_engine.py`).

```text
Visitor Input / Data Packet
         │
         ▼
[ cls_engine.py ]  <-- Deterministic CPU Layer (Python / C)
         │  • Phase Index Tracking: k (mod 4)
         │  • Substrate Energy Balance: ΔE_sub = 0
         │  • Instant Sub-Millisecond Path Classification
         │  • Hard Invariant / Safety Gate Execution
         ▼
[ LLM / Interface ] <-- Generative / Display Layer
            • Ingests pre-conditioned CLS metrics payload
            • Synthesizes output in target persona or protocol format
