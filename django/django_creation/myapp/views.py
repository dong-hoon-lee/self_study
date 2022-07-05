from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import random

# Create your views here.
topics = [
    {'id':1, 'title':'Routing', 'body':'Routing is ...'},
    {'id':2, 'title':'View', 'body':'View is ...'},
    {'id':3, 'title':'Model', 'body':'Model is ...'}
]

def HTML_template(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''

# client에게 정보 전송하는 함수
def index(request):
    article = '''
        <h2>Welcome!</h2>
        Hello, Django
    '''
    return HttpResponse(HTML_template(articleTag=article))

def read(request, id):
    global topics
    article = ''

    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'

    return HttpResponse(HTML_template(article))

def create(request):
    article = '''
        <form action="/create/">
            <p><input type="text" placeholder="Title" name="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTML_template(article))
