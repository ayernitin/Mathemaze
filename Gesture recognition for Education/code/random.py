import random
import bge

cont = bge.logic.getCurrentController()
obj = cont.owner

scene = bge.logic.getCurrentScene()
eq= scene.objects['eq']
output= scene.objects['output']
next= scene.objects['next']
timer= scene.objects['timer']

rnos=[0,0,0,0]
     
def randomGen():
    for i in range(0,4):
        rnos[i] = random.randrange(1,10)
        print(rnos[i])

def optGen(min,max):
    opt1= scene.objects['opt1']
    opt2= scene.objects['opt2']
    opt3= scene.objects['opt3']
    opt=[0,0,0]
    for j in range(0,3):
        opt[j] = random.randrange(min,max)
    print(opt)
    ans=random.randrange(0,3)
    opt[ans]=sum
    print(opt)
    opt1['Text']=opt[0]
    opt2['Text']=opt[1]
    opt3['Text']=opt[2]
    output['ans']=ans + 1

    
def lvlDisp():
    if obj['replay'] == 1:
        obj['replay']=0
    else:
        eq['lvl']= eq['lvl'] + 1 
    level = scene.objects['level']
    level['Text'] = "Level: " + str(eq['lvl'])
    
def playerDisp():
    player = scene.objects['player']
    player.position.x=0
    player.position.y=-6
    player.position.z=1.2
    
def timerExpire():
    if timer['time'] == -1 :
        eq['lvl']=0 
        
        
def init():
    output['Text']="null"
    output.visible = False
    next.visible = False  
    happy = scene.objects['happy']
    happy.visible = False
    sad = scene.objects['sad']   
    sad.visible = False
        
timerExpire()
    
if eq['lvl'] == 0 or obj['replay'] == 1 or output['Text'] == "Correct" :
    timer.visible = True
    if eq['lvl'] <= 3:
        init()
        playerDisp()
        randomGen() 
        lvlDisp()
        
        if eq['lvl'] == 1:
            timer['time']=45
            sum = rnos[0] + rnos[1] - rnos[2] + rnos[3] 
            txtsum = str(rnos[0]) + '+' + str(rnos[1]) + '-' + str(rnos[2]) + '+' + str(rnos[3]) 
            optGen(-6,25)
            
        elif eq['lvl'] == 2:
            timer['time']=75
            sum = rnos[0] * rnos[1] - rnos[2] * rnos[3] 
            txtsum = str(rnos[0]) + '*' + str(rnos[1]) + '-' + str(rnos[2]) + '*' + str(rnos[3]) 
            optGen(0,80)
            
        elif eq['lvl'] == 3:
            timer['time']=60
            sum = rnos[0] - rnos[1] + (rnos[2] * rnos[3])
            txtsum = str(rnos[0]) + '-' + str(rnos[1]) + '+' + str(rnos[2]) + '*' + str(rnos[3])   
            optGen(-7,89)
            
        print(sum)
        print(txtsum)
        eq['Text']= txtsum
    
    
        


   
    
    

