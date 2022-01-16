# Chronophotographie.py
Le document est extrait du site <a href="allophysique.com/docs/PC_1ere/meca/page1/">allophysique.com</a>.

Le but de la séance est d'enregistrer la trajectoire de plusieurs mouvements, sous la forme d'une chronophotographie.

Les chronophotographies sont utiles pour repérer les phases accélérées du mouvement. C'est à dire, les phases du mouvement où il y a une/des interaction(s).

## Préparer la tablette Android
Il sera nécessaire de charger, dans cet ordre, les 2 applications suivantes:


* *Cx explorateur de fichiers* (Play Store, gratuit)
* *Motion shot*, qui n'est pas sur le Play store: 
  * à l'aide du navigateur (chrome par exemple), aller à l'adresse: [https://motion-shot.fr.uptodown.com/android](https://motion-shot.fr.uptodown.com/android)
  * Télecharger l'application (version en cours: 2.2.1)
* Ouvrir l'application *Cx explorateur de fichiers*. Choisir le stockage *principal*.
* Aller dans le dossier *Download* et rechercher le fichier *motion-shot-2-2-1.apk*. Cliquer sur le fichier et *accepter l'installation*. Un message vous avertit des risques encourus pour l'installation d'une application non distribuée par le Play store. Accepter.


## Premiers tests
On pourra alors utiliser l'application pour enregistrer les trajectoires de quelques mouvements (pas trop rapides). Comme présenté sur la video ci-dessous:

<a href="https://www.youtube.com/watch?v=FF8Qd48FO7o">video de la chaine spc Richard Escudé</a>

Vous pouvez alors vous tester l'application avec un premier mouvement.<br>
Choisissez un objet présentant un contraste suffisant par rapport au fond de l'image. Démarrez la vidéo, enregistrez le mouvement. 

La chronophtographie est générée lors de l'arrêt de l'enregistrement. Il s'agit d'une image qui se trouve dans le dossier *Pictures/Motion_Shot*

Un exemple de chronophotographie obtenue:

<figure>
  <img src="images/Motion_Shot.jpg">
</figure> 

# Travail pratique
## Expérimentations
Le matériel dans la classe permet de réaliser plusieurs situations expérimentales:

* Une bille lancée sur un plan horizontal
* Une bille lancée sur un plan incliné
* Une bille lâchée en haut d'un plan incliné, guidée par un rail
* Un pendule suspendu au plafond, en oscillation
* ...

Pour chacune de ces expériences, vous réaliserez la chronophotographie la plus précise possible, à l'aide de l'application téléchargée.

Vous téléchargerez ensuite l'image obtenue sur votre ordinateur (envoi en piece jointe d'un mail par exemple).

## Pointage des positions
Télécharger:

* le programme :chronophotographie.py
* ainsi que l'image test: *images/Motion_Shot.jpg*

Déplacer les 2 fichiers dans un dossier de vos documents: *Documents/physique/* par exemple.

Dans *Winpython*: Lancer un IDE Python, comme par exemple *IDLE Python*. Dans le menu *Fichier*, ouvrir le programme *chronophotographie.py*. Puis *Executer*

Dans la fenêtre graphique, cliquer sur *select image*. Et réaliser le pointage, c'est à dire, cliquer sur la position du même point, au fur et à mesure de son avancée dans le mouvement. Des marqueurs s'ajoutent à l'image.<br>
Et la liste des coordonnées s'affiche à droite.


Lorsque la saisie est terminée, cliquer sur *valider*. Un fichier *coordonnees.txt* est alors créé dans le même dossier, avec les coordonnées du point. On peut consulter le contenu avec un editeur de texte (Visual Studio, ou Notepad++).

## Exploitation
Dans le programme IDLE python: Créer un nouveau script, que vous appelerez *exploitation.py*

* Commencer par importer le module *pandas* puis les données des coordonnées:

```python
import pandas as pd  # on importe la librairie pandas
data = pd.read_csv("coordonnees.txt")
print(data)
```


* Ajouter l'instruction suivante pour explorer l'objet *data*

```python
print(data.columns)
```

* Pour obtenir les valeurs de la seule colonne Y, on peut alors faire:

```python
print(data.Y)
```


* Pour afficher le tracé (X,Y):

```python
data.plot.scatter(x='X', y='Y')
```


On remarque que la coordonnée Y est repérée à partir du bord inférieur de la fenêtre graphique. Alors que pour le pointage, c'était à partir du bord supérieur. On peut modifier les valeurs de TOUTE la colonne Y en faisant par exemple:

```python
data.Y = 300 - data.Y
```

Le graphique généré est alors le suivant:


* Enfin, pour sauvegarder le graphique, il faudra ajouter le module matplotlib. Le programme complet devrait alors être:

```python
import pandas as pd  
import matplotlib.pyplot as plt
data = pd.read_csv("coordonnees.txt")
data.Y = 300- data.Y
data.plot.scatter(x='X', y='Y')
plt.savefig('output.png')
```





