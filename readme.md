# HTML Translation Script

This Python script automates the process of replacing placeholder text in an HTML template with corresponding translations from an Excel file. The script is configured using a JSON file (translate_config.json) to specify the input files and output destination.
Prerequisites

Before running the script, make sure you have the following installed:

    Python 3.x
    The required Python libraries: pandas, beautifulsoup4

You can install the necessary libraries using pip:

bash

pip install pandas beautifulsoup4

How It Works

The script reads translation data from an Excel file, where:

    Column A contains the placeholders (e.g., text1, text2, etc.).
    Column C contains the corresponding translations.

The script then replaces the placeholders in the HTML template with the translations and saves the result to a new HTML file.
Setup

    Prepare the Translation Data: Ensure your Excel file is structured with placeholders in Column A and translations in Column C.

    Create the JSON Configuration File:

    The script requires a configuration file named translate_config.json, with the following structure:

    json

```json
{
    "input": "path_to_excel_file.xlsx",
    "template": "path_to_html_template.html",
    "output": "path_to_output_html.html"
}
```

    input: Path to the Excel file containing the translations.
    template: Path to the HTML template file.
    output: Path where the translated HTML file will be saved.

Run the Script:

Execute the script with Python:

bash

    python translate_html.py

Example

Here’s an example of how your translate_config.json might look:

json

{
    "input": "translate_FR.xlsx",
    "template": "template.html",
    "output": "output_FR.html"
}

This configuration will take the translations from translate_FR.xlsx, apply them to template.html, and save the translated HTML to output_FR.html.
Important Notes

    Ensure that the placeholders in the HTML template exactly match the entries in Column A of the Excel file.
    The script uses the BeautifulSoup library to parse and modify the HTML content. It handles only text replacements and does not affect the structure or attributes of the HTML.

Troubleshooting

    File Not Found Errors: Ensure the paths specified in translate_config.json are correct.
    Incorrect Translations: Double-check that the placeholders in the HTML match those in the Excel file.

License

This project is open-source and available under the MIT License.
