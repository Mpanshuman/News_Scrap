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
    all_countries = list(map(attrgetter('alpha_2', 'name'), list(pycountry.countries)))
    return all_countries

def top_headlines(country,category):
    try:
        top_headlines = newsapi.get_top_headlines(
            category=category, language="en", country=country
        )
        top_headlines = pd.json_normalize(top_headlines["articles"])
        newdf = top_headlines[["title", "url"]]
        dic = newdf.set_index("title")["url"].to_dict()
        return dic
    except Exception as error:
        print(error)
        return {'error':error}


@app.route("/",methods = ['GET','POST'])
def hello_world():
    countries = getCountries()
    news = {}
    categories = [('business','business'),('entertainment','entertainment'),('general','general'),('health','health'),('science','science'),('sports','sports'),('technology','technology')]
    context = {"countries": countries, "categories": categories,"all_news":news}
    if request.method == 'POST':
        country = request.form.get('country')
        category = request.form.get('category')
        print(country)
        news = top_headlines(country.lower(),category)
    return render_template("index.html",context=context)


# main driver function
if __name__ == "__main__":
    app.run(debug=True)
    # top_headlines()
