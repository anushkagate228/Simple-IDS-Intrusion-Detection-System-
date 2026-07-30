import json
import re
import logging

# Create log file
logging.basicConfig(
    filename="ids.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Load rules from rules.json
with open("rules.json", "r") as file:
    rules = json.load(file)

print("===== Simple Intrusion Detection System =====")

while True:
    message = input("\nEnter Network Data (type exit to stop): ")

    if message.lower() == "exit":
        print("IDS Stopped")
        break

    attack_found = False

    for rule in rules:
        if re.search(rule, message, re.IGNORECASE):
            print("\nALERT! Intrusion Detected")
            print("Matched Rule:", rule)

            logging.info(
                "Attack Detected | Rule: %s | Data: %s",
                rule,
                message
            )

            attack_found = True
            break

    if not attack_found:
        print("No Attack Detected")