import time
import sys

def makejs(textin):
    f=open(textin+'.txt','r')
    o=open('js_'+textin+'.js','w')
    o.write(textin+'=[\n')
    linelist=[]
    for line in f:
        linelist.append(line)
    
    for index in range(len(linelist)):
        line=linelist[index]
        linenoat=line[1:-1].lower()
        if index != len(linelist)-1:
            o.write("'"+linenoat+"',\n")
        else:
            o.write("'"+linenoat+"'\n")
    o.write(']\n')


    
    f.close()
    o.close()
    print "all dun"

#use for small file first
makejs('tags_small_heroes')

makejs('tags_small_abilities')

makejs('tags_small_items')

