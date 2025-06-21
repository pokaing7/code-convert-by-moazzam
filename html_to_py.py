def convert(code):
    if "<p>" in code and "</p>" in code:
        content = code.split("<p>")[-1].split("</p>")[0]
        return f"print('{content}')"
    return "# Unsupported HTML"
