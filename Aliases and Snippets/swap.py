embed
<drac2>
# Swap the grid Location (and Height, if present) between two combatants.
# Usage:
#   !swap Goblin Knight
#   !swap -t "Goblin Boss" -t Knight
# Notes:
#   - Expects Map Utilities-style notes: "Location: <cell>" and optional "Height: <ft>" on each token.

args = argparse(&ARGS&)
c = combat()
if not c:
    err("No active combat is running in this channel.")

# Resolve two names: prefer -t flags, else the first two positional args.
names = args.get('t') or []
if len(names) < 2:
    argv = &ARGS&
    if len(argv) >= 2:
        names = [argv[0], argv[1]]
    else:
        err("Please specify two combatants. Example: `!swap -t Goblin -t Knight` or `!swap Goblin Knight`")

def resolve_one(q):
    ql = q.lower()
    exact = [cmb for cmb in c.combatants if cmb.name.lower() == ql]
    if len(exact) == 1:
        return exact[0]
    if len(exact) > 1:
        err(f'Multiple combatants named exactly "{q}" were found: ' + ", ".join(x.name for x in exact[:10]) + ". Be more specific.")
    subs = [cmb for cmb in c.combatants if ql in cmb.name.lower()]
    if len(subs) == 1:
        return subs[0]
    if len(subs) > 1:
        err(f'Ambiguous "{q}". Matches: ' + ", ".join(x.name for x in subs[:10]) + ". Be more specific or use `-t`.")
    err(f'No combatant found matching "{q}".')

A = resolve_one(names[0])
B = resolve_one(names[1])
if A.id == B.id:
    err("Please specify two different combatants.")

# --- note helpers ---
def parse_note(note):
    note = note or ""
    parts = [p for p in note.split(" | ") if ": " in p]
    data, order = {}, []
    for p in parts:
        k, v = p.split(": ", 1)
        kl = k.strip().lower()
        data[kl] = v.strip()
        order.append((kl, k.strip()))
    return data, order, note

def rebuild_note(orig_note, data, order):
    case_map = {kl: kor for kl, kor in order}
    seen, out = set(), []
    for p in (orig_note or "").split(" | "):
        if ": " not in p:
            continue
        k_orig, _ = p.split(": ", 1)
        kl = k_orig.strip().lower()
        if kl in data:
            label = "Location" if kl == "location" else "Height" if kl == "height" else case_map.get(kl, k_orig.strip())
            out.append(f"{label}: {data[kl]}")
            seen.add(kl)
        else:
            out.append(p.strip())
    for kl, label in (("location","Location"), ("height","Height")):
        if kl in data and kl not in seen:
            out.append(f"{label}: {data[kl]}")
            seen.add(kl)
    for kl, v in data.items():
        if kl not in seen:
            out.append(f"{kl.title()}: {v}")
            seen.add(kl)
    return " | ".join([p for p in out if p])

Ak, Aord, Anote = parse_note(A.note)
Bk, Bord, Bnote = parse_note(B.note)

if "location" not in Ak:
    err(f'{A.name} does not have position information (no "Location:" in its note).')
if "location" not in Bk:
    err(f'{B.name} does not have position information (no "Location:" in its note).')

# Originals
A_loc, B_loc = Ak.get("location"), Bk.get("location")
A_h,   B_h   = Ak.get("height"),   Bk.get("height")

# Swap locations
Ak["location"], Bk["location"] = B_loc, A_loc

# Swap heights (preserve "missing" as missing)
if A_h is not None and B_h is not None:
    Ak["height"], Bk["height"] = B_h, A_h
elif A_h is not None and B_h is None:
    Bk["height"] = A_h
    Ak.pop("height", None)
elif A_h is None and B_h is not None:
    Ak["height"] = B_h
    Bk.pop("height", None)
# else both None -> nothing

# Write back
A.set_note(rebuild_note(Anote, Ak, Aord))
B.set_note(rebuild_note(Bnote, Bk, Bord))

def hchg(old, new):
    if old is None and new is None:
        return ""
    return f" (Height {old if old is not None else '—'} → {new if new is not None else '—'})"

a_line = f"{A.name}: {A_loc} → {Ak['location']}{hchg(A_h, Ak.get('height'))}"
b_line = f"{B.name}: {B_loc} → {Bk['location']}{hchg(B_h, Bk.get('height'))}"

return f'-title "Map Swap" -desc "Positions updated." -f "Summary|{a_line}\\n{b_line}"'
</drac2>
