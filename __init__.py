"""
49 43 58 43 20 4E 49 4B 41
------------------------------------------
 __  __ ___ _____ ____  _   _ __  __ _____     
|  \/  |_ _|_   _/ ___|| | | |  \/  | ____| 
| |\/| || |  | | \___ \| | | | |\/| |  _|  
| |  | || |  | |  ___) | |_| | |  | | |___ 
|_|  |_|___| |_| |____/ \___/|_|  |_|_____|
                                           
-------------------------------------------
* Mistu (honey) + Me (eyes) = mitsume (staring)

Library for interfacing with Mitsuba 3.

essentially just a series of helper functions.
Focus is on visualizing atomistic simulation data 
(i.e. proteins)

its not very good... but thats okay, because I dont care
I didn't use any AI because it is good to suffer.


------------------------------------
If using in a publication, please cite:

@software{jakob2022mitsuba3,
    title = {Mitsuba 3 renderer},
    author = {Wenzel Jakob and Sébastien Speierer and Nicolas Roussel and Merlin Nimier-David and Delio Vicini and Tizian Zeltner and Baptiste Nicolet and Miguel Crespo and Vincent Leroy and Ziyi Zhang},
    note = {https://mitsuba-renderer.org},
    version = {3.0.1},
    year = 2022,
}

"""
"""import mitsuba as mi
try:
    mi.set_variant("cuda_ad_rgb")
except Exception as exc:
    mi.set_variant("llvm_ad_rgb")
"""
from .src.render import blob
from .src.functs import *
