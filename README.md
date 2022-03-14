## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell
exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des
  profils, `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## DÉPLOIEMENT

### Fonctionnement

Le déploiement du projet ce fait via le pipeline CI/CD CircleCI, celui-ci - par le biais d'un fichier config.yml - va
permettre de :

- Tester le linting du code du site
- Exécuter une suite de tests unitaires à l'aide de pytest
- Créer une image du projet sur la plateforme DockerHub
- Deployer le site via heroku
- Programmer la surveillance du site et le suivi des erreurs via Sentry

### Prérequis pour le bon fonctionnement du déploiement

Afin de pouvoir reproduire le déploiement du site chez vous vous aurez besoin :

- D'un compte CircleCI (il est conseillé d'utiliser votre compte GitHub)
- D'un compte Docker, vous permettant d'utiliser Docker Hub pour le stockage et la gestion de vos images et d'installer
  si nécessaire Docker Desktop afin de pouvoir gérer en local vos images via le terminal/invite de commandes
- D'un compte Heroku
- D'un compte Sentry

### Étapes à suivre pour le déploiement

Veuillez créer une application sur le site Heroku et nommez-la `orange-county-lettings`

Créez ensuite un projet sur le site Sentry en le configurant pour une application Django (ignorez la partie suivante
vous indiquant comment modifier le code source, ceci est déjà fait !)

Après avoir cloné le projet sur votre machine et l'avoir lié à un dépôt GitHub, ouvrez CircleCI puis activez le suivi du
projet en cliquant sur "Projects" dans la barre de menu de gauche sous votre identifiant.

Il détectera la présence d'un fichier yml dans le projet et vous proposera de l'utiliser.

Cliquez ensuite en haut à droite sur le bouton "Project Settings" et rendez-vous dans la fenêtre de déclaration des
variables d'environnement. Vous devrez alors renseigner les informations suivantes (merci de respecter l'écriture des
variables comme indiqué ci-dessous) :

**1. Les identifiants Docker afin de permettre à CircleCI de vous connecter automatiquement**

- DOCKER_USERNAME = `Votre identifiant de connexion à Docker`
- DOCKER_PASSWORD = `Votre mot de passe de connexion à Docker`

**2. Le nom de l'application Heroku et votre clé API afin de mettre en place le déploiement du site**

- HEROKU_APP_NAME = `orange-county-lettings`
- HEROKU_API_KEY = `afin de l'obtenir, cliquez sur votre profil en haut à droite de la fenêtre de Heroku puis sur "
  Account Settings". Une fois sur la page descendez en bas de page, vous devriez voir votre "API KEY"`

**3. La clé secrète pour le fonctionnement de l'application Django :**

- SECRET_KEY = `vous pouvez obtenir une clé aléatoire en vous rendant sur le site` **https://djecrety.ir/**

**4. Le fichier de settings spécifique au déploiement sur Heroku :**

- DJANGO_SETTINGS_MODULE = `oc_lettings_site.heroku_settings`

**5. Le DSN de Sentry afin de permettre le suivi en temps réel des erreurs :**

- SENTRY_DSN
  = `Rendez-vous dans les paramètres du projet puis aller jusqu'à la partie SDK Setup du menu puis cliquez sur Client Keys (DSN). Vous aurez alors accés au DSN du projet`

Une fois ces réglages de fait vous n'avez rien d'autres à faire si ce n'est effectuer des push sur votre dépôt GitHub.
En effet, lors de chaque envoi de modifications circleCI exécutera les instructions dans l'ordre repris dans la partie
`Fonctionnement`. Si une erreur venait à être levée, elle vous sera alors indiquée.

### Utilisation de l'image Docker déjà existante

Une image Docker permettant l'exécution du code sans difficultés est disponible, pour cela vous devez simplement taper
dans votre terminal/invite de commandes :

`
$ docker run -p 8000:8000 -it ldm3110/orange_county_lettings:e46ffc36d28994bb2778c10e9274c1579546e76a
`

L'application s'installera et s'exécutera alors automatiquement. Pour le fermer veuillez presser Ctrl + C.

Pour un explicatif des commandes Docker, merci de vous référer à la documentation officielle : **https://docs.docker.com/**

### Visualisation de l'application actuellement déployée sur Heroku

Rendez-vous à l'adresse suivant :

**https://orange-county-lettings.herokuapp.com/**

