import re
from datetime import datetime

# 🔹 Clean and format generated text
def clean_text(text):
    """
    Removes unnecessary spaces, symbols, or weird tokens from GPT output.
    """
    cleaned = re.sub(r'\s+', ' ', text).strip()
    return cleaned

# 🔹 Save generated text to a timestamped file
def save_text_to_file(prompt, generated_text, folder='generated_outputs'):
    """
    Saves prompt + output into a .txt file inside 'generated_outputs/' folder.
    """
    import os
    os.makedirs(folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/output_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Prompt: {prompt}\n\n")
        f.write(f"Generated Text:\n{generated_text}")
    
    return filename

# 🔹 Optional: Count words
def count_words(text):
    return len(text.strip().split())
