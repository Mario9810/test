
from Scripts.Index import *
import random
image = SR()
image.glInit()
image.glCreateWindow(1500,1500)
image.lookAt((-1,1.765,5), (0,0,0), (0,0.5,0))
image.glViewPort(0,0,1500,1500)
image.setFileName("./proyecto.bmp")

print("inicia renderizado")
print("render (1/6)")
image.loadOBJ("./OBJs/CloudN.obj", translate=(-0.6,0.65,0), scale=(0.08,0.08,0.08), rotate=(-0.2,-0.8,0))
print("render (2/6)")
image.loadOBJ("./OBJs/CloudN.obj", translate=(0.075,0.2,0), scale=(0.08,0.08,0.08), rotate=(-0.2,-0.8,0))
print("render (3/6)")
image.loadOBJ("./OBJs/floor.obj", translate=(0.25,-1,-0.5), scale=(0.25,-0.4,0.08), rotate=(0.75,0,-0.2), fill=True)
print("render (4/6)")
image.loadOBJ("./OBJs/polyhouse.obj", translate=(0.70,-1,0), scale=(0.15,0.15,0.15), rotate=(-0.35,1,-0.10), fill=True)
print("render (5/6)")
image.loadOBJ("./OBJs/PolyT.obj", translate=(-0.30,-0.8,0), scale=(0.15,0.15,0.15),fill=True)
print("render (6/6)")
image.loadOBJ("./OBJs/outlamp.obj", translate=(0.075,-0.9,0), scale=(0.08,0.08,0.08), rotate=(-0.2,-0.8,0))
print("render terminado")

image.glFinish()
