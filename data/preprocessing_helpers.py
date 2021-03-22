import os

from tqdm import tqdm
from Bio.PDB import PDBList


def load_data(experiment):
    in_file = os.path.join('./', experiment, 'full_list.txt')
    out_dir = os.path.join('./raw/', experiment)
    pdbl = PDBList()
    with open(in_file, 'r') as molecule_id_list:
        for molecule_id in tqdm(molecule_id_list):
            pdbl.retrieve_pdb_file(molecule_id, pdir=out_dir)
            
    