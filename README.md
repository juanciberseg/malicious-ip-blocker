# 🛡️ Malicious IP Blocker Automator (Python + UFW)

This project automates a basic **Incident Response (IR)** containment task on **Linux Mint/Ubuntu** environments. It reads a list of malicious IP addresses from a text file and automatically blocks them using the system's firewall, **UFW** (Uncomplicated Firewall).

## 🛠️ Demonstrated Skills

* **Python:** File handling, **List Comprehension**, and utilizing the `subprocess` library to execute system commands.
* **Linux/UFW:** Interaction with the **UFW** firewall for security configuration.
* **SOC Function:** Automation of repetitive **Incident Response (IR)** and containment tasks.

## 🚀 How to Use

1.  **Clone** this repository to your Linux Mint machine.
2.  **Populate** the `malicious_ips.txt` file with the list of IP addresses you wish to block (one IP per line).
3.  **Execute** the script from your terminal:
    ```bash
    chmod +x ip_blocker.py  # Give execution permission (optional but recommended)
    ./ip_blocker.py
    ```
    *Note: The script requires your administrator password because it uses the `sudo` command internally to modify the UFW rules.*

## Project Files

| File | Description |
| :--- | :--- |
| `ip_blocker.py` | The main Python script that handles the logic and UFW command execution. |
| `malicious_ips.txt` | The input file containing the list of IPs to be blocked. |
| `README.md` | This documentation file. |

## Evidence

* [View Script Execution and UFW Verification](Evidence/imagen.png)

## License
This project is licensed under the MIT License.
