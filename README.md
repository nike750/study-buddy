# 📚 Study Buddy — Private & Local AI Learning Assistant

> A fast, lightweight, and completely private AI study companion built with **Flask**, **Ollama (`llama3.2:1b`)**, and **JavaScript Streaming**.

![Hacktoberfest](https://img.shields.io/badge/Hacktoberfest-2026-orange?style=for-the-badge&logo=hacktoberfest)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Llama_3.2_1B-black?style=for-the-badge)

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Getting Started](#-getting-started)
  - [Prerequisites](#1-prerequisites)
  - [Installation](#2-installation)
  - [Running the App](#3-running-the-app)
- [Folder Structure](#-folder-structure)
- [Troubleshooting & FAQs](#-troubleshooting--faqs)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 About the Project

**Study Buddy** is an open-source, local-first web application designed to help students, developers, and self-learners study efficiently without relying on expensive cloud API keys or sacrificing data privacy.

Powered by Meta's **Llama 3.2 (1B)** model via **Ollama**, Study Buddy streams AI responses in real-time right in your browser, formatted with clean headings, bold text, and bullet points.

---

## ✨ Key Features

* **🔒 100% Local & Private:** Runs entirely on your local machine using Ollama — zero cloud APIs, zero subscription fees, and complete data privacy.
* **⚡ High-Speed Streaming:** Utilizes Flask's chunked response generator paired with JavaScript's `ReadableStreamReader` for low-latency, token-by-token output.
* **🧠 Optimized for CPU:** Powered by `llama3.2:1b` (1.3 GB footprint), making it ultra-responsive even on laptops without dedicated GPUs.
* **🎨 Clean Markdown UI:** Integrated with `Marked.js` to automatically parse raw Markdown (`**bold**`, `# headers`, `* lists`) into styled HTML elements.
* **🌐 Offline Capable:** Once installed, you can study anywhere — even without an internet connection.

---

## 🛠️ Tech Stack

| Domain | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | [Python 3.8+](https://www.python.org/) | Core programming runtime |
| **Web Framework** | [Flask](https://flask.palletsprojects.com/) | Lightweight WSGI web application framework |
| **Model Engine** | [Ollama](https://ollama.com/) | Local Large Language Model runner |
| **AI Model** | Meta Llama 3.2 (1B) | Lightweight, instruction-tuned LLM |
| **Frontend** | HTML5, CSS3, JavaScript | Modern, responsive chat UI |
| **Markdown Parsing** | [Marked.js](https://marked.js.org/) | Fast real-time Markdown-to-HTML parser |

---

## 🏗️ Project Architecture

```text
┌─────────────────┐       HTTP Stream       ┌──────────────────┐
│                 │ <---------------------> │                  │
│ Browser Frontend│   fetch('/chat') API    │  Flask Backend   │
│  (Marked.js)    │                         │ (study-buddy.py) │
└─────────────────┘                         └────────┬─────────┘
                                                     │
                                               REST  │ Local Request
                                              API    │
                                                     ▼
                                            ┌──────────────────┐
                                            │  Ollama Engine   │
                                            │  (llama3.2:1b)   │
                                            └──────────────────┘
```

---

## 🚀 Getting Started

Follow these steps to get your local instance of Study Buddy up and running.

### 1. Prerequisites

Make sure you have the following installed on your computer:

* **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
* **Git** ([Download Git](https://git-scm.com/))
* **Ollama** ([Download Ollama](https://ollama.com/download))

---

### 2. Installation

#### Step A: Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone https://github.com/nike750/study-buddy.git
cd study-buddy
```

#### Step B: Pull the Llama 3.2 1B Model
Ensure Ollama is running in the background, then pull the lightweight model:
```bash
ollama pull llama3.2:1b
```

#### Step C: Set Up Python Environment & Install Dependencies
```bash
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt
```

---

### 3. Running the App

1. Launch the Flask application:
   ```bash
   python study-buddy.py
   ```
2. Open your web browser and navigate to:
   ```text
   http://127.0.0.1:5000
   ```
3. Type any study query (e.g., *"Explain binary search trees with an example"*) and watch your Study Buddy stream answers in real time!

---

## 📁 Folder Structure

```text
study-buddy/
├── templates/
│   └── index.html          # Chat interface, streaming JS, and CSS styles
├── .gitignore              # Configured to ignore cache & model binaries
├── CONTRIBUTING.md         # Guidelines for open-source contributors
├── Modelfile.txt           # Ollama custom model configuration
├── README.md               # Comprehensive project documentation
├── requirements.txt        # Python dependency manifest
└── study-buddy.py          # Main Flask app & streaming server
```

---

## ❓ Troubleshooting & FAQs

<details>
<summary><b>1. Error: "Connection refused" or Ollama not responding</b></summary>
<br>
Make sure Ollama is actively running in your system tray or background process. You can test it by running <code>ollama list</code> in your terminal.
</details>

<details>
<summary><b>2. Responses are taking too long to generate</b></summary>
<br>
Ensure <code>study-buddy.py</code> is configured to use <code>llama3.2:1b</code> instead of larger models (e.g., 8B/70B). The 1B variant is optimized specifically for CPU performance.
</details>

<details>
<summary><b>3. Raw asterisks (<code>**</code>) appearing in the chat UI</b></summary>
<br>
Verify that <code>Marked.js</code> script is properly included in the <code>&lt;head&gt;</code> of <code>templates/index.html</code> and that <code>marked.parse()</code> is called during text rendering.
</details>

---

## 🤝 Contributing

Contributions are welcome! Whether it's fixing bugs, adding new features, or improving documentation:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) for details on code standards and Hacktoberfest participation.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<p align="center">
  Crafted with ❤️ for <b>Hacktoberfest</b>
</p>