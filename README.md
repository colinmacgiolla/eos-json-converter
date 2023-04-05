# EOS JSON Running-Config to Text Converter
This script reformats the output of `show running-config | json` back into plain-text for easier human review/manipulation. It also attemts to reformat to a similar syle to the plain-text running-config output.

## Requirements
* Python 3.x
* Libraries:
   * json
   * argparse

## Usage
To run the program, execute the following command:
```bash
python eos-json-converter.py input.json output.eos
```
The input file should be in JSON format and contain a dictionary with a `cmds` key, which is a list of commands. The program will parse these commands, reformat them, and write the output to the specified output file.

## Licence
See [licence file](LICENCE)
