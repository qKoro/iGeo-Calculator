import sys
import time
from tqdm import tqdm
from colorama import *
import os


#        ||
#        ||
#variable\/

pi = 3.142

#        ||
#        ||
#fonction\/


def carreP(coteP1):
    aireC2 = coteP1 * 4
    print(Fore.RED + "Le périmetre du carre est de " + str(aireC2) + Style.RESET_ALL)

def rectangle(longueur1, largeur1):
    aireR2 = (longueur1 + largeur1) * 2
    print(Fore.RED + "Le périmetre du rectangle est de " + str(aireR2) + Style.RESET_ALL)

def losangeP(coteP2):
    aireL2 = coteP2 * 4
    print(Fore.RED + "Le périmetre du losange est de " + str(aireL2) + Style.RESET_ALL)

def TriangleP(coteT1, coteT2, coteT3):
    aireT2 = coteT1 + coteT2 + coteT3
    print(Fore.RED + "Le périmetre du triangle est de " + str(aireT2) + Style.RESET_ALL)

def cercleP(rayonP):
    aireCe2 = pi * (rayonP * 2)
    print(Fore.RED + "Le périmetre du cercle est de " + str(aireCe2) + Style.RESET_ALL)

def parallélogrammeP(base1, cote1):
    aireP2 = 2 * (base1 + cote1)
    print(Fore.RED + "Le périmetre du parallélogramme est de " + str(aireP2) + Style.RESET_ALL)

def trapèze(pBaseP, gBaseP, CoteP2, CoteP3):
    aireTra2 = pBaseP + gBaseP + CoteP2 + CoteP3
    print(Fore.RED + "Le périmetre du trapèze est de " + str(aireTra2) + Style.RESET_ALL)

#-------------------------------------------------------------------------------------------------------  

def carreA(coteA1):
    aireC1 = coteA1 * coteA1
    print(Fore.RED + "L'aire du carre est de " + str(aireC1) + Style.RESET_ALL)

def rectangleA(coteAR1, coteAR2):
    aireR = coteAR1 * coteAR2
    print(Fore.RED + "L'aire du rectangle est de " + str(aireR) + Style.RESET_ALL)

def losangeA(DiagoA1, DiagoA2):
    aireL = DiagoA1 * DiagoA2 / 2
    print(Fore.RED + "L'aire du losange est de " + str(aireL) + Style.RESET_ALL)

def TriangleA(baseA, hauterA):
    aireT = baseA * hauterA / 2
    print(Fore.RED + "L'aire du triangle est de " + str(aireT) + Style.RESET_ALL)

def cercleA(rayonA):
    aireC = pi * rayonA ** 2
    print(Fore.RED + "L'aire du cercle est de " + str(aireC) + Style.RESET_ALL)

def parallélogrammeA(BaseA, HauteurA):
    aireP = BaseA * HauteurA
    print(Fore.RED + "L'aire du parallélogramme est de " + str(aireP) + Style.RESET_ALL)

def trapèzeA(GbaseA, PbaseA, hauteurAt):
    aireTp = (GbaseA + PbaseA) * hauteurAt / 2
    print(Fore.RED + "L'aire du trapèze est de " + str(aireTp) + Style.RESET_ALL)

def cubeA(areteA):
    aireCu = 6 * areteA ** 2
    print(Fore.RED + "L'aire du cube est de " + str(aireCu) + Style.RESET_ALL)

def sphèreA(RayonA):
    aireS = 4 * pi * RayonA ** 2
    print(Fore.RED + "L'aire de la sphère est de " + str(aireS) + Style.RESET_ALL)

def cylindreA(RayonAc, hauteurAc):
    aireCy = 2 * pi * RayonAc * hauteurAc
    print(Fore.RED + "L'aire du cylindre est de " + str(aireCy) + Style.RESET_ALL)
# transformer la réponse en entier


