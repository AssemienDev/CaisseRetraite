# Portail de Gestion pour Caisse de Retraite

Ce projet est une application web développée avec le framework Django. Son objectif est de fournir une plateforme complète et sécurisée pour la gestion des adhérents, des demandes de retraite, du suivi de l'épargne et des opérations financières d'une caisse de retraite.


## Description des Modules

Le projet est composé des modules suivants, chacun ayant un rôle bien défini :

### 1. Module `gestion` (Le Cœur)
C'est le socle de l'application. Il est responsable de la gestion des informations fondamentales sur les adhérents et leurs contributions.
*   **Fonctionnalités :** Gestion des profils adhérents, suivi des cotisations.
*   **Données gérées :** Informations personnelles des adhérents, historique des cotisations versées.

### 2. Module `retraites`
Ce module gère l'intégralité du processus de demande de retraite.
*   **Fonctionnalités :** Permet aux adhérents de soumettre des demandes de retraite et aux administrateurs de les traiter.
*   **Données gérées :** Demandes de retraite, montants souhaités, dates et statuts (en attente, approuvée, rejetée).

### 3. Module `epargne`
Dédié au suivi financier de l'épargne individuelle des membres.
*   **Fonctionnalités :** Consultation du solde d'épargne, historique des opérations (dépôts, intérêts).
*   **Données gérées :** Comptes d'épargne, transactions, intérêts accumulés.

### 4. Module `rapports`
Ce module est responsable de la génération et du stockage des rapports financiers périodiques.
*   **Fonctionnalités :** Met à disposition des rapports mensuels téléchargeables.
*   **Données gérées :** Fichiers de rapports, "instantanés" des totaux financiers (cotisations, paiements de retraite, épargnes) à une date donnée.

### 5. Module `audit`
Assure la traçabilité des actions importantes réalisées sur la plateforme.
*   **Fonctionnalités :** Enregistre un historique des opérations significatives pour consultation par les administrateurs.
*   **Données gérées :** Logs d'actions, utilisateur responsable, date et heure de l'action.

### 6. Module `repartition`
Modélise la gestion des fonds collectifs et des paiements effectués aux retraités.
*   **Fonctionnalités :** Suivi du montant total des fonds de la caisse et enregistrement de chaque paiement de retraite.
*   **Données gérées :** Solde global du fonds de retraite, historique détaillé des paiements mensuels.

## Rôles et Permissions

L'application définit deux rôles principaux avec des accès différents :

#### Adhérent (Utilisateur Standard)
*   Peut se connecter et accéder à son tableau de bord personnel.
*   Peut consulter le solde et l'historique de son compte épargne.
*   Peut soumettre de nouvelles demandes de retraite et consulter le statut des anciennes.
*   Peut télécharger les rapports financiers publics.

#### Administrateur
*   A accès à toutes les fonctionnalités des adhérents.
*   Peut accéder à l'interface d'administration complète de Django pour gérer toutes les données de l'application.
*   Peut approuver ou rejeter les demandes de retraite.
*   Peut gérer les comptes épargne et y ajouter des opérations.
*   Peut consulter l'historique complet des actions via le module d'audit.

## Instructions d'Installation

Pour lancer ce projet sur une machine de développement, suivez ces étapes :

1.  **Prérequis :** Assurez-vous d'avoir Python (version 3.9+), Git et PostgreSQL installés sur votre système.
2.  **Cloner le Dépôt :** Récupérez les fichiers du projet depuis le dépôt Git.
3.  **Créer un Environnement Virtuel :** Isolez les dépendances du projet en créant et en activant un environnement virtuel Python.
4.  **Installer les Dépendances :** Exécutez la commande `pip install -r requirements.txt` pour installer toutes les bibliothèques nécessaires.
5.  **Configurer l'Environnement :** Créez un fichier `.env` à la racine du projet pour y stocker les informations sensibles (clé secrète de Django, informations de connexion à la base de données PostgreSQL).
6.  **Appliquer les Migrations :** Exécutez `python manage.py migrate` pour créer la structure de la base de données.
7.  **Créer un Superutilisateur :** Exécutez `python manage.py createsuperuser` et suivez les instructions pour créer votre compte administrateur.
8.  **Lancer le Serveur :** Exécutez `python manage.py runserver` pour démarrer l'application. Elle sera accessible à l'adresse `http://127.0.0.1:8000`.

## Utilisation

Une fois le serveur lancé, vous pouvez :
1.  Vous connecter en tant qu'administrateur pour accéder à l'interface d'administration (`/admin/`).
2.  Créer des utilisateurs standards et les lier à des profils "Adhérent".
3.  Vous déconnecter et vous reconnecter avec un compte adhérent pour voir l'interface utilisateur standard et tester les fonctionnalités.