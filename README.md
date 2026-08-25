# 🛠️ RedTeam Recon Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey.svg)]()

> Modularny zestaw autorskich skryptów w Pythonie do rekonesansu sieciowego, enumeracji celów oraz podstawowych ocen bezpieczeństwa.

---

## 📑 Spis treści

- [O projekcie](#-o-projekcie)
- [Dostępne moduły](#-dostępne-moduły)
- [Instalacja](#-instalacja)
- [Użycie](#-użycie)
- [Roadmapa](#-roadmapa)
- [Disclaimer](#-disclaimer)
- [Licencja](#-licencja)

---

## 📖 O projekcie

**RedTeam Recon Tool** to zbiór niezależnych, lekkich skryptów Python, tworzonych jako część mojego portfolio w obszarze cyberbezpieczeństwa. Każdy moduł działa samodzielnie i można go uruchomić bezpośrednio z poziomu katalogu głównego projektu.

Projekt rozwijany jest równolegle z moim domowym laboratorium Active Directory — celem jest zbudowanie praktycznego zestawu narzędzi wspierających naukę pentestingu.

## 🧩 Dostępne moduły

| Moduł | Ścieżka do skryptu | Opis |
|---|---|---|
| **Port Scanner** | `src/scanner.py` | Podstawowy skaner portów TCP z rozwiązywaniem nazw domenowych i obsługą fallback dla celu. |

> 📌 Kolejne moduły będą dodawane wraz z rozwojem projektu — zobacz [Roadmapę](#-roadmapa).

## ⚙️ Instalacja

```bash
# Sklonuj repozytorium
git clone https://github.com/miloszlabedzki/RedTeam-Recon-Tool.git
cd RedTeam-Recon-Tool

# (opcjonalnie) utwórz środowisko wirtualne
python3 -m venv venv
source venv/bin/activate

# zainstaluj zależności
pip install -r requirements.txt
```

## 🚀 Użycie

Każdy moduł uruchamiany jest bezpośrednio z poziomu katalogu głównego projektu:

```bash
python <script_path> [target]
```

**Przykład — skanowanie portów:**

```bash
python src/scanner.py 192.168.1.10
```

## 🗺️ Roadmapa

- [ ] Skaner usług i banner grabbing
- [ ] Moduł enumeracji subdomen
- [ ] Integracja z Active Directory home labem
- [ ] Eksport wyników do JSON/CSV
- [ ] Prosty raport HTML z wynikami skanu

## ⚠️ Disclaimer

Narzędzia zawarte w tym repozytorium zostały stworzone **wyłącznie w celach edukacyjnych** oraz do testowania w środowiskach, na których użycie masz **wyraźną, pisemną zgodę** (np. własny home lab, CTF, autoryzowany pentest). Autor nie ponosi odpowiedzialności za niewłaściwe użycie tego oprogramowania.

## 📜 Licencja

Projekt udostępniony na licencji [MIT](LICENSE).

---

<div align="center">
Zbudowane z 🦊 przez <a href="https://github.com/miloszlabedzki">miloszlabedzki</a>
</div>