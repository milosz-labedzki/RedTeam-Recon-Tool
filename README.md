# RedTeam Recon Tool 🛠️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

A modular collection of Python scripts for network reconnaissance and target enumeration, built as part of my cybersecurity portfolio.

## Available Modules

| Module | Script Path | Description |
|---|---|---|
| Port Scanner | `src/scanner.py` | Basic TCP port scanner with domain resolution and fallback target handling. |
| Banner Grabber | `src/banner_grabber.py` | Simple banner grabbing tool to retrieve service banners and application headers. |

## Usage

Run any module directly from the project root using Python 3:

    python <script_path> [target]

**Example:**

    python src/banner_grabber.py scanme.nmap.org

No dependencies — standard library only.

## Disclaimer

Built for educational purposes as part of my red team / pentesting practice. For use only on systems you own or have explicit permission to test (own lab, CTFs, authorized engagements).

## License

MIT — see [LICENSE](LICENSE).
