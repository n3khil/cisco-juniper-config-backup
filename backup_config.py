import os
import yaml
from datetime import datetime
from netmiko import ConnectHandler

# Load devices from YAML
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)["devices"]

# Create backups folder if not exists
if not os.path.exists("backups"):
    os.makedirs("backups")

# Get timestamp
timestamp = datetime.now().strftime("%Y%m%d-%H%M")

for device in devices:
    try:
        print(f"Connecting to {device['name']} ({device['host']})...")
        connection = ConnectHandler(
            device_type=device["device_type"],
            host=device["host"],
            username=device["username"],
            password=device["password"]
        )

        # Choose command per vendor
        if "cisco" in device["device_type"]:
            output = connection.send_command("show running-config")
        elif "juniper" in device["device_type"]:
            output = connection.send_command("show configuration | display set")
        else:
            print(f"Unsupported device type: {device['device_type']}")
            continue

        # Save to file
        filename = f"backups/{device['name']}_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write(output)

        print(f"Backup saved: {filename}")

        connection.disconnect()

    except Exception as e:
        print(f"Failed to backup {device['name']}: {e}")
