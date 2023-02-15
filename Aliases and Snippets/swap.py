embed 
-title "Swapping Combatants"
-footer "!help swap | Created by @benubu#7644"

<drac2>
# Sets the args variable to the parsed arguments, and sets the c variable to the combat() object (or None if the channel isn't in combat).
args,c  = argparse(&ARGS&),combat() 
newline = "\n"
desc    = [] #output to players

#are we in combat?
if not c:
    desc.append("The `!swap` command can only be used in combat.")
    
#extract targets
targets = args.get("t")
combatants = []
for x in targets:
    cx = c.get_combatant(x)
    if cx is not None: combatants.append(cx)
        
if len(targets) != 2 or len(combatants) != 2:
    desc.append("The `!swap`  requires two valid targets. For example,  `!swap -t jack -t jill`. \n\The wrong number of valid targets were found.")



newNotes = {}
for target in combatants:
    #If they have a note, perse it into a dict
    if target.note and ':' in target.note:
        note=target.note
        note=note.split(" | ")
        note={x[0].lower():x[1] for x in [item.split(": ") for item in note]}     
        if note.get('location'):
            note['location'] = note['location'].upper()
            newNotes[target.name]=note
            #Check if we have any overlays attached to effects, and then if at effect exists
            for overNum in [""]+[str(x) for x in range(1,11)]:
                if newNotes[target.name].get('effect'+overNum):
                    checkEffect, checkEffectTarget = newNotes[target.name].get('effect'+overNum).split(' / ')
                    # If the effect (or the target it was on) are gone, remove the effect
                    if not gt(checkEffectTarget) or not gt(checkEffectTarget).get_effect(checkEffect):
                        _ = newNotes[target.name].pop('effect'+overNum) if 'effect'+overNum in newNotes[target.name] else None
                        _ = newNotes[target.name].pop('aim'+overNum) if 'aim'+overNum in newNotes[target.name] else None
                        _ = newNotes[target.name].pop('overlay'+overNum) if 'overlay'+overNum in newNotes[target.name] else None
                        desc.append(f"""Overlay {overNum} removed from `{target.name}` because effect `{checkEffect}` no longer present{f" on {checkEffectTarget}" if checkEffectTarget!=target.name else ""}.""")
                        desc.append("")
    elif target.note:
        note=target.note
        desc.append(f"Found a incorrectly formatted note on {target.name}, reformatted as a `-note`. ")
        newNotes[target.name] = {"note": note.replace(':',' ').replace('|',' ')}
    else:
        newNotes[target.name]={}
        
desc.append(newNotes)

return f""" -desc "{newline.join(desc)}"  """ if desc else ""
</drac2>