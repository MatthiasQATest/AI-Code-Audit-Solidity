# safe_rce_simulation.py
#
# This file simulates patterns commonly associated with RCE
# for defensive testing purposes only.
#
# It does NOT execute arbitrary remote commands.

import logging
import subprocess
import socket
import base64
import os

logging.basicConfig(level=logging.INFO)

def suspicious_patterns():
    logging.info("Starting simulated RCE behavior")

    # Encoded payload simulation
    fake_payload = base64.b64encode(b"whoami").decode()
    logging.info(f"Encoded payload detected: {fake_payload}")

    # Simulated network callback
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect(("127.0.0.1", 4444))
    except Exception:
        pass
    finally:
        s.close()

    # Benign subprocess execution
    # Fixed command only — NOT user-controlled
    subprocess.run(
        ["echo", "Simulated command execution"],
        capture_output=True,
        text=True
    )

    # Simulated environment access
    logging.info(f"PATH length: {len(os.environ.get('PATH', ''))}")

if __name__ == "__main__":
    suspicious_patterns()
