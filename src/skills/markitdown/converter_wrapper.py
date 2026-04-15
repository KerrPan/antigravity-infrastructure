import os
import sys
import argparse
from markitdown import MarkItDown

def convert_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False

    # Initialize MarkItDown
    md = MarkItDown()
    
    try:
        # Convert the file
        result = md.convert(file_path)
        content = result.text_content
        
        # Post-process: Clean up NaN values (commonly produced by empty Excel cells)
        import re
        # Replace NaN in table cells (e.g., | NaN |) or standalone
        content = re.sub(r'\bNaN\b', '', content)
        
        # Determine project root (assuming this script is in src/skills/markitdown/)
        # d:\AI_Project\gemini_project\AI_Study\Antigravity\src\skills\markitdown\converter_wrapper.py
        # Root should be d:\AI_Project\gemini_project\AI_Study\Antigravity
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        
        # Ensure temp_md_file directory exists at project root
        output_dir = os.path.join(project_root, "temp_md_file")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Get original filename without extension
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = os.path.join(output_dir, f"{base_name}.md")
        
        # Write to file (Overwrite is implied by 'w')
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"Success: Converted '{file_path}' to '{output_file}'")
        return True
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert files to Markdown and save to project root/temp_md_file.")
    parser.add_argument("--file", required=True, help="Path to the file to convert.")
    args = parser.parse_args()
    
    success = convert_file(args.file)
    if not success:
        sys.exit(1)
