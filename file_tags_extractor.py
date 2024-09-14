import re

class FileTagsExtractor():
    
    tags_pattern = re.compile(r'^\s*//\s*\+build\s+(.+)')
    
    def __init__(self):
        pass 

    def extract(self, file_path):
        file_tags_list = []
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read all lines into a list
            lines = file.readlines()
        
            # Print each line
            for line in lines:
                 # Check if the line matches the build tag pattern
                match = self.tags_pattern.match(line)
                if match:
                    file_tags = match.group(1)
                    file_tags_list += re.split(r'[,\s]+', file_tags.replace('!',''))
        return file_tags_list        
        