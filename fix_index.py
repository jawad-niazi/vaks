import re

file_path = "/home/jk-niazi/Documents/Iinternship_work/vaks/index.html"
with open(file_path, "r") as f:
    content = f.read()

# 1. Add overflow-x-hidden to <body>
body_pattern = r'<body class="bg-\[\#F9FAF7\] text-vaks-charcoal font-sans antialiased selection:bg-vaks-lime selection:text-vaks-dark">'
body_new = '<body class="bg-[#F9FAF7] text-vaks-charcoal font-sans antialiased selection:bg-vaks-lime selection:text-vaks-dark overflow-x-hidden">'
content = content.replace(body_pattern, body_new)

# 2. Update Map Section Wrapper & Pins
# Currently it looks like:
# <section id="global-network" class="py-10 px-4 bg-[#F4F6F0] w-full">
#         <div class="w-full max-w-7xl mx-auto px-2 sm:px-6">
# ...
#             <div class="relative w-full h-[260px] sm:h-[340px] flex items-center justify-center overflow-hidden">
#                 <img src="..."
#                     alt="World Map Vector" class="w-full h-full object-fill opacity-75 filter grayscale contrast-125">
#
#                 <!-- FLAG MARKERS -->

# We need to replace it with the precise block requested by the user:

old_section_pattern = r'<section id="global-network" class="py-10 px-4 bg-\[\#F4F6F0\] w-full">.*?</section>'
new_section = """<section id="global-network" class="py-12 px-4 bg-[#F4F6F0] w-full overflow-hidden">
  <div class="max-w-6xl mx-auto text-center">
    <!-- Header -->
    <div class="mb-6">
      <h2 class="text-2xl sm:text-3xl font-black text-[#0D3B22] tracking-tight mb-2">
        OUR <span class="text-vaks-lime">GLOBAL EXPORT</span> NETWORK
      </h2>
      <p class="text-gray-600 max-w-lg mx-auto text-xs sm:text-sm font-medium">
        Supplying fresh produce across key destinations in Middle East, Asia, and beyond.
      </p>
    </div>

    <!-- Filter Badges -->
    <div class="flex flex-wrap justify-center items-center gap-2 max-w-4xl mx-auto mb-8">
      <span class="bg-[#0D3B22] text-white text-xs font-bold px-3 py-1.5 rounded-full">MIDDLE EAST</span>
      <span class="bg-[#0D3B22] text-white text-xs font-bold px-3 py-1.5 rounded-full">EUROPE</span>
      <span class="bg-[#0D3B22] text-white text-xs font-bold px-3 py-1.5 rounded-full">ASIA</span>
      <span class="bg-white text-gray-800 text-xs font-semibold px-3 py-1.5 rounded-full border border-gray-200 shadow-sm">📍 UAE</span>
      <span class="bg-white text-gray-800 text-xs font-semibold px-3 py-1.5 rounded-full border border-gray-200 shadow-sm">📍 Qatar</span>
      <span class="bg-white text-gray-800 text-xs font-semibold px-3 py-1.5 rounded-full border border-gray-200 shadow-sm">📍 Oman (Muscat)</span>
      <span class="bg-white text-gray-800 text-xs font-semibold px-3 py-1.5 rounded-full border border-gray-200 shadow-sm">📍 Malaysia</span>
      <span class="bg-white text-gray-800 text-xs font-semibold px-3 py-1.5 rounded-full border border-gray-200 shadow-sm">📍 Singapore</span>
    </div>

    <!-- Map Container Locked to Image Bounds -->
    <div class="relative inline-block w-full max-w-4xl mx-auto">
      <img src="https://upload.wikimedia.org/wikipedia/commons/8/80/World_map_-_low_resolution.svg" 
           alt="World Map Vector" 
           class="w-full h-auto object-contain opacity-80 filter grayscale contrast-125 block">

      <!-- UAE Pin -->
      <div class="absolute top-[48%] left-[58.5%] -translate-x-1/2 -translate-y-full flex flex-col items-center group cursor-pointer z-10" title="UAE">
        <div class="w-8 h-5 bg-white rounded shadow border border-gray-200 flex items-center justify-center text-xs">🇦🇪</div>
        <div class="w-0.5 h-6 bg-[#0D3B22]"></div>
        <div class="w-2.5 h-2.5 bg-[#0D3B22] rounded-full border border-white"></div>
      </div>

      <!-- Qatar Pin -->
      <div class="absolute top-[46.5%] left-[57%] -translate-x-1/2 -translate-y-full flex flex-col items-center group cursor-pointer z-10" title="Qatar">
        <div class="w-8 h-5 bg-white rounded shadow border border-gray-200 flex items-center justify-center text-xs">🇶🇦</div>
        <div class="w-0.5 h-6 bg-[#0D3B22]"></div>
        <div class="w-2.5 h-2.5 bg-[#0D3B22] rounded-full border border-white"></div>
      </div>

      <!-- Oman Pin -->
      <div class="absolute top-[51.5%] left-[60%] -translate-x-1/2 -translate-y-full flex flex-col items-center group cursor-pointer z-10" title="Oman">
        <div class="w-8 h-5 bg-white rounded shadow border border-gray-200 flex items-center justify-center text-xs">🇴🇲</div>
        <div class="w-0.5 h-6 bg-[#0D3B22]"></div>
        <div class="w-2.5 h-2.5 bg-[#0D3B22] rounded-full border border-white"></div>
      </div>

      <!-- Sri Lanka Pin -->
      <div class="absolute top-[62%] left-[69.5%] -translate-x-1/2 -translate-y-full flex flex-col items-center group cursor-pointer z-10" title="Sri Lanka">
        <div class="w-8 h-5 bg-white rounded shadow border border-gray-200 flex items-center justify-center text-xs">🇱🇰</div>
        <div class="w-0.5 h-6 bg-[#0D3B22]"></div>
        <div class="w-2.5 h-2.5 bg-[#0D3B22] rounded-full border border-white"></div>
      </div>

      <!-- Malaysia Pin -->
      <div class="absolute top-[64%] left-[76.5%] -translate-x-1/2 -translate-y-full flex flex-col items-center group cursor-pointer z-10" title="Malaysia">
        <div class="w-8 h-5 bg-white rounded shadow border border-gray-200 flex items-center justify-center text-xs">🇲🇾</div>
        <div class="w-0.5 h-6 bg-[#0D3B22]"></div>
        <div class="w-2.5 h-2.5 bg-[#0D3B22] rounded-full border border-white"></div>
      </div>

      <!-- Singapore Pin -->
      <div class="absolute top-[68%] left-[77.5%] -translate-x-1/2 -translate-y-full flex flex-col items-center group cursor-pointer z-10" title="Singapore">
        <div class="w-8 h-5 bg-white rounded shadow border border-gray-200 flex items-center justify-center text-xs">🇸🇬</div>
        <div class="w-0.5 h-6 bg-[#0D3B22]"></div>
        <div class="w-2.5 h-2.5 bg-[#0D3B22] rounded-full border border-white"></div>
      </div>
    </div>
  </div>
</section>"""
content = re.sub(old_section_pattern, new_section, content, flags=re.DOTALL)

with open(file_path, "w") as f:
    f.write(content)

print("index.html updated successfully.")
