"""
flask_warmup_app.py — Generic Web/API Orchestrator Sample using CLS Middleware

Demonstrates how to integrate `cls_engine.py` into a web server or REST API pipeline:
1. Initializes `CLSEngine` as deterministic state middleware.
2. Exposes a `/process` endpoint for processing incoming payloads.
3. Exposes a `/warmup` endpoint for system health & calibration checks.
"""

import sys
import os
from flask import Flask, request, jsonify

# Resolve module paths regardless of execution directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from engine.cls_engine import CLSEngine
except ImportError:
    from cls_engine import CLSEngine

app = Flask(__name__)

# Initialize the global CLS State Engine instance
cls_middleware = CLSEngine(capacity_bits=32)


@app.route('/warmup', methods=['GET'])
def warmup_check():
    """System health and initial state calibration endpoint."""
    return jsonify({
        "status": "calibrated",
        "system": "Canonical Logic System (CLS)",
        "current_phase": f"σ_{cls_middleware.state.current_phase}",
        "substrate_energy": cls_middleware.state.E_sub,
        "capacity_bits": cls_middleware.capacity_bits
    }), 200


@app.route('/process', methods=['POST'])
def process_payload():
    """
    Primary payload processing endpoint:
    Steps the state machine, evaluates intent path, and returns pre-conditioned payload.
    """
    data = request.get_json(silent=True) or {}
    user_input = data.get("input", "").strip()

    if not user_input:
        return jsonify({"error": "No input payload provided."}), 400

    # Step state machine and evaluate invariants on CPU (<0.01ms)
    metrics, conditioned_context = cls_middleware.step(user_input)

    return jsonify({
        "status": "success",
        "metrics": metrics,
        "conditioned_context": conditioned_context,
        "input_processed": user_input
    }), 200


if __name__ == '__main__':
    print("Starting CLS Web Orchestrator Server on http://127.0.0.1:5000 ...")
    app.run(host='127.0.0.1', port=5000, debug=True)
