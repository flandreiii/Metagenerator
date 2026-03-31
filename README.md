```
  ███╗   ███╗███████╗████████╗ █████╗  ██████╗ ███████╗███╗   ██╗
  ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝████╗  ██║
  ██╔████╔██║█████╗     ██║   ███████║██║  ███╗█████╗  ██╔██╗ ██║
  ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║
  ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝███████╗██║ ╚████║
  ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
```

<div align="center">

**msfvenom payload generator for Termux · Kali proot**

[![made-with-python](https://img.shields.io/badge/Made%20with-Python%203-1f425f?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Android-black?style=for-the-badge&logo=android&logoColor=3DDC84)](https://termux.dev/)
[![kali](https://img.shields.io/badge/Requires-Kali%20proot-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)](https://www.kali.org/)
[![license](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support%20my%20work-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/flandreiii)

> **⚠️ For educational and authorized penetration testing use only.**  
> Always get written permission before testing any device or network you don't own.

</div>

---

## 📖 What is Metagenerator?

**Metagenerator** is a terminal-based Python tool built for **Termux on Android** that streamlines the entire msfvenom payload workflow — from installing Kali Linux proot to generating ready-to-deploy payloads with a clean, numbered interface. No more memorizing msfvenom syntax. Just pick, configure, generate.

Built and maintained by **[flandreiii](https://github.com/flandreiii)**.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🖥️ **Friendly TUI** | Numbered payload menu grouped by platform — no syntax memorization needed |
| 📦 **Auto Installer** | Installs proot-distro → Kali Linux → Metasploit in one flow |
| 🎯 **23 Payloads** | Covers Android, Windows, Linux, macOS, PHP, Python, Java |
| 📍 **Custom Output Path** | Save payloads anywhere, including `/sdcard/Download/` |
| 🔌 **Listener Helper** | Prints the exact `msfconsole` handler command after generation |
| ✅ **Status Check** | Shows msfvenom install status on every launch |

---

## 📋 Requirements

- Android phone with **[Termux](https://termux.dev/)** installed
- Python 3 (`pkg install python`)
- ~3–5 GB free storage (for Kali proot)
- WiFi connection (for installation)

---

## 🚀 Installation & Usage

### 1 — Clone or download

```bash
# option A: download directly
curl -o ~/metagenerator.py https://raw.githubusercontent.com/flandreiii/metagenerator/main/metagenerator.py

# option B: clone the repo
git clone https://github.com/flandreiii/metagenerator
cd metagenerator
```

### 2 — Run it

```bash
python3 ~/metagenerator.py
```

### 3 — First time? Install Kali + Metasploit

Select **option 2** from the main menu. Metagenerator will:

```
[1/4]  pkg install proot-distro
[2/4]  proot-distro install kali
[3/4]  apt install metasploit-framework  (inside Kali)
[4/4]  Create ~/bin/msfvenom wrapper
```

> ⏱️ This takes 20–60 minutes depending on your connection.

After install, run:
```bash
source ~/.bashrc
python3 ~/metagenerator.py
```

---

## 🎯 Payload List

### 🤖 Android
| # | Payload | Description |
|---|---|---|
| 1 | `android/meterpreter/reverse_tcp` | APK reverse shell (TCP) |
| 2 | `android/meterpreter/reverse_https` | APK reverse shell (HTTPS) |
| 3 | `android/shell/reverse_tcp` | APK dumb shell (TCP) |

### 🪟 Windows
| # | Payload | Description |
|---|---|---|
| 4 | `windows/meterpreter/reverse_tcp` | x86 Meterpreter reverse TCP |
| 5 | `windows/meterpreter/reverse_https` | x86 Meterpreter reverse HTTPS |
| 6 | `windows/meterpreter/bind_tcp` | x86 Meterpreter bind TCP |
| 7 | `windows/shell_reverse_tcp` | x86 dumb shell reverse TCP |
| 8 | `windows/x64/meterpreter/reverse_tcp` | x64 Meterpreter reverse TCP |
| 9 | `windows/x64/meterpreter/reverse_https` | x64 Meterpreter reverse HTTPS |
| 10 | `windows/x64/shell_reverse_tcp` | x64 dumb shell reverse TCP |
| 11 | `windows/x64/powershell_reverse_tcp` | x64 PowerShell reverse TCP |

### 🐧 Linux
| # | Payload | Description |
|---|---|---|
| 12 | `linux/x86/meterpreter/reverse_tcp` | x86 Meterpreter reverse TCP |
| 13 | `linux/x64/meterpreter/reverse_tcp` | x64 Meterpreter reverse TCP |
| 14 | `linux/x86/shell_reverse_tcp` | x86 dumb shell reverse TCP |
| 15 | `linux/x64/shell_reverse_tcp` | x64 dumb shell reverse TCP |

### 🍎 macOS
| # | Payload | Description |
|---|---|---|
| 16 | `osx/x64/meterpreter/reverse_tcp` | x64 Meterpreter reverse TCP |
| 17 | `osx/x64/shell_reverse_tcp` | x64 dumb shell reverse TCP |

### 🐘 PHP
| # | Payload | Description |
|---|---|---|
| 18 | `php/meterpreter/reverse_tcp` | PHP Meterpreter reverse TCP |
| 19 | `php/reverse_php` | PHP reverse shell |

### 🐍 Python
| # | Payload | Description |
|---|---|---|
| 20 | `python/meterpreter/reverse_tcp` | Python Meterpreter reverse TCP |
| 21 | `python/shell_reverse_tcp` | Python reverse shell |

### ☕ Java
| # | Payload | Description |
|---|---|---|
| 22 | `java/meterpreter/reverse_tcp` | Java Meterpreter reverse TCP |
| 23 | `java/shell_reverse_tcp` | Java dumb shell reverse TCP |

---

## ⚙️ How Payload Generation Works

```
Select payload number
       ↓
Enter LHOST (your IP address)
       ↓
Enter LPORT (your listener port)
       ↓
Enter output path (default: ~/metagenerator_<payload>.<ext>)
       ↓
msfvenom runs inside Kali proot
       ↓
✓ File saved + listener command printed
```

**Example listener command printed after generation:**
```bash
msfconsole -q -x "use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST 192.168.1.x; set LPORT 4444; run"
```

---

## 📁 File Structure

```
metagenerator/
├── metagenerator.py     # main script
└── README.md            # this file
```

---

## 🛠️ Troubleshooting

**`msfvenom not found` on launch**
→ Run option 2 to install Kali + Metasploit, then `source ~/.bashrc`

**`Error: invalid format`**
→ Make sure you're using the latest version of the script (format bug was fixed)

**Payload saved to wrong location**
→ When prompted for output path, type the full path e.g. `/sdcard/Download/payload.apk`

**Installation hangs**
→ Make sure you have a stable WiFi connection and enough storage space (~5 GB free)

---

## 👤 Author

**flandreiii**
- GitHub: [github.com/flandreiii](https://github.com/flandreiii)
- ☕ Support: [buymeacoffee.com/flandreiii](https://buymeacoffee.com/flandreiii)

If this tool saved you time, consider buying me a coffee — it keeps projects like this alive. 🙏

---

## 📄 License

MIT License — free to use, modify, and distribute with credit.

---

<div align="center">

*Made with 🖤 on CachyOS + Termux*

`#metasploit` `#msfvenom` `#termux` `#kali` `#kalilinux` `#android` `#pentest` `#pentesting` `#ethicalhacking` `#hacking` `#cybersecurity` `#infosec` `#redteam` `#payloadgenerator` `#reverseShell` `#meterpreter` `#termuxtools` `#androidhacking` `#proothack` `#flandreiii` `#metagenerator` `#opensource` `#python` `#python3` `#linux` `#tools` `#security` `#hacker` `#ctf` `#bugbounty`

</div>
