# 🤖 My Agentic AI Playground

A collection of AI agents and experiments I built while exploring **[Agno](https://github.com/agno-agi/agno)** (formerly Phidata) and **[Groq](https://groq.com/)**. 

I wanted to experiment with how agents handle tools like web search, financial data, YouTube transcripts, and multi-agent coordination with fast inference.

---

## 🧪 What's in Here

Here are the different agents and experiments in this repo:

### 1. 📺 YouTube Video Analyzer (`youtube_analyzer.py` & `ui.py`)
- Takes a YouTube link, pulls the transcript, and generates structured chapter summaries with timestamps.
- Comes with a quick **Streamlit UI** (`ui.py`) so you can just paste a link and get the breakdown.

### 2. 📈 Finance Agent (`finance.py`)
- An investment research agent powered by `yfinance` and DuckDuckGo search.
- Pulls live stock prices (e.g. MSFT), analyst ratings, and fundamentals, and formats them in markdown tables.

### 3. 🌐 Multi-Agent Team (`team.py`)
- An experiment with Agno's `Team` feature.
- A team leader coordinates three agents (English, Chinese, German) to answer a prompt in each language simultaneously.

### 4. ✈️ Travel Assistant (`agent.py`)
- A simple travel agent equipped with DuckDuckGo search to check real-time travel safety and updates.

### 5. 🔍 Model Checker (`models.py`)
- A quick script to list all available models on Groq via their API.

---

## 🚀 Quick Setup

### 1. Clone & Set Up Virtual Environment

```bash
git clone https://github.com/your-username/AGENTICAI.git
cd AGENTICAI

python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Add Your Groq API Key

Grab a free API key from [Groq Console](https://console.groq.com/keys), then:

```bash
cp .env.example .env
```

Open `.env` and paste your key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🏃 How to Run

- **YouTube Analyzer Web UI:**
  ```bash
  streamlit run ui.py
  ```

- **Finance Agent:**
  ```bash
  python finance.py
  ```

- **Multi-Agent Translation Team:**
  ```bash
  python team.py
  ```

- **Travel Agent:**
  ```bash
  python agent.py
  ```

- **List Groq Models:**
  ```bash
  python models.py
  ```

---

## 🛠️ Built With

- **[Agno](https://github.com/agno-agi/agno)** - Agent and multi-agent framework
- **[Groq](https://groq.com/)** - Fast LLM inference
- **[Streamlit](https://streamlit.io/)** - Simple UI for the YouTube agent
- **[yfinance](https://github.com/ranaroussi/yfinance)** & **[duckduckgo-search](https://duckduckgo.com)** - Agent tools
