#DarkMode
import tkinter as tk
from tkinter import scrolledtext

# conversion functions
def to_sentence_case(text):
    return text.capitalize()

def to_lower_case(text):
    return text.lower()

def to_upper_case(text):
    return text.upper()

def to_capitalized_case(text):
    return text.title()

def to_alternating_case(text):
    return ''.join(c.lower() if i % 2 else c.upper() for i, c in enumerate(text))

def to_title_case(text):
    return text.title()

def remove_characters(text, chars_to_remove):
    return text.translate({ord(c): None for c in chars_to_remove})

def replace_characters(text, chars_to_replace, replace_with):
    return text.replace(chars_to_replace, replace_with)

def remove_duplicates(text):
    # Split the text by spaces, remove duplicates, sort, and join back to string
    items = text.split()
    unique_items = sorted(set(items), key=items.index)
    return ' '.join(unique_items)

#  button click handlers
def on_convert_button_click(conversion_func):
    input_text = input_text_box.get("1.0", tk.END).strip()
    converted_text = conversion_func(input_text)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, converted_text)

def on_remove_button_click():
    input_text = input_text_box.get("1.0", tk.END).strip()
    chars_to_remove = remove_entry.get()
    converted_text = remove_characters(input_text, chars_to_remove)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, converted_text)

def on_replace_button_click():
    input_text = input_text_box.get("1.0", tk.END).strip()
    chars_to_replace = replace_entry.get()
    replace_with = with_entry.get()
    converted_text = replace_characters(input_text, chars_to_replace, replace_with)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, converted_text)

# main window
root = tk.Tk()
root.title("Text Converter")

# dark mode colors
bg_color = "#2E2E2E"
fg_color = "#FFFFFF"
button_color = "#4A4A4A"
button_fg_color = "#FFFFFF"
entry_bg_color = "#3E3E3E"
entry_fg_color = "#FFFFFF"
text_box_bg_color = "#1E1E1E"
text_box_fg_color = "#FFFFFF"

root.configure(bg=bg_color)

# Create the input text box
input_text_label = tk.Label(root, text="Enter your text:", bg=bg_color, fg=fg_color)
input_text_label.pack()
input_text_box = scrolledtext.ScrolledText(root, width=50, height=10, bg=text_box_bg_color, fg=text_box_fg_color, insertbackground=fg_color)
input_text_box.pack()

#  buttons
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack()

buttons = [
    ("Sentence case", to_sentence_case),
    ("lower case", to_lower_case),
    ("UPPER CASE", to_upper_case),
    ("Capitalized Case", to_capitalized_case),
    ("aLtErNaTiNg cAsE", to_alternating_case),
    ("Title Case", to_title_case),
]

for btn_text, func in buttons:
    button = tk.Button(button_frame, text=btn_text, command=lambda func=func: on_convert_button_click(func),
                       bg=button_color, fg=button_fg_color)
    button.pack(side=tk.LEFT)

#  remove 
remove_frame = tk.Frame(root, bg=bg_color)
remove_frame.pack()

remove_label = tk.Label(remove_frame, text="Remove characters:", bg=bg_color, fg=fg_color)
remove_label.pack(side=tk.LEFT)
remove_entry = tk.Entry(remove_frame, bg=entry_bg_color, fg=entry_fg_color, insertbackground=fg_color)
remove_entry.pack(side=tk.LEFT)
remove_button = tk.Button(remove_frame, text="Remove", command=on_remove_button_click, bg=button_color, fg=button_fg_color)
remove_button.pack(side=tk.LEFT)

# replace text
replace_frame = tk.Frame(root, bg=bg_color)
replace_frame.pack()

replace_label = tk.Label(replace_frame, text="Replace character:", bg=bg_color, fg=fg_color)
replace_label.pack(side=tk.LEFT)
replace_entry = tk.Entry(replace_frame, width=5, bg=entry_bg_color, fg=entry_fg_color, insertbackground=fg_color)
replace_entry.pack(side=tk.LEFT)
with_label = tk.Label(replace_frame, text="with:", bg=bg_color, fg=fg_color)
with_label.pack(side=tk.LEFT)
with_entry = tk.Entry(replace_frame, width=5, bg=entry_bg_color, fg=entry_fg_color, insertbackground=fg_color)
with_entry.pack(side=tk.LEFT)
replace_button = tk.Button(replace_frame, text="Replace", command=on_replace_button_click, bg=button_color, fg=button_fg_color)
replace_button.pack(side=tk.LEFT)

#  remove duplicates 
duplicates_frame = tk.Frame(root, bg=bg_color)
duplicates_frame.pack()

duplicates_button = tk.Button(duplicates_frame, text="Remove Duplicates", command=lambda: on_convert_button_click(remove_duplicates),
                              bg=button_color, fg=button_fg_color)
duplicates_button.pack(side=tk.LEFT)

# output text box
output_text_label = tk.Label(root, text="Converted text:", bg=bg_color, fg=fg_color)
output_text_label.pack()
output_text_box = scrolledtext.ScrolledText(root, width=50, height=10, bg=text_box_bg_color, fg=text_box_fg_color, insertbackground=fg_color)
output_text_box.pack()

# Run 
root.mainloop()
