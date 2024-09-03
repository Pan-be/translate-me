import pandas as pd
from bs4 import BeautifulSoup
import json
import os

# Function to load an Excel file and convert tags into translations
def translate_html(excel_file, html_file, output_file):
    # Load excel file
    translations = pd.read_excel(excel_file)

    # Load HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Mapping of tags to transaltions (col A -> col C)
    translation_dict = dict(zip(translations.iloc[:, 0], translations.iloc[:, 2]))

    # Fun to replace tags in HTML
    def replace_text(soup, translation_dict):
        for tag in soup.find_all(text=True):
            stripped_text = tag.string.strip() if tag.string else ''
            if stripped_text in translation_dict:
                tag.string.replace_with(translation_dict[stripped_text])
        return soup

    # HTML text replacement
    soup = replace_text(soup, translation_dict)

    # Save the modified HTML file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f"Translation completed. Result saved in '{output_file}' file")

# Main part of tools
if __name__ == "__main__":
    # load configuration from json file
    with open('translate_config.json', 'r') as config_file:
        config = json.load(config_file)
    
    excel_file = config["input"]
    html_file = config["template"]
    output_file = config["output"]

    # Check whether the specified files exist
    if not os.path.isfile(excel_file):
        print("Excel file doesn't exist.")
    elif not os.path.isfile(html_file):
        print("HTML file doesn't exist.")
    else:
        # Make the translation
        translate_html(excel_file, html_file, output_file)
