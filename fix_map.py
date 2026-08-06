import re

file_path = "/home/jk-niazi/Documents/Iinternship_work/vaks/index.html"
with open(file_path, "r") as f:
    content = f.read()

old_map_pattern = r'<!-- Map Container Locked to Image Bounds -->\n    <div class="relative inline-block w-full max-w-4xl mx-auto">\n      <img src="https://upload.wikimedia.org/wikipedia/commons/8/80/World_map_-_low_resolution.svg" \n           alt="World Map Vector" \n           class="w-full h-auto object-contain opacity-80 filter grayscale contrast-125 block">'

new_map_str = """<!-- Map Container Locked to Image Bounds -->
    <div class="relative w-full max-w-7xl mx-auto h-[300px] sm:h-[400px] md:h-[480px]">
      <img src="https://upload.wikimedia.org/wikipedia/commons/8/80/World_map_-_low_resolution.svg" 
           alt="World Map Vector" 
           class="w-full h-full object-fill opacity-80 filter grayscale contrast-125 block">"""

content = content.replace(old_map_pattern, new_map_str)

# I should also slightly adjust the coordinates back to what they were before my "precise" tweaks 
# because if we use object-fill and standard stretch, the original coordinates worked best.
# Original coordinates they provided previously:
# UAE: top-[46%] left-[58%]
# Qatar: top-[45%] left-[56.5%]
# Oman: top-[49%] left-[60%]
# Sri Lanka: top-[58%] left-[68%]
# Malaysia: top-[62%] left-[75%]
# Singapore: top-[65%] left-[76%]

content = content.replace('top-[48%] left-[58.5%]', 'top-[46%] left-[58%]')
content = content.replace('top-[46.5%] left-[57%]', 'top-[45%] left-[56.5%]')
content = content.replace('top-[51.5%] left-[60%]', 'top-[49%] left-[60%]')
content = content.replace('top-[62%] left-[69.5%]', 'top-[58%] left-[68%]')
content = content.replace('top-[64%] left-[76.5%]', 'top-[62%] left-[75%]')
content = content.replace('top-[68%] left-[77.5%]', 'top-[65%] left-[76%]')

with open(file_path, "w") as f:
    f.write(content)

print("Map updated successfully.")
