embed
<drac2>

# Output text
title = f"""{name} recalls all the ice shards to Winter's Fang!"""
desc = "As a bonus action, you can speak the spear's command word to cause all embedded shards to magically return to the blade of the spear, flying through the air and avoiding creatures and objects to do so. When you do, the target takes 1d6 cold for each embedded shard as it leaves the body."
shardName = "Embedded Ice Shard"
shardCC = "Shard of Elemental Ice"
thumb = "https://static.wikia.nocookie.net/zelda/images/3/3d/Breath_of_the_Wild_Elemental_Spears_%28Ice%29_Frostspear_%28Icon%29.png"
nl = "\n"

output = ""
footer = []

if not combat() or not combat().me:
  output += '-f "|This command can only be used if you\'re in combat!" '
else:
  for combatant in combat().combatants:
    effectCount = 0
    for effect in combatant.effects:
      if shardName in effect.name:
        effectCount += 1
        combatant.remove_effect(shardName)
        character().mod_cc(shardCC,1)
        
    if effectCount > 0:
      damage = combatant.damage(str(effectCount)+"d6[cold]")
      output += f""" -f "{combatant.name}|{damage['damage']}" """
      footer.append(f"""{combatant.name} {combatant.hp_str()}""")
      if effectCount >= 3:
        output += f""" -f "{combatant.name}|Speed halved until end of {name}'s next turn" """
        combatant.add_effect("Speed Halved (ice shards)", duration=2, end=1, tick_on_combatant_id=combat().me.id)

footer.append(f'{shardCC}: {character().cc_str(shardCC)}')

return f""" -title "{title}" -desc "{desc}" {output} -thumb "{thumb}" -footer "{nl.join(footer)}" """

</drac2>