echo`Combatant List:`
<drac2>

args = &ARGS&

if not combat():
  return "The channel isn't in combat!"

monsterNames = []
playerNames = []

for combatant in combat().combatants:
    if combatant.levels.get('Monster',None):
        monsterNames.append(combatant.name)
    elif combatant.levels.get('Monster',None) == None:
        playerNames.append(combatant.name)

if args:
    filteredMonsterNames = [name for name in monsterNames if any(keyword.lower() in name.lower() for keyword in args)]
    monsterNames = filteredMonsterNames
    
    filteredPlayerNames = [name for name in playerNames if any(keyword.lower() in name.lower() for keyword in args)]
    playerNames = filteredPlayerNames


output = ''

for name in monsterNames:
    output += f'-t "{name}|"\n'

output += '\n'

for name in playerNames:
    output += f'-t "{name}|"\n'
    
output += f'\n\n`Filter: &*&`' if args else ''

return output
</drac2>