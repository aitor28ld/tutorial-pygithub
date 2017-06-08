from github import Github

g = Github('<usuario>','<contraseña>')

p = g.get_api_status()

#Status
print p.status

#Last_updated
print p.last_updated

#Last_modified
print p.last_modified
