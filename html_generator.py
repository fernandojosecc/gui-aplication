class HTMLGenerator:
    def __init__(self, html_file='index.html'):
        self.html_file = html_file

    def generate_html(self, content):
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{content['title']}</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background-color: #FFD700; /* Bright yellow background */
            background-image: linear-gradient(90deg, rgba(255, 215, 0, 0.8) 10%, rgba(255, 215, 0, 0.6) 90%);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .card {{
            background-color: white;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            width: 300px;
            text-align: center;
            padding: 20px;
        }}
        .card h1 {{
            font-size: 24px;
            color: #4B0082; /* Indigo color */
            margin-bottom: 10px;
        }}
        .card h2 {{
            font-size: 18px;
            color: #696969; /* Dim grey */
            margin-bottom: 20px;
        }}
        .card p {{
            font-size: 16px;
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{content['title']}</h1>
        <h2>{content['description']}</h2>
        <p>{content['body']}</p>
    </div>
</body>
</html>
"""
        with open(self.html_file, 'w') as file:
            file.write(html_template)
