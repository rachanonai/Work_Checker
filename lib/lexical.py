import re
import os
import json

PWD_PATH = os.getcwd()
OUTPUT_SEQUENCE_JSON=os.getenv('OUTPUT_SEQUENCE_JSON')

TOKENS = [
    (r'CASE', 'CASE'),
    (r'\d+', 'INTEGER'),
    (r':', 'COLON'),
    (r'>', 'SLASH'),
    (r';', 'ENDLINE'),
    (r'=', 'ASSIGNMENT'),
    (r'@', 'AT'),
    (r'\*', 'EVERYWHERE'),
    (r'"[^"]*"', 'QUOTED_STRING'),
    (r'(?!CASE)\w+(?=\s)(?!\s?=)|\w*(?=;)', 'RESERVED'),
    (r'\w+(?=\s=)', 'ARGUMENT'),
]

TOKEN_REGEXES = [(re.compile(pattern), token_type) for pattern, token_type in TOKENS]

class Tokenizer:
    def tokenize(self, string):
        tokens = []
        current_token = []
        pos = 0

        while pos < len(string):
            match = None
            for regex, token_type in TOKEN_REGEXES:
                match = regex.match(string, pos)
                if match:
                    text = match.group(0)
                    if token_type == 'ENDLINE':
                        tokens.append(current_token)
                        current_token = []
                    current_token.append((token_type, text))
                    pos = match.end(0)
                    break

            if not match:
                raise SyntaxError(f"Illegal character at position {string[pos]}")

            while pos < len(string) and string[pos].isspace():
                pos += 1

        return tokens

    def xpath_convert(self, tokens):
        xpart = []

        for token_group in tokens:
            part = []
            for token_type, text in token_group:
                match token_type:
                    case 'COLON':
                        part.append('/')
                    case 'RESERVED':
                        part.append(text)
                    case 'SLASH':
                        part.append('/')
                    case 'EVERYWHERE':
                        part.append('/')
                    case 'AT':
                        part.append('[@')
                    case 'ARGUMENT':
                        part.append(f'{text}=')
                    case 'QUOTED_STRING':
                        part.append(f'"{text[1:-1]}"]')

            xpart.append(''.join(part))
        return xpart

    def obj2json(self, obj):
        obj = {i + 1: value for i, value in enumerate(obj)}
        return obj

    def get_xpath(self, string):
        token = self.tokenize(string)
        xpaths = self.xpath_convert(token)
        json_obj = self.obj2json(xpaths)
        
        config_path = os.path.join(PWD_PATH, OUTPUT_SEQUENCE_JSON)
        self.save_json(config_path, json_obj)
        
        
        return "complate"
    
    @staticmethod
    def save_json(path, data):
        with open(path, 'w') as file:
            file.truncate(0)
            json.dump(data, file, indent=4)
