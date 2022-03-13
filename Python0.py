from random import randint #importation de la fonction randint depuis la librairie random.
from matplotlib import pyplot #importation de pyplot depuis la librairie matplotlib
confiance = 0 #création de la variable global confiance qui permet au coequipier de savoir si il doit coopérer ou non.
detect = 0 #création de la variable detect qui permet au Inspecteur de savoir si il doit coopérer ou non.
Liste=[] #définit la liste qui contiendra les IAs pour tous l'algo.
point=[] #définit la liste qui contiendra les score pour tous l'algo.
gagnant=[] #définit la liste qui contiendra les gagnant pour tous l'algo.




class IA(object): #class qui regroupe toutes les IAs.

    def IAs(choice1,choice2,turn): #fonction qui permet de passer les arguments et les choix pour lancer les IAs avec les arguments correspondant.

        bool = True # déclaration d'une variable booléenne qui par défaut est sur True.

        if choice1 == 1 : #si le choix fait par l'utilisateur est de 1 alors l"IA qui va jouer sera un Tricheur.

            bool = IA.Tricheur() #on va renvoyer le résultat de la fonction du tricheur dans la variable bool.
            return bool #on retourne bool pour savoir si on joue ou si on triche.

        elif choice1 == 2 : #si le choix fait par l'utilisateur est de 2 alors l"IA qui va jouer sera un Enfant.

            bool = IA.Enfant() #on va renvoyer le résultat de la fonction de l'enfant dans la variable bool.
            return bool #on retourne bool pour savoir si on joue ou si on triche.

        elif choice1 == 3 : #si le choix fait par l'utilisateur est de 3 alors l"IA qui va jouer sera un Coéquipier.

            bool = IA.Coequipier(choice2, turn) #on va renvoyer le résultat de la fonction du coéquipier dans la variable bool.
            return bool #on retourne bool pour savoir si on joue ou si on triche.

        elif choice1 == 4 : #si le choix fait par l'utilisateur est de 4 alors l"IA qui va jouer sera un copieur.

            bool = IA.copieur(choice2,turn) #on va renvoyer le résultat de la fonction du copieur dans la variable bool.
            return bool #on retourne bool pour savoir si on joue ou si on triche.

        elif choice1 == 5 : #si le choix fait par l'utilisateur est de 5 alors l"IA qui va jouer sera un ivrogne.

            bool = IA.ivre(turn) #on va renvoyer le résultat de la fonction de l'ivrogne dans la variable bool.
            return bool #on retourne bool pour savoir si on joue ou si on triche.

        elif choice1 == 6: #si le choix fait par l'utilisateur est de 6 alors l"IA qui va jouer sera un indécie.

            bool = IA.indecie() #on va renvoyer le résultat de la fonction de l'indécie dans la variable bool.
            return bool #on retourne bool pour savoir si on joue ou si on triche.

        elif choice1 == 7 : #si le choix fait par l'utilisateur est de 7 alors l"IA qui va jouer sera un Inspecteur.

            bool = IA.detective(choice2,turn) #on va renvoyer le résultat de la fonction du Inspecteur dans la variable bool.
            return bool #on retourne bool pour savoir si on joue ou si on triche.


    def Tricheur(): #L'IA du tricheur consiste à tous le temps triché alors on renvoie tous le temps False.

        bool = False #la variable booléenne est donc sur False.
        return bool #on retourne la variable booléenne.


    def Enfant(): #L'IA de l'enfant consiste à tous le temps jouer alors on renvoie tous le temps True.

        bool = True #la variable booléenne est donc sur True.
        return bool #on retourne la variable booléenne.


    def Coequipier(choice2, turn): #L'IA du coequipier consiste à voir si l'autre IA triche ou joue, si l'autre IA triche la variable confiance baisse. Mais si il joue la confiance augmente.
                                   #Si la confiance est au dessus de ou égale à 0 alors le coequipier joue, si la confiance est en dessous de 0 alors le coequipier triche.

        global confiance #on déclare la variable global confiance.
        bool=True #on déclare la variable bool.

        if turn == 0 : #si on est au tour 0 l'adversaire n'a pas encore joué donc l'IA joue et ne triche pas.

            bool=True #la variable booléenne est donc sur True.
            confiance = 0 #la confiance est sur 0 ce qui permet de reset la confiance pour chaque nouvelle IA contre qui il joue.
            return bool #on retourne la variable booléenne.

        else : #si on est à un tour autre que 0 alors on fait les choses suivante :

            if choice2 == True : #si L'IA numéro 2 à joué au dernier tour alors la confiance augmente de 2.

                confiance = confiance + 2 #on ajoute 2 à la variable confiance.

            elif choice2 ==  False : #si L'IA numéro 2 à triché au dernier tour alors la confiance baisse de 4.

                confiance = confiance - 4 #on retire 4 à la variable confiance.


            if confiance < 0 : #si la variable de confiance est inférieur à 0 :

                bool = False #la variable booléenne est donc sur False.
                return bool #on retourne la variable booléenne.

            elif confiance >= 0 : #si la variable de confiance est égale à 0 ou supérieur :

                bool = True #la variable booléenne est donc sur True.
                return bool #on retourne la variable booléenne.


    def copieur(choice2,turn): #L'IA du copieur consiste à faire exactement ce que à fait l'adversaire au dernier tour. Au premier tour le copieur joue vu que l'adversaire est considerer comme jouant et ne trichant pas.

        if turn == 0 : #si on est au tour 0 l'adversaire n'a pas encore joué donc l'IA joue et ne triche pas.

            bool=True #la variable booléenne est donc sur True.
            return bool #on retourne la variable booléenne.

        if choice2 == True : #si l'ennemi à joué :

            bool = True #la variable booléenne est donc sur True.
            return bool #on retourne la variable booléenne.

        elif choice2 == False : #si l'ennemi à triché :

            bool = False #la variable booléenne est donc sur False.
            return bool #on retourne la variable booléenne.


    def ivre(turn): #L'IA de l'ivrogne consiste au fait que si le nombre du tour est un numéro paire alors il joue, mais si c'est un nombre impaire alors il triche.

        if turn % 2 == 1 : #si le numéro du tour est impaire :

            bool = False #la variable booléenne est donc sur False.
            return bool #on retourne la variable booléenne.

        elif turn % 2 == 0 : #si le numéro du tour est paire :

            bool = True #la variable booléenne est donc sur True.
            return bool #on retourne la variable booléenne.


    def indecie(): #L'IA de l'indécie consiste à jouer ou tricher de manière aléatoire.

        a=randint(1,2) #variable qui contient 1 ou 2. Choisis de façon aléatoire.

        if a == 1 : #Si a est égale à 1 alors l'indécie triche.

            bool = False #la variable booléenne est donc sur False.
            return bool #on retourne la variable booléenne.

        if a == 2 : #Si a est égale à 2 alors l'indécie joue.

            bool = True #la variable booléenne est donc sur True.
            return bool #on retourne la variable booléenne.

    def detective(choice2,turn): #L'IA du détéctive consiste à tester selon un comportement précis de sa part (joué, triché, joué, joué) si la personne en face à plus tendance à tricher ou à jouer.
                                 #Si l'adversaire triche le plus souvent, la variable detect sera inférieur à 0 et donc le Inspecteur ne fera que tricher jusqu'à la fonction.
                                 #Si l'adversaire joue le plus souvent, la variable detect sera égale ou supérieur à 0 et donc le Inspecteur ne fera que jouer jusqu'à la fonction.

        global detect # déclaration de la variable global detect

        if turn == 0 : #Si tour 0 :

            bool = True #la variable booléenne est donc sur True.
            detect = 0 #la variable detect est sur 0 ce qui permet de la reset pour chaque nouvelle IA contre qui il joue.
            return bool #on retourne la variable booléenne.

        elif turn == 1 : #Si tour 1 :

            if choice2 == True : #Si l'adversaire à joué :

                bool = False #la variable booléenne est donc sur False.
                detect = detect + 1 #on ajoute 1 à la variable detect
                return bool #on retourne la variable booléenne.

            elif choice2 == False : #Si l'adversaire à triché

                bool = False #la variable booléenne est donc sur False.
                detect = detect - 1 #on retire 1 à la variable detect
                return bool #on retourne la variable booléenne.

        elif turn == 2 : #Si tour 2 :

            if choice2 == True : #Si l'adversaire à joué :

                bool = True #la variable booléenne est donc sur True.
                detect = detect + 1 #on ajoute 1 à la variable detect
                return bool #on retourne la variable booléenne.

            elif choice2 == False : #Si l'adversaire à triché :

                bool = True #la variable booléenne est donc sur True.
                detect = detect - 1 #on retire 1 à la variable detect
                return bool #on retourne la variable booléenne.

        elif turn == 3 : #Si tour 3 :

            if choice2 == True : #Si l'adversaire à joué :

                bool = True #la variable booléenne est donc sur True.
                detect = detect + 1 #on ajoute 1 à la variable detect
                return bool #on retourne la variable booléenne.

            elif choice2 == False : #Si l'adversaire à triché :

                bool = True #la variable booléenne est donc sur True.
                detect = detect - 1 #on retire 1 à la variable detect
                return bool #on retourne la variable booléenne.

        else : #si autre que le tour 0, 1, 2 ou 3 :

            if detect >= 0 : #Si la variable detect supérieur ou égale à 0 :

                bool = True #la variable booléenne est donc sur True.
                return bool #on retourne la variable booléenne.

            elif detect < 0 : #Si la variable detect inférieur à 0 :

                bool = False #la variable booléenne est donc sur False.
                return bool #on retourne la variable booléenne.


