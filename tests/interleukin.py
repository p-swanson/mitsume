"""
49 43 58 43 20 4E 49 4B 41
download and render interleukin-6 (IL6)

"""
from ..src import *
try:
    stage = "fetching protein"
    fetch("1ALU")
    stage = "downloaded protein"
    stage = "turning into .obj file "
    structure_to_obj("1ALU.cif")
    ###################
    stage = "__init__ mitsume w/defaults"
    to_render = blob()
    stage = "loading obj into mitsume"
    to_render.add_obj("test.obj",color=[1,0,1])
    stage = "adding background light"
    to_render.background_light()
    stage = "passing to mitsuba "
    scene = mi.load_dict(to_render)
    stage = "going to render"
    image = mi.render(scene,sensor=to_render.load_sensor(100,50,45),spp=256)
    stage = "render finished, plotting now"
    plt.axis("off")
    plt.imshow(image ** (1.0 / 2.2));
    plt.show()
except Exception as exc:
    print("FAILED AT STAGE",stage)
    print(exc)
