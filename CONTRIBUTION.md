# Contributing to Study Buddy 🚀

Thank you for your interest in contributing to **Study Buddy**! We welcome contributions from developers, technical writers, and open-source enthusiasts of all experience levels—especially during **Hacktoberfest**! 🎃

By contributing to this repository, you help build a faster, more accessible, and completely private AI learning assistant for students worldwide.

---

## 📋 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [Hacktoberfest Participation](#-hacktoberfest-participation)
- [Ways to Contribute](#-ways-to-contribute)
- [Getting Started](#-getting-started)
- [Development Workflow](#-development-workflow)
- [Pull Request Guidelines](#-pull-request-guidelines)

---

## 📜 Code of Conduct

We are committed to providing a welcoming, inclusive, and friendly environment for all contributors. Please ensure that all communications and interactions remain respectful, constructive, and professional.

---

## 🎃 Hacktoberfest Participation

This repository is actively taking part in **Hacktoberfest**. To make sure your contributions count toward your Hacktoberfest goals:

1. **Quality First:** We value quality contributions over quantity. Low-effort PRs (e.g., fixing a single typo, adding white spaces, automated spam) will be marked as `invalid` or `spam`.
2. **Issues First:** Please check the [Issue Tracker](https://github.com/nike750/study-buddy/issues) for existing open issues or open a new issue before submitting a PR.
3. **Labels:** Valid pull requests that meet our standards will be reviewed, merged, or tagged with the `hacktoberfest-accepted` label.

---

## 💡 Ways to Contribute

You don't need to be an AI expert to contribute! Here are several ways you can help:

- **🎨 UI / Frontend Enhancements:** Improve CSS formatting, add dark/light mode toggling, or polish markdown rendering and responsiveness.
- **⚡ Backend Optimization:** Improve streaming handling in Flask, optimize prompts in `study-buddy.py`, or refine error handling.
- **✨ Features:** Add prompt templates (e.g., "Flashcard Mode", "Summarize Notes Mode") or export chat logs to PDF/Markdown.
- **📖 Documentation:** Fix errors in setup guides, improve code comments, or create usage tutorials.

---

## 🛠️ Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/)
- [Git](https://git-scm.com/)
- [Ollama](https://ollama.com/) running locally with the `llama3.2:1b` model.

### Setting Up Your Local Environment

1. **Fork the Repository**  
   Click the **Fork** button at the top right of the [Study Buddy Repository](https://github.com/nike750/study-buddy).

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/study-buddy.git
   cd study-buddy
   ```

3. **Set Up Python Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate on Windows CMD / PowerShell:
   venv\Scripts\activate

   # Activate on macOS / Linux:
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Pull the Local LLM**
   ```bash
   ollama pull llama3.2:1b
   ```

6. **Run the App Locally**
   ```bash
   python study-buddy.py
   ```
   Navigate to `http://127.0.0.1:5000` in your web browser.

---

## 🔄 Development Workflow

1. **Keep `main` Clean:** Create a new branch for every feature or fix you work on.
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. **Commit Your Changes:** Write clear, concise commit messages.
   ```bash
   git add .
   git commit -m "feat: add copy-to-clipboard button for code blocks"
   ```

3. **Push to Your Fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

---

## 📥 Pull Request Guidelines

When submitting a Pull Request (PR):

1. **Reference Issues:** Link your PR to an existing issue if applicable (e.g., `Fixes #12`).
2. **Clear Description:** Clearly explain what changes were made, why they are necessary, and how to test them locally.
3. **Screenshots / GIFs:** If you modified the UI, please attach visual proof showing the before and after.
4. **Clean Code:** Ensure no unnecessary debug statements, temp files, or unneeded dependencies are committed.

---

Thank you for contributing to **Study Buddy**! Happy coding! 🚀