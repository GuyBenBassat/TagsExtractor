import os 
from file_tags_extractor import FileTagsExtractor
class DirTagsExtractor():        
    def __init__(self, file_tags_extractor:FileTagsExtractor):
        self.file_tags_extractor = file_tags_extractor
    
    def extract(self, dir_path):
        tags = {}
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root,file)
                if file_path.endswith('.go'):
                    current_tags = self.file_tags_extractor.extract(file_path)
                    for tag in current_tags:
                        tags[tag] = True
        return list(tags.keys())        
        