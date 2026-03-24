from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI
import json
import os
import fitz

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract", methods=["POST"])
def extract():
    file = request.files["resume"]
    pdf_bytes = file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return jsonify({"text": text.strip()})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    resume_text = data["resume"]
    job_description = data["jobDescription"]

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": f"""
            You are an ATS resume expert. Analyze this resume 
            against the job description and return ONLY a JSON 
            object. No extra text. No markdown. Just JSON.
            {{
                "overallScore": number (0-100),
                "verdict": "one sentence summary",
                "keywordsFound": ["keyword1", "keyword2"],
                "keywordsMissing": ["keyword1", "keyword2"],
                "quickWins": ["fix 1", "fix 2", "fix 3"]
                }}
                Resume: {resume_text}
                Job Description: {job_description} """
                }]
                )
    raw = response.choices[0].message.content.strip()
    print("RAW RESPONSE:", raw)
    clean = raw.replace("```json", "").replace("```", "").strip()
    print("CLEAN RESPONSE:", clean)
    result = json.loads(clean)
    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)