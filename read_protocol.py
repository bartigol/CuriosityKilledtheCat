from promptflow import tool
import os

@tool
def read_input_from_file() -> str:

    try:
        # Define the data folder and file path
        data_folder = 'data_to_save'
        file_path = os.path.join(data_folder, 'protocol.txt')
        
        # Check if the file exists
        if not os.path.exists(file_path):
            return "Error: The file 'protocol.txt' does not exist in 'data_to_save' folder."
        
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        return content
    except Exception as e:
        return f"Error: {str(e)}"