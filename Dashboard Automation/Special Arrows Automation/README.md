# Expanded Arrows
Questions? @BN on Enter Ravenloft.

[Enter Ravenloft Expanded Arrows](https://drive.google.com/file/d/1wwtqeXpVPMYdraSLVZFhdaF62ybvbZNH/view) *Links PDF on Google Drive*

Ammunition tracking is done via Custom Counters (CCs).

For each ammunition type has a matching CC. For example, the Magefire automation uses a CC called `Magefire Arrow`

Add this CC with this command:

```!cc create "Magefire Arrow" -min 0 -reset none```
(a CC named Magefire Arrow that can't go below zero, has no maximum value, and doesn't reset on rests)

For regular arrows, or any arrows that are recoverable, you need to track how many are used, not just remaining. This will work with the `!collect` alias to recover half after an encounter. 

```!cc create "Arrows" -min 0 -reset none```
(tracking arrows remaining)

```!cc create "Used Arrows" -min 0 -reset none```
(tracking arrows used and can potentially be recovered)

Want to add a bunch at once? Copy/paste the following, but editing to the arrows you actually have and edit the amounts for starting quantities. The list below is all the ones my character BJ has so far.
```
!multiline
!cc create "Arrows" -min 0 -reset none -value 10
!cc create "Used Arrows" -min 0 -reset none -value 0
!cc create "Magefire Arrows" -min 0 -reset none -value 10
!cc create "Blinding Arrows" -min 0 -reset none -value 10
!cc create "Glue Arrows" -min 0 -reset none -value 10
!cc create "Ice Arrows" -min 0 -reset none -value 10
!cc create "Mind Piercer Arrows" -min 0 -reset none -value 10
!cc create "Rope Arrows" -min 0 -reset none -value 10
!cc create "Smoking Arrows" -min 0 -reset none -value 10
!cc create "Healing Arrows" -min 0 -reset none -value 10
```

TIP: Use the `!hud` alias for a much more user friendly to check how many arrows you have on hand. Much cleaner than `!cc` !

-----
To use this with Crossbow Bolts instead, swap out Arrow to Bolt in the CC names, and modify the actions (YAML files) with a find/replace on Arrow to Bolt.
-----
Each of the arrow automations are in the all-in-one, and are split off into their own files. I recommend using the split ones, and just having a separate attack for each arrow type. The all-in-one is a beast to maintain.

I've configured each to be based on a Shortbow +1 (+1 to hit and damage, damage type is magical). Customize that bit to suit yourself - modify the attack and damage lines as needed.
-----
### To Import
Many of these are too large to import directly into discord. Instead, to to the [Avrae Workshop](https://avrae.io/dashboard/characters). Login with your discord credentials if needed. Click Characters at the top left of the left menu bar. 
1) Find the character you would like to add these to. 
2) Click on their portrait.
3) Click the `Wrench` 🔧 icon.
4) Click the `Import YAML` `(arrow pointing down over a horizontal line)`
5) In the pop-up window, copy/paste one of the automations.
6) Click `Import`
7) Repeat steps 4, 5 and 6 for any others you want to add!
8) Need to edit something? Select the action/attack name from the drop down list! 
9) Click the purple `Save` button. They should now be loaded to your character in Discord/Avrae!

-----
### Arrows Implemented so far:
- Normal Arrows (with ammunition tracking)
- Magefire Arrows
- Blinding Arrows
- Glue Arrows
- Ice Arrows
- Mind Piercer Arrows
- Rope Arrows
- Smoking Arrows
- Healing Arrows

### Arrows To Be Implemented (TODO):
- Hammerhead Arrows (adapt normal arrows, but bludgeoning damage)
- Broadhead Arrows (adapt normal arrows, but slashing damage)
- Corkscrew Arrows (adapt normal arrow, add explanatory text)
- Fire Arrows (adapt magefire arrows)
- Concussion Arrows
- Poisoncloud Arrows
- Explosive Arrows
- Thunderclap Arrows
- Lightning Arrows
- Holy Arrows
- Unholy Arrows
- Acid Arrows


