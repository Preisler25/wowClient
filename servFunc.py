import requests
from appConst import player

def sendToServer():
    # The API endpoint
    url = "http://localhost:3000/login?username=admin&password=admin&email=admin"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    print(response_json)

def sendLogin(name, password):
    # The API endpoint
    url = "http://localhost:3000/login?username=" + name + "&password=" + password

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    print(response_json)
    if response_json["status"] == True:
        player.name = name
        player.password = password
        player.email = response_json["email"]
        player.best_time = response_json["best_time"]
        player.games_played = response_json["games_played"]
        player.miss_clicked = response_json["miss_clicked"]
        print(player)
        return True
    

"""
{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
"""