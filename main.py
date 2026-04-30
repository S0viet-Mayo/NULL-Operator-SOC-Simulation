import os
import time

# -------------------------
# Username
# -------------------------
user_name = input("Enter operator name: ").strip().upper()


# -------------------------
# UI Util
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
# Effect For Secret Ending
# -------------------------
def secret_ending():
    clear()

    slow(f"RECONNECTING TO OPERATOR: {user_name}...")
    time.sleep(1.2)

    slow("...connection unstable...")
    time.sleep(1)

    slow(f"I see you, {user_name}.")
    time.sleep(1.5)

    slow("ACCESS GRANTED")
    time.sleep(1)

    for i in range(8):
        print(f"[CRITICAL] SYSTEM OVERRIDE ACTIVE :: {user_name}")
        time.sleep(0.25)

    time.sleep(1)
    print("\n" + "=" * 60)

    slow("All systems are considered untrusted...")
    time.sleep(1.2)

    slow("Containment has failed...")
    time.sleep(1.5)

    slow("Administrative control revoked.")
    time.sleep(1.5)

    print("\n" * 2)

    slow("Lasciate ogne speranza, voi ch'intrate.")
    time.sleep(2)

    print("\n" + "=" * 60)
    slow("ENDING: IRRECOVERABLE COMPROMISE")

    print("\n" * 2)
    input("Press Enter to terminate session...")

    clear()
# -------------------------
# Story Nodes
# -------------------------

nodes = {
    1: {
        "text": "SOC Alert: Unauthorized outbound traffic detected!",
        "logs": [
            "Unusual outbound connection detected from IoT device",
            "Possible C2 beacon pattern identified"
        ],
        "explanation": "Unusual outbound traffic is often an early indicator of compromise. Devices may be attempting to communicate with a command-and-control (C2) server.",
        "options": {
            "Isolate Device": 2,
            "Ignore Alert": 3,
            "Investigate Logs": 4
        }
    },

    2: {
        "text": "You Isolate the device from the network. Outbound Traffic stops immediately.",
        "logs": ["Device quarantined from network"],
        "explanation": "Isolating a compromised device prevents it from communicating with command-and-control (C2) servers and limits further spread across the network.",
        "options": {
            "Analyze Device": 5,
            "Reset Device": 6
        }
    },

    5: {
        "text": "You analyze the isolated device. It appears to be an IoT device (Smart Lights in this case) using default credentials.",
        "logs": ["Default credentials in use (admin/admin)"],
        "options": {
            "Change Credentials": 7,
            "Reset Device": 6
        }
    },

    6: {
        "text": "Device reset completed.",
        "explanation": "Some IoT malware is non-persistent (Like Mirai) and can be temporarily removed by rebooting a device. However, if the underlying vulnerability is not fixed, the device can be quickly reinfected.",
        "ending": "REINFECTION"
    },

    7: {
        "text": "Credentials updated. Device secured.",
        "explanation": "Changing default credentials is one of the most effective ways to prevent reinfection. Many botnets rely entirely on weak or unchanged passwords.",
        "ending": "THREAT CONTAINED"
    },

    3: {
        "text": "5 minutes later: Multiple devices now show abnormal traffic.",
        "logs": ["Propagation suspected across network"],
        "options": {
            "Investigate Now": 8,
            "Keep Ignoring": 9
        }
    },

    9: {
        "text": "You ignore the alerts. Traffic spikes dramatically across the network. External reports indicate your network is participating in a DDoS attack. Your boss is NOT happy!",
        "explanation": "Ignoring early warning signs allows attackers to expand their presence. At this stage, compromised devices are likely participating in coordinated botnet activity.",
        "ending": "FULL COMPROMISE"
    },

    8: {
        "text": "You begin investigating after noticing widespread anomalies. Several devices now show signs of compromise",
        "explanation": "Late detection reduces the effectiveness of response efforts. By this stage, attackers may have already achieved lateral movement across the network.",
        "options": {
            "Isolate Devices": 10,
            "Reset Network": 11
        }
    },

    10: {
        "text": "You isolate infected devices, but the attack has already spread",
        "ending": "PARTIAL CONTAINMENT"
    },

    11: {
        "text": "You reset the network and remove infected devices",
        "explanation": "Resetting network infrastructure can disrupt botnet communication, but may not fully eliminate compromised devices if vulnerabilities remain.",
        "ending": "RECOVERY WITH DAMAGE"
    },

    4: {
        "text": "The logs show repeated login attempts using default credentials. (This suggest early-stage botnet scanning)",
        "logs": ["Mirai-style brute force activity detected"],
        "explanation": "Repeated login attempts using default credentials are a common indicator of Mirai-style botnet activity. These attacks scan large numbers of devices for weak access points.",
        "options": {
            "Isolate Device": 2,
            "Continue Monitoring": 12
        }
    },

    12: {
        "text": "You continue monitoring the device. Traffic increases and new outbound connections appear. Multiple login attempts are detected across other devices.",
        "logs": ["Lateral movement suspected"],
        "explanation": "Delaying action allows botnet malware to propagate. IoT infections can spread rapidly across devices sharing weak or reused credentials.",
        "options": {
            "Isolate Devices": 10,
            "Ignore": 9,
            "Continue Monitoring All Activity": 13
        }
    },

    13: {
        "text": "You continue monitoring without taking action. Outbound Traffic patterns stabilize into consistent intervals. The device is no longer scanning randomly. It appears to be receiving comand-and-control instructions",
        "logs": ["C2 beacon established"],
        "explanation": "Consistent outbound traffic patterns suggest the device has established communication with a command-and-control server and is now receiving instructions.",
        "options": {
            "Continue Monitoring": 14,
            "Isolate Device": 10
        }
    },

    14: {
        "text": "New Alerts Appear across multiple devices. \nAuthentication logs show successful logins across the network using reused credentials. \nInternal traffic between devices increases significantly",
        "logs": ["Lateral movement confirmed"],
        "explanation": "Credential reuse enables attackers to move laterally between devices, significantly increasing the scope of compromise.",
        "options": {
            "Isolate Devices": 10,
            "Reset Network": 11,
            "Continue Monitoring": 15
        }
    },

    15: {
        "text": "Multiple systems begin initiating outbound connections simultaneously. Configuration changes are detected across devices. Some systems no longer respond to admin commands",
        "explanation": "At this stage, attackers may have established persistence and altered system configurations, limiting the effectiveness of defensive actions.",
        "options": {
            "Emergency Isolation": 17,
            "Initiate Full Network Shutdown ": 17,
            "Continue Monitoring Activity": 16,
            "Attempt to regain control of affected systems": 17
        }
    },

    16: {
        "text": "All systems are considered untrusted. \nContainment has failed.",
        "explanation": "Administrative control has been lost. Systems can no longer be reliably managed or trusted.",
        "ending": "SECRET"
    },

    17: {
        "text": "You attempt emergency isolation procedures. However multiple systems fail to respond. \nSome devices appear to have altered configurations and ignore shutdown commands. \nThe attack has already established persistent access. \nYour response has limited effect...",
        "explanation": "Persistent compromise allows attackers to maintain control even during active response efforts, rendering traditional mitigation ineffective.",
        "options": {
            "Attempt full shutdown": 16,
            "Do nothing": 16
        }
    }
}


