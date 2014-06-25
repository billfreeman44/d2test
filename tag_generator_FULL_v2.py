import time
import sys

def maketags(textin,textout,otherout):
    f=open(textin+'.txt','r')
    o=open(textout+'.txt','w')

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
                  'VoiceFile' \
                  ]

    tagmothers = []
    tagsNoDuplicates = []
    #TODO: Consider things after "\\" a comment
    for line in f:
        #parse line into things with quotes
        parsed=line.split('"')
        #print parsed
        closetag=0
        for par in parsed:
            if '}' in par :closetag=1
            if '\t' in par or '\n' in par or \
            '//' in par or par == '':
                try:
                    parsed.remove(par)
                except:
                    pass

        #remove a tag if a "}" was found in that line
        if closetag == 1 :
            t=tagmothers.pop()

        #add tag to tagsNoDuplicates if it doesn't exist in there already
        if len(parsed) >=1 :
            if parsed[0] not in tagsNoDuplicates:
                tagsNoDuplicates.append(parsed[0])

        #ensure tags don't get wonky.  I'm not even sure
        #how this was happening, but it was...
        if len(parsed) == 1 :
            if parsed[0].count('npc_dota_hero') == 1:
                while len(tagmothers) > 1  : t=tagmothers.pop()
            tagmothers.append(parsed[0])

        
        doprint=1
        for tag in tagmothers:
            for bltag in tagblacklist:
                if tag == bltag: doprint=0
                if len(parsed) >= 1 and parsed[0] == bltag: doprint=0
                
        if doprint == 1 and len(parsed) >=1 :      
            for tag in tagmothers:
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

