import os
import re
import argparse

def extract_python_code(markdown_text):
    """Extracts all Python code blocks from a given markdown text."""
    return re.findall(r'```python(.*?)```', markdown_text, re.DOTALL)

def process_markdown_files(directory, output_directory=None):
    """Processes markdown files and extracts Python code into separate .py files."""
    if output_directory and not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):  # Only process Markdown files
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    markdown_text = f.read()
                    code_blocks = extract_python_code(markdown_text)

                    for idx, code in enumerate(code_blocks):
                        # Create a unique filename based on the markdown file name and block index
                        code_filename = f"{os.path.splitext(file)[0]}_{idx + 1}.py"
                        code_filepath = os.path.join(output_directory if output_directory else root, code_filename)
                        
                        # Save the extracted Python code
                        with open(code_filepath, 'w', encoding='utf-8') as code_file:
                            code_file.write(code.strip())

                        print(f"Extracted: {code_filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract Python code blocks from Markdown files.")
    parser.add_argument("directory", help="Path to the directory containing Markdown files.")
    parser.add_argument("--output", "-o", help="Optional output directory for extracted code files.", default=None)
    
    args = parser.parse_args()
    process_markdown_files(args.directory, args.output)
