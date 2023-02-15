embed -title "{{name}} drink's a Potion of Fire Breath!"
{{desc = "After drinking this potion, you can use a bonus action to exhale fire at a target within 30 feet of you. The target must make a DC 13 Dexterity saving throw, taking 4d6 fire damage on a failed save, or half as much damage on a successful one. The effect ends after you exhale the fire three times or when 1 hour has passed."}}
-desc '{{desc}}'
-thumb "https://cdnb.artstation.com/p/assets/images/images/043/067/573/medium/jsngne-fire-potion-d.jpg"
-f "Fire Breath: Uses remaining| ◉◉◉"


<drac2>
ch = character()
cc = "Potion of Fire Breath: Uses remaining"
ch.create_cc(cc, 0, 3, "none", "bubble", None, None, cc, desc, 3)

if combat() and combat().me:
    combat().me.add_effect("Potion of Fire Breath", duration = 601, 
        attacks = [{
                "attack": {
                    "name": "Breathe Fire",
                    "_v": 2,
                    "activation_type": 3,
                    "automation": [{
                        "type": "counter",
                        "counter": "Potion of Fire Breath: Uses remaining",
                        "amount": "1",
                        "allowOverflow": "false",
                        "errorBehaviour": "warn"
                    }, {
                        "type": "roll",
                        "dice": "4d6 [fire]",
                        "name": "damage",
                        "hidden": "false"
                    }, {
                        "type": "target",
                        "target": "all",
                        "effects": [{
                            "type": "save",
                            "stat": "dex",
                            "fail": [{
                                "type": "damage",
                                "damage": "{damage}",
                                "overheal": "false"
                            }],
                            "success": [{
                                "type": "damage",
                                "damage": "({damage})/2",
                                "overheal": "false"
                            }],
                            "dc": "13"
                        }]
                    }, {
                        "type": "condition",
                        "condition": "lastCounterRemaining < 1",
                         "onTrue": [{
                            "type": "remove_ieffect",
                            "removeParent": "always"
                        }],
                        "onFalse": [],
                        "errorBehaviour": "false"
                    }]
                }
            }]
    )
    return """-f '|Syntax: `!a "breathe fire" -t <target1> -t <target2> ...`' """
else: 
    return """-f '|Tracking CC added, but no there is no additional automation outside of combat!'"""
</drac2>