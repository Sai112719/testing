import json
from bs4 import BeautifulSoup

# Path to your HTML file
html_file_path = html_file_path = "C:/Users/shiva/Downloads/sort.html"

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Example: Extract all text inside <p> tags
paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]

# Example: Convert into JSON
data = {
    "paragraphs": paragraphs
}

# Save to JSON file
with open("output.json", 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Conversion complete. JSON saved as output.json")
