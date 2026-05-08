"""
49 43 58 43 20 4E 49 4B 41

just a series of functions for interfacing with mitsuba.
loading and manipulating objects according to mitsuba protocols
its just kind of annoying to deal with dictionaries so
i made these to simplify
"""
import mitsuba as mi
class blob(dict):
  def __init__(self,integrator:str='path',max_depth:int=1):
    """
    Initialize the class with an existing .obj file if you want.
    if you dont input an .obj file thats fine too, you just create empty scence
    ----------
    obj_: path/to/file.obj
    integrator : integrator name to use. default: path integrator
    """

    #self.t_scene = {'type': 'scene','integrator': {'type': 'path'}}
    self['type'] = 'scene'
    self['integrator'] = {'type': integrator,'max_depth': max_depth}
    ###

    self.ball_count = int()
    self.obj_count = int()
    self.rect_count = int()
    self.cube_count = int()
    self.material_count = int()
    ####

    ####
    ## here i will create some of the known materials and give them some names
    names = {'default':{'type':'diffuse'},
             'glass':{'type':'dielectric','int_ior': 'water','ext_ior': 'air'},
             'hair':{'type': 'hair','eumelanin': 0.2,'pheomelanin': 0.4},
             'light2':{'type':'twosided',
                       'material':{'type':'diffuse',
                                   'reflectance': {
                                       'type': 'rgb',
                                       'value': 0.4}}}}

    for key,val in names.items():
      self[key] = val

  def add_material(cls,name:str,params:dict):
    """
    Choose material to pass to your uh, thingy
    see : https://mitsuba.readthedocs.io/en/stable/src/generated/plugins_bsdfs.html
    -
    now you can pass the name of your material when creating objects yeheahae
    """
    #cls.material_count += 1
    cls[name] = params


  def add_obj(cls,obj_:str,translate:list=[0,0,-1.5],rotate:tuple=([0,0,0],0),color:list=[1.0,1.0,1.0],name:str=None,material:str=None,light:bool=False):
    """
    add ANYTHING in a .obj file
    ------------
    center
    """
    from mitsuba import ScalarTransform4f as T
    #####
    assert type(obj_) == str, "must be filename (with appropriate path) of .obj file"
    ###
    cls.obj_count += 1
    if not name:
      name = f"object{cls.obj_count}"
    if not material:
      if light:
        cls[name] = {
            'type': 'obj',
            'filename': obj_,
            'to_world': mi.ScalarAffineTransform4f().translate(translate),
            'emitter': {'type': 'area','radiance': {'type': 'rgb','value': color,}}}
      else:
        cls[name] = {
            'type': 'obj',
            'filename': obj_,
            'to_world': mi.ScalarAffineTransform4f().translate(translate),
            'bsdf': {'type': 'diffuse','reflectance': {'type': 'rgb', 'value':color},}}
    else:
      cls[name] = {
            'type': 'obj',
            'filename': obj_,
            'to_world': T().translate(translate),
            'bsdf': {'type': 'ref','id':material}}

  def add_ball(cls,coords:list=[0,0,0],radius:int=1,color:list=[1.0,1.0,1.0],name:str=None,material:str=None,light:bool=True):
    """
    Add ball to the image
    ---------------
    coords: uhh
    radius: cmonn dude
    color: [r,g,b] (scales intensity fyi)
    light: if you want your ball to glow
    """
    cls.ball_count += 1

    if not name:
      name = f"ball{cls.ball_count}"

    if not material:
      if light:
        cls[name] = {'type': 'sphere',
                     'to_world': mi.ScalarAffineTransform4f().scale([radius,radius,radius]).translate([i/radius for i in coords]),
                     'emitter': {'type': 'area','radiance': {'type': 'rgb','value': color,}}}
      else:
        cls[name] = {'type': 'sphere',
                     'to_world': mi.ScalarAffineTransform4f().scale([radius,radius,radius]).translate([i/radius for i in coords]),
                     'bsdf': {'type': 'diffuse','reflectance': {'type': 'rgb', 'value': color},}}
    else:
      cls[name] = {'type': 'sphere',
                   'to_world': mi.ScalarAffineTransform4f().scale([radius,radius,radius]).translate([i/radius for i in coords]),
                   'bsdf': {'type': 'ref',
                            'id':material}}

  def background_light(cls,rgb_:list=[1,1,1]):
    """
    Add default constant environemntal light with
    color: [r,g,b]
    """
    cls["bg_light"] = {'type': 'constant','radiance': {'type': 'rgb','value': rgb_}}

  def add_rectangle(cls,size:list=[20, 10, 1],translate:list=[0,0,-5],rotate:tuple=([0,0,0],0),color:list=[0.1, 0.2, 0.3],name:str=None,material:str=None,light:bool=False):
    """
    add a rectangle
    args are self-explanatory
    --------
    rotate: rotate roatate[1] degrees around the axis rotate[0]
    """
    cls.rect_count +=1
    if not name:
      name = f"rectangle{cls.rect_count}"

    if not material:
      if light:
        cls[name] = {'type': 'rectangle',
            'to_world': mi.ScalarAffineTransform4f().scale(size).translate(translate).rotate(rotate[0],rotate[1]),
            'emitter': {'type': 'area','radiance': {'type': 'rgb', 'value': color},}}
      else:
        cls[name] = {'type': 'rectangle',
            'to_world': mi.ScalarAffineTransform4f().scale(size).translate(translate).rotate(rotate[0],rotate[1]),
            'bsdf': {'type': 'diffuse','reflectance': {'type': 'rgb', 'value': color},}}
    else:
      cls[name] = {'type': 'rectangle',
            'to_world': mi.ScalarAffineTransform4f().scale(size).translate(translate).rotate(rotate[0],rotate[1]),
            'bsdf': {'type': 'ref','id':material}}

  def add_cube(cls,size:list=[5, 5, 5],translate:list=[0,0,0],rotate:tuple=([0,0,0],0),color:list=[0.1, 0.2, 0.3],name:str=None,material:str=None,light:bool=False):
    """
    Add that cube
    """
    cls.cube_count += 1
    if not name:
      name = f"cube{cls.cube_count}"

    if not material:
      if light:
        cls[name] ={'type': 'cube',
                    'to_world':mi.ScalarAffineTransform4f().scale(size).translate(translate).rotate(rotate[0],rotate[1]),
                    'emitter': {'type': 'area','radiance': {'type': 'rgb', 'value': color},}}
      else:
        cls[name] = {'type': 'cube',
            'to_world': mi.ScalarAffineTransform4f().scale(size).translate(translate).rotate(rotate[0],rotate[1]),
            'bsdf': {'type': 'diffuse','reflectance': {'type': 'rgb', 'value': color},}}
    else:
      cls[name] = {'type': 'cube',
            'to_world': mi.ScalarAffineTransform4f().scale(size).translate(translate).rotate(rotate[0],rotate[1]),
            'bsdf': {'type': 'ref','id': material}}

  def load_sensor(cls, r, phi, theta,resolution:tuple=(256,256)):
    """
    this is where you view the picture from
    centered around the origin
    r: distance
    phi: phi angle
    theta: okay you get it now
    -----------
    resolution: in x,y pixels
    """
    from mitsuba import ScalarTransform4f as T
    # Apply two rotations to convert from spherical coordinates to world 3D coordinates.
    origin = T().rotate([0, 0, 1], phi).rotate([0, 1, 0], theta) @ mi.ScalarPoint3f([0, 0, r])

    return mi.load_dict({
        'type': 'perspective',
        'fov': 39.3077,
        'to_world': T().look_at(
            origin=origin,
            target=[0, 0, 0],
            up=[0, 0, 1]
        ),
        'sampler': {
            'type': 'independent',
            'sample_count': 16
        },
        'film': {
            'type': 'hdrfilm',
            'width': resolution[0],
            'height': resolution[1],
            'rfilter': {
                'type': 'tent',
            },
            'pixel_format': 'rgb',
        },
    })
