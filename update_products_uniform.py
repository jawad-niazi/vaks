import re

file_path = "/home/jk-niazi/Documents/Iinternship_work/vaks/products.html"
with open(file_path, "r") as f:
    content = f.read()

# Pattern for Potato Card image block
potato_pattern = r'<div class="relative h-56 w-full flex overflow-hidden bg-gray-100">.*?</div>\n                    </div>'
potato_new = """<div class="relative h-60 overflow-hidden bg-gray-100 rounded-t-3xl">
                        <img src="realImages/potato1.jpeg" alt="Export Quality Potatoes"
                            class="h-60 object-cover w-full group-hover:scale-105 transition-transform">
                        <div class="absolute top-3 right-3 bg-white/90 backdrop-blur-md text-[#0D3B22] text-[10px] font-bold px-2.5 py-1 rounded-full shadow-sm uppercase tracking-wider">
                            PAKISTAN ORIGIN
                        </div>
                    </div>"""
content = re.sub(potato_pattern, potato_new, content, flags=re.DOTALL)

# Pattern for Onion Card image block
onion_pattern = r'<div class="relative h-56 w-full flex overflow-hidden bg-gray-100">.*?</div>\n                    </div>'
onion_new = """<div class="relative h-60 overflow-hidden bg-gray-100 rounded-t-3xl">
                        <img src="realImages/onion1.jpeg" alt="Export Quality Onions"
                            class="h-60 object-cover w-full group-hover:scale-105 transition-transform">
                        <div class="absolute top-3 right-3 bg-white/90 backdrop-blur-md text-[#0D3B22] text-[10px] font-bold px-2.5 py-1 rounded-full shadow-sm uppercase tracking-wider">
                            PAKISTAN ORIGIN
                        </div>
                    </div>"""
# Note: since onion and potato had the EXACT same pattern, the first sub replaced potato, the second will replace onion
content = re.sub(onion_pattern, onion_new, content, flags=re.DOTALL)

# Pattern for Mangoes Card image block
mango_pattern = r'<div class="relative h-56 overflow-hidden bg-gray-100">\s*<img src="mangoes.jpeg" alt="Export Quality Mangoes"\s*class="h-56 object-cover w-full group-hover:scale-105 transition-transform">\s*<div\s*class="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-\[10px\] font-black tracking-wider text-vaks-dark">\s*SEASONAL EXPORT</div>\s*</div>'
mango_new = """<div class="relative h-60 overflow-hidden bg-gray-100 rounded-t-3xl">
                        <img src="mangoes.jpeg" alt="Export Quality Mangoes"
                            class="h-60 object-cover w-full group-hover:scale-105 transition-transform">
                        <div class="absolute top-3 right-3 bg-white/90 backdrop-blur-md text-[#0D3B22] text-[10px] font-bold px-2.5 py-1 rounded-full shadow-sm uppercase tracking-wider">
                            SEASONAL EXPORT
                        </div>
                    </div>"""
content = re.sub(mango_pattern, mango_new, content)

# Pattern for Kinnow Card image block
kinnow_pattern = r'<div class="relative h-56 overflow-hidden bg-gray-100">\s*<img src="oranges.jpg" alt="Export Quality Kinnow"\s*class="h-56 object-cover w-full group-hover:scale-105 transition-transform">\s*<div\s*class="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-\[10px\] font-black tracking-wider text-vaks-dark">\s*SEASONAL EXPORT</div>\s*</div>'
kinnow_new = """<div class="relative h-60 overflow-hidden bg-gray-100 rounded-t-3xl">
                        <img src="oranges.jpg" alt="Export Quality Kinnow"
                            class="h-60 object-cover w-full group-hover:scale-105 transition-transform">
                        <div class="absolute top-3 right-3 bg-white/90 backdrop-blur-md text-[#0D3B22] text-[10px] font-bold px-2.5 py-1 rounded-full shadow-sm uppercase tracking-wider">
                            SEASONAL EXPORT
                        </div>
                    </div>"""
content = re.sub(kinnow_pattern, kinnow_new, content)

with open(file_path, "w") as f:
    f.write(content)

print("Updated uniform products.")