def rules():#fonction qui contient le nombre de points gagné ou perdu et de tour
    a=[]#

    f= open("Infos_jeux.txt","r")#ouvre le fichier qui contient toutes les variables de la simulation
    Lignes=f.readlines()[0:5]#lit des lignes 1 à 5
    for i,ligne in enumerate(Lignes) :#enumère les ligne 1 à 5


        a.append(int(ligne))#ajoute les points gagné ou perdu et le nombre de tour à la liste

    return a

def choix_IAs():#fonction qui choisis les IA qui vont jouer dans la partie

    global Liste #définit la liste qui contiendra les IAs pour tous l'algo.
    global point #définit la liste qui contiendra les score pour tous l'algo.
    global gagnant #définit la liste qui contiendra les gagnant pour tous l'algo.





    nmb_IA=[]#liste qui va recevoir les infos du fichier texte contenant les IAs qui vont jouer.
    a=int()#variable qui contient le nombre d'IA Tricheur
    b=int()#variable qui contient le nombre d'IA Enfant
    c=int()#variable qui contient le nombre d'IA Coequipier
    d=int()#variable qui contient le nombre d'IA Copieur
    e=int()#variable qui contient le nombre d'IA Ivrogne
    f=int()#variable qui contient le nombre d'IA Indécie
    g=int()#variable qui contient le nombre d'IA Inspecteur





    f= open("Infos_jeux.txt","r")#ouvre le fichier qui contient toutes les variables de la simulation
    Lignes=f.readlines()[5:12]#lit des lignes 6 à 12
    for i,ligne in  enumerate(Lignes) :#enumère les ligne 6 à 12


        nmb_IA.append(int(ligne))#prend les nombre des différents IA depuis le fichier et les mets dans une liste


    a=nmb_IA[0] #prend le nombre de tricheur de la liste
    b=nmb_IA[1] #prend le nombre de Enfant de la liste
    c=nmb_IA[2] #prend le nombre de Coequipier de la liste
    d=nmb_IA[3] #prend le nombre de Copieur de la liste
    e=nmb_IA[4] #prend le nombre de Ivrogne de la liste
    f=nmb_IA[5] #prend le nombre de Indécie de la liste
    g=nmb_IA[6] #prend le nombre de Inspecteur de la liste

    nmb = a+b+c+d+e+f+g #variable qui contient le nombre total d'IAS.

    point=[int()]*nmb #Liste qui va contenir les points des IAs.
    gagnant=[int()]*nmb #liste qui contiendra l'endroit du gagnant dans la liste qui servira  à l'affichage du camembert (fera sortir la partie du gagnant).




    i=0#variable qui sert à ajouter les IA dans la liste qui contient les IAs.

    while i != a: #Tant que i différent de a

        Liste.append(1) #on ajoute des Tricheurs dans la liste
        i=i+1 #permet de faire avancer la boucle et de ne pas boucler à l'infini

    i=0 #permet de reset la variable pour les autres boucle while

    while i != b: #Tant que i différent de b

        Liste.append(2) #on ajoute des Enfants dans la liste
        i=i+1 #permet de faire avancer la boucle et de ne pas boucler à l'infini

    i=0 #permet de reset la variable pour les autres boucle while

    while i != c: #Tant que i différent de c

        Liste.append(3) #on ajoute des Coequipiers dans la liste
        i=i+1 #permet de faire avancer la boucle et de ne pas boucler à l'infini

    i=0 #permet de reset la variable pour les autres boucle while

    while i != d: #Tant que i différent de d

        Liste.append(4) #on ajoute des copieurs dans la liste
        i=i+1 #permet de faire avancer la boucle et de ne pas boucler à l'infini

    i=0 #permet de reset la variable pour les autres boucle while

    while i != e: #Tant que i différent de e

        Liste.append(5) #on ajoute des ivrognes dans la liste
        i=i+1 #permet de faire avancer la boucle et de ne pas boucler à l'infini

    i=0 #permet de reset la variable pour les autres boucle while

    while i != f: #Tant que i différent de f

        Liste.append(6) #on ajoute des indécies dans la liste
        i=i+1 #permet de faire avancer la boucle et de ne pas boucler à l'infini

    i=0 #permet de reset la variable pour les autres boucle while

    while i != g: #Tant que i différent de g

        Liste.append(7) #on ajoute des inspecteurs dans la liste
        i=i+1 #permet de faire avancer la boucle et de ne pas boucler à l'infini





