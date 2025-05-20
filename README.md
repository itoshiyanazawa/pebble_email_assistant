## 📫 Pebble – AI Email Assistant for Customer Service

**Pebble** is a Chrome extension powered by an AI backend that helps users rewrite casual or poorly written messages into **clear, polite, and professional customer service responses** — all through a friendly, chat-style UI.

> ✨ Built using Flask, NVIDIA’s OpenAI-compatible `rakutenai-7b-chat` model, and a lightweight Chrome extension.

---

### 💡 Features

* ✅ Rewrite informal or poorly written sentences into polished customer service emails
* 🧠 Detects whether user is chatting or submitting a sentence for correction
* 💬 Chat-style interface for natural interactions
* 📋 One-click copy-to-clipboard functionality
* 🌐 Publicly hosted backend via Render (or use locally)

---

### 📁 Project Structure

```
pebble-email-assistant/
├── app.py              # Flask API using OpenAI-compatible NVIDIA API
├── requirements.txt    # Dependencies for backend
├── popup.html          # Chat-style Chrome extension UI
├── popup.js            # Frontend logic for Chrome extension
├── manifest.json       # Chrome extension config
├── .env                # (optional, for local dev – excluded from Git)

```

---

### 🚀 How to Run Locally

#### 1. Clone the Repo

```bash
git clone https://github.com/your-username/pebble-email-assistant.git
cd pebble-email-assistant/backend
```

#### 2. Set Up and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the Flask API

```bash
python app.py
```

> Make sure to update `app.py` with your own NVIDIA API key.

---

### 🧩 How to Use the Chrome Extension

1. Open `chrome://extensions`
2. Enable **Developer Mode**
3. Click **Load unpacked**
4. Select the `extension/` folder
5. Open the extension and interact with Pebble ✨

> Update `popup.js` with your live Render URL (or localhost for dev)

---

### 📦 Deploying the Backend to Render

Make sure your `app.py` includes:

```python
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
```

Then push to GitHub and connect the repo to [https://render.com](https://render.com) as a new web service.

---

### 🧠 Example Input → Output

**User input:**

```
yo i need this fixed asap
```

**Pebble response:**

```
Could you please assist with resolving this at your earliest convenience?
```

---

### 🔐 API Key Notice

This project uses the `rakutenai-7b-chat` model via NVIDIA’s OpenAI-compatible endpoint. You must obtain your own API key from:

* [https://developer.nvidia.com/nvidia-api-access](https://developer.nvidia.com/nvidia-api-access)

Store it securely in the backend — never expose it in client-side JS.

---

