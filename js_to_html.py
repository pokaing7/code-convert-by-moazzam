def convert(code):
    if "document.write" in code:
        content = code.split("document.write(")[-1].split(")")[0].strip('"').strip("'")
        return f"<p>{content}</p>"
    return "<!-- Unsupported JS code -->"
