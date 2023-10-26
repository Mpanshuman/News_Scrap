from flask import Flask, render_template, request
from newsapi import NewsApiClient

# from pandas.io.json import json_normalize
import pandas as pd
from bs4 import BeautifulSoup
from operator import attrgetter
import pycountry

app = Flask(__name__)
newsapi = NewsApiClient(api_key="abc08bbe1747418c8f71eeed0119d4ac")


def getCountries():
    """ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za"""
    # fetch only above states
    return list(map(attrgetter("alpha_2", "name"), list(pycountry.countries)))


def top_headlines(country, category):
    try:
        top_headlines = newsapi.get_top_headlines(
            category=category, language="en", country=country
        )
        if top_headlines["totalResults"] > 0:
            # dic = newdf.set_index("title")["url"].to_dict()
            return top_headlines["articles"]
        return {"data": "No News Found"}
    except Exception as error:
        print(error)
        return {"error": error}


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


# main driver function
if __name__ == "__main__":
    app.run(debug=True)
    # top_headlines()
