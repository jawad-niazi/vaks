import re

file_path = "/home/jk-niazi/Documents/Iinternship_work/vaks/index.html"
with open(file_path, "r") as f:
    content = f.read()

# 1. GLOBAL OVERFLOW PREVENT
content = content.replace('<html lang="en" class="scroll-smooth">', '<html lang="en" class="scroll-smooth overflow-x-hidden w-full max-w-full">')
content = content.replace('<body class="bg-[#F9FAF7] text-vaks-charcoal font-sans antialiased selection:bg-vaks-lime selection:text-vaks-dark overflow-x-hidden">', '<body class="bg-[#F9FAF7] text-vaks-charcoal font-sans antialiased selection:bg-vaks-lime selection:text-vaks-dark overflow-x-hidden w-full max-w-full">')

# Add overflow-x-hidden to every <section ...> that doesn't have it
def add_overflow_to_section(match):
    section_tag = match.group(0)
    if 'overflow-hidden' not in section_tag and 'overflow-x-hidden' not in section_tag:
        # Add to existing class or create class
        if 'class="' in section_tag:
            return section_tag.replace('class="', 'class="overflow-x-hidden max-w-full ')
        else:
            return section_tag.replace('<section', '<section class="overflow-x-hidden max-w-full"')
    return section_tag

content = re.sub(r'<section\b[^>]*>', add_overflow_to_section, content)

# 2. HERO SECTION MOBILE RESPONSIVENESS
# Text wrapper
content = re.sub(
    r'<div class="relative z-10 max-w-4xl mx-auto text-center mt-8 md:mt-16 px-4">',
    r'<div class="relative z-10 w-full max-w-full px-4 text-left sm:text-center mt-8 md:mt-16 mx-auto">',
    content
)

# Background image wrappers
# Let's add max-w-full overflow-hidden to the absolute div containing hero images
content = content.replace('<div class="absolute right-0 top-1/2 -translate-y-1/2 w-1/3 hidden lg:block opacity-60">', '<div class="absolute right-0 top-1/2 -translate-y-1/2 w-1/3 hidden lg:block opacity-60 max-w-full overflow-hidden">')

# Green feature bar
# Currently: <div class="bg-vaks-dark rounded-full py-4 px-8 mt-12 flex items-center justify-between shadow-2xl border border-emerald-900/50 backdrop-blur-sm">
content = content.replace(
    '<div class="bg-vaks-dark rounded-2xl md:rounded-full py-4 px-4 md:px-8 mt-12 flex flex-col md:flex-row items-center justify-between gap-4 md:gap-0 shadow-2xl border border-emerald-900/50">',
    '<div class="bg-vaks-dark rounded-2xl sm:rounded-full py-4 px-4 sm:px-8 mt-12 flex flex-col sm:flex-row items-center justify-between gap-4 w-full shadow-2xl border border-emerald-900/50">'
)

# 3. DIRECT FROM OUR FARMS & ABOUT US SECTIONS
# Farm cards: w-full h-auto
# Let's replace 'w-full h-64 object-cover' with 'w-full h-auto sm:h-64 object-cover'
content = content.replace('w-full h-64 object-cover', 'w-full h-auto sm:h-64 object-cover aspect-video sm:aspect-auto')

# Your Trusted Partner grid
# Currently: <div class="grid lg:grid-cols-12 gap-12 items-center">
content = content.replace(
    '<div class="grid lg:grid-cols-12 gap-12 items-center">',
    '<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center">'
)

# Wait, if it was grid-cols-12, the children might have col-span-5 and col-span-7. Let's fix those to not break on grid-cols-2.
# Let's just remove col-span-5 and col-span-7 from the children in that section.
content = content.replace('<div class="lg:col-span-5" data-aos="fade-right">', '<div data-aos="fade-right">')
content = content.replace('<div class="lg:col-span-6" data-aos="fade-left">', '<div data-aos="fade-left">')
content = content.replace('<div class="lg:col-span-7" data-aos="fade-left">', '<div data-aos="fade-left">')


with open(file_path, "w") as f:
    f.write(content)

print("Updated index.html for mobile responsiveness.")
