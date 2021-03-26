# OCMovies-API: Test API providing movie information

The OCMovies-API project is a REST API application to be executed locally in the context
of educational projects. It provides movie information from GET http endpoints.
The API provides these endpoints to get detailed infomation about movies filtered by
various criteria such as genre, IMDB score or year. Endpoints allow users to retrieve
information for individual movies or lists of movies.

## Installation

This locally-executable API can be installed and executed from [http://localhost:8000/api/v1/titles/](http://localhost:8000/api/v1/titles/) using the following steps.

### Option 1: Installation and execution with pipenv

For this method, it is necessary to have pipenv already installed on your python installation. If pipenv is not already installed on your computer, refer to [this page](docs/pipenv/installation-en.md).

1. Clone this repository using `$ git clone https://github.com/OpenClassrooms-Student-Center/OCMovies-API-EN-FR.git` (you can also download the code using [as a zip file](https://github.com/OpenClassrooms-Student-Center/OCMovies-API-EN-FR/archive/refs/heads/master.zip))
2. Move to the ocmovies-api root folder with `$ cd ocmovies-api-en`
3. Install project dependencies with `pipenv install` 
4. Create and populate project database with `pipenv run python manage.py create_db`
5. Run the server with `pipenv run python manage.py runserver`

When the server is running after step 5 of the procedure, the OCMovies API can
be requested from endpoints starting with the following base URL: [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/titles/).

Steps 1-4 are only required for initial installation. For subsequent launches
of the API, you only have to execute step 5 from the root folder of the project.

### Option 2: Installation and execution without pipenv (using venv and pip)

1. Clone this repository using `$ git clone clone https://github.com/OpenClassrooms-Student-Center/OCMovies-API-EN-FR.git` (you can also download the code using [as a zip file](https://github.com/OpenClassrooms-Student-Center/OCMovies-API-EN-FR/archive/refs/heads/master.zip))
2. Move to the ocmovies-api root folder with `$ cd ocmovies-api-en`
3. Create a virtual environment for the project with `$ py -m venv env` on windows or `$ python3 -m venv env` on macos or linux.
4. Activate the virtual environment with `$ env\Scripts\activate` on windows or `$ source env/bin/activate` on macos or linux.
5. Install project dependencies with `$ pip install -r requirements.txt`
6. Create and populate the project database with `$ python manage.py create_db`
7. Run the server with `$ python manage.py runserver`

When the server is running after step 7 of the procedure, the OCMovies API can be requested from endpoints starting with the following base URL: http://localhost:8000/api/v1/titles/.

Steps 1-3 and 5-6 are only required for initial installation. For subsequent launches of the API, you only have to execute steps 4 and 7 from the root folder of the project.

## Usage and detailed endpoint documentation

One you have launched the server, you can read the documentation through the
browseable documentation interface of the API by visiting [http://localhost:8000/api/v1/titles/](http://localhost:8000/api/v1/titles/).

The API provides the following endpoints. All these endpoints are read-only and exclusively support HTTP requests using the **GET method**:

- Search and filter movies: [http://localhost:8000/api/v1/titles/](http://localhost:8000/api/v1/titles/). The filters available are:

   - `year=<year>`, `min_year=<year>` or `max_year=<year>` to get movies 
   filterd by year. The first does an exact match of the year.
   - `imdb_score_min=<score>` and `imdb_score_max<score>` to get movies with only a 
   given imdb score.
   - `title=<title>` or `title_contains=<string>` to get movies matching 
   the searched string. The first performs an exact match while the second
   searches titles containing the search term. The search 
   is independent of character case.
   - `director=<director-name>` or `director_contains=<string>` to get movies
   whose directors correspond to the searched string. The first performs an exact match 
   with the director name while the second searches director names containing the 
   search term. The search is independent of character case.
   - `writer=<name>` or `writer_contains=<string>` to get movies
   whose writers contain to the searched string. The first performs an exact match 
   with the writer name while the second searches writer names containing the 
   search term. The search is independent of character case.
   - `actor=<name>` or `actor_contains=<string>` to get movies
   whose actors correspond to the searched string. The first performs an exact match 
   with the actor name while the second searches actor names containing the 
   search term. The search is independent of character case.
   - `genre=<name>` or `genre_contains=<string>` to get movies
   whose genres correspond to the searched string. The first performs an exact match 
   with the genre name while the second searches genre names containing the 
   search term. The search is independent of character case.
   - `country=<name>` or `country_contains=<string>` to get movies
   whose countries correspond to the searched string. The first performs an exact match 
   with the country name while the second searches country names containing the 
   search term. The search is independant of character case.
   - `lang=<name>` or `lang_contains=<string>` to get movies
   whose languages corresponds to the searched string. The first performs an exact match 
   with the language name while the second searches language names containing the 
   search term. The search is independent of character case.
   - `company=<name>` or `company_contains=<string>` to get movies
   whose company corresponds to the searched string. The first performs an exact match 
   with the company name while the second searches company names containing the 
   search term. The search is independent of character case.
   - `rating=<name>` or `rating_contains=<string>` to get movies
   whose rating corresponds to the searched string. The first performs an exact match 
   with the rating name while the second searches rating names containing the 
   search term. The search is independent of character case.
   - `sort_by=<field>` to sort movies in a particular order. For example,
   use `sort_by=title` to order the movies alphabetically by title and 
   `sort_by=-title` to order the movies in the reverse direction. You can also
   sort with multiple criteria by separating the criteria using commas as in `sort_by=-year,title` that filters the movie with the most recent ones first.
   Then, within a same year, movies are filtered alphabetically according to
   their title.

- Request detailed info about a movie: [http://localhost:8000/api/v1/titles/499549](http://localhost:8000/api/v1/titles/499549) where 499549 is the `id` of the 
movie "Avatar".
- Search the available genres: [http://localhost:8000/api/v1/genres/](http://localhost:8000/api/v1/genres/). The filters available are:
   - `name_contains=<search string>` to filter only the genres containing the
   searched string.
   - `movie_title_contains=<search string>` to find the genres associated with
   a particular movie searched by title.


# OCMovies-API: API de test fournissant des informations sur des films

Le projet OCMovies-API est une application web à éxécuter localement dans le cadre de projets éducatifs. Cette application est implémentée sous la forme d'une API REST. Elle fournit des informations cinématogratphiques à partir d'urls interrogeables à l'aide d'un client HTTP graphique comme un navigateur web ou postman, ou d'un client HTTP programmatique comme requests en python ou fetch/axios en javascript. Les points d'entrées fournis par cette API de test sont consultables en lecture-seule avec des points d'entrée limités aux requêtes GET.

## Installation

Cette API exécutable localement peut être installée en suivant les étapes décrites ci-dessous. L'usage de pipenv est recommandé, mais des instuctions utilisant venv et pip sont également fournies plus bas. Si pipenv n'est pas encore installé sur votre ordinateur, vous trouverez des instuctions d'installation détaillées [sur cette page](docs/pipenv/installation-fr.md).

### Installation et exécution de l'application avec pipenv

1. Cloner ce dépôt de code à l'aide de la commande `$ git clone clone https://github.com/OpenClassrooms-Student-Center/OCMovies-API-EN-FR.git` (vous pouvez également télécharger le code [en temps qu'archive zip](https://github.com/OpenClassrooms-Student-Center/OCMovies-API-EN-FR/archive/refs/heads/master.zip))
2. Rendez-vous depuis un terminal à la racine du répertoire ocmovies-api-fr avec la commande `$ cd ocmovies-api-fr`
3. Installez les dépendances du projet à l'aide de la commande `pipenv install` 
4. Créer et alimenter la base de données à l'aide de la commande `pipenv run python manage.py create_db`
5. Démarrer le serveur avec `pipenv run python manage.py runserver`

Lorsque le serveur fonctionne, après l'étape 5 de la procédure, l'API OCMovies peut être interrogée à partir des points d'entrée commençant par l'url de base [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/). Le point d'entrée principal permettant de consulter les films est [http://localhost:8000/api/v1/titles](http://localhost:8000/api/v1/titles/). Si vous accédez à cette url depuis un navigateur,ce dernier vous présentera une interface naviguable servant de documentation et de laboratoire d'expériementation. Vous trouvez également une documentation plus formelle en bas de ce README.

Les étapes 1 à 4 ne sont requises que pout l'installation initiale. Pour les lancements ultérieurs du serveur de l'API, il suffit d'exécuter l'étape 5 à partir du répertoire racine du projet.

### Installation et exécution de l'application sans pipenv (avec venv et pip)

1. Cloner ce dépôt de code à l'aide de la commande `$ git clone clone https://github.com/OpenClassrooms-Student-Center/OCMovies-API-EN-FR.git` (vous pouvez également télécharger le code [en temps qu'archive zip](https://github.com/OpenClassrooms-Student-Center/OCMovies-API-EN-FR/archive/refs/heads/master.zip))
2. Rendez-vous depuis un terminal à la racine du répertoire ocmovies-api-fr avec la commande `$ cd ocmovies-api-fr`
3. Créer un environnement virtuel pour le projet avec `$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.
4. Activez l'environnement virtuel avec `$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.
5. Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`
6. Créer et alimenter la base de données avec la commande `$ python manage.py create_db`
7. Démarrer le serveur avec `$ python manage.py runserver`

Lorsque le serveur fonctionne, après l'étape 7 de la procédure, l'API OCMovies peut être interrogée à partir des points d'entrée commençant par l'url de base [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/). Le point d'entrée principal permettant de consulter les films est [http://localhost:8000/api/v1/titles](http://localhost:8000/api/v1/titles/). Si vous accédez à cette url depuis un navigateur,ce dernier vous présentera une interface naviguable servant de documentation et de laboratoire d'expériementation. Vous trouvez également une documentation plus formelle en bas de ce README.

Les étapes 1 à 6 ne sont requises que pout l'installation initiale. Pour les lancements ultérieurs du serveur de l'API, il suffit d'exécuter les étapes 4 et 7 à partir du répertoire racine du projet.

## Utilisation et documentation des points d'entrée

Une fois que vous avez lancé le serveur, vous pouvez lire la documentation depuis un navigateur web par le biais de l'interface navigable disponible ici [http://localhost:8000/api/v1/titles/](http://localhost:8000/api/v1/titles/). Cette interface naviguable vous sert à la fois de source de documentation et de laboratoire d'expérimentation. L'API actuelle ne fournit que les points d'entrées suivants. Tous ces points d'entrée sont en lecture seule et supportent exclusivement les requêtes HTTP utilisant la **méthode GET**: 

- Rechercher et filtrer des films: [http://localhost:8000/api/v1/titles/](http://localhost:8000/api/v1/titles/). Vous pouvez tester directement chaque filtre en accédant à l'URL ci-dessus depuis un navigateur web. Les filtres disponibles sont:

   - `year=<year>`, `min_year=<year>` ou `max_year=<year>` pour obtenir des films filtrés par années. Le premier de ces filtres réalise une correspondance exacte lors de la recherche.
   - `imdb_score_min=<score>` et `imdb_score_max<score>` pour obtenir des films avec un score imdb inférieurs ou supérieur à une note donnée.
   - `title=<title>` ou `title_contains=<string>` pour obtenir des films dont le titre correspond à la chaine de caractères recherchée. Le premier effectue une recherche avec une correspondance extacte tandis que le second recherche les titres contenant le terme recherché. La recherche est indédendante de la casse.
   - `director=<director-name>` ou `director_contains=<string>` pour obtenir des films dont un réalisateur correspond à la chaine de caractères recherchée. Le premier effectue une recherche avec une correspondance extacte tandis que le second filtre en fonction des réalisateurs contenant le terme recherché. La recherche est indédendante de la casse.
   - `writer=<name>` ou `writer_contains=<string>` pour obtenir des films dont un auteur correspond à la chaine de caractères recherchée. Le premier effectue une recherche avec une correspondance extacte tandis que le second filtre en fonction des auteurs contenant le terme recherché. La recherche est indédendante de la casse.
   - `actor=<name>` ou `actor_contains=<string>` pour obtenir des films dont un des acteurs correspond à la chaine de caractères recherchée. Le premier effectue une recherche avec une correspondance extacte tandis que le second recherche filtre en fonction des acteurs contenant le terme recherché. La recherche est indédendante de la casse.
   - `genre=<name>` ou `genre_contains=<string>` pour obtenir des films dont un genre correspond à la chaine de caractères recherchée. Le premier effectue une recherche avec une correspondance extacte tandis que le second filtre en fonction des genres contenant le terme recherché. La recherche est indédendante de la casse.
   - `country=<name>` ou `country_contains=<string>` pour obtenir des films dont un pays correspond à la chaine de caractères recherchée. Le premier effectue une recherche avec une correspondance extacte tandis que le second filtre en fonction des pays contenant le terme recherché. La recherche est indédendante de la casse.
   - `lang=<name>` ou `lang_contains=<string>` pour obtenir des films dont la langue correspond la chaine de caractères recherchée. Le premier effectue une recherche avec une correspondance extacte tandis que le second filtre en fonction des langues contenant le terme recherché. La recherche est indédendante de la casse.
   - `company=<name>` ou `company_contains=<string>` pour obtenir des films dont la compagnie de production correspond à la chaine de caractères recherchée. Le premier effectue une recherche avec une correspondance extacte tandis que le second filtre en fonction des compagnies contenant le terme recherché. La recherche est indédendante de la casse.
   - `rating=<name>` ou `rating_contains=<string>` pour obtenir des films dont le politique de restriction correspond à la chaine de caractères recherchée. Le premier effectue une recherche avec une correspondance extacte tandis que le second filtre en fonction des restrictions contenant le terme recherché. La recherche est indédendante de la casse.
   - `sort_by=<field>` pour obtenir des films triés selon un ordre particulier. Par exemple, utiliser `sort_by=title` pour trier les films selon l'ordre alphabétique de teur titre et `sort_by=-title` pour trier les films dans le sens inverse. Il est également possible de trier par critères multiples en séparant les critères par des virgules comme dans `sort_by=-year,title` qui affiche d'abord les films les plus récents, puis trie les films de la même années par ordre alphabétique.

- Demander des informations détaillées sur un film dont on connait l'identifiant: [http://localhost:8000/api/v1/titles/499549](http://localhost:8000/api/v1/titles/499549) où 499549 est l'identifiant (`id`) du film "Avatar".
- Rechercher les genres disponibles: [http://localhost:8000/api/v1/genres/](http://localhost:8000/api/v1/genres/). Les filtres disponibles sont:
   - `name_contains=<search string>` pour n'afficher que les genres dont la nom contient la chaine de caractère recherchée.
   - `movie_title_contains=<search string>` pour rechercher les genres associés à film dont le titre contient la chaine de caractère recherchée.
   a particular movie searched by title.
