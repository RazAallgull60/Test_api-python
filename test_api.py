import requests

Post = requests.post('http://127.0.0.1:5000/movies', json={'genre': 'Adventure', 'title': 'Doctor Strange', 'year': 2022}).status_code
if Post == 201:
    print(Post, "Le test est une réussite totale")
else:
    print(Post, "Le test est un échec cuisant")     

Get = requests.get('http://127.0.0.1:5000/movies/1').status_code
if Get == 200:
    print(Get, "Le test est une réussite totale ")
else:
    print(Get, "Le test est un échec cuisant")  

Put = requests.put('http://127.0.0.1:5000/movies/2', json={'genre': 'Adventure', 'title': 'Doctor Strange', 'year': 2030}).status_code
if Put == 200:
    print(Put, "Le test est une réussite totale")
else:
    print(Put, "Le test est un échec cuisant")  

Delete = requests.delete('http://127.0.0.1:5000/movies/1').status_code
if Delete == 200:
    print(Delete, "Le test est une réussite totale")
else:
    print(Delete, "Le test est un échec cuisant")