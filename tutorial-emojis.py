#g = Github('<usuario>','<contraseña>')

p = g.get_emojis()

#Obtener emoji
print p.get('smile')

#Ver todos los items
print p.viewitems()

#Obtener clave de emojis
print p.keys()

#Comprobar si existe un emoji llamado sunny
print p.has_key('sunny')
