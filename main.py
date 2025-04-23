from functions import from_english_to_finnish, from_finnish_to_english


def main():
    while True:
        print("\nEnglannin harjoittelua")
        print("Kummin päin haluat harjoitella?")
        print("Paina 1, jos haluat harjoitella suomesta englanniksi")
        print("Paina 2, jos haluat harjoitella englannista suomeksi")
        print("Paina mitä tahansa muuta näppäintä, jos haluat poistua ohjelmasta")
        answer = input("Syötä valintasi: ")
        print()

        if answer == "1":
            from_finnish_to_english()
        elif answer == "2":
            from_english_to_finnish()
        else:
            print("Kiitos ohjelman käytöstä!")
            break


main()




