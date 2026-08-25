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

Built for educational purposes and authorized testing only (own lab, CTFs, engagements with explicit permission).

## License

MIT — see [LICENSE](LICENSE).