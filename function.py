from data import word_pairs


# def from_finnish_to_english():
#     print("Käännä sanat englanniksi")
#     print("------------------------------", end="\n")
#     points = 0
#     for key, values in word_pairs.items():
#         count = 0
#         while count < len(values):
#             if count == len(values) - 1:
#                 answer = input(f"{values[count]}: ")
#                 if answer == key:
#                     points += 1
#                     print("Oikein!", end=" ")
#                 else:
#                     print("Väärin!", end=" ")

#                 print(f"Oikea vastaus: {key}")
#                 print()
#             else:
#                 print(values[count], end=", ")
#             count += 1
#     print()
#     print(f"Valmista tuli! Vastasit oikein {points}/{len(word_pairs)}")


# def from_english_to_finnish():
#     print("Käännä sanat suomeksi")
#     print("------------------------------", end="\n")
#     points = 0
#     for key, values in word_pairs.items():
#         answer = input(f"{key}: ")

#         corrects = [True if word in values else False for word in answer.split(", ")]

#         if False in corrects:
#             print("Väärin!", end=" ")
#         else:
#             points += 1
#             print("Oikein!", end=" ")

#         print("Oikea vastaus: ", end="")
#         count = 0
#         while count < len(values):
#             if count == len(values) - 1:
#                 print(values[count])
#             else:
#                 print(values[count], end=", ")
#             count += 1
#         print()
#     print(f"Valmista tuli! Vastasit oikein {points}/{len(word_pairs)}")


def from_finnish_to_english():
    print("Käännä sanat englanniksi")
    print("------------------------------", end="\n")
    points = 0
    for pairs in word_pairs:
        finnish_words = ""
        count = 0
        while count < len(pairs[1]):
            if count == len(pairs[1]) - 1:
                finnish_words += pairs[1][count]
            else:
                finnish_words += f"{pairs[1][count]}, "
            count += 1

        answer = input(f"{finnish_words}: ")

        corrects = [True if word in pairs[0] else False for word in answer.split(", ")]

        if False in corrects:
            print("Väärin!", end=" ")
        else:
            points += 1
            print("Oikein!", end=" ")

        print("Oikea vastaus: ", end="")
        count = 0
        while count < len(pairs[0]):
            if count == len(pairs[0]) - 1:
                print(pairs[0][count])
            else:
                print(pairs[0][count], end=", ")
            count += 1
        print()
    print(f"Valmista tuli! Vastasit oikein {points}/{len(word_pairs)}")


def from_english_to_finnish():
    print("Käännä sanat suomeksi")
    print("------------------------------", end="\n")
    points = 0
    for pairs in word_pairs:
        english_words = ""
        count = 0
        while count < len(pairs[0]):
            if count == len(pairs[0]) - 1:
                english_words += pairs[0][count]
            else:
                english_words += f"{pairs[0][count]}, "
            count += 1

        answer = input(f"{english_words}: ")

        corrects = [True if word in pairs[1] else False for word in answer.split(", ")]

        if False in corrects:
            print("Väärin!", end=" ")
        else:
            points += 1
            print("Oikein!", end=" ")

        print("Oikea vastaus: ", end="")
        count = 0
        while count < len(pairs[1]):
            if count == len(pairs[1]) - 1:
                print(pairs[1][count])
            else:
                print(pairs[1][count], end=", ")
            count += 1
        print()
    print(f"Valmista tuli! Vastasit oikein {points}/{len(word_pairs)}")