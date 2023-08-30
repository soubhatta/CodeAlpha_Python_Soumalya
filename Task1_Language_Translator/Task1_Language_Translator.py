import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def translate_text():
    text = text_entry.get()
    source_lang = source_lang_var.get()
    dest_lang = dest_lang_var.get()
    translation = translate(text, source_lang, dest_lang)
    translation_label.config(text=translation)

def translate(text, source_lang, dest_lang):
    translator = Translator()
    translated = translator.translate(text, src=source_lang, dest=dest_lang)
    return translated.text

def main():
    global text_entry, translation_label, source_lang_var, dest_lang_var  # Declare variables as global

    root = tk.Tk()
    root.title("Language Translator")
    root.geometry("500x350")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12), background="blue", foreground="black")

    title_label = ttk.Label(root, text="Language Translator", font=("Arial", 16, "bold"), padding=(0, 10))
    title_label.pack()

    source_lang_label = ttk.Label(root, text="Main Language")
    source_lang_label.pack(pady=5)

    source_lang_var = tk.StringVar()
    source_lang_combobox = ttk.Combobox(root, textvariable=source_lang_var, values=list(LANGUAGES.values()))
    source_lang_combobox.pack(pady=5)
    source_lang_combobox.set("English")

    label = ttk.Label(root, text="Enter Your Text")
    label.pack(pady=5)

    text_entry = ttk.Entry(root, font=("Arial", 12), width=30)
    text_entry.pack(pady=5)

    dest_lang_label = ttk.Label(root, text="Translated Language")
    dest_lang_label.pack(pady=5)

    dest_lang_var = tk.StringVar()
    dest_lang_combobox = ttk.Combobox(root, textvariable=dest_lang_var, values=list(LANGUAGES.values()))
    dest_lang_combobox.pack(pady=5)
    dest_lang_combobox.set("Bengali")

    translate_button = ttk.Button(root, text="Translate", command=translate_text)
    translate_button.pack(pady=10)

    translation_label = ttk.Label(root, text="", font=("Arial", 12), wraplength=450, justify="center")
    translation_label.pack()

    footer_label = ttk.Label(root, text="Project of Soumalya", font=("Arial", 10, "bold" ), padding=(0, 10))
    footer_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
