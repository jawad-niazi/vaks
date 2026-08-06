import re

file_path = "/home/jk-niazi/Documents/Iinternship_work/vaks/index.html"
with open(file_path, "r") as f:
    content = f.read()

# 1. Update DIRECT FROM OUR FARMS section
farm_section_pattern = r'<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">.*?</div>\n        </div>\n    </section>'
new_farm_section = """<div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-7xl mx-auto">
                <!-- Farm Fields -->
                <div class="bg-white rounded-2xl shadow-md overflow-hidden group hover:shadow-lg transition-all relative">
                    <span class="absolute top-3 left-3 bg-[#0D3B22] text-white text-xs font-semibold px-3 py-1 rounded-full z-10">Farm Direct</span>
                    <img src="realImages/feild1.jpeg" alt="Onion Crop Fields" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-300">
                    <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 to-transparent p-4 pt-12">
                        <h3 class="text-white font-bold text-lg">Onion Crop Fields</h3>
                    </div>
                </div>
                <div class="bg-white rounded-2xl shadow-md overflow-hidden group hover:shadow-lg transition-all relative">
                    <span class="absolute top-3 left-3 bg-[#0D3B22] text-white text-xs font-semibold px-3 py-1 rounded-full z-10">Farm Direct</span>
                    <img src="realImages/feild2.jpeg" alt="Field Irrigation & Sourcing" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-300">
                    <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 to-transparent p-4 pt-12">
                        <h3 class="text-white font-bold text-lg">Field Irrigation & Sourcing</h3>
                    </div>
                </div>
                <div class="bg-white rounded-2xl shadow-md overflow-hidden group hover:shadow-lg transition-all relative">
                    <span class="absolute top-3 left-3 bg-[#0D3B22] text-white text-xs font-semibold px-3 py-1 rounded-full z-10">Farm Direct</span>
                    <img src="realImages/feild4.jpeg" alt="Direct Agriculture Operations" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-300">
                    <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 to-transparent p-4 pt-12">
                        <h3 class="text-white font-bold text-lg">Direct Agriculture Operations</h3>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
content = re.sub(farm_section_pattern, new_farm_section, content, flags=re.DOTALL)


# 2. Update Map Markers
def make_pin(top, left, flag, title):
    return f"""<!-- {title} -->
                <div class="absolute z-10" style="{top} {left}">
                    <div class="relative -left-1/2 -top-full flex flex-col items-center hover:-translate-y-1 transition-transform cursor-pointer" title="{title}">
                        <div class="w-10 h-6 bg-white rounded shadow-md border border-gray-200 overflow-hidden flex items-center justify-center">
                            <span class="text-sm leading-none">{flag}</span>
                        </div>
                        <div class="w-0.5 h-8 bg-[#0D3B22]"></div>
                        <div class="w-3 h-3 bg-[#0D3B22] rounded-full border border-vaks-lime -mt-1"></div>
                    </div>
                </div>"""

map_container_pattern = r'<!-- FLAG MARKERS -->.*?</div>\n            </div>\n        </div>\n    </section>'

new_markers = f"""<!-- FLAG MARKERS -->
                {make_pin('top: 46%;', 'left: 58%;', '🇦🇪', 'Dubai / UAE')}
                {make_pin('top: 45%;', 'left: 56.5%;', '🇶🇦', 'Qatar')}
                {make_pin('top: 49%;', 'left: 60%;', '🇴🇲', 'Muscat / Oman')}
                {make_pin('top: 58%;', 'left: 68%;', '🇱🇰', 'Sri Lanka')}
                {make_pin('top: 62%;', 'left: 75%;', '🇲🇾', 'Malaysia')}
                {make_pin('top: 65%;', 'left: 76%;', '🇸🇬', 'Singapore')}
            </div>
        </div>
    </section>"""

content = re.sub(map_container_pattern, new_markers, content, flags=re.DOTALL)

with open(file_path, "w") as f:
    f.write(content)

print("Updates applied successfully.")
