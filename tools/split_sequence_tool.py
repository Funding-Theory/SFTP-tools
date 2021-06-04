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
sequence = SeqIO.to_dict(SeqIO.parse(sequence_url, 'fasta'))
adjusted_sequence = []
ids_not_present = []

for i in tqdm(selected['ids']):
	if(i in list(sequence.keys())):
		adjusted_sequence.append(sequence[i])
	else:
		ids_not_present.append(i)

if(len(ids_not_present)):
	print('Following ids were not present in the fasta file provided')
	for i in ids_not_present:
		print(i)

SeqIO.write(adjusted_sequence, 'selected_sequences.fasta', 'fasta')
