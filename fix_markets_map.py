import re

file_path = "/home/jk-niazi/Documents/Iinternship_work/vaks/markets.html"
with open(file_path, "r") as f:
    content = f.read()

# We need to remove the header and filter badges from the global-network section in markets.html
# The section starts with <section id="global-network" class="py-12 px-4 bg-[#F4F6F0] w-full overflow-hidden">
# It has <div class="max-w-6xl mx-auto text-center">
# We want to keep <section...> and <div class="max-w-6xl mx-auto text-center">
# But remove everything inside that until <!-- Map Container Locked to Image Bounds -->

pattern = r'(<section id="global-network" class="py-12 px-4 bg-\[\#F4F6F0\] w-full overflow-hidden">\s*<div class="max-w-6xl mx-auto text-center">).*?(<!-- Map Container Locked to Image Bounds -->)'
# Using re.sub with dotall
new_content = re.sub(pattern, r'\1\n            \2', content, flags=re.DOTALL)

with open(file_path, "w") as f:
    f.write(new_content)

print("markets.html map updated successfully.")
