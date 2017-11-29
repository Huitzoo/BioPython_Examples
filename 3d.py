from Bio.PDB import *
import nglview as nv

parse = PDBParser()
pdb = PDBList()
archivo = pdb.retrieve_pdb_file('1FAT')
structure = parser.get_structure('PHA-L','1FAT.cif')
view = nv.show_biopython(structure)
view
