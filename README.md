# RedTeam Recon Tool 🛠️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

A modular collection of Python scripts for network reconnaissance and target enumeration, built as part of my cybersecurity portfolio.

## Available Modules

| Module | Script Path | Description |
|---|---|---|
| Port Scanner | `src/scanner.py` | Basic TCP port scanner with domain resolution and fallback target handling. |

## Usage

```bash
python <script_path> [target]
```

Example:
```bash
python src/scanner.py 192.168.1.10
```

No dependencies — standard library only.

## Disclaimer

Built for educational purposes as part of my red team / pentesting practice. For use only on systems you own or have explicit permission to test (own lab, CTFs, authorized engagements).

## License

MIT — see [LICENSE](LICENSE).