def game(turn,choice1,choice2,nom,nom2,i,e,joue,triche,perd,perd_egau) : #fonction qui simule le dilemme de Tucker.

    count1 = 0 #variable qui compte le score de L'IA1.
    count2 = 0 #variable qui compte le score de L'IA2.
    tour = 0  # variable qui contient le nombre de tour à faire.
    IA2 = True #on part du principe que l'IA1 quoi que soit son comportement pense que l'IA2 va jouer.




    while tour != turn : #Tant que la variable qui compte le nombre de tour est différente de celle qui contient le nombre de tour :

        IA1 = IA.IAs(choice1,IA2,tour) #L'IA1 a un caratère déterminé par un nombre que l'utilisateur a chosis et va lancer l'algorithme qui correspond à ce même nombre.
        IA2 = IA.IAs(choice2,IA1,tour) #L'IA2 a un caratère déterminé par un nombre que l'utilisateur a chosis et va lancer l'algorithme qui correspond à ce même nombre.

        if IA1 == False : #Si l'IA1 triche :

            action = "triche" #la variable action qui sert à l'affichage contient l'argument str triche.

        else : #sinon :

            action = 'joue' #la variable action qui sert à l'affichage contient l'argument str joue.

        if IA2 == False : #Si l'IA2 triche :

            action2 = "triche" #la variable action qui sert à l'affichage contient l'argument str triche.

        else : #Sinon

            action2 = 'joue' #la variable action qui sert à l'affichage contient l'argument str joue.

        print(f"On est au tour {tour+1}, l'IA numéro {i+1} ({nom}) {action} | l'IA numéro {e+1} ({nom2}) {action2}") #affichage du numéro du tour, du numéro des IAs, du caractère des IAs et de si l'IA1 et l'IA2 joue ou triche


        if IA1 == False and IA2 == False : #Si les 2 IAs trichent :

            tour = tour + 1 #ajout de 1 à la variable qui compte le nombre de tour.
            count1 = count1 + perd_egau #ajout de x au compteur de score de l'IA1.
            count2 = count2 + perd_egau #On ajoute x au compteur de score de l'IA2.



        elif IA1 == False and IA2 == True : #Si le première IA triche et le deuxième joue :

            count1= count1 + triche #ajout de x au compteur de score de l'IA1.
            count2 = count2 + perd #On ajoute x au compteur de score de l'IA2.
            tour = tour + 1 #ajout de 1 à la variable qui compte le nombre de tour.

        elif IA1 == True and IA2 == False :

            count1= count1 + perd #On ajoute x au compteur de score de l'IA1.
            count2 = count2 + triche #ajout de x au compteur de score de l'IA2.
            tour = tour + 1 #ajout de 1 à la variable qui compte le nombre de tour.

        elif IA1 == True and IA2 == True :

            count1= count1 + joue #ajout de x au compteur de score de l'IA1.
            count2 = count2 + joue #ajout de x au compteur de score de l'IA2.
            tour = tour + 1 #ajout de 1 à la variable qui compte le nombre de tour.

