from django.shortcuts import HttpResponse

# Create your views here.

topics = [
    {"id": 1, 'title': 'routing', 'body': 'Routing is ..'},
    {"id": 2, 'title': 'view', 'body': 'View is ..'},
    {"id": 3, 'title': 'model', 'body': 'Model is ..'},
]


def HTMLTemplate(articleTag):
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
        </body>
    </html>
    '''


def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''

    return HttpResponse(HTMLTemplate(article))


def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'

    return HttpResponse(HTMLTemplate(article))
