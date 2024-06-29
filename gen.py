import json
import re
from os import path

file_path = path.normpath(path.join(path.dirname(__file__), 'list/scripts.json'))

scripts = open(0).read()
scripts = re.split(r'[ \n]', scripts)

with open(file_path, 'w') as file:
    json.dump(scripts, file, indent=4, ensure_ascii=False)
    file.close()
