# Repositorio con tutorial sobre la librería PyGithub

---

*Autor*: Aitor León

*Fecha de creación*: 08/06/2017

*Contacto*:

- Twitter: [@2Ait8r](https://twitter.com/2Ait8r)
- E-mail: ldaitor28@gmail.com
- Blog: [Open Binary](https://openbinary20.wordpress.com)

---

# Índice
1. [¿Qué es PyGithub?](https://github.com/aitor28ld/tutorial-pygithub/blob/master/README.md#qu%C3%A9-es-pygithub)
2. [Descarga e instalación de la librería](https://github.com/aitor28ld/tutorial-pygithub/blob/master/README.md#descarga-e-instalaci%C3%B3n-de-la-liber%C3%ADa)
3. [Atributos GET](https://github.com/aitor28ld/tutorial-pygithub/blob/master/README.md#atributos-get)
	1. [Atributo api_status](https://github.com/aitor28ld/tutorial-pygithub/blob/master/README.md#atributo-api_status)
	2. [Atributo emojis](https://github.com/aitor28ld/tutorial-pygithub/blob/master/README.md#atributo-emojis)

# ¿Qué es PyGithub?

PyGithub es una librería (de otras muchas) de python. Gracías a esta librería podemos administrar los recursos, que Github nos ofrece, a través de scripts de Python.

Desafortunadamente, PyGithub no dispone de mucha [documentación](http://pygithub.readthedocs.io/en/latest/introduction.html#very-short-tutorial) en su web, tan sólo una pequeña introducción que nos permite listar los repositorios que tenemos creados en nuestro perfil de Github.

De todas formas, su uso es intuitivo y fácil para aquel que haya trabajado minimamente con alguna librería anteriormente. Si tenemos el paquete Ipython instalado en nuestro sistema, podremos acceder a todos los métodos que nos ofrece PyGithub una vez nos hemos “logueado” con dicha librería.

# Descarga e instalación de la libería

Para poder realizar los ejemplos de este tutorial, primero debemos de instalarla. 

La librería **PyGithub** no se encuentra en los repositorios oficiales de Debian (qué es dónde realizaré los ejemplos), por lo que debemos de descargarnos el [repositorio](https://github.com/PyGithub/PyGithub) e instalarla siguiendo los siguientes comandos:

	unzip pygithub-master.zip
	cd pygithub-master
	su
	apt install python-setuptools
	python setup.py install

Cuándo termine de instalar, debemos importar la librería en cualquier fichero _.py_ en el que usemos PyGithub

	from github import Github

Con ello, ya podemos ejecutar cualquier aplicación.

# Atributos GET

## Atributo api_status

El atributo _api\_status_ contiene estos atributos:

- CHECK_AFTER_INIT_FLAG 
- last_modified
- raw_headers
- etag
- last_updated
- setCheckAfterInitFlag
- get\_\_repr\_\_
- raw_data
- status

El más importante y posiblemente, con más uso, es _[status](https://github.com/aitor28ld/tutorial-pygithub/blob/master/tutorial-api_status.py#L8)_ el cuál podemos usar para ver si la conexión ha sido buena.

También está _[last\_updated](https://github.com/aitor28ld/tutorial-pygithub/blob/master/tutorial-api_status.py#L11)_ y _[last\_modified](https://github.com/aitor28ld/tutorial-pygithub/blob/master/tutorial-api_status.py#L14)_ las cuales nos pueden servir para ver si se ha efectuado correctamente nuestros *push*

**NOTA**: El atributo _api\_status\_messages__ contiene los mismos métodos que se usan con las listas en Python y su función en la misma.

## Atributo emojis

Este atributo contiene todos los emoticonos que Github permite insertar en cualquier cuadro de texto.

Su contenido se guarda en un diccionario y posee los  métodos correspondientes a un [diccionario en Python](http://librosweb.es/libro/algoritmos_python/capitulo_9/utilizando_diccionarios_en_python.html).

Podemos ver algunos ejemplos en el siguiente [fichero](https://github.com/aitor28ld/tutorial-pygithub/blob/master/tutorial-emojis.py)
