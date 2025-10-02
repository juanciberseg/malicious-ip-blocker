#!/usr/bin/env python3
import subprocess
import sys

# File containing the malicious IP addresses, one per line
IP_FILE = 'malicious_ips.txt'
# Base UFW command to deny traffic from an IP
UFW_COMMAND_BASE = ['sudo', 'ufw', 'deny', 'from']

def block_ip(ip_address):
    """
    Executes the command 'sudo ufw deny from [ip_address] to any' to block the IP.
    """
    # Construct the full UFW command
    command = UFW_COMMAND_BASE + [ip_address, 'to', 'any']
    
    print(f"-> Attempting to block IP: {ip_address}...")
    
    try:
        # Execute the command. 'check=True' will raise an exception on command failure.
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # If no error was raised, the block was (likely) successful
        print(f"   ✅ Block successful. Message: {result.stdout.strip()}")
        
    except subprocess.CalledProcessError as e:
        # Handles errors from the UFW command itself (e.g., if the rule already exists)
        # Note: UFW often returns an error code if the rule is a duplicate.
        print(f"   ❌ ERROR blocking {ip_address}: Command failed.")
        print(f"      UFW Message: {e.stderr.strip()}")
    
    except FileNotFoundError:
        # Handles the rare case where the 'ufw' command itself is not found
        print("   ❌ ERROR: The 'ufw' command was not found. Ensure UFW is installed and in your PATH.")
        sys.exit(1) # Terminate the script

def main():
    """
    Main function to read the IP list and process the blocks.
    """
    blocked_count = 0
    
    print("==============================================")
    print(f"  MALICIOUS IP BLOCKER AUTOMATOR (Python + UFW)")
    print("==============================================")

    try:
        # Open the IP file in read mode ('r')
        with open(IP_FILE, 'r') as f:
            # Read all lines, strip whitespace, and ignore empty lines
            ip_list = [line.strip() for line in f if line.strip()]
    
    except FileNotFoundError:
        print(f"ERROR: File '{IP_FILE}' not found.")
        print("Ensure the file exists in the same directory.")
        return # Exit the function

    if not ip_list:
        print("Warning: The IP file is empty. Nothing to block.")
        return

    print(f"🔥 Found {len(ip_list)} IPs to process.")
    print("-" * 30)

    for ip in ip_list:
        # Call the block function for each IP
        block_ip(ip)
        blocked_count += 1
        
    print("-" * 30)
    print(f"✨ Process complete. Attempted to block {blocked_count} IPs.")
    print("==============================================")

# Ensure the 'main' function only runs when the script is executed directly
if __name__ == "__main__":
    main()