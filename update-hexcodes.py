import os

# Define old and new colors as a dictionary
colors = {
    "#282A36": "#1e1e2e",
    "#44475A": "#45475a",
    "#F8F8F2": "#cdd6f4",
    "#6272A4": "#a6adc8",
    "#8BE9FD": "#89dceb",
    "#50FA7B": "#f9e2af",  # Green to Yellow
    "#FFB86C": "#fab387",
    "#FF79C6": "#f5c2e7",
    "#BD93F9": "#cba6f7",
    "#FF5555": "#f38ba8",
    "#F1FA8C": "#a6e3a1"  # Yellow to Green
}

def replace_colors_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    for old_color, new_color in colors.items():
        content = content.replace(old_color, new_color)

    with open(file_path, 'w') as file:
        file.write(content)

def update_colors_in_repository(repo_path):
    script_path = os.path.realpath(__file__)
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.css') or file.endswith('.less'):
                file_path = os.path.join(root, file)
                # Skip the script file itself
                if os.path.realpath(file_path) == script_path:
                    continue
                replace_colors_in_file(file_path)

# Update colors in the cloned repository
repository_path = "."
update_colors_in_repository(repository_path)

print("Repository colors updated successfully.")
