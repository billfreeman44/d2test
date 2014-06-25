import time

lane_creeps=['Melee','Ranged','Siege']
lane_creep_type=['Normal Lane Creep','Mega Lane Creep']

lane_creep_attributes=['Level',
'experience granted',
'HP',
'HP regen',
'Mana',
'Mana regen',
'Damage',
'Armor',
'Armor Type',
'Movespeed',
'BAT',
'Missile speed',
'Damage Point',
'Damage Point Backswing',
'Casting Point',
'Casting Point backswing',
'Vision day',
'Vision night',
'Acquisition range',
'Type',
'Bounty',
'Upgrade']


Jungle_creep_attributes=['Level',
'HP',
'HP Regen',
'Mana',
'Mana Regen',
'Damage',
'Armor',
'Movespeed',
'BAT',
'Missile speed',
'Damage Point',
'Damage Point Backswing',
'Casting Point',
'Casting Point backswing',
'Vision day',
'Vision night',
'Acquisition range',
'Type',
'Bounty']


jungle_creeps=['[nkob] Kobold',
'[nkot] Kobold Tunneler',
'[nkol] Kobold Taskmaster',
'[ncen] Centaur Outrunner',
'[ncnk] Centaur Khan',
'[ngns] Gnoll Assassin',
'[npfl] Fel Beast',
'[ngh1] Ghost',
'[nfpc] Polar Furbolg Champion',
'[nfpu] Polar Furbolg Ursa Warrior',
'[n026] Mud Golem',
'[nogm] Ogre Mauler',
'[nomg] Ogre Magi',
'[ndtr] Dark Troll',
'[ndtw] Dark Troll Warlord',
'[nwlg] Giant Wolf',
'[n00S] Alpha Wolf',
'[nowb] Wildkin',
'[nowe] Enraged Wildkin',
'[nsat] Satyr Trickster',
'[nstl] Satyr Soulstealer',
'[nsth] Satyr Hellcaller',
'[nftb] Forest Troll Berserker',
'[nfsh] Forest Troll High Priest',
'[n0HW] Harpy Scout',
'[n0HX] Harpy Storm']

Summoned_units=['[n004] Spirit Bear (1)',
'[n018] Spirit Bear (2)',
'[n01C] Spirit Bear (3)',
'[n01G] Spirit Bear (4)',
'[hwat] Lesser Eidolon',
'[hwt2] Eidolon',
'[hwt3] Greater Eidolon',
'[h006] Dire Eidolon',
'[efon] Treant (Force of Nature)',
'[osp4] Serpent Ward (Mass Serpent Ward 1)',
'[o008] Serpent Ward (Mass Serpent Ward 2)',
'[o009] Serpent Ward (Mass Serpent Ward 3)',
'[o01C] Serpent Ward (Mass Serpent Ward 1 Aghanim)',
'[o01D] Serpent Ward (Mass Serpent Ward 2 Aghanim)',
'[o01E] Serpent Ward (Mass Serpent Ward 3 Aghanim)',
'[npn3] Earth (1)',
'[npn6] Earth (2)',
'[n010] Earth Level 3',
'[npn2] Storm Level 1',
'[npn5] Storm Level 2',
'[n012] Storm Level 3',
'[npn1] Fire (1)',
'[npn4] Fire (2)',
'[n011] Fire (3)',
'[n01Q] Scout Hawk',
'[n01R] Greater Hawk',
'[n01M] Quilbeast',
'[n01S] Greater Quilbeast',
'[o00C] Healing Ward',
'[u00G] Ghosts (Exorcism)',
'[ntor] Tornado',
'[uske] Skeleton Warrior',
'[o00T] Plague Ward (1)',
'[o00U] Plague Ward (2)',
'[o00V] Plague Ward (3)',
'[o00W] Plague Ward (4)',
'[u014/u01D/u01R] Familiar (1)',
'[u015/u01E/u01S] Familiar (2)',
'[u016/u01F/u01T] Familiar (3)',
'[o005] Lycanthropy Wolf (1)',
'[o006] Lycanthropy Wolf (2)',
'[o007] Lycanthropy Wolf (3)',
'[o00F] Lycanthropy Wolf (4)',
'[n01E] Spiderite',
'[n019] Spiderling',
'[o000] Death Ward (1)',
'[o001] Death Ward (2)',
'[o00A] Death Ward (3)',
'[o00X] Death Ward (Aghanims)',
'[n00U] Infernal (1)',
'[n00Y] Infernal (2)',
'[n00Z] Infernal (3)',
'[n0KU] Infernal (1 Aghanim)',
'[n0KV] Infernal (2 Aghanim)',
'[n0KW] Infernal (3 Aghanim)',
'[n0FJ/n0FI/n0F6/n0FH] Tombstone - Level 1/2/3/4',
'[n0F5] Living Dead',
'[n027] Forged Spirit',
'[n00J] Necronomicon Warrior 1',
'[n00A] Necronomicon Warrior 2',
'[n006] Necronomicon Warrior 3',
'[n00H] Necronomicon Archer 1',
'[n00G] Necronomicon Archer 2',
'[n00K] Necronomicon Archer 3',
'[o00M] Nether Ward 1',
'[o00L] Nether Ward 2',
'[o00O] Nether Ward 3',
'[o00N] Nether Ward 4',
'[n00O/n00P/n00Q/n00N] Land Mine (1/2/3/4)',
'[otot] Stasis Trap',
'[o018/o002/o00B/o01B] Remote Mine (1/2/3/Aghanim)',
'[e020] Psionic Trap',
'[h0BT/h0BU] Sentinel (passive/active)',
'[u012/u013] Scarab (unburrowed/burrowed)',
'[u01K] Beetle level 1',
'[u01H] Beetle level 2',
'[u01J] Beetle level 3',
'[u01L] Beetle level 4',
'[o01J/o01K/o01L/o01M] Frozen Sigil (1/2/3/4)']

