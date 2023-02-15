!alias longExportAttack <drac2>
# Croebh's exportAttack alias, tweaked by <@278245170208571394> for pagination of long outputs.

#Lathaon's embed module: https://github.com/Lathaon/Avrae-Aliases/blob/main/Modules/embeds%2072fea181-ba03-4cb4-8edf-1f3bc5a49578.gvar
using(
    embeds = "72fea181-ba03-4cb4-8edf-1f3bc5a49578"
    )

a = '&1&'.lower() if &ARGS& else 'list'
graves = "`"*3
n = '\n'
target = combat().me if combat() and combat().me else character()
if combat() and (t := argparse(&ARGS&).last('t', type_=combat().get_combatant)):
  target = t
attacks = target.attacks
lenAttacks = len(str(len(attacks)))
attack = None
if (not &ARGS& ) or a == 'list':
  return f"""echo {graves}swift\n{n.join([f"[{i:>{lenAttacks}}] - {x.name}" for i, x in enumerate(attacks)])}{graves}\n> `{ctx.prefix+ctx.alias} [index|name|list] [yaml|json] [-t <target>]` """
else:
  if a.isdigit() and (len(attacks) - 1) >= int(a):
    attack = attacks[int(a)]
  else:
    attack = ([i for i in attacks if a in i.name.lower()] + [None])[0]

  if not attack:
    return f"""echo Could not find an attack {f'at index `{a}`' if a.isdigit() else f'with `{a}` in the name'}."""

  json = dump_json(attack.raw).replace(', "meta": []','')
  yaml = dump_yaml(load_json(json))
  
  #begin to build embed
  desc = ""
  if 'yaml' in '&*&'.lower():
    desc = yaml
  if 'json' in '&*&'.lower():
    decs = json
  else:
    desc = yaml
    
output = {}
output["title"] = "Export Raw Attacks"
fields = []
if len(desc) < 1950:
    output["desc"] = graves+desc+graves
else:
    n = 1000 #chunk size. Discord max field length: 1024
    i = 0
    while i < len(desc):
        if i+n < len(desc):
            fields.append({"title": "", "body": graves+desc[i:i+n]+graves, "inline": False})
        else:
            fields.append({"title": "", "body": graves+desc[i:len(desc)]+graves, "inline": False})
        i += n
output["fields"] = fields

return embeds.get_output(output)
</drac2>
