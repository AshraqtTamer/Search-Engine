import streamlit as st
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

WIKIPEDIA_HEADERS = {
    "User-Agent": "plagiarism-detector-app/1.0 (https://www.wikipedia.org/)"
}

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Wikipedia TF-IDF Search Engine",
    page_icon="🔍",
    layout="centered"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>

.search-logo {
    text-align: center;
    font-size: 65px;
    font-weight: bold;
    font-family: Arial, sans-serif;
    margin-top: 40px;
    margin-bottom: 20px;
}

.g-blue { color: #4285F4; }
.g-red { color: #EA4335; }
.g-yellow { color: #FBBC05; }
.g-green { color: #34A853; }

div.stTextInput > div > div > input {
    border-radius: 24px !important;
    padding: 14px 24px !important;
    border: 1px solid #dfe1e5 !important;
    font-size: 18px !important;
}

.card {
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 15px;
    border: 1px solid #eaeaea;
    box-shadow: 0px 1px 4px rgba(0,0,0,0.08);
}

.score {
    color: green;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOGO
# =====================================================
st.markdown("""
<div class="search-logo">
    <span class="g-blue">W</span>
    <span class="g-red">i</span>
    <span class="g-yellow">k</span>
    <span class="g-blue">i</span>
    <span class="g-green">S</span>
    <span class="g-red">e</span>
    <span class="g-yellow">a</span>
    <span class="g-blue">r</span>
    <span class="g-green">c</span>
    <span class="g-red">h</span>
</div>
""", unsafe_allow_html=True)


# =====================================================
# WIKIPEDIA FETCH
# =====================================================
def fetch_documents(query):

    titles = []
    documents = []
    urls = []

    try:
        search_params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": query,
            "srlimit": 15,
            "utf8": 1,
        }

        search_resp = requests.get(
            "https://en.wikipedia.org/w/api.php",
            params=search_params,
            headers=WIKIPEDIA_HEADERS,
            timeout=10,
        )
        search_resp.raise_for_status()
        search_data = search_resp.json()

        search_results = search_data.get("query", {}).get("search", [])
        search_titles = [item["title"] for item in search_results]

        if not search_titles:
            return search_titles, documents, urls

        info_params = {
            "action": "query",
            "format": "json",
            "prop": "extracts|info",
            "exintro": 1,
            "explaintext": 1,
            "inprop": "url",
            "redirects": 1,
            "utf8": 1,
            "titles": "|".join(search_titles),
        }

        info_resp = requests.get(
            "https://en.wikipedia.org/w/api.php",
            params=info_params,
            headers=WIKIPEDIA_HEADERS,
            timeout=10,
        )
        info_resp.raise_for_status()
        info_data = info_resp.json()

        pages = info_data.get("query", {}).get("pages", {})
        page_map = {page["title"]: page for page in pages.values()}

        for title in search_titles:
            page = page_map.get(title)
            if not page:
                continue

            titles.append(title)
            documents.append(page.get("extract", ""))
            urls.append(page.get("fullurl", "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")))

    except Exception:
        pass

    return titles, documents, urls


# =====================================================
# TF-IDF SEARCH
# =====================================================
def tfidf_search(query):

    titles, documents, urls = fetch_documents(query)

    if len(documents) == 0:
        return []

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    query_vector = vectorizer.transform([query])

    scores = cosine_similarity(
        query_vector,
        tfidf_matrix
    ).flatten()

    results = []

    ranked_indices = scores.argsort()[::-1]

    for idx in ranked_indices:

        if scores[idx] > 0:

            results.append({
                "title": titles[idx],
                "score": scores[idx],
                "content": documents[idx][:700],
                "url": urls[idx]
            })

    return results


# =====================================================
# SEARCH BAR
# =====================================================
query = st.text_input(
    "Search Engine",
    placeholder="Enter any topic, keyword, or question...",
    label_visibility="visible"
)

# =====================================================
# SEARCH RESULTS
# =====================================================
if query:

    with st.spinner("Searching Wikipedia..."):
        results = tfidf_search(query)

    if len(results) == 0:

        st.warning("No results found.")

    else:

        st.subheader("Top Matching Results")

        for result in results[:10]:

            st.markdown(f"""
            <div class="card">
                <h3>📄 {result['title']}</h3>
                <p class="score">
                    Similarity Score: {result['score']:.4f}
                </p>
                <p>
                    {result['content']}...
                </p>
                <p><a href="{result['url']}" target="_blank">Read on Wikipedia</a></p>
            </div>
            """, unsafe_allow_html=True)