Ancient_creeps=['[nbdk] Black Drake',
'[nbwm] Black Dragon',
'[njg1] Jungle Stalker',
'[njga] Elder Jungle Stalker',
'[nbds] Blue Dragonspawn Sorcerer',
'[nbdo] Blue Dragonspawn Overseer',
'[ngst] Rock Golem',
'[nggr] Granite Golem',
'[n0LC] Thunder Lizard (big)',
'[n0LD] Thunder Lizard (small)']


hero_list=['Abaddon',
'Alchemist',
'Ancient Apparation',
'Anti-Mage',
'Axe',
'Bane',
'Batrider',
'Beastmaster',
'Bloodseeker',
'Bounty Hunter',
'Brewmaster',
'Bristleback',
'Broodmother',
'Centaur Warrunner',
'Chaos Knight',
'Chen',
'Clinkz',
'Clockwerk',
'Crystal Maiden',
'Dark Seer',
'Dazzle',
'Death Prophet',
'Disruptor',
'Doom',
'Dragon Knight',
'Drow Ranger',
'Earthshaker',
'Enchantress',
'Enigma',
'Faceless Void',
'Gyrocopter',
'Huskar',
'Invoker',
'Io',
'Jakiro',
'Juggernaut',
'Keeper of the Light',
'Kunkka',
'Leshrac',
'Lich',
'Lifestealer',
'Lina',
'Lion',
'Lone Druid',
'Luna',
'Lycanthrope',
'Magnus',
'Medusa',
'Meepo',
'Mirana',
'Morphling',
'Naga Siren',
'Natures Prophet',
'Necrolyte',
'Night Stalker',
'Nyx Assassin',
'Outworld Devourer',
'Ogre Magi',
'Omniknight',
'Phantom Assassin',
'Phantom Lancer',
'Pheonix',
'Puck',
'Pudge',
'Pugna',
'Queen of Pain',
'Razor',
'Riki',
'Rubick',
'Sand King',
'Shadow Demon',
'Shadow Fiend',
'Shadow Shaman',
'Silencer',
'Skeleton King',
'Skywrath Mage',
'Slardar',
'Slark',
'Sniper',
'Spectre',
'Spirit Breaker',
'Storm Spirit',
'Sven',
'Templar Assassin',
'Terrorblade',
'Tidehunter',
'Timbersaw',
'Tinker',
'Tiny',
'Treant Protector',
'Troll Warlord',
'Tusk',
'Undying',
'Ursa',
'Vengeful Spirit',
'Venomancer',
'Viper',
'Visage',
'Warlock',
'Weaver',
'Windrunner',
'Witch Doctor',
'Zeus'
]
hero_attributes=['Side',
'Movespeed',
'MaxDmg',
'MinDmg',
'HP',
'Mana',
'HPRegen',
'ManaRegen',
'Armor',
'Range',
'ProjectileSpeed',
'BaseStr',
'BaseAg',
'BaseInt',
'StrGain',
'AgiGain',
'IntGain',
'PrimaryStat',
'BaseAttackTime',
'DayVision',
'NightVision',
'AttackPoint',
'AttackSwing',
'CastPoint',
'CastSwing',
'Turnrate']

