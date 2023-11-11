embed <drac2>

nl = "\r\n"

out = [
    f'-title "{character().name} makes a transaction."',
    f'-footer "!help transaction | Created by psykhe#7776"'

]

coin_multiplier = {'pp':(1000,'gp'),'gp':(100,'ep'),'ep':(50,'sp'),'sp':(10,'cp'),'cp':(1,None)}
coin_transactions = {'pp':0,'gp':0,'ep':0,'sp':0,'cp':0}
args = &ARGS&
for i in range(len(args)):
    if i+1 < len(args):
        if args[i] == '+' or args[i] == '-':
            args[i] = f'{args[i]}{args[i+1]}'.strip()
            args[i+1:i+2] = []
for i in range(len(args)):
    if i+1 < len(args):
        try:
            val = float(args[i])
        except:
            continue
        if args[i+1].lower() in coin_multiplier:
            args[i] = f'{args[i]}{args[i+1]}'
            args[i+1:i+2] = []
total_transaction = 0

#Eligibility Validation
# if ctx.channel.id != 908125593206394900: # channels: transactions
#    out.append(f'-f "Wrong channel. This command can only be executed in <#908125593206394900>"')
#    return ' '.join(out)

# check if old coin pouch still exists
bags = load_json(get('bags','[[""]]'))
new_bags = []
should_update_bags = False
for bag_item in bags:
    if "Coin Pouch" in bag_item:
        coin_pouch = bag_item[1]
        coin_pouch_total = 0
        
        # check if the coin pouch is empty. if it is just update the bags without the coin pouch. if it's not, requires the other command
        for currency in coin_pouch:
            coin_pouch_total += coin_pouch[currency]
            
        if coin_pouch_total > 0:
            out.append('-f "Error|Your character is using the old version of the coin pouch. Update to the new one by using the command `!coins` twice, before you can make any transactions."')
            return ' '.join(out)
        else:
            should_update_bags = True
    else:
        new_bags.append(bag_item)

if should_update_bags:
    character().set_cvar("bags",dump_json(new_bags))

# check args    
if not args:
    out.append('-f "Error|No log provided."')
    return ' '.join(out)

if not args[1:]:
    out.append('-f "Error|No transactions were recorded\nNot enough arguments."')
    return ' '.join(out)

def update_coin(coins, val, currency, mult):
    cp_val = floor(coin_multiplier[currency][0] * val * 100)/100.0
    cur_currency = currency
    while cp_val > 0:
        cur_currency_val, next_currency = coin_multiplier[cur_currency]
        cur_val = int(cp_val // cur_currency_val)
        coins[cur_currency] += mult * cur_val
        cp_val = cp_val % cur_currency_val
        cur_currency = next_currency
        if not cur_currency:
            break

# get all coin changes requested
for arg in args[1:]:
    try: # test if it's only number, if so, assume it's in GP
        transaction_currency = 'gp'
        transaction_value = abs(float(arg))
    except:
        transaction_currency = arg[-2:]
        try:
            transaction_value = abs(float(arg[:-2]))
        except:
            out.append(f'-f "Error|\'{arg}\' is not a valid amount."')
            return ' '.join(out)
    
    if transaction_currency.lower() not in coin_transactions.keys():
        out.append(f'-f "Error|\'{transaction_currency}\' is not a valid coin type."')
        return ' '.join(out)
    
    if arg[0] == "-":
        multiplier = -1
    else:
        multiplier = 1
    update_coin(coin_transactions, transaction_value, transaction_currency, multiplier)
    total_transaction += multiplier * transaction_value * coin_multiplier[transaction_currency][0]
    
# output transaction reason and given values
transaction_str = str(args[1:])
for c in "[],'":
    transaction_str = transaction_str.replace(c,"")
out.append(f'-desc "**Reason:** {args[0]}\n**Transaction:** {transaction_str}"')
    
# check if transaction is possible
if character().coinpurse.total*100 + total_transaction < 0:
    out.append(f'-f "Error|You don\'t have enough currency to complete the transaction."')
    return ' '.join(out)
    
# make transaction
transaction_result = character().coinpurse.modify_coins(pp=coin_transactions['pp'], gp=coin_transactions['gp'], ep=coin_transactions['ep'], sp=coin_transactions['sp'], cp=coin_transactions['cp'], autoconvert = True) 

# output results
transaction_result_str = ""
for currency in coin_transactions.keys():
    transaction_result_str += character().coinpurse.coin_str(currency)
    if transaction_result[currency] != 0:
        transaction_result_str += f" ({transaction_result[currency]:+g} {currency})"
    transaction_result_str += "\n"

out.append(f'-f "Transaction Result|{transaction_result_str}"')

# Tool Proficiencies
# using(toollib = "6251e20c-7545-4c63-92af-31e0745f2b0c") # tool lib
proficiencies = character().get_cvar("pTools", default='').replace(', ', nl)
if proficiencies:
  proficiencies = proficiencies + nl
proficiencies = proficiencies + character().get_cvar("eTools", default='').replace(', ', nl)

if len(proficiencies):
  out.append(f' -f "Proficiencies (`!tool`)|{proficiencies}"')
else:
  out.append('-f "|No `!tool` proficiencies"')

# Grab character sheet, add as footer.
types={
 "beyond":{
  "url":"https://ddb.ac/characters/",
  "name":"D&D Beyond"
 },
 "dicecloud":{
  "url":"https://v1.dicecloud.com/character/",
  "name":"Dicecloud v1"
 },
 "dicecloudv2":{
  "url":"https://dicecloud.com/character/",
  "name":"Dicecloud v2"
 },
 "google":{
  "url":"https://docs.google.com/spreadsheets/d/",
  "name":"Google Sheets"
 }
}
raw=character()
if raw.sheet_type in types:
  out.append(f'''-f "{'[Character Sheet]('+types[raw.sheet_type].url+raw.upstream.replace(raw.sheet_type+'-','')+')'}" ''')

out.append(f'-thumb {get("image")}')
out.append(f'-color {get("color")}')


return ' '.join(out)
</drac2>
