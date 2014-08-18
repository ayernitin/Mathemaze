import bge

cont = bge.logic.getCurrentController()
obj = cont.owner

val = obj['time']
obj['Text'] = "Time Remaining: " + str(val) + " secs"
