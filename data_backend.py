import json

class ContentStorage:
    def __init__(self, file_path='page_content.json'):
        self.file_path = file_path

    def load_content(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Default content structure
            return {
                "title": "My Website",
                "description": "Welcome to my website!",
                "body": "This is the main content of the webpage."
            }

    def save_content(self, content):
        with open(self.file_path, 'w') as file:
            json.dump(content, file, indent=4)
