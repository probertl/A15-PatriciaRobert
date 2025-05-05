# Projecte Flask RSS - UF3 M04

Hola, em dic Patricia Robert de 1r DAW :), aquest és el meu README.

## Instruccions per desplegar l’aplicació

### 1. Crear un entorn virtual

Per començar, hem de crear un entorn virtual amb Python per treballar de manera aïllada. Això ens ajuda a evitar conflictes amb altres projectes i tenir totes les dependències en un sol lloc.

Primer instal·lem els paquets que necessitem (si encara no els tenim):

```bash
sudo pip install flask feedparser
```

Després, per si de cas falta algun paquet o hi ha alguna actualització, creem i activem un entorn virtual amb:

```
python3 -m venv venv
source venv/bin/activate
```

Els dos paquets que necessitem són `flask` i `feedparser`.

* El paquet de Flask s'encarrega de crear el servidor web i gestionar les rutes.
* Feedparser el que farà és llegir i interpretar els fitxers RSS, que són arxius XML amb notícies.

### 2. Estructura de carpetes i fitxers

Seguit, creem l'estructura de carpetes i fitxers com aquesta:
projecte_flask_rss/
├── app.py
├── templates/
│   ├── index.html
│   ├── lavanguardia.html
├── static/
│   └── css/
│       └── estil.css
├── xml/
│   └── politica.xml
│   └── economia.xml
│   └── cultura.xml
│   └── internacional.xml
├── venv/
└── README.md

Cada fitxer te una funcio:

* **app.py**: Conté el codi principal de Flask. Gestiona les rutes i tria entre mode local o remot.
* **templates/***.html: Són les pàgines que veu l’usuari. Fan servir Jinja2 per mostrar dades dinàmiques.
* **static/css/estil.css**: Full d’estils amb una aparença fosca i tons lila neó.
* **xml/politica.xml**: RSS guardat localment, útil si no tens connexió.
* **venv/**: L’entorn virtual (millor afegir-lo a .gitignore perquè no cal pujar-lo a Git).

### 3. Executar l’aplicació

Per fer aixo hem d'estar ins l’entorn virtual (source venv/bin/activate) i llançem l'aplicació amb:
```
flask run 
```

Si tot ha sortit correctament ens proporcionara un link intern per al navegador
```
http://127.0.0.1:5000/
```

### 4. Com fer servir el mode remot o locals
**Mode remot**
Per defecte, l’aplicació llegeix l’RSS directament des de La Vanguardia, amb aquesta línia a app.py
```
feed = feedparser.parse("https://www.lavanguardia.com/rss/politica.xml")
```
Aquest mode necessita connexió a internet, que es el que fem servir.

**Mode local**
Per fer-ho descarregem l'arxiu xml i el guardem a la carpeta 
```
feed = feedparser.parse("xml/politica.xml")
```

### 5. Documentacio
[Que es un entorn virtual a Python](https://docs.python.org/es/3.9/library/venv.html#:~:text=Un%20entorno%20virtual%20es%20un,parte%20de%20tu%20sistema%20operativo.)

[Doc Flask](https://flask.palletsprojects.com/en/stable/)
