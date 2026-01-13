# Clash Royale API Wrapper (Python)

A clean, typed, and testable Python 3 wrapper for the official **Clash Royale REST API**.

This library provides a simple and Pythonic interface to interact with Clash Royale data such as players, clans, cards, and tournaments — without dealing directly with HTTP requests.

---

## Features

- ✅ Python 3.10+
- ✅ Clean object-oriented API
- ✅ Typed models (`dataclasses`)
- ✅ Fully unit-tested (`unittest`)
- ✅ No magic, easy to debug
- ✅ Built on top of `requests`

---

## Installation

> PyPI publication coming soon.

For now, install from source:

```shell
git clone https://github.com/yourusername/clashroyale.git
cd clashroyale
pip install -e .
```

Or add it as a dependency in your project.

## Requirements

- Python 3.10+

```shell
pip install -r requirements.txt
```

## Getting an API Token

1. Go to: https://developer.clashroyale.com
2. Create a new API key
3. Whitelist your IP address
4. Copy your **Bearer Token**

**[!WARNING] Never commit your token to source control**

## Quick Start

```python
from crapi import CRApiClient

client = CRApiClient("YOUR_API_TOKEN")

player = client.players.get_by_tag("#2PCRVJUYQ")

print(player.name)
print(player.trophies)
```

## Project Structure

```
crapi/
├──src/
│   ├── crapi/
│   │   ├── client.py          # Main public client
│   │   ├── commons/           # Common functions
│   │   ├── http/              # Low-level HTTP logic
│   │   ├── models/            # Typed response models
│   │   └── resources/         # API domains
│   └── tests/                 # Unit tests (unittest)
│
├── pyproject.toml, etc        # Python project files
└── README.md, LICENSE, etc    # Docs files
```

# Error Handling

The wrapper raises Python exceptions on API errors.
```python
from crapi.exceptions import ClientError

try:
    player = client.players.get_by_tag("INVALID")
except ClientError as exc:
    print(exc)
```

## Testing

All tests use the standard library `unittest` module.

Run the full tests suite:

```shell
python -m unittest -v
```

## Disclaimer

This project is not affiliated with Supercell.
Clash Royale and its content are trademarks of Supercell.
