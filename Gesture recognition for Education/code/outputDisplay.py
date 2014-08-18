import bge

cont = bge.logic.getCurrentController()
obj = cont.owner
ans= obj['ans']

scene = bge.logic.getCurrentScene()
next = scene.objects['next']
eq = scene.objects['eq']
timer = scene.objects['timer']

timer['time']=-30
timer.visible = False
msgSensor = cont.sensors["msgS"]
msgs= msgSensor.subjects
if msgs[0] == str(ans):
    obj['Text']="Correct"
    happy = scene.objects['happy']
    happy.visible = True
    if eq['lvl'] < 3:
        next.visible = True
else:
    obj['Text']="Wrong"      
    sad = scene.objects['sad']   
    sad.visible = True
