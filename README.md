# 🌐 Hezil Network Tool 🛠️

Bienvenue à **Hezil Network Tool** ! Un outil puissant conçu pour gérer et manipuler les interfaces réseau sur Linux. Ce script, écrit en Python, vous permet d'afficher l'adresse IP et MAC, de changer les adresses IP, et même de gérer l'état des interfaces réseau. 🔧

## 🚀 Fonctionnalités

### 🔍 1. Visualiser l'adresse IP
Vous pouvez facilement afficher l'adresse IP actuelle d'une interface réseau. 🖥️ Que ce soit pour l'interface Ethernet (`eth0`) ou une interface Wi-Fi (`wlan0`), ce script le fait pour vous en un clin d'œil.

### 🔄 2. Changer l'adresse IP
Besoin de changer rapidement l'adresse IP de votre interface ? Pas de souci ! 🆕 Utilisez simplement l'option pour définir une nouvelle adresse IP sur l'interface de votre choix. Parfait pour les tests de réseau ou les configurations avancées.

### 🛡️ 3. Visualiser l'adresse MAC
Ce script permet également d'afficher l'adresse MAC de n'importe quelle interface réseau. 🔐 L'adresse MAC (Media Access Control) est unique et essentielle dans la communication réseau.

### ⚡ 4. Activer une interface réseau
En une seule commande, vous pouvez activer une interface réseau désactivée. 📡

### 📴 5. Désactiver une interface réseau
À l'inverse, vous pouvez désactiver une interface réseau facilement. Cela peut être pratique lorsque vous avez besoin de déconnecter temporairement une interface.

### ❌ 6. Quitter l'outil
Quittez proprement l'outil avec cette option. 🛑

## 🎯 Utilisation

### Installation

Pour utiliser cet outil, vous devez d'abord cloner le dépôt GitHub :

```bash
git clone https://github.com/ademoo077/network-tool.git
cd network-tool
```
Installez les dépendances requises avec pip :
```bash
pip install termcolor
```
## Exécution
Lancer l'outil avec Python :
Installez les dépendances requises avec pip :
```bash
python3 network_tool.py
```
## 📜 Menu Interactif
Voici à quoi ressemble le menu d'accueil :
🌐 Hezil Network Tool 🛠️
1️⃣  Voir l'adresse IP
2️⃣  Changer l'adresse IP
3️⃣  Voir l'adresse MAC
4️⃣  Activer une interface réseau
5️⃣  Désactiver une interface réseau
6️⃣  Quitter
Sélectionnez simplement une option pour interagir avec le réseau.
## 📢 Avertissement
- **🛑 Attention**: Les commandes de ce script nécessitent des droits sudo. Assurez-vous d'avoir les autorisations suffisantes avant de lancer certaines opérations, comme le changement d'adresse IP ou l'activation/désactivation d'une interface
## 🛠️ Technologies Utilisées
- **Python** : Langage principal pour le développement de l'outil.
- **subprocess** : Pour exécuter des commandes système Linux.
- **termcolor** : Pour colorer les sorties dans le terminal.
- **Regex (re)** : Pour extraire les adresses IP des interfaces.
##🧑‍💻 Contribution
Ce projet est ouvert aux contributions ! Si vous avez des idées pour améliorer cet outil ou souhaitez corriger des bugs, n'hésitez pas à faire une pull request. 🙌
🎉 Merci d'utiliser Hezil Network Tool et bonne gestion de vos interfaces réseau ! 🌐💻
