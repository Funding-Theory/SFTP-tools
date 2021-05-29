import numpy
import pandas
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--search', help='Enter Search File with header as ids')
parser.add_argument('--metadata', help='Enter NIBMG Datahub metadata')
args = parser.parse_args()
search_url = args.search
metadata_url = args.metadata
temp = search_url.split('/')

search = pandas.read_csv(search_url, delimiter = '\t', encoding = 'utf-8', low_memory = False)
metadata = pandas.read_csv(metadata_url, delimiter = '\t', encoding = 'utf-8', low_memory = False)
matched = []
unmatched = []
multimatch = []

for i in tqdm(search['ids']):
	match = [j for j in metadata['Virus name'].tolist() if(i in j)]
	if(len(match) == 0):
		unmatched.append(i)
	elif(len(match) == 1):
		matched.append({
			"search query": i,
			"matched term": match[0]
		})
	else:
		multimatch.append(i)

pandas.DataFrame(unmatched, columns = ['All Unmatched']).to_csv('unmatched.tsv', index = False, sep = '\t')
pandas.DataFrame(multimatch, columns = ['All Multimatch']).to_csv('multi_matched.tsv', index = False, sep = '\t')
pandas.DataFrame(matched).to_csv('matched.tsv', index = False, sep = '\t')