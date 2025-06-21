#!/usr/bin/env python3
import os
from termcolor import cprint
from converters.py_to_html import convert as py_to_html
from converters.js_to_html import convert as js_to_html
from converters.html_to_py import convert as html_to_py

def pick_file():
    print("📂 Open your File Manager and choose a file to convert...")
    os.system("termux-open --choose")
    path = input("📄 Paste the full file path here: ").strip()
    return path if os.path.exists(path) else None

def main():
    cprint("\n==========================", "red")
    cprint("        MOAZZAM KHAN      ", "red", attrs=["bold"])
    cprint("==========================\n", "red")

    print("1️⃣ Convert Code")
    print("2️⃣ Follow WhatsApp Channel")

    choice = input("👉 Enter your choice: ")

    if choice == "1":
        file_path = pick_file()
        if not file_path:
            print("❌ File not found or not selected.")
            return

        print("\nSelect target language:")
        print("1: HTML")
        print("2: JavaScript")
        print("3: Python")

        lang_choice = input("🎯 Enter language number: ")

        with open(file_path, "r") as f:
            code = f.read()

        if lang_choice == "1":
            result = py_to_html(code)
            ext = "html"
        elif lang_choice == "2":
            result = js_to_html(code)
            ext = "js"
        elif lang_choice == "3":
            result = html_to_py(code)
            ext = "py"
        else:
            print("❌ Invalid language choice.")
            return

        save_path = f"/storage/emulated/0/Documents/converted_output.{ext}"
        with open(save_path, "w") as f:
            f.write(result)

        print(f"✅ File saved to: {save_path}")

    elif choice == "2":
        os.system("termux-open-url https://wa.me/YOUR_CHANNEL_LINK")
    else:
        print("❌ Invalid option.")

if __name__ == "__main__":
    main()
