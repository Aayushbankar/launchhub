import re

def parse_and_replace_tokens(file_path, context=None):
    
    
    
    ALLOWED_TOKENS = {"project_name", "author", "date", "description", "license"}

    if context is None:
        context = {}

    # Read file
    with open(file_path, "r") as f:
        content = f.read()

    # Find all {{token}} fields
    raw_tokens = re.findall(r"\{\{(.*?)\}\}", content)
    tokens = set(token.strip() for token in raw_tokens if token.strip() in ALLOWED_TOKENS)


    # Ask for missing values
    for token in tokens:
        if token not in context:
            user_input = input(f"Enter value for '{token}': ").strip()
            context[token] = user_input

    # Replace all tokens
    for key, value in context.items():
        content = content.replace(f"{{{{{key}}}}}", value)

    # Write modified content back
    with open(file_path, "w") as f:
        f.write(content)

    return context  # Can be logged if needed
