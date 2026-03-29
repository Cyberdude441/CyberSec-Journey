#!/usr/bin/env python3

"""
system-info-gatherer.py
------------------------
Collects and displays key system information:
  • OS type and version
  • IP address
  • Current username
  • Running process count
  • Disk usage
  • Network interfaces

Uses only Python standard library — no pip installs needed.
Usage: python3 system-info-gatherer.py
"""

import os
import sys
import socket
import platform
import datetime

# psutil gives richer process/disk/network info — use if available, else fallback
try:
    import psutil
    PSUTIL = True
except ImportError:
    PSUTIL = False


# ── display helpers ────────────────────────────────────────────────────────────

BOLD   = "\033[1m"
CYAN   = "\033[0;36m"
GREEN  = "\033[0;32m"
YELLOW = "\033[1;33m"
RED    = "\033[0;31m"
RESET  = "\033[0m"

def header(title: str):
    print(f"\n{BOLD}{CYAN}{'─' * 45}")
    print(f"  {title}")
    print(f"{'─' * 45}{RESET}")

def row(label: str, value: str):
    print(f"  {YELLOW}{label:<28}{RESET}{value}")


# ── info collectors ────────────────────────────────────────────────────────────

def get_os_info() -> dict:
    return {
        "OS":         platform.system(),
        "Release":    platform.release(),
        "Version":    platform.version()[:60],     # trim long kernel strings
        "Machine":    platform.machine(),
        "Processor":  platform.processor() or "N/A",
        "Python":     platform.python_version(),
    }


def get_hostname_and_ip() -> dict:
    hostname = socket.gethostname()
    try:
        # Connect to an external address (no packet actually sent) to find
        # the outbound interface IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        local_ip = "Unable to determine"

    return {
        "Hostname": hostname,
        "Local IP": local_ip,
    }


def get_username() -> str:
    # os.getlogin() can fail in some environments; fallback to env var
    try:
        return os.getlogin()
    except OSError:
        return os.environ.get("USER", os.environ.get("USERNAME", "Unknown"))


def get_process_count() -> str:
    if PSUTIL:
        count = len(psutil.pids())
        return str(count)

    # Fallback: count /proc entries on Linux
    if os.path.isdir("/proc"):
        pids = [d for d in os.listdir("/proc") if d.isdigit()]
        return str(len(pids))

    return "N/A (install psutil for this feature)"


def get_disk_usage() -> list:
    """Return a list of (mount, total_gb, used_gb, free_gb, percent) tuples."""
    results = []

    if PSUTIL:
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                results.append({
                    "mount":   part.mountpoint,
                    "total":   f"{usage.total / 1e9:.1f} GB",
                    "used":    f"{usage.used  / 1e9:.1f} GB",
                    "free":    f"{usage.free  / 1e9:.1f} GB",
                    "percent": f"{usage.percent}%",
                })
            except PermissionError:
                pass
    else:
        # Fallback: use os.statvfs on the root filesystem
        try:
            stat = os.statvfs("/")
            total   = stat.f_blocks * stat.f_frsize
            free    = stat.f_bfree  * stat.f_frsize
            used    = total - free
            percent = round((used / total) * 100, 1) if total > 0 else 0
            results.append({
                "mount":   "/",
                "total":   f"{total / 1e9:.1f} GB",
                "used":    f"{used  / 1e9:.1f} GB",
                "free":    f"{free  / 1e9:.1f} GB",
                "percent": f"{percent}%",
            })
        except Exception:
            pass

    return results


def get_network_interfaces() -> list:
    """Return list of (interface, ip) tuples."""
    interfaces = []

    if PSUTIL:
        for iface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                # AF_INET = IPv4
                if addr.family == socket.AF_INET:
                    interfaces.append((iface, addr.address))
    else:
        # Fallback: hostname-based single IP
        hostname = socket.gethostname()
        try:
            ip = socket.gethostbyname(hostname)
            interfaces.append((hostname, ip))
        except Exception:
            interfaces.append(("N/A", "Unable to determine"))

    return interfaces


# ── main ───────────────────────────────────────────────────────────────────────

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n{BOLD}{GREEN}")
    print("  ╔══════════════════════════════════════════╗")
    print("  ║       🖥️  SYSTEM INFO GATHERER            ║")
    print("  ╚══════════════════════════════════════════╝")
    print(f"{RESET}")
    print(f"  Scan time : {now}")
    print(f"  psutil    : {'✅ available (full data)' if PSUTIL else '❌ not installed (limited data)'}")

    # ── OS ────────────────────────────────────────────────────────────────────
    header("🖥️  OPERATING SYSTEM")
    for label, value in get_os_info().items():
        row(label, value)

    # ── user & network ────────────────────────────────────────────────────────
    header("👤  USER & NETWORK")
    row("Username", get_username())
    net = get_hostname_and_ip()
    for label, value in net.items():
        row(label, value)

    # ── processes ─────────────────────────────────────────────────────────────
    header("⚙️  PROCESSES")
    row("Running processes", get_process_count())

    # ── disk ─────────────────────────────────────────────────────────────────
    header("💾  DISK USAGE")
    disks = get_disk_usage()
    if disks:
        print(f"  {'Mount':<16} {'Total':>8}  {'Used':>8}  {'Free':>8}  {'Usage':>6}")
        print(f"  {'─'*16} {'─'*8}  {'─'*8}  {'─'*8}  {'─'*6}")
        for d in disks:
            print(f"  {d['mount']:<16} {d['total']:>8}  {d['used']:>8}  {d['free']:>8}  {d['percent']:>6}")
    else:
        print(f"  {YELLOW}No disk info available.{RESET}")

    # ── network interfaces ────────────────────────────────────────────────────
    header("🌐  NETWORK INTERFACES")
    ifaces = get_network_interfaces()
    if ifaces:
        for iface, ip in ifaces:
            row(iface, ip)
    else:
        print(f"  {YELLOW}No interface info available.{RESET}")

    # ── footer ────────────────────────────────────────────────────────────────
    print(f"\n{CYAN}{'─' * 45}{RESET}")
    print(f"  {GREEN}✅ Done!{RESET}  Install {YELLOW}psutil{RESET} for richer data.")
    print(f"  {CYAN}{'─' * 45}{RESET}\n")


if __name__ == "__main__":
    main()
