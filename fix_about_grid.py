import re

file_path = "/home/jk-niazi/Documents/Iinternship_work/vaks/index.html"
with open(file_path, "r") as f:
    content = f.read()

# Replace <div class="lg:col-span-6 space-y-5" data-aos="fade-right"> with <div class="space-y-5" data-aos="fade-right">
content = content.replace(
    '<div class="lg:col-span-6 space-y-5" data-aos="fade-right">',
    '<div class="space-y-5" data-aos="fade-right">'
)

with open(file_path, "w") as f:
    f.write(content)

print("Fixed about us grid in index.html")
