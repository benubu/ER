embed
<drac2>
arg = argparse(&ARGS&)
ch = character()
out = []
elixlist= ["Healing","Swiftness","Resilience","Boldness","Flight","Transformation"]
NEWLINE = "\n"
cc_disp = []

for elix in elixlist:
    ch.create_cc_nx(name=(elix+" Elixirs"), minVal=0, reset="long", reset_to=0)

out.append(f'-f "__Creating an Expiermental Elixir__|"')

noresources = arg.last("i",0,int)
slotlvl = arg.last("l", 1, int) # default to level 1 if not specified
sb = ch.spellbook
flag = True  # Set to false if not ok to create potion.

matching_elixirs = []
for elixir in elixlist:
    if "&1&".lower() in elixir.lower(): # If no argument was given, it'll just be &1&, which won't be in existlist anyway.
        matching_elixirs.append(elixir)

if len(matching_elixirs) is 0:
    out.append(f''' -f "No Matching Elixirs|No valid experimental elixir types found, aborting..." ''')
    flag = False
elif len(matching_elixirs) > 1:
    out.append(f''' -f "Multiple Matching Elixirs|Multiple matching experimental elixirs found, aborting..." ''')
    flag = False
else:
    elixir = matching_elixirs[0]
    
if not noresources and flag: #flag is still true! Let's find a spell slot.
    if sb.get_slots(slotlvl) > 0:
        sb.use_slot(slotlvl)
        out.append(f' -f "Spell Slots|{sb.slots_str(slotlvl)} (-1)"')
    else:
        out.append(f''' -f "Spell Slots|You don't have any level {slotlvl} spell slots remaining, aborting..."''' )
        flag = False
          
if flag and elixir: #flag is still true! Let's create the elixir.
    ch.mod_cc((elixir+" Elixirs"), 1)
    out.append(f' -f "Elixir Created|{elixir}"')

for elix in elixlist: # And lets display the elixirs on hand.
    cc_value = ch.cc_str(elix + " Elixirs")    
    if cc_value[-1] != '0': # Check if the last character of cc_value is not zero
        cc_disp.append(f"{elix}: {cc_value}")
    
elixirs = NEWLINE.join(cc_disp)

if elixirs:
  out.append(f'-f "__Experimental Elixirs On Hand__|{elixirs}"')

return ' '.join(out)
</drac2>

-title "<name>"
-thumb <image>
-color <color>

-footer "!elixir [optional: rest|create|use] [optional: elixir name]"