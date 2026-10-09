import pandas as pd
from bs4 import BeautifulSoup
import json
import os

def translate_html(excel_file, html_file, output_file):
    # Load Excel file
    translations = pd.read_excel(excel_file)

    # Load HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Mapping of tags to translations (col A -> col C)
    translation_dict = dict(zip(translations.iloc[:, 0], translations.iloc[:, 2]))

    # Replace text in HTML
    def replace_text(soup, translation_dict):
        for node in soup.find_all(string=True):
            if node.parent.name not in ['script', 'style']:
                original_text = str(node).strip()
                new_text = original_text
                for key, value in translation_dict.items():
                    if key in original_text:
                        new_text = new_text.replace(key, value)
                if new_text != original_text:
                    node.replace_with(new_text)
        return soup

    soup = replace_text(soup, translation_dict)

    # Save the modified HTML file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f"Translation completed. Result saved in '{output_file}' file")

if __name__ == "__main__":
    with open('translate_config.json', 'r') as config_file:
        config = json.load(config_file)

    excel_file = config["input"]
    html_file = config["template"]
    output_file = config["output"]

    if not os.path.isfile(excel_file):
        print("Excel file doesn't exist.")
    elif not os.path.isfile(html_file):
        print("HTML file doesn't exist.")
    else:
        translate_html(excel_file, html_file, output_file)
