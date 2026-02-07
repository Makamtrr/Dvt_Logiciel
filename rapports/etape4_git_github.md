# Étape 4 : Utiliser Git et GitHub pour la collaboration en équipe

**Date de début :** 07/02/2026
**Statut :** En cours

## Objectifs de cette étape

1. Initialiser un dépôt Git local
2. Créer un dépôt GitHub distant
3. Mettre en place une stratégie de branches (main, develop, feature branches)
4. Configurer les bonnes pratiques Git (messages de commit explicites, pull requests)

---

## 1. Initialisation du dépôt Git local

### Actions réalisées :

#### 1.1 Vérification de l'état actuel
- Aucun dépôt Git n'existe actuellement dans le projet
- Le projet contient déjà :
  - Un notebook tutoriel Titanic (`titanic-tutorial.ipynb`)
  - Un dossier de cours (`cours_prjoet/`)
  - Un dossier de données Titanic (`titanic/`)

#### 1.2 Initialisation de Git

Commande exécutée :
```bash
git init
```

Résultat : Dépôt Git initialisé avec succès dans `.git/`

---

## 2. Configuration du fichier .gitignore

### Actions réalisées :

Création d'un fichier `.gitignore` adapté pour un projet Python Data Science :
- Exclusion des fichiers Python compilés (`__pycache__/`, `*.pyc`)
- Exclusion des environnements virtuels (`venv/`, `env/`)
- Exclusion des notebooks checkpoints (`.ipynb_checkpoints`)
- Exclusion des fichiers de configuration IDE
- Autorisation exceptionnelle des fichiers CSV du dossier `titanic/`
- Exclusion des modèles ML (`*.pkl`, `*.h5`)

---

## 3. Structure du projet créée

### Dossiers créés :
- `src/` : Code source des scripts Python modulaires
- `tests/` : Tests unitaires
- `docs/` : Documentation du projet
- `data/` : Données (non versionnées sauf titanic/)
- `rapports/` : Rapports de chaque étape
- `.github/workflows/` : Configuration GitHub Actions (pour l'étape 5)

### Fichiers initiaux :
- `README.md` : Documentation principale du projet
- `src/__init__.py` : Module Python principal
- `tests/__init__.py` : Package de tests
- `docs/README.md` : Index de la documentation

---

## 4. Premier commit

### Commit initial :
```bash
git add .
git commit -m "Initial commit: Configuration initiale du projet"
```

**Contenu du commit :**
- Structure complète des dossiers
- Fichiers de configuration (.gitignore)
- Documentation initiale (README.md)
- Données Titanic (train.csv, test.csv, gender_submission.csv)
- Notebook tutoriel de base
- Documents de cours et TPs

---

## 5. Configuration du dépôt distant GitHub

### Actions réalisées :

#### 5.1 Ajout du remote
```bash
git remote add origin git@github.com:Makamtrr/Dvt_Logiciel.git
```

#### 5.2 Premier push vers GitHub
```bash
git push -u origin master
```

Résultat : Code poussé avec succès sur la branche `master` du dépôt GitHub.

---

## 6. Stratégie de branches (Git Flow simplifié)

### Branches créées :

#### 6.1 Branche `master` (principale)
- Branche de production
- Contient le code stable et testé
- Protégée contre les pushs directs

#### 6.2 Branche `develop` (développement)
```bash
git branch develop
git push -u origin develop
```

- Branche de développement principal
- Point de départ pour les feature branches
- Intégration continue des nouvelles fonctionnalités

### Stratégie prévue pour la suite :

1. **Feature branches** : Pour chaque nouvelle fonctionnalité
   - Nomenclature : `feature/nom-fonctionnalite`
   - Exemple : `feature/data-preprocessing`, `feature/model-training`
   - Créées depuis `develop`
   - Mergées dans `develop` via Pull Request

2. **Workflow recommandé** :
   ```
   develop → feature/xxx → Pull Request → develop → master
   ```

---

## 7. Bonnes pratiques Git appliquées

### 7.1 Messages de commit
- Format explicite et descriptif
- Structure : Titre court + Description détaillée
- Liste des modifications principales

### 7.2 Organisation du dépôt
- `.gitignore` bien configuré
- Structure de dossiers claire et modulaire
- Séparation du code source, tests et documentation

### 7.3 Collaboration
- Utilisation de branches pour isoler le développement
- Préparation pour les Pull Requests (étapes suivantes)
- Remote configuré pour le travail d'équipe

---

## 8. État actuel du dépôt

### Branches disponibles :
- ✅ `master` : Branche principale (stable)
- ✅ `develop` : Branche de développement

### Remote :
- ✅ GitHub : `git@github.com:Makamtrr/Dvt_Logiciel.git`

### Prochaines étapes :
1. Créer une branche `feature/refactoring` depuis `develop`
2. Commencer l'étape 1 : Refactorisation du notebook
3. Utiliser des Pull Requests pour merger les features

---

## Résumé de l'Étape 4

**Statut :** ✅ **TERMINÉ**

**Réalisations :**
- [x] Initialisation du dépôt Git local
- [x] Configuration du .gitignore adapté
- [x] Création de la structure de dossiers
- [x] Premier commit avec tous les fichiers de base
- [x] Configuration du remote GitHub
- [x] Push du code vers GitHub
- [x] Création de la branche `develop`
- [x] Mise en place de la stratégie de branches

**Outils utilisés :**
- Git (ligne de commande)
- GitHub (dépôt distant)
- VSCode (IDE)

**Bonnes pratiques appliquées :**
- Messages de commit explicites
- Structure de projet modulaire
- Stratégie de branches Git Flow
- .gitignore complet

---

**Date de fin :** 07/02/2026
