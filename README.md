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
  python search_tool.py --metadata <Location of metadata file> --search <Location of search file>
```

> Help
```
  python search_tool.py --help
```
