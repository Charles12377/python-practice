players=['charles','martina','macheal','florence','eli']
print('The first three items in the list are:')
print(players[:3])
print(players[-3:])

player=(players[:])
print(players)
print(player)

players.append('kobe')
print(players)
player.append('lebron')
print(player)

for players_1 in players:
    print(players_1)
for player_1 in player:
    print(player_1)