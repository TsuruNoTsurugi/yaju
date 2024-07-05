import lib.yaju_match as yaju_match
from os import path
import sys

with open(path.normpath(path.join(path.dirname(__file__), 'out.txt')), 'r', encoding='utf-8') as file:
    S = file.read()
    file.close()
yjmtch = yaju_match.yaju_match(S, path.normpath(path.join(path.dirname(__file__), 'list/re.json')))
yjmtch.findall()
print(yjmtch.isMatch, end="")