<!--
GitHub-ready README for the Currency Converter project.
Designed to be concise, presentable on a GitHub repository page, and helpful for visitors.
-->

# Currency Converter

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![Streamlit](https://img.shields.io/badge/streamlit-%E2%9C%93-orange)

A simple, well-documented currency converter built with Python and Streamlit. It fetches live exchange rates from ExchangeRate-API, caches responses for efficiency, and provides an interactive web UI plus a minimal CLI-style script for quick testing.

Key highlights:
- Real-time exchange rates via ExchangeRate-API
- In-memory caching of rates (3-hour TTL) using `cachetools`
- Clean Streamlit interface (`src/run.py`) for quick demos

## Demo

Open `src/run.py` with Streamlit to see the UI locally. Add screenshots or a short GIF to this section later for a repository showcase.

## Quick Start

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install requests cachetools streamlit
```

Set your ExchangeRate-API key (example):

PowerShell (Windows):

```powershell
$Env:API_KEY = "your_api_key_here"
```

macOS / Linux:

```bash
export API_KEY="your_api_key_here"
```

Run the Streamlit app:

```bash
cd src
streamlit run run.py
```

The app opens in your browser where you can choose base/target currencies and convert amounts.

## Files Overview
- `src/constant.py` — List of supported currency codes (`CURRENCIES`).
- `src/currency_convertor.py` — Core functions: `get_exchange_rate()` and `convert_currency()`.
- `src/run.py` — Streamlit app UI and orchestration.
- `src/main.ipynb` — Notebook used for development or demonstration.

## Implementation Notes
- API endpoint used: `https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}`
- Caching: in-memory TTLCache (`ttl=3*60*60`) reduces duplicate API calls.
- Make sure `API_KEY` is set in the environment before running.

## Troubleshooting
- If the app shows an error fetching exchange rates, confirm the `API_KEY` value and network connectivity.
- If unexpected currency results appear, validate the currency code against `src/constant.py`.

## Suggestions for a polished GitHub listing
- Add a `requirements.txt` (run `pip freeze > requirements.txt`) to make installs reproducible.
- Include a short demo GIF or screenshots in the repository root and reference them under **Demo**.
- Add a `LICENSE` file (e.g., MIT) and a brief `CONTRIBUTING.md` if you welcome contributions.

## Contributing
Contributions are welcome. For small fixes or docs improvements, open a PR. For larger changes, please open an issue first to discuss the approach.

## License
This project is available under the MIT License — see the `LICENSE` file.

## Included files
- `requirements.txt` — pinned dependency list for quick installs
- `LICENSE` — MIT license
- `CONTRIBUTING.md` — contribution guidelines
- `Dockerfile` — container image to run the Streamlit app
- `assets/` — place demo screenshots or GIFs here (see `assets/README.md`)

## Using the added files

Install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Run locally (Streamlit):

```bash
cd src
streamlit run run.py
```

Build and run with Docker:

```bash
docker build -t currency-converter:latest .
docker run -p 8501:8501 currency-converter:latest
```


## Contact
If you'd like help packaging this for a demo or GitHub Pages, I can add a `requirements.txt`, example screenshots, or a Dockerfile.

