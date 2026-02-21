from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_codes(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    codes = soup.find_all("span", class_="code-text")
    return [code.text.strip() for code in codes]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shindo")
def shindo():
    code_list = get_codes("https://progameguides.com/roblox/roblox-shindo-life-codes/")
    return render_template("shindolife.html", codes=code_list)

@app.route("/kaizen")
def kaizen():
    code_list = get_codes("https://progameguides.com/roblox/kaizen-codes/")
    return render_template("kaizen.html", codes=code_list)

@app.route("/bloxfruit")
def bloxfruit():
    code_list = get_codes("https://progameguides.com/roblox/roblox-blox-fruits-codes/")
    return render_template("bloxfruit.html", codes=code_list)

if __name__ == "__main__":
    app.run(debug=True)