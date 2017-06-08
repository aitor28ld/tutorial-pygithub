from github import Github

g = Github('<usuario>','<contraseña>')

#Saber si estamos bien logueados
p = g.get_user()
print p

#Listar repositorios existentes en nuestro perfil
for x in p.get_repos():
	print x.name 

#Obtener email del usuario
print p.email

#Crear repositorio
p.create_repo('<nombre del repositorio>')

#Eliminar repositorio
p.get_repo('<nombre-del-repositorio>').delete
