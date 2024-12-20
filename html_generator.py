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
               font-family: 'Figtree', sans-serif;
                background-color: #f4d04e;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
        }}
        .card {{
            background-color: white;
            border-radius: 20px;
            max-width: 384px; 
            overflow: hidden;
            box-shadow: 8px 8px rgba(0, 0, 0, 1);
        }}
        .card-image img{{
            width: 336px;
            height: 200px;
            border-radius: 40px;
            padding: 20px;
        }}
        .card-content{{
            padding: 20px;
        }}
        .card h1 {{
            font-weight: 800;
            font-size: 25px;
            margin: 8px 0px;
        }}
            .card h1  > a {{
                text-decoration: none;
                color: #111111;
                transition: color 0.5s ease-in-out;
            }}
            
            .card h1  > a:hover {{
                color: #f4d04e;
            }}
        .card h2 {{
            font-size: 12px;
            color: #6b6b6b;
            line-height: 1.5;
            margin: 8px 0 16px;
        }}
        .card p {{
            font-size: 16px;
            color: #111111;
            margin: 8px 0;
        }}
        .author{{
            display: flex;
            align-items: center;
            padding: 20px;
        }}

        .author-photo{{
            width: 32px;
            height: 32px;
            border-radius: 50%;
            margin-right: 8px;
        }}

        .author-name{{
            font-size: 14px;
            color: #111111;
            font-weight: bold;
        }}
            .author-name  > a {{
                text-decoration: none;
                color: #111111;
                transition: color 0.5s ease-in-out;
            }}
            
            .author-name > a:hover {{
                color: #f4d04e;
            }}
    </style>
</head>
<body>
    <div class="card">
        <div class="card-image">
            <img src="./assets/images/illustration-article.svg" alt="Blog illustration">
        </div>
        <div class="card-content">
            <h1><a href="https://github.com/fernandojosecc/blog-preview-card">{content['title']}</a></h1>
            <h2>{content['description']}</h2>
            <p>{content['body']}</p>
        </div>
        <div class="author">
            <img src="./assets/images/image-avatar.png" alt="Author's photo" class="author-photo">
            <span class="author-name"><a href="https://github.com/fernandojosecc">Fernando Contreras</a></span>
      </div>
    </div>
</body>
</html>
"""
        with open(self.html_file, 'w') as file:
            file.write(html_template)
