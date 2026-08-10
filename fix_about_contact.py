import re

# 1. FIX ABOUT.HTML
file_path_about = "/home/jk-niazi/Documents/Iinternship_work/vaks/about.html"
with open(file_path_about, "r") as f:
    about_content = f.read()

# HTML & BODY
about_content = about_content.replace('<html lang="en" class="scroll-smooth">', '<html lang="en" class="scroll-smooth overflow-x-hidden w-full max-w-full">')
about_content = about_content.replace('<body class="bg-[#F9FAF7] text-vaks-charcoal font-sans antialiased selection:bg-vaks-lime selection:text-vaks-dark">', '<body class="bg-[#F9FAF7] text-vaks-charcoal font-sans antialiased selection:bg-vaks-lime selection:text-vaks-dark overflow-x-hidden w-full max-w-full">')

# Main tag
about_content = about_content.replace('<main class="py-16 md:py-24 bg-white">', '<main class="py-16 md:py-24 bg-white overflow-x-hidden w-full max-w-full">')

# Header and Footer tags (if they don't have it)
def add_overflow(match):
    tag = match.group(0)
    if 'overflow-x-hidden' not in tag and 'overflow-hidden' not in tag:
        if 'class="' in tag:
            return tag.replace('class="', 'class="overflow-x-hidden max-w-full w-full ')
        else:
            return tag.replace('>', ' class="overflow-x-hidden max-w-full w-full">')
    return tag

about_content = re.sub(r'<(section|header|footer)\b[^>]*>', add_overflow, about_content)

# Specific Fixes for about.html
# Hero/Overview Grid: Ensure grid layouts use grid-cols-1 lg:grid-cols-2
# Find all <div class="grid lg:grid-cols-12...> and convert to grid-cols-1 lg:grid-cols-2
about_content = about_content.replace('<div class="grid lg:grid-cols-12 gap-12 items-center">', '<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center w-full px-4 sm:px-0">')
about_content = about_content.replace('<div class="lg:col-span-5"', '<div')
about_content = about_content.replace('<div class="lg:col-span-6"', '<div')
about_content = about_content.replace('<div class="lg:col-span-7"', '<div')

with open(file_path_about, "w") as f:
    f.write(about_content)


# 2. FIX CONTACT.HTML
file_path_contact = "/home/jk-niazi/Documents/Iinternship_work/vaks/contact.html"
with open(file_path_contact, "r") as f:
    contact_content = f.read()

# HTML & BODY
contact_content = contact_content.replace('<html lang="en" class="scroll-smooth">', '<html lang="en" class="scroll-smooth overflow-x-hidden w-full max-w-full">')
contact_content = contact_content.replace('<body class="bg-[#F9FAF7] text-vaks-charcoal font-sans antialiased selection:bg-vaks-lime selection:text-vaks-dark">', '<body class="bg-[#F9FAF7] text-vaks-charcoal font-sans antialiased selection:bg-vaks-lime selection:text-vaks-dark overflow-x-hidden w-full max-w-full">')

# Main tag
contact_content = contact_content.replace('<main class="py-16 md:py-24 bg-white relative z-10">', '<main class="py-16 md:py-24 bg-white relative z-10 overflow-x-hidden w-full max-w-full">')

contact_content = re.sub(r'<(section|header|footer)\b[^>]*>', add_overflow, contact_content)

# Form & Address Cards Grid: grid-cols-1 lg:grid-cols-2
contact_content = contact_content.replace('<div class="grid lg:grid-cols-3 gap-12">', '<div class="grid grid-cols-1 lg:grid-cols-3 gap-12 w-full">')
contact_content = contact_content.replace('<div class="grid md:grid-cols-2 gap-8">', '<div class="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-full">')
contact_content = contact_content.replace('<div class="lg:col-span-2">', '<div>')

# Form Inputs & Textareas -> box-border w-full max-w-full
def fix_inputs(match):
    tag = match.group(0)
    if 'w-full' in tag:
        tag = tag.replace('w-full', 'w-full max-w-full box-border')
    else:
        if 'class="' in tag:
            tag = tag.replace('class="', 'class="w-full max-w-full box-border ')
        else:
            tag = tag.replace('>', ' class="w-full max-w-full box-border">')
    return tag

contact_content = re.sub(r'<(input|textarea|select)\b[^>]*>', fix_inputs, contact_content)

# Embedded Maps/Iframes: wrap in w-full overflow-hidden rounded-2xl
# Find iframe and add classes if needed
contact_content = contact_content.replace('<iframe', '<iframe class="w-full max-w-full box-border"')

with open(file_path_contact, "w") as f:
    f.write(contact_content)

print("Updated about.html and contact.html")
