from flask import Flask
from newsapi import NewsApiClient
from pandas.io.json import json_normalize
import pandas as pd
from bs4 import BeautifulSoup

app = Flask(__name__)
newsapi = NewsApiClient(api_key="abc08bbe1747418c8f71eeed0119d4ac")


# def top_headlines():
#     country = input("Which country are you interested in?")
#     category = input(
#         """Which category are you interested in? \nHere
#    are the categories to choose from:\nbusiness\nentertainment
#    \ngeneral\nhealth\nscience\ntechnology"""
#     )
#     top_headlines = newsapi.get_top_headlines(
#         category=category, language="en", country=country
#     )
#     top_headlines = json_normalize(top_headlines["articles"])
#     newdf = top_headlines[["title", "url"]]
#     dic = newdf.set_index("title")["url"].to_dict()


@app.route("/")
def hello_world():
    return "Hello World"


# main driver function
if __name__ == "__main__":
    app.run()
