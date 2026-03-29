#!/usr/bin/env python3

"""
port-scanner.py
---------------
A simple TCP port scanner for ports 1-1024.
Usage: python3 port-scanner.py
"""

import socket
import time
import sys
from datetime import datetime


# ── helpers ────────────────────────────────────────────────────────────────────

def print_banner():
    print("=" * 50)
    print("        PYTHON PORT SCANNER")
    print("=" * 50)


def validate_ip(ip: str) -> bool:
    """Return True if ip is a valid IPv4 address or resolvable hostname."""
    try:
        socket.gethostbyname(ip)   # also handles hostnames
        return True
    except socket.error:
        return False


def scan_port(ip: str, port: int, timeout: float = 0.5) -> bool:
    """
    Try to connect to ip:port.
    Returns True if the port is open, False otherwise.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))   # 0 = success (port open)
        sock.close()
        return result == 0
    except socket.error:
        return False


def get_service_name(port: int) -> str:
    """Try to resolve the well-known service name for a port."""
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


# ── main ───────────────────────────────────────────────────────────────────────

def main():
    print_banner()

    # ── get target ──────────────────────────────────────────────────────────
    target = input("\n[?] Enter target IP or hostname: ").strip()

    if not target:
        print("[!] No target provided. Exiting.")
        sys.exit(1)

    if not validate_ip(target):
        print(f"[!] Cannot resolve '{target}'. Check the address and try again.")
        sys.exit(1)

    # Resolve to IP for display
    resolved_ip = socket.gethostbyname(target)

    # ── scan settings ───────────────────────────────────────────────────────
    START_PORT = 1
    END_PORT   = 1024

    print(f"\n[*] Target   : {target} ({resolved_ip})")
    print(f"[*] Port range: {START_PORT} – {END_PORT}")
    print(f"[*] Started  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    open_ports = []
    start_time = time.time()

    # ── scan loop ────────────────────────────────────────────────────────────
    try:
        for port in range(START_PORT, END_PORT + 1):
            # Simple progress indicator every 100 ports
            if port % 100 == 0:
                elapsed = time.time() - start_time
                print(f"    Scanning port {port}... ({elapsed:.1f}s elapsed)", end="\r")

            if scan_port(resolved_ip, port):
                service = get_service_name(port)
                open_ports.append((port, service))
                # Print immediately so user sees results live
                print(f"  [OPEN]  Port {port:5d}  →  {service}")

    except KeyboardInterrupt:
        print("\n\n[!] Scan interrupted by user.")

    # ── results ──────────────────────────────────────────────────────────────
    end_time  = time.time()
    duration  = end_time - start_time

    print("\n" + "=" * 50)
    print("           SCAN RESULTS")
    print("=" * 50)
    print(f"  Target      : {target} ({resolved_ip})")
    print(f"  Ports scanned: {START_PORT}–{END_PORT}")
    print(f"  Open ports  : {len(open_ports)}")
    print(f"  Time taken  : {duration:.2f} seconds")
    print("-" * 50)

    if open_ports:
        print(f"  {'PORT':<8} {'SERVICE'}")
        print(f"  {'----':<8} {'-------'}")
        for port, service in open_ports:
            print(f"  {port:<8} {service}")
    else:
        print("  No open ports found in range 1–1024.")

    print("=" * 50)


if __name__ == "__main__":
    main()
