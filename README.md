# Instagram Clone API

Este es un proyecto realizado en Django REST Framework. Como su nombre lo dice, es una API de un clon de instagram.
Las funcionalidades que tiene son:

###### Users:
- Signup
- Login
- Verify Account
- Update user
- Update profile
- Detail user

###### Posts:
- Create post
- Detail post
- List posts
- Delete post


#### Como puedo probar el proyecto?
Facil, solo debes descargarte el codigo y tenes instalado docker y docker-compose.
Una vez que tenes listo todo, solo debes correr los siguientes comandos:
`docker-compose -f local.yml build`
`docker-compose -f local.yml up`
Luego debes crear un super usuario para poder acceder al admin de django:
`docker-compose -f local.yml run --rm django python manage.py createsuperuser`
Y listo! En el repositorio esta el archivo de postman con todos los request listo!
