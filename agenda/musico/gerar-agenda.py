from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
F=os.path.expanduser('~/.fonts/')
W,H=1080,1920
NAVY1=(16,28,48); NAVY2=(31,55,83); GOLD=(200,145,79); CREAM=(240,232,218); MUTED=(160,170,186)
im=Image.new('RGB',(W,H),NAVY1)
# radial glow
g=Image.new('L',(W,H),0); gd=ImageDraw.Draw(g); gd.ellipse((-200,300,1280,1500),fill=255); g=g.filter(ImageFilter.GaussianBlur(260))
im=Image.composite(Image.new('RGB',(W,H),NAVY2),im,g)
d=ImageDraw.Draw(im)
f=lambda n,s: ImageFont.truetype(F+n+'.ttf',s)
def ctext(y,t,font,fill,sp=0):
    if sp:
        ws=[d.textlength(c,font=font) for c in t]; tw=sum(ws)+sp*(len(t)-1); x=(W-tw)/2
        for c,w in zip(t,ws): d.text((x,y),c,font=font,fill=fill); x+=w+sp
    else:
        tw=d.textlength(t,font=font); d.text(((W-tw)/2,y),t,font=font,fill=fill)
ctext(170,'ABNADABY BONAPARTE · AO VIVO',f('Montserrat-Medium',30),GOLD,sp=5)
ctext(240,'Agenda',f('CormorantGaramond-MediumItalic',190),CREAM)
ctext(470,'novembro — dezembro · 2026',f('CormorantGaramond-MediumItalic',48),GOLD)
d.line((470,560,610,560),fill=GOLD,width=2)
ev=[('19','QUI','NOV','APAE','Abnadaby Bonaparte & Léa Soares','Homenagem ao Dia da Consciência Negra','10h'),
    ('20','SEX','NOV','Kanoas','Abnadaby Bonaparte & Banda','','20h'),
    ('22','DOM','NOV','Encontro das Águas','Abnadaby Bonaparte','','12h'),
    ('28','SÁB','NOV',"Aldeia's",'Abnadaby Bonaparte','','12h'),
    ('05','SÁB','DEZ','Evento fechado','Abnadaby Bonaparte, Carlinhos Cruz & bateria','Trio','')]
y=640; X0=110; X1=300
for dia,sem,mes,local,quem,obs,hora in ev:
    d.text((X0,y-8),dia,font=f('CormorantGaramond-SemiBold',110),fill=GOLD,features=['lnum'])
    d.text((X0+4,y+112),f'{sem} · {mes}',font=f('Montserrat-Medium',24),fill=MUTED)
    d.text((X1,y+6),local,font=f('CormorantGaramond-SemiBold',64),fill=CREAM)
    d.text((X1,y+86),quem,font=f('Montserrat-Regular',27),fill=CREAM)
    if obs: d.text((X1,y+124),obs,font=f('CormorantGaramond-MediumItalic',34),fill=GOLD)
    if hora:
        hf=f('Montserrat-SemiBold',40); tw=d.textlength(hora,font=hf); d.text((W-110-tw,y+20),hora,font=hf,fill=GOLD)
    y+=210
    d.line((X0,y-30,W-110,y-30),fill=(60,80,108),width=1)
ctext(1720,'Contratações  (63) 99242-8800',f('Montserrat-Medium',30),CREAM)
ctext(1770,'@abnadabyoliveira',f('Montserrat-Regular',28),GOLD)
im.save('agenda-nov-dez-2026.jpg',quality=93)
