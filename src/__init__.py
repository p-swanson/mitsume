"""
49 43 58 43 20 4E 49 4B 41
"""
import mitsuba as mi
try:
    mi.set_variant("cuda_ad_rgb")
except Exception as exc:
    mi.set_variant("llvm_ad_rgb")
from .render import *
