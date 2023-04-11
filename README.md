# py-pet-feeder-service
Proyecto para la construcción de un alimentador de perros automático. Esta consta de una API escrita en Python y construida con el framework FLASK que permite realizar la accion de dispensar alimento.

El proyecto actualmente posee una funcionalidad basica para controlar remotamente la alimentacion de las mascotas. Permite abrir remotamente la compuerta de alimentacion y cerrar automaticamente luego de unos segundos.

## Requerimientos
- Python
- Flask
- Gunicorn

## Endpoints
- <code>GET http://localhost/status</code>
- <code>GET http://localhost/abrir</code>
- <code>GET http://localhost/cerrar</code>

## Instalación
- Clonar el repositorio
- Instalar las dependencias
- Ejecutar el servidor