#Affichage
    print("-")
    print(f"score IA1 : {count1} | score IA2 : {count2}") #Affichage des scores à la fin du tour.
    print("-")
#Affichage

    return  [count1, count2] #on retourne les scpres des 2 IAs.



def Trad(a_traduire): #fonction qui traduit les numéro des IAs en leur nom


    if type(a_traduire) == int : #Si la variable envoyer dans la fonction est un int :

        if a_traduire == 1 : #Si IA2 = 1 :

            nom = 'Tricheur' #variable qui contient le nom aura comme argument str tricheur.
            return nom #retourne son nom

        elif a_traduire == 2 : #Si IA2 = 2 :

            nom = 'Enfant' #variable qui contient le nom aura comme argument str enfant.
            return nom #retourne son nom

        elif a_traduire == 3 : #Si IA2 = 3 :

            nom = 'Coequipier' #variable qui contient le nom aura comme argument str coéquipier.
            return nom #retourne son nom

        elif a_traduire == 4 : #Si IA2 = 4 :

            nom = 'Copieur' #variable qui contient le nom aura comme argument str copieur.
            return nom #retourne son nom

        elif a_traduire == 5 : #Si IA2 = 5 :

            nom = 'Ivrogne' #variable qui contient le nom aura comme argument str ivrogne.
            return nom #retourne son nom

        elif a_traduire == 6 : #Si IA2 = 6 :

            nom = 'Indécie' #variable qui contient le nom aura comme argument str indécie.
            return nom #retourne son nom

        elif a_traduire == 7 : #Si IA2 = 7 :

            nom = 'Inspecteur' #variable qui contient le nom aura comme argument str Inspecteur.
            return nom #retourne son nom


    else : #Si la variable envoyer dans la fonction est autre chose qu'un int (mais ne fonctionnera que si c'est une liste) :

        for i in range(len(a_traduire)) : #On transforme les int de la liste qui contient les nombres pour lancer les algos des différentes IAs par leur nom.

            if a_traduire[i] == 1 : #Si le int est égale à 1 dans l'emplacement i de la liste alors :

                a_traduire[i] = 'Tricheur' #On remplace le 1 par Tricheur.

            elif a_traduire[i] == 2 : #Si le int est égale à 2 dans l'emplacement i de la liste alors :

                a_traduire[i]= 'Enfant' #On remplace le 2 par Enfant.

            elif a_traduire[i] == 3 : #Si le int est égale à 3 dans l'emplacement i de la liste alors :

                a_traduire[i] = 'Coequipier' #On remplace le 3 par Coequipier.

            elif a_traduire[i] == 4 : #Si le int est égale à 4 dans l'emplacement i de la liste alors :

                a_traduire[i] = 'Copieur' #On remplace le 4 par Copieur.

            elif a_traduire[i] == 5 : #Si le int est égale à 5 dans l'emplacement i de la liste alors :

                a_traduire[i] = 'Ivrogne' #On remplace le 5 par Ivrogne.

            elif a_traduire[i] == 6 : #Si le int est égale à 6 dans l'emplacement i de la liste alors :

                a_traduire[i] = 'Indécie' #On remplace le 6 par Indécie.

            elif a_traduire[i] == 7 : #Si le int est égale à 7 dans l'emplacement i de la liste alors :

                a_traduire[i] = 'Inspecteur' #On remplace le 7 par Inspecteur.

        return a_traduire #retourne la liste avec les noms traduit





