from random import randrange
from math import ceil
import os

argent = 1000
continue_partie = True

print("Vous vous installez à la table de la roulette avec %s $" % argent)

while continue_partie:
	nb_mise = -1
	while nb_mise < 0 or nb_mise > 49:
		nb_mise = input("Saisissez le nombre sur lequel vous voulez misez entre 0 et 49 : ")
		try:
			nb_mise = int(nb_mise)
		except ValueError:
			print("Vous n'avez pas misé")
			nb_mise = -1
			continue
		if nb_mise < 0:
			print("Ce nombre est négatif")
		if nb_mise > 49:
			print("Ce nombre est supèrieur à 49")

	mise = 0
	while mise <= 0 or mise > argent:
		mise = input("Veuillez saisir le montant de votre mise : ")
		try:
			mise = int(mise)
		except ValueError:
			print("Vous n'avez pas misé")
			mise = -1
			continue
		if mise <= 0:
			print("Votre mise est négative")
		if mise > argent:
			print("Votre mise est supérieur à votre argent qui est de %s" % argent)



	numero_gagnant = randrange(50)
	print("La roulette tourne ........ Le numéro gagnant est %s" % numero_gagnant)
	if numero_gagnant == nb_mise:
		print("Félicitation !!! vous avez gagné %s $" % mise * 3)
		argent += mise * 3
	elif numero_gagnant % 2 == nb_mise % 2:
		print("Félicitation ! vous avez trouvé la bonne couleur, vous gagner %s $" % ceil(mise * 0.5))
		argent += ceil(mise * 0.5)
	else:
		print("Ah !!!! dommage c'est raté vous perdez votre mise de %s $" % mise)
		argent -= mise


	if argent <= 0:
		print("Pas de chance l'ami vous n'avez plus d'argent, je vous pris donc de quitter le casino")
		continue_partie = False
	else:
		print("Il vous reste %s $" % argent)
		rest_casino = input("Souhaitez vous continuer ? (o/n)")
		if rest_casino == "n" or rest_casino == "N":
			print("Très bien, vous partez avec %s $, à la prochaine!!" % argent)
			continue_partie = False


os.system("pause")

