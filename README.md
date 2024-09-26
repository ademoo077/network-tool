# Network Tool

**Network Tool** est un script Python permettant de gérer les interfaces réseau sur un système Linux. Il offre des fonctionnalités telles que la visualisation et la modification des adresses IP, l'affichage des adresses MAC, ainsi que l'activation et la désactivation des interfaces réseau.

## Fonctionnalités

- **Voir l'adresse IP** : Affiche l'adresse IP actuelle d'une interface spécifiée.
- **Changer l'adresse IP** : Permet de modifier l'adresse IP d'une interface réseau.
- **Voir l'adresse MAC** : Affiche l'adresse MAC de l'interface réseau spécifiée.
- **Activer une interface réseau** : Active une interface réseau.
- **Désactiver une interface réseau** : Désactive une interface réseau.

## Prérequis

Avant d'utiliser cet outil, assurez-vous d'avoir installé Python 3 et les droits d'accès appropriés pour exécuter des commandes réseau. De plus, le module `termcolor` doit être installé pour la coloration de la sortie.

Vous pouvez installer `termcolor` avec la commande suivante :

```bash
pip install termcolor
```
## Installation 
Cloner le dépôt :
```bash
git clone https://github.com/ademoo077/network-tool.git
```
Naviguer vers le répertoire du projet :
```bash
cd network-tool
```
## Utilisation 
Pour exécuter l'outil, assurez-vous que vous êtes dans le répertoire du projet, puis lancez le script:
```bash
python3 network.py
```
## Menu des options
Une fois lancé, l'outil affichera un menu avec les options suivantes :

- **Voir l'adresse IP** : Saisissez le nom de l'interface (ex. eth0, wlan0) pour voir l'adresse IP actuelle.
- **Changer l'adresse IP** : Saisissez le nom de l'interface et la nouvelle adresse IP pour la changer.
- **Voir l'adresse MAC** : Saisissez le nom de l'interface pour afficher l'adresse MAC.
- **Activer une interface réseau** : Saisissez le nom de l'interface que vous souhaitez activer.
- **Désactiver une interface réseau** : Saisissez le nom de l'interface que vous souhaitez désactiver.
- **Quitter** : Quitte l'outil.

## Remarques
Droits d'accès : Certaines fonctionnalités nécessitent des privilèges root. Exécutez le script avec sudo si nécessaire.
Compatibilité : Cet outil est conçu pour fonctionner sous Linux et peut ne pas être compatible avec d'autres systèmes d'exploitation.