def winner(point):

    a=0 #Variable qui contient le score le plus élevé.

    for i in range(len(point)): #On parcour la liste point et si on croise un score plus élevé on le garde en mémoire.

        if point[i] >= a : #Si le int à l'emplacement i dans la liste point est supérieur ou égale à a, a prendre cette élément en valeur.

            a = point[i] #a = l'élément à l'emplacement i dans la liste point.

        elif point[i] < a : #Si a est supérieur au score situé à l'emplacement i dans la liste point, alors on ne fait rien.

            None #permet de ne rien faire

    return a #retourne le score le plus élevé


def rendu(score,a,point,gagnant): #fonction qui renvoie l'affichage des score sous forme de graphe en png.

    nég = False #variable qui va savoir si un score est négatif.
    x = 0 #variable qui contiendra le score le plus grand.

    for c,v in score : #On parcour la liste k qui contient les nom et score :

        if v >=0 : #si un score est psoitif on ne fait rien.

            None #permet de ne rien faire.

        elif v<0: #si un score est négatif :

            nég = True #la variable booléenne devient True.


    for i in range(len(point)) : #on va regarder dans la liste point :
        if a == point[i] : #si a qui est le plus grand score est égale à un ou des scores dans la liste point.
            gagnant[i]=0.2 #on met 0.2 dans gagnant à l'endroit correspondant au gagnant de la simulation pour emttre leur part de camembert en évidence.
        else :#sinon on ne fait rien
            None #permet de ne rien faire


    if nég == True : #Si la variable est négative :

        width = 1.0 #Taille des barre.
        pyplot.bar(Liste, point, width ) #donne les x, y et taille des barres.
        pyplot.savefig('barre.png')#transforme le resultat en png.

    else :

        pyplot.figure(figsize = (16, 16))#donne la taille de la figure.

        pyplot.pie(point, labels = k, autopct = lambda x: str(round(x, 2)) + '%', explode = gagnant  ) #donne les pourcentages du camembert et le nom des pourcentages (les noms sont les nom des IA et leur scores).
        pyplot.savefig("camembert.png")#transforme le resultat en png.





