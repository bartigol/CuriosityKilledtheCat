from promptflow import tool
import os

@tool
def save_input_to_file(input_text: str) -> str:

    try:
        # Define the data folder and ensure it exists
        data_folder = 'data_to_save'
        os.makedirs(data_folder, exist_ok=True)
        
        # Define the output file path
        output_file_path = os.path.join(data_folder, 'protocol.txt')
        
        # Save the input_text to 'protocol.txt'
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            outfile.write(input_text)
        
        return "Success: Input has been saved to 'protocol.txt'."
    except Exception as e:
        return f"Error: {str(e)}"