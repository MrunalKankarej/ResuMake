# ResuMake

An AI-powered resume scoring tool that analyzes your resume against a job description and tells you exactly how well it performs against an Applicant Tracking System (ATS).

---

## What It Does

Paste your resume and a job description, and ResuMake will return:

- An overall ATS score out of 100
- A list of keywords your resume already contains
- A list of important keywords you are missing
- Quick wins — the top changes you can make right now to improve your score

---

## Tech Stack

- **Frontend** — HTML, CSS, JavaScript
- **Backend** — Python, Flask
- **AI** — OpenRouter API (GPT-4o Mini)
- **PDF Parsing** — PyMuPDF

---

## Getting Started

### Prerequisites

- Python 3.11 or higher
- An OpenRouter API key — get one at [openrouter.ai](https://openrouter.ai)

### Installation

1. Clone the repository

```bash
git clone https://github.com/MrunalKankarej/ResuMake.git
cd resumake
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your API key

```
OPENROUTER_API_KEY= API_key_goes_here
```

5. Run the app

```bash
python app.py
```

6. Open your browser and go to `http://localhost:5000`

---

## How to Use

1. Paste your resume text into the left text box
2. Paste the job description into the right text box
3. Click **Analyze Resume**
4. View your ATS score, matched keywords, missing keywords, and quick wins

---

## Project Structure

```
resumake/
├── app.py                  # Flask backend and API routes
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   └── style.css           # Styles
├── .env                    # API key (not committed to git)
├── requirements.txt        # Python dependencies
└── README.md
```

---
