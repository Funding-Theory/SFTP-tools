# SFTP-tools
These tools are used to make searching and extracting data easier

### Install the required packages by using the following command
```
  pip install -r requirements.txt
```

### Search Tool
> Requirements

- `Search file` and `Metadata file` must be in `tsv` format
- `Search file` must contain the header `ids` as shown below


| ids |
| - |
| search term 1 | 
| search term 2 | 
| search term 3 | 
| ... |
| search term n |

> Usage
```
  python tools/search_tool.py --metadata <Location of metadata file> --search <Location of search file>
```

> Help
```
  python tools/search_tool.py --help
```

### Split sequence Tool
> Requirements

- `Selected file` must be in `tsv` format
- `Selected file` must contain the header `ids` as shown below


| ids |
| - |
| header 1 | 
| header 2 | 
| header 3 | 
| ... |
| header n |

> Usage
```
  python tools/split_sequences_tool.py --fasta <Location of fasta file> --selected <Location of selected header file>
```

> Help
```
  python tools/split_sequences_tool.py --help