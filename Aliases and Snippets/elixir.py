embed <drac2>
ch = character()
out = []
elixlist= ["Healing","Swiftness","Resilience","Boldness","Flight","Transformation"]
NEWLINE = "\n"
cc_disp = []

for elix in elixlist:
    ch.create_cc_nx(name=(elix + " Elixirs"), minVal=0, reset="long", reset_to=0)    
    cc_value = ch.cc_str(elix + " Elixirs")    
    if cc_value[-1] != '0': # Check if the last character of cc_value is not zero
        cc_disp.append(f"{elix}: {cc_value}")

elixirs = NEWLINE.join(cc_disp)

# Output
if elixirs:
  out.append(f'-f "__Experimental Elixirs On Hand__|{elixirs}"')

return ' '.join(out)
</drac2>

-title "<name>"
-thumb <image>
-color <color>

-footer "!elixir [optional: rest|create|use] [optional: elixir name]"