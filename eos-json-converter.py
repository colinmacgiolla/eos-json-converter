#!/usr/bin/python
# Copyright (c) 2023 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,  this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of the Arista nor the names of its contributors may be used to endorse or promote products derived from this software without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
# GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.

import json
import argparse


def parse_block(block: list, indent=0) -> list:
    '''
    This function takes a dictionary containing information about a block of code, and recursively parses the dictionary to create a list of strings representing the code block.

    Args:
        block (dictionary): A dictionary containing information about a block of code
        indent (integer, optional): An integer representing the amount of indentation to apply to the output.
                                    Default value is 0.

    Returns:
        List: A list of strings representing the parsed block of code with the specified indentation.

    '''
    text = []
    for k,v in block.items():
        if v == None:

            text.append( (k.rjust(len(k)+indent)) )
        else:
            text.append( (k.rjust(len(k)+indent)) )
            text.extend(parse_block(v['cmds'],indent+3))

    return(text)


def reformat_output(config: list) -> list:
    '''
    This function takes a list of strings representing the output of a command or configuration
     and reformats it based on specific rules. The reformatted output is then returned as a new list.

    Args:
        config (list): A list of strings representing the output of a command or configuration.

    Returns:
        A list of strings representing the reformatted output of the input 'config' list.

    Note:
        It is assumed that the input list 'config' contains strings only.
    '''
    formatted_output = []

    for index in range(0,len(config)):
        if index == 0:
            formatted_output.append(config[index])
        elif not config[index][0].isspace():
            if config[index].split()[0] != config[index-1].split()[0]:
                formatted_output.append('!')
                formatted_output.append(config[index])
            else:
                formatted_output.append(config[index])
        else:
            formatted_output.append(config[index])

    return formatted_output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="path to input file")
    parser.add_argument("output_file", help="path to output file")
    args = parser.parse_args()


    with open('args.input_file','r') as f:
        data = json.load(f)

    output = parse_block(data['cmds'])

    formatted_output = reformat_output(output)

    with open(args.outfile,'w') as outFile:
        for item in formatted_output:
            outFile.write("%s\n" % item)

    print("Completed")

    return 0

if __name__ == "__main__":
   main()
