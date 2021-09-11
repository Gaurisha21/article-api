from flask import Flask, render_template, jsonify
from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)

newsapi = NewsApiClient(api_key='f92ab52775a4452fbf21b768de65c9fc')

@app.route('/')
def home():
    return '''<h1>Articles</h1>'''

@app.route('/WomenHealth')
def WomenHealth():

    all_articles = newsapi.get_everything(
        q='Women Health',
        language='en',
    )
    length = len(all_articles['articles'])
    r1 = random.randint(0, length-1)
    article = all_articles['articles'][r1]
    Source = article['source']['name']
    Title = article['title']
    Link = article['url']
    ImgLink = article['urlToImage']

    source = requests.get(Link).text
    soup = BeautifulSoup(source, 'lxml')
    blacklist = ['p']
    text_elements = [t for t in soup.find_all(text=True) if t.parent.name in blacklist]
    x = ""
    for i in text_elements:
        x = x + i + " \n\n "

    return jsonify({'Title': Title,
                    'Content': x,
                    'Source': Source,
                    'ImgLink': ImgLink})
    #render_template('index.html', Source='{}'.format(Source), Title='{}'.format(Title), Content='{}'.format(x))

@app.route('/MenstrualHealth')
def MenstrualHealth():

    all_articles = newsapi.get_everything(
        q='Menstrual Health',
        language='en',
    )
    length = len(all_articles['articles'])
    r1 = random.randint(0, length-1)
    article = all_articles['articles'][r1]
    Source = article['source']['name']
    Title = article['title']
    Link = article['url']
    ImgLink = article['urlToImage']

    source = requests.get(Link).text
    soup = BeautifulSoup(source, 'lxml')
    blacklist = ['p']
    text_elements = [t for t in soup.find_all(text=True) if t.parent.name in blacklist]
    x = ""
    for i in text_elements:
        x = x + i + " \n\n "

    return jsonify({'Title': Title,
                    'Content': x,
                    'Source': Source,
                    'ImgLink': ImgLink})
    #render_template('index.html', Source='{}'.format(Source), Title='{}'.format(Title), Content='{}'.format(x))

@app.route('/Gynaecology')
def Gynaecology():

    all_articles = newsapi.get_everything(
        q='Gynaecology',
        language='en',
    )
    length = len(all_articles['articles'])
    r1 = random.randint(0, length-1)
    article = all_articles['articles'][r1]
    Source = article['source']['name']
    Title = article['title']
    Link = article['url']
    ImgLink = article['urlToImage']

    source = requests.get(Link).text
    soup = BeautifulSoup(source, 'lxml')
    blacklist = ['p']
    text_elements = [t for t in soup.find_all(text=True) if t.parent.name in blacklist]
    x = ""
    for i in text_elements:
        x = x + i + " \n\n "

    return jsonify({'Title': Title,
                    'Content': x,
                    'Source': Source,
                    'ImgLink': ImgLink})
    #render_template('index.html', Source='{}'.format(Source), Title='{}'.format(Title), Content='{}'.format(x))

@app.route('/SustainableMenstruation')
def SustainableMenstruation():

    all_articles = newsapi.get_everything(
        q='Sustainable Menstruation',
        language='en',
    )
    length = len(all_articles['articles'])
    r1 = random.randint(0, length-1)
    article = all_articles['articles'][r1]
    Source = article['source']['name']
    Title = article['title']
    Link = article['url']
    ImgLink = article['urlToImage']

    source = requests.get(Link).text
    soup = BeautifulSoup(source, 'lxml')
    blacklist = ['p']
    text_elements = [t for t in soup.find_all(text=True) if t.parent.name in blacklist]
    x = ""
    for i in text_elements:
        x = x + i + " \n\n "

    return jsonify({'Title': Title,
                    'Content': x,
                    'Source': Source,
                    'ImgLink': ImgLink})
    #render_template('index.html', Source='{}'.format(Source), Title='{}'.format(Title), Content='{}'.format(x))


if __name__ == "__main__":
    app.run(debug=True)



