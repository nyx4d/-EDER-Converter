import tkinter as tk
from tkinter import filedialog
import os
import base64

def encode_js_to_binary(input_file, output_file):
    """Encodes a JavaScript file into binary format."""
    with open(input_file, 'r', encoding='utf-8') as f:
        js_code = f.read()
    
    # Encode to Base64
    binary_data = base64.b64encode(js_code.encode('utf-8'))
    
    # Save to output file
    with open(output_file, 'wb') as f:
        f.write(binary_data)

def process_file():
    """Handles file selection and encoding."""
    input_file = filedialog.askopenfilename(filetypes=[("JavaScript Files", "*.js")])
    if not input_file:
        return

    output_file = os.path.splitext(input_file)[0] + ".bin"
    encode_js_to_binary(input_file, output_file)
    result_label.config(text=f"Encoded file saved as: {output_file}")

# Create GUI
root = tk.Tk()
root.title("JavaScript to Binary Converter")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Drag and drop your JavaScript file:")
label.pack()

process_button = tk.Button(frame, text="Select File", command=process_file)
process_button.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

root.mainloop()
