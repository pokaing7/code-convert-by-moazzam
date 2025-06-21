def convert(code):
    if "print(" in code:
        content = code.split("print(")[-1].split(")")[0].strip('"').strip("'")
        return f"<p>{content}</p>"
    return "<!-- Unsupported Python code -->"
