!alias hpdump echo
<drac2>
c = combat
newline = "\n"
output = []

#are we in combat?
if not c:
    desc.append("`!hpdump can only be used in combat.")

monsters = []
players = []
others = []

for combatant in combat().combatants:
    if combatant.levels.get('Monster',None):
        monsters.append(combatant)
    elif combatant.levels.get('Monster',None) == None:
        players.append(combatant)
	else:
	    others.append(combatant)
		
output = 'HP Dump\n'

output += '---> Players <---\n'

for player in players:
    output += f'({player.init}) {player.name}: {player.hp_str()}\n'
	
output += '\n---> Monsters <---\n'

for monster in monsters:
    output += f'({monster.init}) {monster.name}: {monster.hp_str()}\n'
	
if len(others):
    output += '\n---> Others <---\n'

for other in others:
    output += f'({other.init}) {other.name}: {other.hp_str()}\n'

return output
</drac2>
