multiline
<drac2>
arg = argparse(&ARGS&)
ch = character()
out = []
elixlist= ["Healing","Swiftness","Resilience","Boldness","Flight","Transformation"]
NEWLINE = "\n"
cc_disp = []

for elix in elixlist:
    ch.create_cc_nx(name=(elix+" Elixirs"), minVal=0, reset="long", reset_to=0)
    
out.append("!embed")
out.append(f'-f "__Using an Expiermental Elixir__|"')

noresources = arg.last("i",0,int)
flag = True  # Set to false if not ok to use elixir

# is the elixir passed a valid elixir? Partial matches ok.
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
    
# Check CC to see if we have any valid elixirs of that type!
if not noresources and flag: 
    if int(ch.get_cc(elixir+" Elixirs")) > 0:
        ch.mod_cc(elixir+" Elixirs", -1)
        out.append(f' -f "Using {elixir} Elixir|{elixir} Elixirs remaining: {ch.get_cc(elixir+" Elixirs")} (-1)"')
    else:
        out.append(f''' -f "{elixir} Elixirs|You don't have any level {elixir} Elixirs remaining, aborting..."''' )
        flag = False

out.append(f'-title "{name}"')
out.append(f'-thumb {image}')
out.append(f'-color {color}')
out.append('-footer "!elixir [optional: rest|create|use] [optional: elixir name]"')

if flag is True and elixir:
    out.append(f'''!a "Experimental Elixir ({elixir})" {" ".join(&ARGS&[1:]) if len(&ARGS&)>2 else ""}''')

#    out.append(f'!a "Experimental Elixir ({elixir})" {" ".join(['healing'][1:]) if len(['healing'])>2 else ""}')

return NEWLINE.join(out)
</drac2>