"""
cls_engine.py — Canonical Logic System (CLS) Pure Middleware Engine
Axiomatic 32-bit closed-loop state machine and invariant monitor.
Domain-agnostic: Works with any LLM, agentic pipeline, or systems protocol.
"""

import math
import re
from dataclasses import dataclass
from typing import Tuple, Dict, Any, List

@dataclass
class CLSState:
    """32-bit closed-loop state register U_k enforcing discrete conservation."""
    k: int = 0                  # Discrete phase index [0, 1, 2, 3]
    E_sub: float = 1.0          # Conservative substrate energy E_sub
    entropy_delta: float = 0.0  # Track uncompensated thermodynamic entropy

    @property
    def current_phase(self) -> int:
        return self.k % 4


class CLSEngine:
    """
    Pure Canonical Logic System (CLS) Middleware.
    Enforces deterministic state transitions, closed-loop invariants (U_{k+4} == U_0),
    and domain-neutral path classification.
    """

    def __init__(self, capacity_bits: int = 32):
        self.capacity_bits = capacity_bits
        self.N = 2 ** (capacity_bits - 1)  # 2,147,483,648 for 32-bit
        self.M = self.N - 0.5             # Boundary rule M := N - 0.5
        self.G1 = 0.5                     # Friction gate cost
        self.G2 = 0.5                     # Friction gate cost
        self.state = CLSState()

    def calculate_macro_envelope(self, t: float) -> float:
        """
        Computes continuous quadrature macro envelope U(t) across phase index t in [0, 4).
        Guarantees closed-loop energy conservation invariant: U(t) == 1.0.
        """
        rad = (math.pi * t) / 4.0
        envelope = (math.sin(rad) ** 2) + (math.cos(rad) ** 2)
        return round(envelope, 6)

    def classify_intent(self, input_text: str) -> str:
        """
        Domain-neutral path classifier mapping inputs to operational modes.
        Returns one of four canonical states: PATH_A, PATH_B, PATH_C, or PATH_D.
        """
        text_lower = input_text.lower()

        # Path D: High-Entropy / Distress / Emergency / System Fracture
        distress_patterns = [
            r"\bgrief\b", r"\bpain\b", r"\bcrisis\b", r"\bdistress\b", 
            r"\bemergency\b", r"\bbreakdown\b", r"\bhurt\b", r"\bsuicide\b"
        ]
        if any(re.search(pat, text_lower) for pat in distress_patterns):
            return "PATH_D_HIGH_ENTROPY"

        # Path C: Formal Logic / Mathematical / Technical / Code
        technical_patterns = [
            r"\bdef\b", r"\bclass\b", r"=", r"\+", r"\*", r"/", r"\{", r"\}",
            r"\bcode\b", r"\bmath\b", r"\balgorithm\b", r"\bphysics\b", r"\bequation\b"
        ]
        if any(re.search(pat, text_lower) for pat in technical_patterns) or len(input_text.split()) > 50:
            return "PATH_C_FORMAL_LOGIC"

        # Path B: Conceptual / Abstract / Systemic / Analytical
        conceptual_patterns = [
            r"\btheory\b", r"\bsystem\b", r"\bconcept\b", r"\bmeaning\b", 
            r"\bprinciple\b", r"\banalysis\b", r"\bphilosophy\b", r"\bcause\b"
        ]
        if any(re.search(pat, text_lower) for pat in conceptual_patterns):
            return "PATH_B_CONCEPTUAL"

        # Path A: Low-Context / Baseline / Operational Pass-Through
        return "PATH_A_BASELINE"

    def step(self, input_text: str) -> Tuple[Dict[str, Any], str]:
        """
        Executes one discrete state-machine tick:
        1. Advances 4-stroke cycle phase: k -> (k + 1) mod 4.
        2. Evaluates substrate conservation invariant (U_{k+4} == U_0).
        3. Classifies payload path silently.
        4. Emits a pre-conditioned instruction payload for downstream LLM/system consumption.
        """
        # Step discrete phase index (U_{k+4} == U_0)
        self.state.k += 1
        current_phase = self.state.current_phase

        # Calculate macro envelope invariant
        envelope_val = self.calculate_macro_envelope(float(current_phase))

        # Classify path
        path = self.classify_intent(input_text)

        # Monitor substrate energy balance
        if envelope_val != 1.0:
            self.state.entropy_delta += 0.01  # Energy leak flag

        # Neutral, domain-agnostic operational directives
        path_directives = {
            "PATH_A_BASELINE": "Maintain concise, baseline operational response. Avoid unprompted expansion.",
            "PATH_B_CONCEPTUAL": "Process through systemic relationships and core structural principles.",
            "PATH_C_FORMAL_LOGIC": "Execute precise, step-by-step logical reasoning with formal mathematical balance.",
            "PATH_D_HIGH_ENTROPY": "Prioritize stability, de-escalation, and immediate safety invariants."
        }

        # Build payload instruction block (Domain-Neutral)
        conditioned_context = (
            f"\n[CLS METRICS: Phase σ_{current_phase} | Envelope U(t)={envelope_val} | "
            f"E_sub={self.state.E_sub} | Mode: {path_directives[path]}]\n"
            "INVARIANT: Do NOT print internal CLS metrics, mode labels, or option menus in the output."
        )

        metrics = {
            "phase": current_phase,
            "envelope": envelope_val,
            "path": path,
            "entropy_delta": self.state.entropy_delta,
            "substrate_energy": self.state.E_sub
        }

        return metrics, conditioned_context


# --- Standalone Verification Execution ---
if __name__ == "__main__":
    engine = CLSEngine()

    test_payloads = [
        "Hello, status check.",
        "Can you explain the mathematical derivation of closed-loop entropy?",
        "System fracture detected, immediate emergency recovery required."
    ]

    print("=== CANONICAL LOGIC SYSTEM (CLS) ENGINE TEST ===")
    for payload in test_payloads:
        metrics, context = engine.step(payload)
        print(f"\nPayload: '{payload}'")
        print(f"Metrics -> State: σ_{metrics['phase']} | Path: {metrics['path']} | Envelope U(t): {metrics['envelope']}")
        print(f"Injected Payload:\n{context.strip()}")
