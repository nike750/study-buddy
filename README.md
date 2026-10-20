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