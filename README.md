# Trabajo-Integrador-Final-Django-Polotic (WIP)

<h2>¿Que es esto?</h2> 

Esto es el trabajo integrador que me piden en el curso DESARROLLO WEB FULLSTACK CON PYTHON Y JAVASCRIPT (2021) de PoloTIC Misiones para darme el certificado.
Por favor, primero lee el [enunciado](https://github.com/agus-droid/Trabajo-Integrador-Final-Django/blob/main/Enunciado.pdf).<br>

<h2>¿Como hago para que funcione?</h2>

El deploy lo hice [acá](https://agusssosa.pythonanywhere.com) pero dejo instrucciones para descargarlo y correrlo por ustedes mismos.

<h3>Windows</h3>

Descargamos e instalamos la última versión de python desde [acá](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe) (click en la palabra "acá" por favor, pero en la otra, no en esta).<br>
No olvidar de marcar la opción de agregar al PATH.

Empezamos a tirar comandos en PowerShell.<br>

Creamos un entorno virtual

    python -m venv env
    
Activamos el entorno

    .\env\Scripts\Activate.ps1    

Vamos a clonar el repositorio:

    git clone https://github.com/agus-droid/Trabajo-Integrador-Final-Django-Polotic.git
    
Instalamos los requisitos del proyecto

    pip install -r .\Trabajo-Integrador-Final-Django-Polotic\requirements.txt

Ahora nos movemos dentro de la carpeta que se acaba de crear:

    cd .\Trabajo-Integrador-Final-Django-Polotic\
    
Aplicamos las migraciones:
    
    python .\manage.py migrate

Por último tenemos que prender el servidor:

    python .\manage.py runserver
    
<h2>¿Donde veo el trabajo?</h2>

Para ver el trabajo nos dirigimos a http://127.0.0.1:8000/ desde un navegador.
