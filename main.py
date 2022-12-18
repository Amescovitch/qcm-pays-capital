import random
from liste_questions import questionnaire


def demander_valeur_numerique_user(mini, maxi):
    try:
        reponse = int((input(f"\nRÉPONSE(ENTRE {mini} ET {maxi}): ")))
        if mini <= reponse <= maxi:
            return reponse
        print(f"ERREUR: Réponse entre {mini} et {maxi}.")
    except ValueError:
        print(f"ERREUR: Réponse doit être un chiffre.")
    return demander_valeur_numerique_user(mini, maxi)


def poser_questions(question, num_question=1):
    titre_question = question[0]
    choix = question[1]
    bon_choix = question[2]
    # i = range in (0, len(questionnaire))
    print(f"QUESTION {num_question} sur {len(questionnaire)}:\n\tQuelle est la capitale {titre_question}")
    # i += 1
    for i in range(len(choix)):
        print(f"\t{i+1}-{choix[i]}")
    resultat_reponse_correcte = False
    reponse = demander_valeur_numerique_user(1, len(choix))
    if choix[reponse-1].lower() == bon_choix.lower():
        print("\t\t\tBonne réponse!")
        resultat_reponse_correcte = True
    else:
        print(f"\t\t\tMauvaise réponse!\n\t\t\tLa bonne réponse est: {bon_choix}")
    return resultat_reponse_correcte


def lancer_questionnaire(collection_questions):
    score = 0
    num_question = 1

    for question in collection_questions:
        if poser_questions(question, num_question):
            score += 1

        num_question += 1

    print(f"Votre score final est: {score} sur {len(collection_questions)}")


def main():

    print(f"""
---------------------------------------------------------------------------------------
|    -------------------------------------------------                                |
|    |  QCM SUR LES CAPITALES DES PAYS DE L'AFRIQUE  |                                |
|    -------------------------------------------------                                |
|    Montrez-nous que vous maîtrisez au mieux les capitales des pays africains !      |
|    Aller, c'est parti ..... pour une série de {len(questionnaire)} questions !                        |
|                                                                                     |
---------------------------------------------------------------------------------------
    """)
    # melanger la position
    # des questions
    random.shuffle(questionnaire)

    reprendre = True
    while reprendre:
        reprendre = False
        lancer_questionnaire(questionnaire)

        reprendre = True if input("\nReprendre le programme(o/n)?") == "o".lower() else False


main()

# if __name__ == "__main__":
#     main()