def main(): #Fonction pour l'affichage des règles, du titre et des caractère décrti des IAs.
    print("""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Dilemme du prisonnier
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)

    print("""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                règles
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)

    print("""
            1 - Choisissez qu'elle IA vous voulez faire jouer.

                    Il y a 3 possibilitées lors d'un tour :

            2 - les 2 IA mette une pièce.

            3 - une IA met une piece et l'autre non.

            4 - les deux IA ne mette pas de pièce.

            5 - vous choisissez le nombre de tour que on fait jouer les IA.

            6 - vous choisissez le nombre de point que gagne ou perd un IA en fonction des 3 possibilitées listé ci-dessus.

            7 - si vous voulez qu'il perde des points mettez un chiffres négatif (exemple : -2).

            8 - Vous pouvez choisir 0 comme points gagné.

            """)


    print("""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                Les IAs
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)

    print("""
            1 - Tricheur (triche toujours et ne met jamais de pièce).

            2 - L'Enfant (met toujours une pièce).

            3 - Le coequipier (plus l'adversaire triche, moins il a confiance . A l'inverse moins l'adversaire triche, plus il a confiance
                               Si il a confiance il met une pièce sinon il triche).

            4 - Le copieur (Fait exactement ce que son adversaire à fait au tour précédent).

            5 - L'ivrogne (Choisis un coup de mettre la pièce puis triche puis en met une, etc).

            6 - L'indécie (Choisis de manière aléatoire ce qu'il fait).

            7 - L'inspecteur (joue, puis triche, puis joue, puis joue. Si l'adversaire n'a pas trop triché alors il jouera jsuqu'à la fin
                              Sinon il trichera jusqu'à la fin).

            """)





if __name__ == "__main__": #permet de lancer la fonction d'affichage.
    main()


rules_point=[]#Liste qui contient les points gagné et perdu, ainsi que le nombre de tour.
rules_point=rules()

triche=rules_point[0] #variable qui à le nombre de point gagné si la personne triche et gagne.

perd=rules_point[1] #variable qui à le nombre de point gagné si la personne joue et perd.

perd_egau=rules_point[2] #variable qui à le nombre de point gagné si les deux personne trichent.

joue=rules_point[3] #variable qui à le nombre de point gagné si les deux personne jouent.

tour=rules_point[4] #variable qui contient le nombre de tour.



choix_IAs()#créée le nombre d'IA et lesquels on fait jouer.


i = 1 #variable qui donnera le numéro de l'IA (en fonction de l'ordre dans lequel il a était rentré dans la liste : Liste).



for i in range(len(Liste)) : #Pour la longueur de la liste qui contient les IAs on va donner un nom à IA1 ce qui est utile pour l'affichage.

    IA1 = Liste[i] #IA1 est égale à l'emplacement i de la liste : Liste.
    nom=Trad(IA1) #permet de traduire les numéro de caractère des IA en leur nom (leur nom sont leur caractères).

#Affichage
    print(" ------------------------------------------------------------- ")
    print(f" C'est au tour de l'IA numéro {i+1} qui a comme caractère {nom} ")
    print(" ")
#Affichage




    for e in range(len(Liste)) : #Pour la longueur de la liste : Liste, on va donner un nom à IA2 ce qui est utile pour l'affichage.

        IA2 = Liste[e] #IA2 est égale à l'emplacement e de la liste : Liste.
        nom2 = Trad(IA2) #permet de traduire les numéro de caractère des IA en leur nom (leur nom sont leur caractères).

        if  i>=e : #Si i et e sont égaux on ne fait pas jouer la partis. Cela permet qu'une IA ne joue pas avec elle même quand on parcour la liste pour la deuxième fois.

            if i == e : #si c'est le même IA

                print("Ne joue pas contre lui même")
                print("-")

            elif i>e : #Si c'est un IA contre qui il à déjà joué

                print(f"A déjà jouer contre l'IA numéro {e+1}")
                print("-")

        else : #Sinon :


            points=game(tour,IA1,IA2,nom,nom2,i,e,joue,triche,perd,perd_egau) #On lance la partie entre les 2 IAs avec tous les arguments dont on abesoin pour les différents IAs et l'affichage.
            point[i] = point[i] + points[0] #On ajoute le score de l'IA1 à chaque fin de partie, à l'endroit qui correspond dans la liste des points.
            point[e] = point[e] + points[1] #On ajoute le score de l'IA2 à chaque fin de partie, à l'endroit qui correspond dans la liste des points.


Liste=Trad(Liste)#permet de traduire les numéro de caractère des IA en leur nom (leur nom sont leur caractères), et de les écrire dans la liste les contenants.
win=winner(point)#Va trouver qu'elle est le score le plus élevé.

k = list(zip(Liste,point)) #permet de prendre la liste contenant les noms et la liste contenant les scores et faire une liste de Tuples.
print(f"Voici les scores {k}") #affiche les scores.


for c,v in k : #On parcour la liste k qui contient les nom et score :

    if v == win : #si un score est égale au score le plus élevé :

        print(" ") #Affichage.
        print(f"le gagnant est un 'IA de caractère : {c}, avec {v} points") #Affiche le gagnant avec son numéro, son caractère et ses points.

        i = i + 1#ajoute 1 à la variable des scores.


    else : #Sinon :

        i = i + 1#ajoute 1 à la variable des scores.

rendu(k,win,point,gagnant) #Lance la fonction qui va faire le png de camembert ou le graphe des barres.
