import re

# Read index.html
with open('/home/jk-niazi/Documents/Iinternship_work/vaks/index.html', 'r') as f:
    index_content = f.read()

# Extract global-network section
map_section_match = re.search(r'(<section id="global-network".*?</section>)', index_content, flags=re.DOTALL)
if map_section_match:
    map_section = map_section_match.group(1)
    
    # Read markets.html
    with open('/home/jk-niazi/Documents/Iinternship_work/vaks/markets.html', 'r') as f:
        markets_content = f.read()
    
    # Insert before closing </main> tag
    # In markets.html, the cards grid ends right before </div>\n    </main>
    # Wait, let's look at markets.html structure:
    # 291:             </div>
    # 292:         </div>
    # 293:     </main>
    # We should place it either inside main (after the grid) or after main.
    # The map section in index.html is its own <section> that spans full width. So it's best to place it outside <main> and before <footer>.
    # Let's insert it right after </main>
    
    markets_content = markets_content.replace('</main>', f'</main>\n\n    <!-- GLOBAL REACH WORLD MAP SECTION -->\n    {map_section}')
    
    with open('/home/jk-niazi/Documents/Iinternship_work/vaks/markets.html', 'w') as f:
        f.write(markets_content)
    
    print("Successfully copied map to markets.html")
else:
    print("Could not find global-network in index.html")
