<div align="center">

<img src="assets/images/logo.png" width="160px">

# FastQR

<img src="assets/images/screen.png">

</div>

FastQR est un outil simple et efficace pour générer des QR codes rapidement et facilement. Que vous soyez un utilisateur occasionnel ou un développeur, il vous permet de créer des QR codes en toute simplicité, directement depuis votre terminal<!-- ou en utilisant l'interface intégrée à votre barre des tâches (uniquement pour les appareils sous Windows) -->.



## Fonctionnalités

- Génération rapide
- Interface intuitive
- Personnalisation des QR codes

## Installation

<!-- ### Windows
```bash
winget install --id=JernejSimoncic.Wget  -e
wget 

``` -->

### Linux
```bash
sudo su
git clone https://github.com/Luckyluka17/FastQR.git
cp FastQR/fastqr.py /usr/bin/fastqr
chmod +x /usr/bin/fastqr
```

## Utilisation
Une fois installé, lancez **FastQR** depuis votre terminal en exécutant la commande suivante :

```bash
fastqr -g https://votrelien.com
```

Consultez la [documentation](https://github.com/Luckyluka17/FastQR/wiki) pour en savoir plus sur comment utiliser toutes ses fonctionnalitées.


## Compiler le code
```bash
python3 -u build/build.py
```
Votre exécutable pour Windows sera par la suite disponible dans le dossier `dist`.

## Contribution
FastQR est un projet open-source, et nous accueillons les contributions de la communauté. Si vous souhaitez participer au développement de FastQR, consultez notre guide de contribution pour commencer.

<a href="https://www.buymeacoffee.com/luckyluka17" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>