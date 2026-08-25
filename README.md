# 🛠️ RedTeam Recon Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey.svg)]()

> A modular collection of custom Python scripts for network reconnaissance, target enumeration, and basic security assessments.

---

## 📑 Table of Contents

- [About](#-about)
- [Available Modules](#-available-modules)
- [Installation](#-installation)
- [Usage](#-usage)
- [Roadmap](#-roadmap)
- [Disclaimer](#-disclaimer)
- [License](#-license)

---

## 📖 About

**RedTeam Recon Tool** is a collection of independent, lightweight Python scripts, built as part of my cybersecurity portfolio. Each module is self-contained and can be run directly from the project root.

The project is developed alongside my Active Directory home lab, with the goal of building a practical toolkit to support hands-on pentesting practice.

## 🧩 Available Modules

| Module | Script Path | Description |
|---|---|---|
| **Port Scanner** | `src/scanner.py` | Basic TCP port scanner with domain resolution and fallback target handling. |

> 📌 More modules will be added as the project grows — see the [Roadmap](#-roadmap).

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/miloszlabedzki/RedTeam-Recon-Tool.git
cd RedTeam-Recon-Tool

# (optional) create a virtual environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

Run any module directly from the project root using Python 3:

```bash
python <script_path> [target]
```

**Example — port scanning:**

```bash
python src/scanner.py 192.168.1.10
```

## 🗺️ Roadmap

- [ ] Service scanner and banner grabbing
- [ ] Subdomain enumeration module
- [ ] Integration with the Active Directory home lab
- [ ] Export results to JSON/CSV
- [ ] Simple HTML scan report

## ⚠️ Disclaimer

The tools in this repository are built **strictly for educational purposes** and for testing in environments you have **explicit, written authorization** to assess (e.g. your own home lab, CTFs, an authorized pentest engagement). The author is not responsible for any misuse of this software.

## 📜 License

This project is released under the [MIT License](LICENSE).

---

<div align="center">
Built with 🦊 by <a href="https://github.com/miloszlabedzki">miloszlabedzki</a>
</div>