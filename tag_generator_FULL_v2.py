import time
import sys

def removecomment(text):
    x=text.find('//')
    if x >=0:
        text=text[0:x]
    return text


def maketags(textin,textout,otherout):
    f=open(textin+'.txt','r')
    o=open(textout+'.txt','w')

    #if tag contains this tag, do not display.
    tagblacklist=['RenderablePortrait', \
                  'npc_dota_hero_base', \
                  'ItemSlots', \
                  'Bot', \
                  'BotImplemented', \
                  'ModelScale', \
                  'LoadoutScale', \
                  'HeroGlowColor', \
                  'CMEnabled', \
                  'AbilityPreview', \
                  'ProjectileModel', \
                  'BoundsHullName', \
                  'ParticleFile', \
                  'GameSoundsFile', \
                  'Portrait', \
                  'Model', \
                  'SoundSetBot', \
                  'IdleExpression', \
                  'PickSound', \
                  'BanSound', \
                  'HeroSelectSoundEffect', \
                  'HealthBarOffset', \
                  'var_type', \
                  'precache', \
                  'url', \
                  'HeroUnlockOrder', \
                  'HeroID', \
                  'new_player_enable', \
                  'LastHitChallengeRival', \
                  'Team', \
                  'SoundSet', \
                  'Role', \
                  'Rolelevels', \
                  'IdleSoundLoop', \
                  'Enabled', \
                  'NoCombine', \
                  'NameAliases', \
                  'HeroPool1', \
                  'AbilityBehavior', \
                  'ItemQuality', \
                  'ItemAliases', \
                  'SideShop', \
                  'AbilityDraftDisabled', \
                  'AbilityLayout', \
                  'npc_dota_hero_oracle', \
                  'npc_dota_hero_abyssal_underlord', \
                  'animation_transitions', \
                  'ability_base', \
                  'throw_snowball', \
                  'greevil_miniboss_purple_plague_ward', \
                  'roshan_halloween_candy', \
                  'roshan_halloween_angry', \
                  'roshan_halloween_wave_of_force', \
                  'roshan_halloween_greater_bash', \
                  'roshan_halloween_toss', \
                  'roshan_halloween_shell', \
                  'roshan_halloween_apocalypse', \
                  'roshan_halloween_burn', \
                  'roshan_halloween_levels', \
                  'roshan_halloween_summon', \
                  'roshan_halloween_fireball', \
                  'greevil_magic_missile', \
                  'greevil_cold_snap', \
                  'greevil_decrepify', \
                  'greevil_diabolic_edict', \
                  'greevil_maledict', \
                  'greevil_shadow_strike', \
                  'greevil_laguna_blade', \
                  'greevil_poison_nova', \
                  'greevil_ice_wall', \
                  'greevil_fatal_bonds', \
                  'greevil_blade_fury', \
                  'greevil_phantom_strike', \
                  'greevil_time_lock', \
                  'greevil_shadow_wave', \
                  'greevil_leech_seed', \
                  'greevil_echo_slam', \
                  'greevil_natures_attendants', \
                  'greevil_bloodlust', \
                  'greevil_purification', \
                  'greevil_flesh_golem', \
                  'greevil_hook', \
                  'greevil_rot', \
                  'greevil_black_hole', \
                  'greevil_miniboss_black_nightmare', \
                  'greevil_miniboss_black_brain_sap', \
                  'greevil_miniboss_blue_cold_feet', \
                  'greevil_miniboss_blue_ice_vortex', \
                  'greevil_miniboss_red_earthshock', \
                  'greevil_miniboss_red_overpower', \
                  'greevil_miniboss_yellow_ion_shell', \
                  'greevil_miniboss_yellow_surge', \
                  'greevil_miniboss_white_purification', \
                  'greevil_miniboss_white_degen_aura', \
                  'greevil_miniboss_green_living_armor', \
                  'greevil_miniboss_green_overgrowth', \
                  'greevil_miniboss_orange_dragon_slave', \
                  'greevil_miniboss_orange_light_strike_array', \
                  'greevil_miniboss_purple_venomous_gale', \
                  'greevil_miniboss_sight', \
                  'throw_coal', \
                  'healing_campfire', \
                  'item_winter_greevil_chewy', \
                  'item_winter_greevil_garbage', \
                  'item_winter_greevil_treat', \
                  'item_winter_mushroom', \
                  'item_winter_kringle', \
                  'item_winter_ham', \
                  'item_winter_coco', \
                  'item_winter_cookie', \
                  'item_winter_cake', \
                  'item_winter_skates', \
                  'item_winter_stocking', \
                  'item_present', \
                  'item_greevil_whistle_toggle', \
                  'item_greevil_whistle', \
                  'item_halloween_rapier', \
                  'item_mystery_vacuum', \
                  'item_mystery_toss', \
                  'item_mystery_missile', \
                  'item_mystery_arrow', \
                  'item_mystery_hook', \
                  'item_halloween_candy_corn', \
                  'ItemDeclarations', \
                  'item_recipe_pers', \
                  'item_recipe_power_treads', \
                  'item_recipe_poor_mans_shield', \
                  'item_recipe_ultimate_scepter', \
                  'ItemHideCharges', \
                  'UIPickupSound', \
                  'UIDropSound', \
                  'WorldDropSound', \
                  'ItemShopTags', \
                  'VoiceFile' \
                  ]


    
    replacethis=['magnataur', \
                'wisp', \
                'obsidian_destroyer', \
                'furion', \
                'rattletrap', \
                'skeleton_king', \
                'queenofpain', \
                'zuus', \
                'vengefulspirit', \
                'nevermore', \
                'windrunner', \
                'item_blink', \
                'item_branches', \
                'item_robe', \
                'item_gloves', \
                'item_lifesteal', \
                'item_sobi_mask', \
                'item_ghost', \
                'item_flask', \
                'item_dust', \
                'item_ward_observer', \
                'item_ward_sentry', \
                'item_tpscroll', \
                'item_eagle', \
                'item_relic', \
                'vladmir', \
                'item_pipe', \
                'sheepstick', \
                'ultimate_scepter', \
                'greater_crit', \
                'bfury', \
                'manta', \
                'lesser_crit', \
                'item_armlet', \
                'invis_sword', \
                'skadi', \
                'ancient_janggo', \
                'npc_dota_hero_', \
                'dotaheroes' \
                ]

    
    replacewith=['magnus', \
                'io', \
                'outworld_devourer', \
                'natures_prophet', \
                'clockwerk', \
                'wraith_king', \
                'queen_of_pain', \
                'zeus', \
                'vengeful_spirit', \
                'shadow_fiend', \
                'windranger', \
                'item_blink_dagger', \
                'item_iron_branch', \
                'item_robe_of_the_magi', \
                'item_gloves_of_haste', \
                'item_morbid_mask', \
                'item_sages_mask', \
                'item_ghost_scepter', \
                'item_healing_salve', \
                'item_dust_of_appearance', \
                'item_observer_ward', \
                'item_sentry_ward', \
                'item_town_portal_scroll', \
                'item_eaglesong', \
                'item_sacred_relic', \
                'vladmirs_offering', \
                'item_pipe_of_insight', \
                'scythe_of_vyse', \
                'aghanims_scepter', \
                'daedalus', \
                'battle_fury', \
                'manta_style', \
                'crystalys', \
                'item_armlet_of_mordiggian', \
                'shadow_blade', \
                'eye_of_skadi', \
                'drum_of_endurance', \
                '', \
                'heroes' \
                 ]
    
        

    tagtree = []
    tagsNoDuplicates = []
    #TODO: Consider things after "\\" a comment
    for line in f:
        line=removecomment(line)
        #parse line into things with quotes
        parsed=line.split('"')
        #print parsed
        closetag=0
        for par in parsed:
            if '}' in par :closetag=1
            if '\t' in par or '\n' in par or \
            '//' in par or par == '' or par == ' ':
                try:
                    parsed.remove(par)
                except:
                    pass
        #print line
        #remove a tag if a "}" was found in that line
        if closetag == 1 :
            if len(tagtree) >0:
                t=tagtree.pop()

        #add tag to tagsNoDuplicates if it doesn't exist in there already
        if len(parsed) >=1 :
            if parsed[0] not in tagsNoDuplicates:
                tagsNoDuplicates.append(parsed[0])

        #replace tag if needed.
        if len(parsed) >=1 :
            for index in range(len(replacethis)):
                parsed[0]=parsed[0].replace(replacethis[index],replacewith[index])

        #add to "tag tree" if solo tag.
        if len(parsed) == 1 :
            tagtree.append(parsed[0])


        #check if its "blacklisted"
        doprint=1
        for tag in tagtree:
            for bltag in tagblacklist:
                if tag == bltag: doprint=0
                if len(parsed) >= 1 and parsed[0] == bltag: doprint=0
                
        if doprint == 1 and len(parsed) >=1 :      
            for tag in tagtree:
                o.write("@"+tag)
            if len(parsed) == 1 :
                o.write('\n')
            if len(parsed) == 2 :
                o.write("@"+parsed[0])
                o.write(" = "+parsed[1]+'\n')

            #print


        #print oparsed
    
        



    f.close()
    o.close()
    o=open(otherout+'.txt','w')
    for tag in tagsNoDuplicates:
        o.write("@"+tag+'\n')
    print "all dun"


maketags('npc_heroes','tags_full_heroes','tags_small_heroes')

maketags('npc_abilities','tags_full_abilities','tags_small_abilities')

maketags('items','tags_full_items','tags_small_items')

