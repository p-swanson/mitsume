"""
49 43 58 43 20 4E 49 4B 41

render a scene with three balls stacking in increasing height
the lower two balls are made of glass, the top one is a light
they are all placed on a rectangle

TODO: 
add stages
"""
from .. import *
import matplotlib.pyplot as plt

to_render = blob('prb')
print("using integrator",to_render.integrator)

coordies = [[0,0,0],[0,0,5],[0,0,10]]
for cords in coordies[:2]:
  to_render.add_ball(coords=cords,material='glass')
to_render.add_ball(coords=coordies[-1],color=[100,100,100])
to_render.add_rectangle()
#
#to_render.background_light()
res = 512
scene = mi.load_dict(to_render)
image = mi.render(scene,sensor=to_render.load_sensor(35,0,45,resolution=(res,res)),spp=512)
plt.axis("off")
plt.imshow(image ** (1.0 / 2.2));
plt.show()
