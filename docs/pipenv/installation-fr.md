# Description de l'installation de pipenv

Pipenv est un outils de gestion des dépendance et de gestion des environnements
virtuel recommandé dans la [documentation sur le packaging de Python](https://packaging.python.org/tutorials/managing-dependencies/). Ce document décrit l'installation
de pipenv sur les système d'exploitation Window, Macos et Linux.

## Installation

La procédure d'installation recommande varie légèrement en fonction du système
d'exploitation que vous utilisez. Vous trouverez ci-dessous des procédures
d'installation simples pour chaque système. Elles résument les instructions  
que nous pouvons lire sur [la documentation officielle](https://pipenv.pypa.io/en/latest/#install-pipenv-today).

### Installation de pipenv sur windows

Pour installer pipenv sur windows, l'unique pré-requis est disposer d'une 
installation de Python 3 et de pip fonctionnelle. L'installation de pipenv se
déroule en une commande:

```
$ pip install pipenv
```

Vous pouvez vérifier la bonne installation de pipenv en exécutant la commande
`pipenv --version`. Une fois pipenvinstallé et fonctionnel, n'hésitez pas à jeter un 
oeil à la section "Avantages et utilisation"ci-dessous. Happipenv!

### Installation de pipenv sur macos

Pour installer pipenv sur macos, l'approche recommande est d'utiliser
homebrew si vous en être déjà utilisateur. C'est un indispensable pour faire du
développement sous macos. L'installation avec homebrew est relativement simple:

```
$ brew install pipenv
```

Pour ceux parmi vous qui n'utilisent pas homebrew (rare parmi les devs sous macos), 
il est naturellement également possible d'installer pipenv à l'aide de pip3 comme
suit:

```
$ pip3 install pipenv
```

Vous pouvez vérifier la bonne installation de pipenv en exécutant la commande
`pipenv --version`. Une fois pipenvinstallé et fonctionnel, n'hésitez pas à jeter un 
oeil à la section "Avantages et utilisation"ci-dessous. Happipenv!

## Installation de pipenv sur Fedora > 28

Sur Fedora, il est possible d'installer pipenv à l'aide de dnf dès la version 28 du système. Voici la commande d'installation:

```
sudo dnf install pipenv
```

Vous pouvez également utiliser une installation classique à l'aide de pip3. Si c'est votre désir, référez-vous à la section suivante.

Vous pouvez vérifier la bonne installation de pipenv en exécutant la commande
`pipenv --version`. Une fois pipenvinstallé et fonctionnel, n'hésitez pas à jeter un 
oeil à la section "Avantages et utilisation"ci-dessous. Happipenv!

### Installation de pipenv sur Debian, Ubuntu et n'importe quel linux

Pour installer pipenv sur windows, l'unique pré-requis est disposer d'une 
installation de python3 et de pip3 fonctionnelle. L'installation de pipenv se
déroule en une commande:

```
$ pip3 install --user pipenv
```

Cette commande installera pipenv dans le répertoire `$HOME/.local/bin`. Vérifiez
que ce répertoire est dans le PATH. Ci-nécessaire, vous pouvez ajouter la commande
`export PATH="$HOME/.local/bin:$PATH"` au sein du fichier `$HOME/.profile`.

Vous pouvez ensuite vérifier la bonne installation de pipenv en exécutant la commande
`pipenv --version`. Une fois pipenvinstallé et fonctionnel, n'hésitez pas à jeter un 
oeil à la section "Avantages et utilisation"ci-dessous. Happipenv!

## Avantages et utilisation
Les avantages de cette outils par rapport à une utilisation explicite du couple
venv+pip sont les suivants:

- `pipenv install` crée automatiquement un environnement virtuel lors de 
l'installation d'une bibliothèque ou d'un outils. Vous ne pouvez pas installer
par erreur une dépendance globalement.
- `pipenv install` ajoute automatiquement chaque dépendance installée au sein
d'un fichier Pipfile et un fichier Pipfile.lock. Les deux fichiers peuvent 
être ajouter à vos commit et partagés entre tous les membres de votre équipe de
développement. Ces fichiers jouent le rôle d'un fichier requirements.txt avec
l'avantage d'être automatiquement généré et mis à jour et de séparer les 
dépendance directes et indirectes. Vous ne voyez que vos dépendances directes dans le fichier Pipfile.
- `pipenv shell` permet d'activer l'environnement virtuel avec la même commande
sur tous les systèmes d'exploitation. Plus besoin de détailler des commandes
différentes pour windows et macos/linux. La commande `exit` permet ensuite de
quitter cet environnement virtuel.
- `pipenv run <commande>` permet de lancer une commande au sein d'un environnement
virtuel sans avoir à l'activer.
- `pipenv install` ne crée pas son environnement virtuel dans le répertoire 
courant. Cela évite que vous puissiez par erreur l'envoyer sur github. Pour
pouvez connaître le chemin de cet environnement virtuel à l'aide de la commande
`pipenv --venv` et le détruire avec la commande `pipenv --rm`.
