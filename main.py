import os
import sys
import dotenv
import argparse

dotenv.load_dotenv()
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

import lexical
import logic
import tool

OUTPUT_SEQUENCE_JSON=os.getenv('OUTPUT_SEQUENCE_JSON')
INPUT_SEQUENCE=os.getenv('INPUT_SEQUENCE')
RAR_REGEX=os.getenv('RAR_REGEX')

def main():
    parser = argparse.ArgumentParser(
            description='A script to filtering correct work according to specified conditions. and provide reasons for incorrect work',
            epilog='Checker © 2024 by Rachanon Peasu is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International '
    )
    
    input_group = parser.add_argument_group('Input arguments')
    input_group.add_argument('-i', '--input', type = str, required = False, help = 'Input file path')
    input_group.add_argument('-c', '--compile', action = 'store_true', required = False, help = 'Compile your config file')
    args = parser.parse_args()
    
    file_manager = tool.FileManager()

    if args.compile:
        token = lexical.Tokenizer() 
        line = tool.FileOparetion(INPUT_SEQUENCE)
        xpath = token.get_xpath(line.get_content())
        print(xpath)
        exit(0)
    

    if args.input:
        valid_file = file_manager.validate_files(args.input, RAR_REGEX)
 
        for file in valid_file:
            try:
                tester = file_manager.access_rar(os.path.join(args.input, file), 'index.html')
                print(f'{file}: {logic.Logic(tester).test()}')
            except Exception as e:
                print(f'Error processing {file}: {e}')

if __name__ == "__main__":
    main()
