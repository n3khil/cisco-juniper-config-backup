# Cisco & Juniper Config Backup Automation

## 📌 Overview
This project automates the process of taking configuration backups from Cisco IOS and Juniper devices using **Python + Netmiko**.  
It connects via SSH, runs the appropriate command, and saves the output in a timestamped file.

## 🛠 Features
- Multi-vendor support (Cisco, Juniper)
- YAML-based device inventory
- Timestamped backups
- Simple and extendable

## 📂 Project Structure
```plaintext
cisco-juniper-config-backup/
│
├─ devices.yaml        # Device inventory with IPs, credentials, and vendor type
├─ backup.py           # Main script to run backups
├─ utils.py            # Helper functions for SSH connections and file handling
├─ logs/               # Logs of backup runs
├─ backups/            # Directory where backup files are stored
├─ requirements.txt    # Python dependencies
└─ README.md           # Project documentation