hero_uses_df=[[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[1,1],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[1,1],
[1,0],
[0,0],
[0,0],
[1,1],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[1,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[1,1],
[0,0],
[0,0],
[0,0],
[0,0],
[1,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[1,1],
[0,0],
[1,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0]]

hero_abilities=['Q','W','E','R','D','F']

Ability_type=['Active','Passive','Autocast']

Target_type=['instant','point','unit','area']

ability_attribute=['Cooldown',
                    'Damage',
                    'Damage type','Target Type'
                    'Mana Cost',
                    'Stun Duration',
                    'Slow Duration',
                   'mini-stun',
                   'bash',
                    'Debuff duration',
                   
                    'Buff duration','Radius']


Spell_dmg_type=['Magical','Physical','Pure','Composite','HP Removal',' Universal']


Attack_type=['chaos', 'hero', 'normal', 'pierce', 'siege', 'spells']

armor_type=['light', 'medium', 'heavy', 'fortified', 'hero', 'unarmored']

Statuses=['Blind',
'Cyclone',
'Disable',
'Disarm',
'Disjoint',
'Dispel',
'Ensnare',
'Entangle',
'Ethereal',
'Hex',
'Invisibility',
'Invulnerability',
'Magic immunity',
'Mute',
'Pause',
'Purge',
'Silence',
'Sleep',
'Slow',
'Stun',
'Teleport',
'Trap',
'Taunt'
]

game_things=['miss','invunerable','Magic Immune',
             'Allied Heroes','Enemy Heroes','Illusions',
             'blink','Interrupt Channeling','disjoint',
             'projectile','debuff','buff','','','']



f = open('tags_full.txt', 'w')

creep_abilities=['Q','W','E']

for creep in lane_creeps:
    for ty in lane_creep_type:
        f.write(ty+'-'+creep+'\n')
        for at in lane_creep_attributes:
            f.write(ty+'-'+creep+'-'+at+'\n')

for creep in jungle_creeps:
    f.write('Jungle Creep-'+creep+'\n')
    for at in Jungle_creep_attributes:
        f.write('Jungle Creep-'+creep+'-'+at+'\n')


for creep in Ancient_creeps:
    f.write('Ancient Creep-'+creep+'\n')
    for at in Jungle_creep_attributes:
        f.write('Ancient Creep-'+creep+'-'+at+'\n')

for unit in Summoned_units:
    f.write('Summoned unit-'+unit+'\n')
    for at in Jungle_creep_attributes:
        f.write('Summoned unit-'+unit+'-'+at+'\n')
    

for index in range(len(hero_list)):
    f.write('Hero-'+hero_list[index]+'\n')
    for attr in hero_attributes:
        f.write('Hero-'+hero_list[index]+'-'+attr+'\n')
    for ab in hero_abilities:
        if ab == 'Q' or ab == 'W'or ab == 'E' or ab == 'R':
            f.write('Hero-'+hero_list[index]+'-skill_'+ab+'\n')
        if ab == 'D' and hero_uses_df[index][0] == 1:
            f.write('Hero-'+hero_list[index]+'-skill_'+ab+'\n')
        if ab == 'F' and hero_uses_df[index][1] == 1:
            f.write('Hero-'+hero_list[index]+'-skill_'+ab+'\n')

            
for at in Attack_type :
    f.write('Attack Type-'+at+'\n')

for st in Statuses:
    f.write('Status-'+st+'\n')



##for index in range(len(hero_list)):
##    for attr in hero_attributes:
##        print hero_list[index]+'-'+attr
##    for ab in hero_abilities:
##        if ab == 'Q' or ab == 'W'or ab == 'E' or ab == 'R':
##            print hero_list[index]+'-skill_'+ab
##        if ab == 'D' and hero_uses_df[index][0] == 1:
##            print hero_list[index]+'-skill_'+ab
##        if ab == 'F' and hero_uses_df[index][1] == 1:
##            print hero_list[index]+'-skill_'+ab
##
##            
##for at in Attack_type :
##    print 'Attack Type-'+at
##
##for st in Statuses:
##    print 'Status-'+st



f.close()
print "all dun"





