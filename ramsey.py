#!/usr/bin/env python3

import argparse
import logging
import os
import subprocess
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

log_file = os.path.join(LOG_DIR, "ramsey.log")
logging.basicConfig(
    filename=log_file,
    filemode='a',
    format='[%(asctime)s] %(levelname)s: %(message)s',
    level=logging.INFO
)

def banner():
    print(r"""
   ____                                 _     
  |  _ \ __ _ _ __ ___  _ __   ___  ___| |__  
  | |_) / _` | '__/ _ \| '_ \ / _ \/ __| '_ \ 
  |  _ < (_| | | | (_) | | | |  __/\__ \ | | |
  |_| \_\__,_|_|  \___/|_| |_|\___||___/_| |_|

  > Ramsey-Huub - Termux Automation Toolkit
  > Created by Stuck Idg
    """)

def ping_target(target):
    try:
        print(f"[+] Pinging {target}...")
        subprocess.run(["ping", "-c", "4", target], check=True)
        logging.info(f"Pinged {target} successfully.")
    except subprocess.CalledProcessError:
        logging.error(f"Failed to ping {target}")
        print("[-] Ping failed.")

def main():
    banner()
    parser = argparse.ArgumentParser(description="Ramsey-Huub CLI Tool")
    parser.add_argument("--ping", help="Ping a target IP or domain")
    args = parser.parse_args()

    if args.ping:
        ping_target(args.ping)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
