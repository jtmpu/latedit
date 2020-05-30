# Latedit

A python library with accompanying CLI programs for editing and
manipulating Latex documents.

The CLI programs show case examples of how to use the python API to 
interact with latex documents.

## Setup

Install using

```
pip3 install .
```

This will ensure that dependencies are downloaded, and all CLI programs
are added to your path. The jinja templates are also created in the
directory `~/.latedit/templates`.

A lot of API functions use environment structures. The configuration file
for the environment structures can be generated using `latex-environment.py`.

## latex-environment.py

```
user@dev:~/latex-edit$ latex-environment.py -h
usage: latex-environment.py [-h] [-g] [-f] [-s] [-e]

optional arguments:
  -h, --help      show this help message and exit
  -g, --generate  Generate a default environment configuration
  -f, --force     Overwrites existing configuration when generating
  -s, --show      Show the current environment configuration
  -e, --edit      Edit the current environment configuration
```

## latex-encode.py

```
user@dev:~/latex-edit$ latex-encode.py -h
usage: latex-encode.py [-h] [-d DATA]

optional arguments:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  Data to encode, otherwise reads from STDIN.
```

## latex-csv-to-table.py

```
user@dev:~/latex-edit$ latex-csv-to-table.py -h
usage: latex-csv-to-table.py [-h] [-t] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -t, --has-header      Parse the first row as the header row
  -f FILE, --file FILE  The file to read the CSV from. If not specified, reads
                        from STDIN.
```

## latex-document.py

WIP
