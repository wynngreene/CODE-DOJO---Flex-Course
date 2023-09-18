print("connected")

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32,
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]
# print("---------")

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
    
    def choose_player(number):
        new_player = Player(players[number]["name"],players[number]["age"],players[number]["position"],players[number]["team"])
        return new_player

    def create_player(number):
        create_player = players[number]
        return create_player
    
new_team = []








print("---------")
# player_Kevin = players[0]
# player_Kevin = Player(players[0]["name"],players[0]["age"],players[0]["position"],players[0]["team"])
# print(player_Kevin.team)
# player_kevin = Player.choose_player(0)
print("---------")
kevin = Player.create_player(0)
print(kevin)
print("---------")
new_list = Player.make_list(kevin)

print(new_team)