def main():
    print(Fore.RED + """\n\n\n ▄████▓█████ ▒█████  
 ██▒ ▀█▓█   ▀▒██▒  ██▒
▒██░▄▄▄▒███  ▒██░  ██▒
░▓█  ██▒▓█  ▄▒██   ██░
░▒▓███▀░▒████░ ████▓▒░
 ░▒   ▒░░ ▒░ ░ ▒░▒░▒░ 
  ░   ░ ░ ░  ░ ░ ▒ ▒░ 
░ ░   ░   ░  ░ ░ ░ ▒  
      ░   ░  ░   ░ ░ """ + Style.RESET_ALL)
    ap = input("Voulez vous calculez le\npérimetre(1)\nl'aire(2) ?\nOu voulez vous quittez le proggrame(3)\n------------------------------------------------\n")
    ap = int(ap) 

    if ap == 1:
        print("Vous avez choisi de calculez le périmetre  ! ")
        time.sleep(1)
        fP = input("carré(1)\nrectangle(2)\ntriangle(3)\nparallélogramme(4)\nlosange(5)\ntrapèze(6)\ncercle(7)\nQuittez(8)\n------------------------------------------------\n")
        fP = int(fP)
        

        if fP == 1:
            print("Vous avez choisi de calculez le périmetre du carré !")
            coteP1 = input("quel est la longueur d'un des cotés du carré ?\n------------------------------------------------\n")
            coteP1 = float(coteP1)
            carreP(coteP1)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fP == 2:
            print("Vous avez choisi de calculez le périmetre du rectangle !")
            longueur1 = input("quel est la longueur du rectangle ?\n------------------------------------------------\n")
            longueur1 = float(longueur1)
            largeur1 = input("quel est la largeur du rectangle ?\n------------------------------------------------\n")
            largeur1 = float(largeur1)
            rectangle(longueur1, largeur1)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fP == 3:
            print("Vous avez choisi de calculez le périmetre du triangle !")
            coteT1 = input("quel est la longueur de la base du triangle ?\n------------------------------------------------\n")
            coteT1 = float(coteT1)
            coteT2 = input("quel est la longeur du 1er cote du triangle ?\n------------------------------------------------\n")
            coteT2 = float(coteT2)
            coteT3 = input("quel est la longeur du 2eme cote du triangle ?\n------------------------------------------------\n")
            coteT3 = float(coteT3)
            TriangleP(coteT1, coteT2, coteT3)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fP == 4:
            print("Vous avez choisi de calculez le périmetre du parallélogramme !")
            base1 = input("quel est la longueur de la base du parallélogramme ?\n------------------------------------------------\n")
            base1 = float(base1)
            cote1 = input("quel est la longeur d'une diagonale du parallélogramme ?\n------------------------------------------------\n")
            cote1 = float(cote1)
            parallélogrammeP(base1, cote1)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fP == 5:
            print("Vous avez choisi de calculez le périmetre du losange !")
            coteP2 = input("quel est la longueur d'un des cote du losange ?\n------------------------------------------------\n")
            coteP2 = float(coteP2)
            losangeP(coteP2)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fP == 6:
            print("Vous avez choisi de calculez le périmetre du trapèze !")
            gBaseP = input("quel est la longueur de la Grande base du trapèze ?\n------------------------------------------------\n")
            gBaseP = float(gBaseP)
            pBaseP = input("quel est la longueur de la Petite base du trapèze ?\n------------------------------------------------\n")
            pBaseP = float(pBaseP)
            CoteP2 = input("quel est la longeur du 1er cote du trapèze ?\n------------------------------------------------\n")
            CoteP2 = float(CoteP2)
            CoteP3 = input("quel est la longeur du 2eme cote du trapèze ?\n------------------------------------------------\n")
            CoteP3 = float(CoteP3)
            trapèze(pBaseP, gBaseP, CoteP2, CoteP3)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fP == 7:
            print("Vous avez choisi de calculez le périmetre du cercle !")
            rayonP = input("quel est le rayon du cercle ?\n------------------------------------------------\n")
            rayonP = float(rayonP)
            cercleP(rayonP)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()

        elif fP == 8:
            print("3\n")
            time.sleep(1)
            print("2\n")
            time.sleep(1)
            print("1\n")
            time.sleep(1)
            print("Goodbye had a good day\n ")
            time.sleep(3)
            os.system('cls')
            sys.exit()
        else :
            print("Vous ne pouvez entrez un nombre supérieur à 8 !")
            time.sleep(0.5)
            print("Redirection aux menu principal")
            for i in tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]):
                time.sleep(0.02)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            os.system('cls')
            main()


    elif ap == 2:
        print("Vous avez choisi de calculez l'aire  ! ")
        time.sleep(1)
        fA = input("carré(1)\nrectangle(2)\ntriangle(3)\nparallélogramme(4)\nlosange(5)\ntrapèze(6)\ncercle(7)\ncube(8)\nsphère(9)\ncylindre(10)\nQuittez(11)\n------------------------------------------------\n")
        fA = int(fA)

        if fA == 1:
            print("Vous avez choisi de calculez l'aire du carré !")
            coteA1 = input("quel est la longueur d'un des cotés du carré ?\n------------------------------------------------\n")
            coteA1 = float(coteA1)
            carreA(coteA1)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fA == 2:
            print("Vous avez choisi de calculez l'aire du rectangle !")
            coteAR1 = input("quel est la longueur du rectangle ?\n------------------------------------------------\n")
            coteAR1 = float(coteAR1)
            coteAR2 = input("quel est la largeur du rectangle ?\n------------------------------------------------\n")
            coteAR2 = float(coteAR2)
            rectangleA(coteAR1, coteAR2)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fA == 3:
            print("Vous avez choisi de calculez l'aire du triangle !")
            baseA = input("quel est la longueur de la base du triangle ?\n------------------------------------------------\n")
            baseA = float(baseA)
            hauterA = input("quel est la hauteur du triangle ?\n------------------------------------------------\n")
            hauterA = float(hauterA)
            TriangleA(baseA, hauterA)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fA == 4:
            print("Vous avez choisi de calculez l'aire du parallélogramme !")
            BaseA = input("quel est la longueur de la base du parallélogramme ?\n------------------------------------------------\n")
            BaseA = float(BaseA)
            HauteurA = input("quel est la hauteur du parallélogramme ?\n------------------------------------------------\n")
            HauteurA = float(HauteurA)
            parallélogrammeA(BaseA, HauteurA)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fA == 5:
            print("Vous avez choisi de calculez l'aire du losange !")
            DiagoA1 = input("quel est la longueur de la Grande Diagonale du losange ?\n------------------------------------------------\n")
            DiagoA1 = float(DiagoA1)
            DiagoA2 = input("quel est la longueur de la Petite Diagonale du losange ?\n------------------------------------------------\n")
            DiagoA2 = float(DiagoA2)
            losangeA(DiagoA1, DiagoA2)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fA == 6:
            print("Vous avez choisi de calculez l'aire du trapèze !")
            GbaseA = input("quel est la longueur de la Grande base du trapèze ?\n------------------------------------------------\n")
            GbaseA = float(GbaseA)
            PbaseA = input("quel est la longueur de la Petite base du trapèze ?\n------------------------------------------------\n")
            PbaseA = float(PbaseA)
            hauteurAt = input("quel est la hauteur du trapèze ?\n------------------------------------------------\n")
            hauteurAt = float(hauteurAt)
            trapèzeA(GbaseA, PbaseA, hauteurAt)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fA == 7:
            print("Vous avez choisi de calculez l'aire du cercle !")
            rayonA = input("quel est le rayon du cercle ?\n------------------------------------------------\n")
            rayonA = float(rayonA)
            cercleA(rayonA)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fA == 8:
            print("Vous avez choisi de calculez l'aire du cube !")
            areteA = input("quel est la taille de l'Arête du cube ?\n------------------------------------------------\n")
            areteA = float(areteA)
            cubeA(areteA)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fA == 9:
            print("Vous avez choisi de calculez l'aire du sphère !")
            RayonA = input("quel est le rayon de la sphère ?\n------------------------------------------------\n")
            RayonA = float(RayonA)
            sphèreA(RayonA)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fA == 10:
            print("Vous avez choisi de calculez l'aire du cylindre !")
            RayonAc = input("quel est le rayon de la cylindre ?\n------------------------------------------------\n")
            RayonAc = float(RayonAc)
            hauteurAc = input("quel est la hauteur du cylindre ?\n------------------------------------------------\n")
            hauteurAc = float(hauteurAc)
            cylindreA(RayonAc, hauteurAc)
            print("------------------------------------------------\n")
            time.sleep(3)
            os.system('cls')
            main()
            
        elif fA == 11:
            print("3\n")
            time.sleep(1)
            print("2\n")
            time.sleep(1)
            print("1\n")
            time.sleep(1)
            print("Goodbye had a good day\n ")
            time.sleep(3)
            sys.exit()
        else :
            print("Vous ne pouvez entrez un nombre supérieur à 11 !")
            time.sleep(0.5)
            print("Redirection aux menu principal")
            for i in tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]):
                time.sleep(0.02)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            os.system('cls')
            main()
    elif ap == 3:
        print("------------------------------------------------\n3\n")
        time.sleep(1)
        print("2\n")
        time.sleep(1)
        print("1\n")
        time.sleep(1)
        print("I hope we will meet again very soon\n ")
        time.sleep(3)
        sys.exit()
    else : 
        print(" Vous ne pouvez que choisir de calculez l'aire ou le périmetre !")
        print("Redirection aux menu principal")
        for i in tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]):
            time.sleep(0.02)
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        os.system('cls')
        main()


print("\n---------------------")
main()