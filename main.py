from functions import from_english_to_finnish, from_finnish_to_english
from data import word_pairs2, word_pairs3


def main():
    while True:
        print("\nEnglannin harjoittelua")
        print("Kummin päin haluat harjoitella?")
        print("Paina 1, jos haluat harjoitella suomesta englanniksi sanapareja 1")
        print("Paina 2, jos haluat harjoitella englannista suomeksi sanapareja 1")
        print("Paina 3, jos haluat harjoitella suomesta englanniksi sanapareja 2")
        print("Paina 4, jos haluat harjoitella englannista suomeksi sanapareja 2")
        print("Paina 5, jos haluat harjoitella suomesta englanniksi sanapareja 3")
        print("Paina 6, jos haluat harjoitella englannista suomeksi sanapareja 3")
        print("Paina mitä tahansa muuta näppäintä, jos haluat poistua ohjelmasta")
        answer = input("Syötä valintasi: ")
        print()

        if answer == "1":
            from_finnish_to_english()
        elif answer == "2":
            from_english_to_finnish()
        elif answer == "3":
            from_finnish_to_english(word_pair_list=word_pairs2)
        elif answer == "4":
            from_english_to_finnish(word_pair_list=word_pairs2)
        elif answer == "5":
            from_finnish_to_english(word_pair_list=word_pairs3)
        elif answer == "6":
            from_english_to_finnish(word_pair_list=word_pairs3)
        else:
            print("Kiitos ohjelman käytöstä!")
            break


main()




