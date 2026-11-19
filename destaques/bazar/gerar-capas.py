# Capas de Destaque do Bazar: fundo creme, círculo central, ícone em linha dourada, centralizado em 1080x1920
BG="#F3EDE3"; GOLD="#A8854A"; INK="#2A241E"
icons={
"praia-camping":'''<circle cx="0" cy="-70" r="46"/><path d="M-70,-150 v-22 M70,-150 v-22 M-130,-70 h-24 M130,-70 h24 M-104,-150 l-16,-16 M104,-150 l16,-16"/>
<path d="M-150,40 q37,-30 75,0 t75,0 t75,0 t75,0"/><path d="M-150,100 q37,-30 75,0 t75,0 t75,0 t75,0"/>''',
"estrada":'''<path d="M-60,-170 L-140,140 M60,-170 L140,140"/><path d="M0,-150 v40 M0,-70 v50 M0,20 v60 M0,110 v30"/>''',
"pet":'''<ellipse cx="0" cy="55" rx="70" ry="60"/><ellipse cx="-95" cy="-30" rx="28" ry="36"/><ellipse cx="95" cy="-30" rx="28" ry="36"/><ellipse cx="-40" cy="-105" rx="26" ry="36"/><ellipse cx="40" cy="-105" rx="26" ry="36"/>''',
"presentes":'''<rect x="-120" y="-40" width="240" height="170"/><rect x="-140" y="-90" width="280" height="50"/><path d="M0,-90 v220"/><path d="M0,-90 c-30,-70 -110,-70 -90,-20 c10,20 60,20 90,20 c30,0 80,0 90,-20 c20,-50 -60,-50 -90,20"/>''',
}
for k,ic in icons.items():
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
<rect width="1080" height="1920" fill="{BG}"/>
<circle cx="540" cy="960" r="400" fill="none" stroke="{GOLD}" stroke-width="6"/>
<g transform="translate(540,960) scale(1.35)" fill="none" stroke="{GOLD}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round">{ic}</g>
</svg>'''
    open(f"{k}.svg","w").write(svg)
