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

```
user@dev:~/latex-edit$ echo -e 'col1, col2, col3\nValue, other, "some long, value with &"\nother, other, other' | latex-csv-to-table.py -t
\begin{tabluar}{|c|c|c|}
    col1 & col2 & col3 \\ \hline
    Value & other & some long, value with {\&} \\ \hline
    other & other & other \\ \hline
\end{tabluar}
```

## latex-templates.py

```
user@hdev:~/latex-edit$ latex-templates.py -h
usage: latex-templates.py [-h] [-l] [-s SHOW] [-e EDIT] [-r RENDER] [-d DATA]
                          [--no-data]

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            List available templates
  -s SHOW, --show SHOW  Show the specified template
  -e EDIT, --edit EDIT  Edit the specified template. If the specified
                        templates doesn't exist, creates a new with the given
                        name
  -r RENDER, --render RENDER
                        Render the specified template with the JSON data given
                        in 'data' or 'STDIN'. Defaults to reading from STDIN.
  -d DATA, --data DATA  The JSON structure to use for rendering a template
  --no-data             Dont use any data when rendering template
```

For example, rendering the table template using a JSON structure

```
user@hdev:~/latex-edit$ echo '{"table":[ {"col1": "value", "col2" : "value2" }, { "col1": "other", "col2":"data" }]}' | latex-templates.py -r table.j2
\begin{tabluar}{|c|c|}
    col1 & col2 \\ \hline
    value & value2 \\ \hline
    other & data \\ \hline
\end{tabluar}
```

## latex-document.py

WIP
