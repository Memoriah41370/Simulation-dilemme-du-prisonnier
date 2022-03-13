# Simulation Dilemme du prisonnier Tucker

Il faut installer le module pip
sous ubuntu : sudo apt install python3-pip

puis installer matplotlib
sous ubuntu : pip install matplotlib


L'algo prend plusieurs int en valeur :

 -- Pour les nombres de points --
un pour si l'IA triche et gagne
un pour si l'IA joue et perd
un pour si les 2 IAs trichent
un pour si les 2 IAs jouent

 -- Pour le nombre des différents IAs --
nombre d'IA Enfant
nombre d'IA Tricheur
nombre d'IA Copieur
nombre d'IA coequipier
nombre d'IA Ivrogne
nombre d'IA Indécie
nombre d'IA inspecteur

 -- Pour le nombre de tour --
nombre de tour par round


Ensuite il fait jouer les différents IA en 1vs1 pendant n rounds. en commençant par l'IA numéro 1 contre le numéro 2 puis le 3 jusqu'aux numéro n.
Il calcul les scores selon les points rentrer et selon ce que les IAs font. les IAs renvoient False si il triche ou True si il joue.
A chaque fin de match il sauvegarde les scores des 2 IAs.
Il regarde qu'un IA ne soit pas le même ou que l'IA n'est pas déjà jouer contre l'IA séléctionné sinon il zap ce match
Quand tous les matchs sont fait des fonctions qui servent à l'affichage ce lance
Et une fonction va regarder qu'elle est le plus gros score et affiche le gagnant (ou les gagnants), soit ceux qui on le plus gros score.
L'algo va ensuite envoyer un camembert en image montrant le caractère de l'IA et son scores
ou un graphique en bar si un des scores est négatif
