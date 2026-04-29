import os
import time
import random

# -------------------------
# USER
# -------------------------
user_name = input("Enter operator name: ").strip().upper()


# -------------------------
# SIMPLE UTIL
# -------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def log(msg):
    print(f"[SIEM] {msg}")
    time.sleep(0.3)


def slow(msg):
    for c in msg:
        print(c, end="", flush=True)
        time.sleep(0.01)
    print("\n")


# -------------------------
# SECRET ENDING EFFECT
# -------------------------
def secret_ending():
    clear()
    slow(f"RECONNECTING TO OPERATOR: {user_name}...")
    time.sleep(1)

    slow("ACCESS GRANTED")

    for _ in range(6):
        print(f"[CRITICAL] SYSTEM OVERRIDE ACTIVE :: {user_name}")
        time.sleep(0.3)

    print("\nLasciate ogne speranza, voi ch'intrate.")
    print("[SYSTEM STATUS: IRRECOVERABLE COMPROMISE]")


# -------------------------
# NODES (SIMPLIFIED)
# -------------------------
nodes = {
    1: {
        "text": "SOC Alert: Unauthorized outbound traffic detected!",
        "logs": [
            "Unusual outbound connection detected from IoT device",
            "Possible C2 beacon pattern identified"
        ],
        "options": {
            "Isolate Device": 2,
            "Ignore Alert": 3,
            "Investigate Logs": 4
        }
    },

    2: {
        "text": "Device isolated. Traffic stopped.",
        "logs": ["Device quarantined from network"],
        "options": {
            "Analyze Device": 5,
            "Reset Device": 6
        }
    },

    5: {
        "text": "IoT Smart Light detected using default credentials.",
        "logs": ["Default credentials in use (admin/admin)"],
        "options": {
            "Change Credentials": 7,
            "Reset Device": 6
        }
    },

    6: {
        "text": "Device reset completed.",
        "ending": "REINFECTION"
    },

    7: {
        "text": "Credentials updated. Device secured.",
        "ending": "THREAT CONTAINED"
    },

    3: {
        "text": "More devices now show abnormal traffic.",
        "logs": ["Propagation suspected across network"],
        "options": {
            "Investigate Now": 8,
            "Keep Ignoring": 9
        }
    },

    9: {
        "text": "Network participating in DDoS attack.",
        "ending": "FULL COMPROMISE"
    },

    8: {
        "text": "Multiple devices compromised.",
        "options": {
            "Isolate Devices": 10,
            "Reset Network": 11
        }
    },

    10: {
        "text": "Partial containment achieved.",
        "ending": "PARTIAL CONTAINMENT"
    },

    11: {
        "text": "Network reset completed.",
        "ending": "RECOVERY WITH DAMAGE"
    },

    4: {
        "text": "Logs show repeated login attempts using default credentials.",
        "logs": ["Mirai-style brute force activity detected"],
        "options": {
            "Isolate Device": 2,
            "Continue Monitoring": 12
        }
    },

    12: {
        "text": "Traffic increasing across multiple devices.",
        "logs": ["Lateral movement suspected"],
        "options": {
            "Isolate Devices": 10,
            "Ignore": 9,
            "Escalate": 13
        }
    },

    13: {
        "text": "Device receiving command-and-control instructions.",
        "logs": ["C2 beacon established"],
        "options": {
            "Continue": 14,
            "Isolate Device": 10
        }
    },

    14: {
        "text": "Credential reuse detected across systems.",
        "logs": ["Lateral movement confirmed"],
        "options": {
            "Emergency Response": 15,
            "Continue": 15
        }
    },

    15: {
        "text": "Systems losing control.",
        "options": {
            "Emergency Shutdown": 16,
            "Attempt Recovery": 16
        }
    },

    16: {
        "text": "Systems no longer respond to commands.",
        "ending": "SECRET"
    }
}


# -------------------------
# GAME LOOP
# -------------------------
def play():
    node_id = 1

    while True:
        clear()
        node = nodes[node_id]

        print(f"SOC CONSOLE | OPERATOR: {user_name}\n")
        print(node["text"])

        # logs (simple)
        for entry in node.get("logs", []):
            log(entry)

        # ending
        if "ending" in node:
            print(f"\nENDING: {node['ending']}")
            if node["ending"] == "SECRET":
                time.sleep(1)
                secret_ending()
            break

        # options
        options = list(node["options"].keys())

        print("\nOptions:")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        # input
        while True:
            try:
                choice = int(input("\nSelect: ")) - 1
                if 0 <= choice < len(options):
                    break
            except:
                pass

        node_id = node["options"][options[choice]]


# -------------------------
# START
# -------------------------
play()