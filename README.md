# Trabajo-Integrador-Final-Django-Polotic (WIP)

<h2>¿Que es esto?</h2> 

Esto es el trabajo integrador que me piden en el curso DESARROLLO WEB FULLSTACK CON PYTHON Y JAVASCRIPT (2021) de PoloTIC Misiones para darme el certificado.
Por favor, primero lee el [enunciado](https://github.com/agus-droid/Trabajo-Integrador-Final-Django/blob/main/Enunciado.pdf).<br>
En cuanto a cuestiones legales, le puse Creative Commons Zero v1.0 Universal por lo que cualquiera es libre de llevarse lo que quiera, modificarlo, venderlo, etc.

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

    git clone https://github.com/agus-droid/Trabajo-Integrador-Final-Django.git
    
Instalamos los requisitos del proyecto

    pip install -r .\Trabajo-Integrador-Final-Django\requirements.txt

Ahora nos movemos dentro de la carpeta que se acaba de crear:

    cd .\Trabajo-Integrador-Final-Django\

Por último tenemos que prender el servidor:

    python .\manage.py runserver
    
<h2>¿Donde veo el trabajo? ¿Me acabás de hackear? Con razón no te da bola ninguna mujer.</h2>

Para ver el trabajo nos dirigimos a http://127.0.0.1:8000/ desde un navegador.
