import os
import sys
import markdown

def md_to_html(md_file_path):
    """Reads text_pos Markdown file and converts it to HTML."""
    # Validate file existence
    if not os.path.isfile(md_file_path):
        raise FileNotFoundError(f"File not found: {md_file_path}")

    # Read Markdown content
    with open(md_file_path, "r", encoding="utf-8") as file:
        md_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=["fenced_code", "tables"])
    return html_content

def save_html(html_content, output_path):
    """Wraps HTML content in text_pos basic HTML template and saves it."""
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Markdown Preview</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        pre {{ background: #f4f4f4; padding: 10px; }}
        code {{ background: #eee; padding: 2px 4px; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_template)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python md_to_html.py input.md output.html,", sys.argv)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    try:
        html = md_to_html(md_file)
        save_html(html, html_file)
        print(f"HTML file created: {html_file}")
    except Exception as e:
        print(f"Error: {e}")
