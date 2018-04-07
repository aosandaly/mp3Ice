#Parties finie (Travail réalisé):
- L'interface .ice 
- Communication entre le serveur `Python` et le client `Java`
- La fonction `addDocument()`
- La fonction `searchDocument()`
- La fonction `removeDocument()`
- Makefile pour simplifier l'excution et la compilation
- Menu intéractif en interface au moins pour que le client soit plus facile d'utilisation

#Parties restantes (Pistes d'amélioration) :
- La fonction `downloadDocument()` qui permettrait de télécharger la mlusique sur le client
- Rajouter des log sur le serveur pour avoir des traces
- Faire l'ajout d'un morceau réel en mp3 par exemple
- Jouer/Lecture d'un morceau

# Difficultés rencontrées
- ICE à installer sur un environnement Windows (pour pallier à ce problème une grande structuration s'impose)
- Les deux langages à faire communiquer ensemble avec le mapping pour les types de retour des fonctions
- La compilation JAVA en ligne de commande (Pour pallier à ce problème j'ai mis en place les makefile pour déployer plus rapidement permettant de lancer plus rapidement le client/serveur)

#Pour l'environnement Windows et/ou linux :
**Install**
  - Getgnuwin (makefile for windows) 
    - source  [link to GetGnuwin32](http://getgnuwin32.sourceforge.net)
  - Version de `java/JDK 9.0.1`
    - source  [link to java/JDK 9.0.1](http://www.oracle.com/technetwork/java/javase/downloads/jdk9-downloads-3848520.html)
  - Version de `Python 3.6.3`
    - Module :  _A installer avec pip install_ :   
            ```python
               pip install zeroc-ice  
            ```
            ```python
               pip install Ice 
            ```
    - source  [link to Python 3.6.3](https://www.python.org/downloads/)
  - Version de `ICE 3.7` 
    - source  [link to ICE 3.7](https://zeroc.com/downloads//ice)



**Ajout des différents variables d'environnements**
```
- C:\Users\franck\AppData\Local\Programs\Python\Python36-32
- C:\Users\franck\AppData\Local\Programs\Python\Python36-32\Scripts
- C:\Program Files\Java\jdk-9.0.1\bin
- C:\Program Files (x86)\GnuWin32\bin
```

### Lancer le serveur

#### Step 0
_Ouvrir la console et aller dans le répertoire **`./serveurMp3`**_
#### Step 1 - Compiler
```bash
make build
```
#### Step 2 - Lancer le serveur
```bash
make run
```
#### Step X - Compiler & lancer le serveur
```bash
make
```
#### Step XX - Supprimer les class généré par ICE et les .class compilé par Java
```bash
make clean
```

### Lancer un client

#### Step 0
_Ouvrir la console et aller dans le répertoire **`./clientMp3`**_
#### Step 1 - Compiler
```bash
make build
```
#### Step 2 - Lancer le serveur
```bash
make run
```
#### Step X - Compiler & lancer le client
```bash
make
```
#### Step XX - Supprimer les class généré par ICE et les .class compilé par Java
```bash
make clean
```


Readme 2

pip install python-vlc
pip install eyeD3 eyeD3[display-plugin]

pip install python_magic_bin-0.4.14-py2.py3-none-win32.whl

### web service
pip install flask