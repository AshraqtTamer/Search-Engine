# 🔎 Wikipedia TF-IDF Search Engine

A Streamlit-powered search engine that retrieves Wikipedia articles and ranks them using **TF-IDF Vectorization** and **Cosine Similarity**.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-TF--IDF-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**🚀 Live Demo (Local):**https://search-engine-szvtdxxmczpldzhsqqqe9c.streamlit.app/

Run the application locally:

```bash
streamlit run search_engine.py
```

Then open the URL shown in the terminal, typically:

http://localhost:8502

---

# 📌 Overview

Wikipedia TF-IDF Search Engine is a lightweight Information Retrieval (IR) application built with Python and Streamlit.

Given a user's search query, the application:

* Searches Wikipedia using the official Wikipedia API.
* Retrieves the top matching articles.
* Extracts article summaries.
* Converts the query and article snippets into TF-IDF vectors.
* Computes Cosine Similarity between the query and each article.
* Ranks the results based on semantic relevance.
* Displays ranked articles with similarity scores and direct Wikipedia links.

The project demonstrates a classical Information Retrieval pipeline using TF-IDF and cosine similarity to rank Wikipedia search results.

---

# ✨ Features

* 🔎 Search Wikipedia directly from a Streamlit web application.
* 📄 Retrieve article summaries using the Wikipedia API.
* 📊 Rank articles using TF-IDF Vectorization.
* 📈 Calculate document similarity using Cosine Similarity.
* 🏆 Display ranked search results with similarity scores.
* 🔗 Provide direct links to Wikipedia articles.
* 🎨 Responsive Streamlit interface with custom styling.
* ⚡ Fast and lightweight implementation.

---

# 🧩 How It Works

1. Enter a search query.
2. The application sends the query to the Wikipedia API.
3. Wikipedia returns the top search results.
4. The application fetches article summaries.
5. TF-IDF Vectorizer converts both the query and article summaries into numerical vectors.
6. Cosine Similarity compares each article with the user's query.
7. Articles are ranked from highest to lowest similarity.
8. The application displays:

   * Article title
   * Summary snippet
   * Similarity score
   * Direct Wikipedia link

---

# 🛠 Tech Stack

| Layer                 | Tools                |
| --------------------- | -------------------- |
| Programming Language  | Python               |
| Web Framework         | Streamlit            |
| Information Retrieval | TF-IDF Vectorization |
| Similarity Metric     | Cosine Similarity    |
| Machine Learning      | scikit-learn         |
| API                   | Wikipedia API        |
| HTTP Requests         | requests             |

---

# 📂 Project Structure

```text
wikipedia-tfidf-search/
│
├── search_engine.py          # Streamlit application
├── requirements.txt          # Python dependencies
├── README.md
└── LICENSE
```

---

# 💻 Run Locally

## 1. Clone the repository

```bash
git clone https://github.com/your-username/wikipedia-tfidf-search.git

cd wikipedia-tfidf-search
```

## 2. Create a virtual environment (Recommended)

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the application

```bash
streamlit run search_engine.py
```

Then open the URL shown in the terminal, typically:

http://localhost:8502

---

# ⚙️ Ranking Algorithm

The application ranks retrieved Wikipedia articles using:

* TF-IDF Vectorization
* Cosine Similarity

The higher the cosine similarity score, the more relevant the article is to the user's search query.

---

# 🌐 Data Source

The application uses the public Wikipedia API to:

* Search Wikipedia articles
* Retrieve article summaries
* Fetch article URLs

Up to 15 search results are retrieved before ranking them using TF-IDF similarity.

---

# 📦 Dependencies

Main libraries:

* Streamlit
* Requests
* scikit-learn

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 🚧 Future Improvements

* Replace TF-IDF with Sentence Transformers or BERT embeddings.
* Add semantic search using vector databases such as FAISS.
* Highlight matching query terms.
* Support multilingual Wikipedia search.
* Cache API responses for faster performance.
* Add search history and bookmarks.

---

# 👩‍💻 Author

**Ashraqt Tamer**

GitHub: https://github.com/AshraqtTamer

---

# 📄 License

This project is licensed under the MIT License.

