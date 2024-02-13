import os

def replace_in_files(directory, old_text, new_text):
    for root, dirs, files in os.walk(directory):
        # Check if the current directory is '__pycache__' and skip it
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                file_data = file.read()
            
            # Replace the old_text with new_text in the file data
            new_file_data = file_data.replace(old_text, new_text)
            
            with open(file_path, 'w', encoding='utf-8', errors='ignore') as file:
                file.write(new_file_data)



directory = 'tfsnippet'
old_text = 'import tensorflow as tf'
new_text = """import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()"""

replace_in_files(directory, old_text, new_text)