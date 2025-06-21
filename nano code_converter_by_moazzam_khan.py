"""
Tool Name: CODE CONVERTER
Author: Moazzam Khan
"""

# File: py_to_html.py
def convert_py_to_html(py_code):
    return f"<pre>{py_code}</pre>"

# ============================================================

# File: html_to_py.py
def convert_html_to_py(html_code):
    return html_code.replace("<pre>", "").replace("</pre>", "")

# ============================================================

# File: js2scml.py
def convert_js_to_scml(js_code):
    return f"// Converted to SCML\n{js_code}"

# ============================================================

# File: main.py
import os

# Functions reused from above (normally would import from files)
def convert_py_to_html(py_code):
    return f"<pre>{py_code}</pre>"

def convert_html_to_py(html_code):
    return html_code.replace("<pre>", "").replace("</pre>", "")

def convert_js_to_scml(js_code):
    return f"// Converted to SCML\n{js_code}"

def main():
    print("\033[91m")
    print("  ███╗░░░███╗░█████╗░░██████╗███████╗███████╗███████╗███╗░░░███╗")
    print("  ████╗░████║██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝████╗░████║")
    print("  ██╔████╔██║██║░░██║╚█████╗░█████╗░░█████╗░░█████╗░░██╔████╔██║")
    print("  ██║╚██╔╝██║██║░░██║░╚═══██╗██╔══╝░░██╔══╝░░██╔══╝░░██║╚██╔╝██║")
    print("  ██║░╚═╝░██║╚█████╔╝██████╔╝███████╗███████╗███████╗██║░╚═╝░██║")
    print("  ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝╚══════╝╚══════╝╚═╝░░░░░╚═╝")
    print("\n              Created by MOAZZAM KHAN")
    print("\n[1] Convert Code\n[2] Follow WhatsApp Channel")

    choice = input("\nChoose an option: ")
    if choice == "1":
        file_path = input("Enter file path: ")
        if not os.path.exists(file_path):
            print("File not found.")
            return
        with open(file_path, "r") as file:
            code = file.read()
        print("\nSelect conversion type:")
        print("[1] HTML\n[2] JavaScript\n[3] Python")
        lang_choice = input("Choose (1/2/3): ")
        if lang_choice == "1":
            result = convert_py_to_html(code)
        elif lang_choice == "2":
            result = convert_js_to_scml(code)
        elif lang_choice == "3":
            result = convert_html_to_py(code)
        else:
            print("Invalid option.")
            return
        output_file = "/data/data/com.termux/files/home/storage/shared/Documents/converted_output.txt"
        with open(output_file, "w") as out_file:
            out_file.write(result)
        print(f"Converted code saved to: {output_file}")
    else:
        print("Follow @MOAZZAM_WA_Channel for more tools.")

if __name__ == "__main__":
    main()