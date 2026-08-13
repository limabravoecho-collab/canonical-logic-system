"""
python_orchestrator.py — Generic Canonical Logic System (CLS) Orchestrator Sample

This sample script demonstrates how to integrate `cls_engine.py` into a generic
AI pipeline, CLI tool, or agentic workflow. It acts as deterministic middleware:
1. Ingests user/visitor payloads.
2. Steps the 32-bit state machine (k mod 4, substrate energy tracking).
3. Classifies payload intent into canonical execution paths in <0.01ms.
4. Generates a pre-conditioned context block to steer downstream generation or logic.
"""

import sys
import os

# Ensure engine module can be resolved regardless of execution directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from engine.cls_engine import CLSEngine
except ImportError:
    from cls_engine import CLSEngine


def mock_llm_backend(conditioned_context: str, user_input: str) -> str:
    """
    Simulates a downstream generative LLM or execution protocol.
    In production, pass `conditioned_context + user_input` to your model (e.g., llama.cpp, OpenAI, Anthropic).
    """
    return f"[SYSTEM EXECUTION LAYER] Received pre-conditioned payload.\nProcessing input: '{user_input}'"


def run_orchestrator_loop():
    """Interactive CLI execution loop for testing CLS middleware calibration."""
    print("========================================================================")
    print("     CANONICAL LOGIC SYSTEM (CLS) — GENERIC ORCHESTRATOR SAMPLE        ")
    print("========================================================================")
    print("Type your input below to test state transitions and path routing.")
    print("Type 'exit' or 'quit' to terminate.\n")

    # Initialize the deterministic 32-bit CLS state machine
    cls = CLSEngine(capacity_bits=32)

    while True:
        try:
            user_input = input("User Payload > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("\nExiting CLS Orchestrator loop.")
                break

            # 1. Step the CLS State Machine (CPU Layer)
            metrics, conditioned_context = cls.step(user_input)

            # 2. Inspect Deterministic State Metrics
            print("\n--- [CLS CPU MIDDLEWARE METRICS] ---")
            print(f"Phase Index (k mod 4) : σ_{metrics['phase']}")
            print(f"Macro Envelope U(t)   : {metrics['envelope']}")
            print(f"Substrate Energy E_sub: {metrics['substrate_energy']}")
            print(f"Classified Path Mode  : {metrics['path']}")
            print(f"Entropy Delta         : {metrics['entropy_delta']}")

            # 3. View Pre-Conditioned Payload
            print("\n--- [INJECTED PRE-CONDITIONED PAYLOAD] ---")
            print(conditioned_context)

            # 4. Pass Payload to Downstream Execution Layer
            response = mock_llm_backend(conditioned_context, user_input)
            print("\n--- [SYSTEM RESPONSE] ---")
            print(response)
            print("-" * 72 + "\n")

        except KeyboardInterrupt:
            print("\nTerminated by user.")
            break


if __name__ == "__main__":
    run_orchestrator_loop()
