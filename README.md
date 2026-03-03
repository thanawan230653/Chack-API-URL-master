# 🌐 Simple API Fetcher

A lightweight Python tool to fetch API responses from any URL.

Supports:
- GET requests
- Custom headers
- JSON pretty print
- Raw text fallback
- Save response to file
- Proxy support
- Custom timeout
- Interactive mode

---

# 📦 Requirements

- Python 3.8+
- pip

---

# 🔧 Installation

## 1️⃣ Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/api-fetcher.git
cd api-fetcher

Or download ZIP and extract.

2️⃣ (Optional) Create virtual environment
Windows
python -m venv venv
venv\Scripts\activate
macOS / Linux
python3 -m venv venv
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt

If requirements.txt is missing:

pip install requests
📂 Project Structure
api-fetcher/
│
├── fetch_api.py
├── requirements.txt
└── README.md
🚀 Usage
🔹 Basic GET Request
python fetch_api.py https://api.github.com
🔹 Interactive Mode

If no URL is provided:

python fetch_api.py

Program will prompt:

Enter API URL:
🔹 Custom Header
python fetch_api.py https://api.example.com \
--header "Authorization: Bearer YOUR_TOKEN"

Multiple headers:

python fetch_api.py https://api.example.com \
--header "Authorization: Bearer TOKEN" \
--header "User-Agent: myapp"
🔹 Save Response to File
python fetch_api.py https://api.github.com --save output.json
🔹 Set Timeout (seconds)
python fetch_api.py https://api.github.com --timeout 5
🔹 Use Proxy
python fetch_api.py https://api.github.com --proxy http://127.0.0.1:8080
🧪 Example Test APIs
python fetch_api.py https://jsonplaceholder.typicode.com/posts/1
python fetch_api.py https://api.github.com
⚙️ Build Windows EXE

Install PyInstaller:

pip install pyinstaller

Build:

pyinstaller --onefile fetch_api.py

Executable will be in:

dist/fetch_api.exe

Run:

dist\fetch_api.exe https://api.github.com
🛠 Troubleshooting
❌ ModuleNotFoundError: No module named 'requests'

Fix:

pip install requests

If pip not recognized:

python -m pip install requests
❌ SSL Errors

Upgrade pip and certifi:

python -m pip install --upgrade pip
pip install certifi
🛡 Disclaimer

This tool is intended for:

API testing

Development

Debugging

Educational purposes

Do not use against systems without permission.

📜 License

MIT License
Free to use and modify.
