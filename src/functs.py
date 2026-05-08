"""
49 43 58 43 20 4E 49 4B 41

helper functions to download structure files 
and save as .obj for ease-of-use

"""

import pymol
from pathlib import Path

def structure_to_obj(inputfile:str,outname:str=None):
    """
    read in 3d atomic coordinates
    into pymol and save as a .obj file
    ..warning:: will overwrite existing files if the names are the same
    
    parameters
    ----------
    :param inputfile: file to load
    :param outname: name of the output file, must have .obj suffix

    TODO:
    dont overwrite existing files
    some os, Pathlib stuff
    """
    if not outname:
        outname = "out.obj"
    if Path(outname).stem != ".obj":
        print("must save as .obj, im adding it now")
        outname += ".obj"
    ############################################
    pymol.pymol_argv = ['pymol','-qc']
    pymol.finish_launching()
    cmd = pymol.cmd
    #cmd.fetch('1ALU')
    cmd.load(inputfile,object="to_go")
    cmd.save(outname,"to_go")
    cmd.reinitialize()
    return

def fetch(pdbid:str,debug:bool=True):
    """
    fetch sstructure file from RCSB
    download trucdture to current directory 
    usually as a .cif file
    
    parameters
    ---------
    :param pdbid: PDB ID code to download
    :param debug: run verbose
    
    example
    -------
    cmd.fetch('1ALU')
    """
    pymol.pymol_argv = ['pymol','-qc']
    pymol.finish_launching()
    cmd = pymol.cmd
    cmd.fetch(pdbid)
    if debug:
        print(f"downloaded PDB:{pdbid}")
    cmd.reinitialize()
    return 
