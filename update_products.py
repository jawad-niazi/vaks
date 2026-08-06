import re

file_path = "/home/jk-niazi/Documents/Iinternship_work/vaks/products.html"
with open(file_path, "r") as f:
    content = f.read()

# Potato Card pattern
potato_old = """<div class="relative h-56 overflow-hidden bg-gray-100">
                        <img src="Potatoes.jpg" alt="Export Quality Potatoes"
                            class="h-56 object-cover w-full group-hover:scale-105 transition-transform">
                        <div
                            class="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-[10px] font-black tracking-wider text-vaks-dark">
                            PAKISTAN ORIGIN</div>
                    </div>"""

potato_new = """<div class="relative h-56 w-full flex overflow-hidden bg-gray-100">
                        <!-- Primary Showcase -->
                        <img src="realImages/potato1.jpeg" alt="Freshly Harvested Potatoes" title="Freshly Harvested Potatoes" class="w-2/3 h-full object-cover group-hover:scale-105 transition-transform origin-left">
                        <!-- Stacked Side Photos -->
                        <div class="w-1/3 h-full flex flex-col border-l-2 border-white">
                            <img src="realImages/potato2.jpeg" alt="Field Crop Yield" title="Field Crop Yield" class="w-full h-1/2 object-cover border-b-2 border-white group-hover:scale-105 transition-transform origin-top-right">
                            <img src="realImages/potato3.jpeg" alt="Clean Soil Sourced Potatoes" title="Clean Soil Sourced Potatoes" class="w-full h-1/2 object-cover group-hover:scale-105 transition-transform origin-bottom-right">
                        </div>
                        <div class="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-[10px] font-black tracking-wider text-vaks-dark shadow-sm">
                            PAKISTAN ORIGIN
                        </div>
                    </div>"""

# Onion Card pattern
onion_old = """<div class="relative h-56 overflow-hidden bg-gray-100">
                        <img src="onion.jpg" alt="Export Quality Onions"
                            class="h-56 object-cover w-full group-hover:scale-105 transition-transform">
                        <div
                            class="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-[10px] font-black tracking-wider text-vaks-dark">
                            PAKISTAN ORIGIN</div>
                    </div>"""

onion_new = """<div class="relative h-56 w-full flex overflow-hidden bg-gray-100">
                        <!-- Primary Showcase -->
                        <img src="realImages/onion1.jpeg" alt="Fresh Red Onion Harvest" title="Fresh Red Onion Harvest" class="w-2/3 h-full object-cover group-hover:scale-105 transition-transform origin-left">
                        <!-- Stacked Side Photos -->
                        <div class="w-1/3 h-full flex flex-col border-l-2 border-white">
                            <img src="realImages/onion 5.jpeg" alt="Export Grade Quality" title="Export Grade Quality" class="w-full h-1/2 object-cover border-b-2 border-white group-hover:scale-105 transition-transform origin-top-right">
                            <img src="realImages/onino3.jpeg" alt="Soil & Crop Health Check" title="Soil & Crop Health Check" class="w-full h-1/2 object-cover group-hover:scale-105 transition-transform origin-bottom-right">
                        </div>
                        <div class="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-[10px] font-black tracking-wider text-vaks-dark shadow-sm">
                            PAKISTAN ORIGIN
                        </div>
                    </div>"""

content = content.replace(potato_old, potato_new)
content = content.replace(onion_old, onion_new)

with open(file_path, "w") as f:
    f.write(content)

print("Updated products.html")
