import re
import json

class yaju_match:
    def __init__(self, scripts, re_path):
        self.scripts = scripts
        self.re_path = re_path
        self.isMatch = False
    
    def re_file_open(self):
        with open(self.re_path, 'r', encoding='utf-8') as file:
            self.re_file = json.load(file)
            file.close()
        return self.re_file
    
    def compile(self):
        self.re_file_open()
        self.re_compile = []
        for re_str in self.re_file:
            res = re.compile(re_str)
            self.re_compile.append(res)
        #self.re_compile = [re.compile(re_str) for re_str in self.re_file]
        return self.re_compile          
        
    def match(self):
        self.compile()
        self.matched = []
        for re_str in self.re_compile:
            res = re.match(re_str, self.scripts)
            if res != []:
                self.matched.append(res)
        return self.matched
    
    def fullmatch(self):
        self.compile()
        self.fullmatched = [re.fullmatch(re_str, self.scripts) for re_str in self.re_compile]
        return self.fullmatched
    
    def findall(self):
        self.compile()
        self.found = []
        for re_str in self.re_compile:
            res = re.findall(re_str, self.scripts)
            if res != []:
                self.found.append(res)
                self.isMatch = True
        return self.found
    
    def highlight(self):
        self.compile()
        for re_str in self.re_compile:
            res = re.findall(re_str, self.scripts)
            if res != []:
                self.found = res
                for found in self.found:
                    self.scripts = self.scripts.replace(found, f"\033[1;31;40m{found}\033[0m")
                return self.scripts