from typing import Union
import os

from tqdm import tqdm
from Bio.PDB import PDBList
from graphein.construct_meshes import ProteinMesh


def load_data(experiment: str, in_file: str, out_dir: str) -> None:
    #in_file = os.path.join('../data/', experiment, 'full_list.txt')
    print(in_file)
    #out_dir = os.path.join('../data/raw/', experiment)
    pdbl = PDBList(server='http://ftp.wwpdb.org', verbose=False)
    with open(in_file, 'r') as molecule_id_list:
        molecule_id_list = molecule_id_list.readlines()
        for molecule_id in tqdm(molecule_id_list):
            pdbl.retrieve_pdb_file(molecule_id.strip('\n').split('_')[0], pdir=out_dir, file_format='pdb')
            

def build_mesh_from_pdb_file(pdb_input_file: str, out_dir: str, mesh_object: Union[ProteinMesh, None] = None) -> tuple:
    if mesh_object is None:
        mesh_object = ProteinMesh()
    verts, faces, aux = mesh_object.create_mesh(pdb_file=pdb_input_file)
    return verts, faces, aux
