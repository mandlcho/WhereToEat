# WhereToEat

A lightweight lunch decision-assistant: enter your budget (or hit "Surprise Me") and get a quick recommendation for where to eat.

Built as a small, practical tool to reduce decision fatigue for a recurring, low-stakes choice - while keeping the experience fun and fast.

## The Problem (In One Line)

Choosing lunch is a surprisingly frequent time sink; WhereToEat turns "what should we eat?" into a 5-second decision.

## What It Does

- Budget-based suggestions
  - `0` returns an ultra-cheap option
  - `<= 10` selects from a "cheap eats" list
  - `>= 11` selects from a "regular" list
- Two modes
  - Desktop UI (PyQt4): "Tell Me" + "Surprise Me"
  - CLI: pass a budget argument and print a recommendation
- Simple, explainable logic
  - One function (`WhereToEat(budget)`) determines the outcome

## How To Run

### CLI (prints a recommendation)

```bash
python python3_wheretoeat.py 12
```

### Desktop app (PyQt4 GUI)

```bash
python python3_wheretoeat.py
```

Requirements:

- Python 3
- PyQt4 available in your environment (`from PyQt4 import QtCore, QtGui`)

## How It Works (Quick Tour)

- `python3_wheretoeat.py` contains:
  - `WhereToEat(budget)` - core recommendation logic
  - CLI parsing (optional `budget` arg)
  - PyQt4 window wiring for "Tell Me" and "Surprise Me"
- The UI is designed in Qt Designer and generated into Python:
  - `wheretoeat.ui` - source layout
  - `wheretoeatdesign.py` - generated PyQt4 UI code

## Repository Tour

- `python3_wheretoeat.py` - main app (core logic + CLI + GUI)
- `wheretoeat.ui` - Qt Designer UI layout
- `wheretoeatdesign.py` - generated UI code (PyQt4)
- `location.txt` - sample location list file (currently placeholder content)
- `documentation/` - supporting materials (if present)

## Current Limitations / Known Gaps

- The "Browse" button reads a `.txt` file and prints its contents, but the loaded list is not yet used for recommendations.
- `location.txt` is placeholder content and mainly signals the intended direction (file-driven locations).

## Product-Ready Next Steps (If This Were Shipped)

- Make locations configurable (use the browsed file to drive the picker)
- Add preference controls (exclude repeats, favorites, "not today")
- Add richer constraints (distance, cuisine, dietary needs, time)
- Add lightweight telemetry (most-picked, time-to-decision) to validate impact
- Add tests for boundary conditions (0, 10, 11, invalid inputs)

## License

No license file is currently included. If you plan to share or reuse this project, consider adding one (e.g., MIT or Apache-2.0).
