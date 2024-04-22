import matplotlib.pyplot as plt

# Création des listes de valeurs pour Hn et Pn
liste_Hn = [200000 * 1.042**i for i in range(20)]
liste_Pn = [18216*(i+1) + 26.27658*((i*(i+1))/2) for i in range(20)]

# Création des listes pour les années et l'argent
liste_année = list(range(20))
liste_argent = [10000 * argent for argent in range(20)]

# Création du graphique
plt.plot(liste_année, liste_Hn, label="Hn")
plt.plot(liste_année, liste_Pn, label="Pn")
plt.legend(loc=0)
plt.xlabel('Années')
plt.ylabel('Argent')
plt.title('Comparaison entre Hn et Pn')
plt.grid(True)

# Affichage du graphique
plt.show()
