class ByKnownItemsSeparator():
    def __init__(self, known_items):
        self.known_items = known_items
    
    def extract(self, tags_list):
        known_items = []
        other = []
        for tag in tags_list:
            if tag in self.known_items:
                known_items.extend([tag])
            else:
                other.extend([tag])
        return known_items, other