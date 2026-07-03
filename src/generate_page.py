import os

from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown. Please add a title using a level 1 heading (# Title).")


def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    title = extract_title(markdown)
    html_content = markdown_to_html_node(markdown).to_html()
    with open(template_path, "r") as f:
        template = f.read()
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(html)


def generate_pages_recursive(from_dir, template_path, to_dir):
    for root, dirs, files in os.walk(from_dir):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, from_dir)
                dest_path = os.path.join(to_dir, relative_path).replace(".md", ".html")
                generate_page(from_path, template_path, dest_path)