# Wikipedia TF-IDF Search Engine

A simple Streamlit-based search interface that queries Wikipedia and ranks results using TF-IDF similarity.

The app fetches the top Wikipedia search results for a user query, extracts article summaries, and then compares each article snippet against the query using TF-IDF vectorization and cosine similarity. The results are displayed in a clean Streamlit dashboard with ranking scores and direct Wikipedia links.

## Features

- Search Wikipedia directly from a Streamlit web app
- Fetch page extracts and URLs using the Wikipedia API
- Rank matching documents using TF-IDF and cosine similarity
- Show top matched content snippets with similarity score
- Responsive interface with custom styling

## Required files

- `search_engine.py` — the Streamlit application entrypoint
- `requirements.txt` — Python package dependencies

## Installation

1. Open PowerShell in the repository root:

    ```powershell
    cd C:\Users\ashrakat_tamer\plagiarism_detector
    ```

2. Create and activate a virtual environment if needed:

    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```

3. Install dependencies:

    ```powershell
    pip install -r requirements.txt
    ```

## Run the app

```powershell
streamlit run search_engine.py
```

Then open the URL shown in the terminal, normally `http://localhost:8502`.

## Notes

- The app currently uses Wikipedia's public `api.php` endpoint.
- It requests up to 15 search results and ranks them by TF-IDF similarity to the query.
- If no matches are found, the app displays a warning.

## Dependencies

The app depends on:

- `streamlit`
- `requests`
- `scikit-learn`

For the full environment, see `requirements.txt`.
