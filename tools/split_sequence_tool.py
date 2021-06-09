import pandas
import argparse
from tqdm import tqdm
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument('--fasta', help='Enter Fasta')
parser.add_argument('--selected', help='Enter selected headers')
args = parser.parse_args()
sequence_url = args.fasta
metadata_url = args.selected

selected = pandas.read_csv(metadata_url, delimiter = '\t', encoding = 'utf-8')
selected_sequence = []

test = [selected_sequence.append(i) for i in tqdm(SeqIO.parse(sequence_url, 'fasta')) if(i.id in selected['ids'])]

SeqIO.write(selected_sequence, 'selected_sequences.fasta', 'fasta')