# -------------------------
# Engine
# -------------------------
def play():
    node_id = 1

    while True:
        clear()

        # Safety check (prevents crashes)
        if node_id not in nodes:
            print(f"[ERROR] Node {node_id} does not exist.")
            break

        node = nodes[node_id]

        # -------------------------
        # SOC Header
        # -------------------------
        print(f"SOC CONSOLE | OPERATOR: {user_name}\n")
        print(node.get("text", "[NO TEXT FOUND]"))

        # -------------------------
        # SIEM Log Logic
        # -------------------------
        for entry in node.get("logs", []):
            log(entry)

        # -------------------------
        # Analyst Notes (Explanations)
        # -------------------------
        if node.get("explanation"):
            print("\n[ANALYST NOTE]")
            slow(node["explanation"])
            time.sleep(0.8)

        # -------------------------
        # Ending Logic
        # -------------------------
        if "ending" in node:
            print("\n" + "=" * 60)

            ending = node["ending"]

            if ending == "SECRET":
                secret_ending()
            else:
                print(f"ENDING: {ending}")
                print("=" * 60)

            input("\nPress Enter to exit...")
            break

        # -------------------------
        # Option Logic
        # -------------------------
        options = node.get("options", {})

        if not options:
            print("\n[NO OPTIONS AVAILABLE — TERMINATING]")
            break

        option_keys = list(options.keys())

        print("\nOptions:")
        for i, opt in enumerate(option_keys, 1):
            print(f"{i}. {opt}")

        # -------------------------
        # Input Saftey
        # -------------------------
        choice = None

        while choice is None:
            try:
                raw = input("\nSelect: ").strip()
                idx = int(raw) - 1

                if 0 <= idx < len(option_keys):
                    choice = option_keys[idx]
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Enter a number.")

        # -------------------------
        # Node Transitioning
        # -------------------------
        node_id = options[choice]


# -------------------------
# Game Start
# -------------------------
if __name__ == "__main__":
    play()