from flask import Flask, render_template, request
from newsapi import NewsApiClient

# from wsgi import app

# from pandas.io.json import json_normalize

app = Flask(__name__)
newsapi = NewsApiClient(api_key="abc08bbe1747418c8f71eeed0119d4ac")


def getCountries():
    """ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za"""
    # fetch only above states
    avaibale_countries = [
        ("AE", "United Arab Emirates"),
        ("AR", "Argentina"),
        ("AU", "Australia"),
        ("AT", "Austria"),
        ("BE", "Belgium"),
        ("BG", "Bulgaria"),
        ("BR", "Brazil"),
        ("CA", "Canada"),
        ("CH", "Switzerland"),
        ("CN", "China"),
        ("CO", "Colombia"),
        ("CU", "Cuba"),
        ("CZ", "Czechia"),
        ("DE", "Germany"),
        ("EG", "Egypt"),
        ("FR", "France"),
        ("GB", "United Kingdom"),
        ("GR", "Greece"),
        ("HK", "Hong Kong"),
        ("HU", "Hungary"),
        ("ID", "Indonesia"),
        ("IN", "India"),
        ("IE", "Ireland"),
        ("IL", "Israel"),
        ("IT", "Italy"),
        ("JP", "Japan"),
        ("KR", "Korea, Republic of"),
        ("LT", "Lithuania"),
        ("LV", "Latvia"),
        ("MA", "Morocco"),
        ("MX", "Mexico"),
        ("MY", "Malaysia"),
        ("NG", "Nigeria"),
        ("NL", "Netherlands"),
        ("NO", "Norway"),
        ("NZ", "New Zealand"),
        ("PH", "Philippines"),
        ("PL", "Poland"),
        ("PT", "Portugal"),
        ("RO", "Romania"),
        ("RU", "Russian Federation"),
        ("SA", "Saudi Arabia"),
        ("SG", "Singapore"),
        ("RS", "Serbia"),
        ("SK", "Slovakia"),
        ("SI", "Slovenia"),
        ("SE", "Sweden"),
        ("TH", "Thailand"),
        ("TR", "Turkey"),
        ("TW", "Taiwan, Province of China"),
        ("UA", "Ukraine"),
        ("US", "United States"),
        ("VE", "Venezuela, Bolivarian Republic of"),
        ("ZA", "South Africa"),
    ]
    return avaibale_countries


def top_headlines(country, category):
    try:
        top_headlines = newsapi.get_top_headlines(
            category=category, language="en", country=country
        )
        if top_headlines["totalResults"] > 0:
            # dic = newdf.set_index("title")["url"].to_dict()
            print(top_headlines)
            return top_headlines
        return {"status": "error", "error": "No News Found"}
    except Exception as error:
        print(error)
        return {"status": "error", "error": error}


@app.route("/", methods=["GET", "POST"])
def hello_world():
    countries = getCountries()
    news = {}
    categories = [
        ("business", "business"),
        ("entertainment", "entertainment"),
        ("general", "general"),
        ("health", "health"),
        ("science", "science"),
        ("sports", "sports"),
        ("technology", "technology"),
    ]
    if request.method == "POST":
        country = request.form.get("country")
        category = request.form.get("category")
        news = top_headlines(country.lower(), category)
    context = {"countries": countries, "categories": categories, "all_news": news}
    return render_template("index.html", context=context)


@app.route("/about")
def about():
    return "Hello this is about page."


# main driver function
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # top_headlines()
