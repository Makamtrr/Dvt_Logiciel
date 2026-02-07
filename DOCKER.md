# Docker Deployment Guide

Ce guide explique comment utiliser Docker pour déployer le projet Titanic Survival Prediction.

## 🐳 Prérequis

- Docker installé ([Installation Docker](https://docs.docker.com/get-docker/))
- Docker Compose installé (inclus avec Docker Desktop)
- Compte Docker Hub (optionnel, pour push d'images)

## 🚀 Utilisation Locale

### Option 1 : Docker Run

```bash
# Build l'image
docker build -t titanic-prediction .

# Run le conteneur
docker run --rm -v $(pwd)/output:/app/output titanic-prediction

# Les prédictions seront dans output/submission.csv
```

### Option 2 : Docker Compose (Recommandé)

```bash
# Build et run en une commande
docker-compose up

# Run en arrière-plan
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter le conteneur
docker-compose down
```

## 📦 Pull depuis Docker Hub

Si l'image est déjà publiée sur Docker Hub :

```bash
# Pull l'image
docker pull <username>/titanic-survival-prediction:latest

# Run l'image
docker run --rm -v $(pwd)/output:/app/output <username>/titanic-survival-prediction:latest
```

## 🔧 Configuration

### Variables d'Environnement

Le conteneur utilise les variables d'environnement suivantes :

- `PYTHONUNBUFFERED=1` : Affichage immédiat des logs
- `PYTHONDONTWRITEBYTECODE=1` : Pas de fichiers .pyc
- `PIP_NO_CACHE_DIR=1` : Pas de cache pip

### Volumes

Le conteneur expose un volume pour les résultats :

```bash
-v /chemin/local/output:/app/output
```

Les prédictions seront écrites dans `/app/output/submission.csv`.

## 🏗️ Build Custom

Pour modifier le Dockerfile :

```bash
# Build avec un tag personnalisé
docker build -t titanic-prediction:v1.0 .

# Build sans cache
docker build --no-cache -t titanic-prediction .

# Build avec arguments
docker build --build-arg PYTHON_VERSION=3.10 -t titanic-prediction .
```

## 🚀 CI/CD avec GitHub Actions

Le projet inclut un workflow GitHub Actions pour automatiser le build et le push vers Docker Hub.

### Configuration des Secrets

Dans les paramètres GitHub du projet, ajouter :

1. `DOCKER_USERNAME` : Votre nom d'utilisateur Docker Hub
2. `DOCKER_PASSWORD` : Votre token d'accès Docker Hub

### Déclenchement Automatique

Le workflow se déclenche sur :
- Push vers `main` ou `develop`
- Tags de version (ex: `v1.0.0`)
- Pull Requests vers `main`

### Tags d'Image Générés

- `latest` : Dernière version de main
- `develop` : Dernière version de develop
- `v1.0.0` : Version spécifique (si tag git)
- `main-abc1234` : SHA du commit

## 🧪 Tests du Conteneur

```bash
# Build l'image
docker build -t titanic-prediction .

# Vérifier que l'image existe
docker images | grep titanic-prediction

# Run un test
docker run --rm titanic-prediction python -c "import pandas; import sklearn; print('OK')"

# Inspecter le conteneur
docker run --rm -it titanic-prediction /bin/bash
```

## 📊 Optimisation de l'Image

### Taille de l'Image

```bash
# Voir la taille
docker images titanic-prediction

# Multi-stage build pour réduire la taille (avancé)
# Modifier le Dockerfile pour utiliser plusieurs stages
```

### Cache Layers

Le Dockerfile est optimisé pour le cache :
1. `requirements.txt` copié en premier (change rarement)
2. Code source copié après (change souvent)

## 🔐 Sécurité

### Bonnes Pratiques

- ✅ Image de base officielle (`python:3.9-slim`)
- ✅ Utilisateur non-root (à ajouter si nécessaire)
- ✅ Pas de secrets dans l'image
- ✅ `.dockerignore` pour exclure fichiers sensibles

### Scan de Vulnérabilités

```bash
# Scanner l'image avec Docker Scout
docker scout cves titanic-prediction

# Ou avec Trivy
trivy image titanic-prediction
```

## 🐛 Dépannage

### Problème : Permission denied sur output/

```bash
# Créer le dossier localement d'abord
mkdir -p output
chmod 777 output
```

### Problème : Image trop volumineuse

```bash
# Utiliser python:3.9-alpine au lieu de python:3.9-slim
# Attention : alpine peut avoir des problèmes avec certaines libs scientifiques
```

### Problème : Build échoue

```bash
# Vérifier les logs détaillés
docker build --progress=plain --no-cache -t titanic-prediction .

# Vérifier que tous les fichiers nécessaires sont présents
ls -la titanic/
ls -la src/
```

## 📚 Ressources

- [Documentation Docker](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Best Practices Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

## 🎯 Commandes Utiles

```bash
# Lister les conteneurs en cours
docker ps

# Lister tous les conteneurs
docker ps -a

# Supprimer un conteneur
docker rm <container-id>

# Supprimer une image
docker rmi titanic-prediction

# Nettoyer les ressources inutilisées
docker system prune -a

# Voir les logs d'un conteneur
docker logs <container-id>

# Exécuter une commande dans un conteneur running
docker exec -it <container-id> bash
```