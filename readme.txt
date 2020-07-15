Bienvenue dans le README du projet 5 du parcours Python

Le dossier du projet est organisé de cette manière :
- serveur.py > Le fichier permettant de lancer le serveur avec Flask
- requestsAPI.py > Un fichier que vous pouvez utiliser pour requêter l'API
- templates :
    - index.html > Le fichier HTML du projet. Il est dans le dossier template (la vue du modèle MCV) comme Flask le demande
static :
    - style.css > Le fichier CSS du projet. Il est dans le dossier static comme Flask le demande
        
Pour lancer le projet vous devez installer : 
- Python (la version 3)
- Flask > pip install flask 

(voir https://openclassrooms.com/fr/courses/4425066-concevez-un-site-avec-flask/4525776-installez-flask)
    
Pour lancer le serveur vous devez exécuter le fichier serveur.py, 
et ensuite vous rendre dans votre navigateur web à l'url indiquée par la ligne de commande, en général http://127.0.0.1:5000/

Chaque modification que vous effectuerez dans le fichier html ou css sera visible après avoir rechargé la page. Vous devez évidemment vous assurer que le serveur tourne toujours, et le relancer si nécessaire.

Pour afficher des variables Python dans la page HTML, vous devez les passer en paramètre
de render_template de cette façon :
render_template("index.html", texte = messageBienvenue, message = objectif)

messageBienvenue et objectif sont des variables qui se trouvent dans le fichier serveur.py. On doit créer au sein de la fonction render_template des variables locales, ici texte et message, et leur assigner des valeurs de variables, ici les variables messageBienvenue et objectif. Ce sont les variables créées localement dans la fonction render_template  qui seront ensuite utilisées pour être affichées dans le fichier index.html en utilisant une syntaxe avec des doubles accolades ouvrantes et fermantes
: {{ variable_a_afficher }}

La valeur se trouvant dans les doubles accolades sera convertie en html par Flask. On peut évidemment modifier son style en pointant la balise dans laquelle elle se trouve.

Ici il y a 2 variables, mais vous pouvez mettre autant de variables que vous voulez dans les paramètres de render_template, et les utiliser dans le template (ici index.html). Vous pouvez évidemment les nommer comme vous le voulez, tant qu'ils respectent la convention de nommage de Python.

Attention :
- Ne modifier pas l'emplacement des fichiers html, css et serveur.py
- Dans le fichier serveur.py, ne pas modifier le code des lignes 1 à 5, 17 et 18, 21 et 22.