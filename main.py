import lib.yaju_match as yaju_match
from os import path

yjmtch = yaju_match.yaju_match("免許もってるのか！？", path.normpath(path.join(path.dirname(__file__), 'list/re.json')))
print(yjmtch.highlight())