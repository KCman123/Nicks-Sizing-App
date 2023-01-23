import json
from email.message import EmailMessage
import ssl
import smtplib

# open json file
with open('ClothingSpecs.json') as f:
    # Loads json file into cs
    cs = json.load(f)

# Body Measurements
feet = 0
inches = 0.0
weight = 0.0

# Jacket Measurements
chest = 0.0
coat_waist = 0.0

# Pant Measurements
waist = 0.0
seat = 0.0

# Shirt Measurements
neck = 0.0
sleeve = 0.0

suit_color = ""
jacketFit = ""


def find_jacket_length(feet, inches):
    jacket_length = ""

    if feet <= 4:
        jacket_length = "S"
    elif feet == 5 and inches <= 10:
        jacket_length = "S"
    elif feet == 5 and inches > 10:
        jacket_length = "R"
    elif feet == 6 and inches <= 1:
        jacket_length = "R"
    elif feet == 6 and 2 <= inches < 7:
        jacket_length = "L"
    elif feet == 6 and inches >= 7:
        jacket_length = "XL"
    elif feet == 7:
        jacket_length = "XL"
    else:
        print("Height is out of range")

    return jacket_length


# Finds Jacket size and fit
def find_jacket_size_and_fit(chest, coat_waist, chest_input, suit_color):
    jacketSize = 0
    low_coat_waist = 0.0
    high_coat_waist = 0.0
    low_chest = 0.0
    high_chest = 0.0
    jacket_fit = ""
    suit_color_temp = suit_color

    cassual_array = [40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62]
    euro_array = [34, 36, 38, 40, 42, 44, 46, 48, 50, 52]

    # looks for slim fit suits only
    if suit_color_temp == "Midnight Blue":

        for val in cs.items():
            for temp_jacket_size_array in val[1]:
                for temp_jacket_size_category, temp_jacket_size_score_array in temp_jacket_size_array.items():
                    if temp_jacket_size_category == "Size":
                        if chest == temp_jacket_size_score_array:

                            # sets the fitment parameter for coat waist
                            low_coat_waist = temp_jacket_size_array["Coat Waist"] - 8
                            high_coat_waist = temp_jacket_size_array["Coat Waist"] - 2

                            if low_coat_waist <= coat_waist <= high_coat_waist:

                                # jacket is a match
                                jacketSize = chest
                                jacket_fit = "Slim"
                                return jacketSize, jacket_fit

                            # Coat waist is smaller than the jacket
                            elif low_coat_waist > coat_waist:

                                small_chest = chest - 2

                                for val2 in cs.items():
                                    for temp_jacket_size_array2 in val2[1]:
                                        for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                            if temp_jacket_size_category2 == "Size":
                                                if small_chest == temp_jacket_size_score_array2:

                                                    high_chest = small_chest + 2

                                                    if chest_input < high_chest:
                                                        jacketSize = small_chest
                                                        jacket_fit = "Slim"
                                                        return jacketSize, jacket_fit
                                                    else:
                                                        jacketSize = small_chest + 2
                                                        jacket_fit = "Slim"
                                                        return jacketSize, jacket_fit
                                return jacketSize, jacket_fit

                            # coat Waist is larger than the jacket
                            elif coat_waist > high_coat_waist:

                                fit_status = False
                                big_chest = chest + 2

                                while fit_status == False:
                                    for val2 in cs.items():
                                        for temp_jacket_size_array2 in val2[1]:
                                            for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                if temp_jacket_size_category2 == "Size":
                                                    if big_chest == temp_jacket_size_score_array2:

                                                        high_coat_waist = temp_jacket_size_array2["Coat Waist"] - 2

                                                        if coat_waist <= high_coat_waist:
                                                            jacketSize = big_chest
                                                            fit_status = True
                                                            jacket_fit = "Slim"
                                                            return jacketSize, jacket_fit
                                                        else:
                                                            big_chest += 2
                                                            jacket_fit = "Slim"

                                return jacketSize, jacket_fit

    # looks for slim fit suits only
    if suit_color_temp == "Nicks Blue":

        for val in cs.items():
            for temp_jacket_size_array in val[1]:
                for temp_jacket_size_category, temp_jacket_size_score_array in temp_jacket_size_array.items():
                    if temp_jacket_size_category == "Size":
                        if chest == temp_jacket_size_score_array:

                            # sets the fitment parameter for coat waist
                            low_coat_waist = temp_jacket_size_array["Coat Waist"] - 8
                            high_coat_waist = temp_jacket_size_array["Coat Waist"] - 2

                            if low_coat_waist <= coat_waist <= high_coat_waist:

                                # jacket is a match
                                jacketSize = chest
                                jacket_fit = "Slim"
                                return jacketSize, jacket_fit

                            # Coat waist is smaller than the jacket
                            elif low_coat_waist > coat_waist:

                                small_chest = chest - 2

                                for val2 in cs.items():
                                    for temp_jacket_size_array2 in val[1]:
                                        for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                            if temp_jacket_size_category2 == "Size":
                                                if small_chest == temp_jacket_size_score_array2:

                                                    high_chest = small_chest + 2

                                                    if chest_input < high_chest:
                                                        jacketSize = small_chest
                                                        jacket_fit = "Slim"
                                                        return jacketSize, jacket_fit
                                                    else:
                                                        jacketSize = small_chest + 2
                                                        jacket_fit = "Slim"
                                                        return jacketSize, jacket_fit
                                return jacketSize, jacket_fit

                            # coat Waist is larger than the jacket
                            elif coat_waist > high_coat_waist:

                                fit_status = False
                                big_chest = chest + 2

                                while fit_status == False:
                                    for val2 in cs.items():
                                        for temp_jacket_size_array2 in val2[1]:
                                            for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                if temp_jacket_size_category2 == "Size":
                                                    if big_chest == temp_jacket_size_score_array2:

                                                        high_coat_waist = temp_jacket_size_array2["Coat Waist"] - 2

                                                        if coat_waist <= high_coat_waist:
                                                            jacketSize = big_chest
                                                            fit_status = True
                                                            jacket_fit = "Slim"
                                                            return jacketSize, jacket_fit
                                                        else:
                                                            big_chest += 2
                                                            jacket_fit = "SLIM"
                                return jacketSize, jacket_fit

    # looks for slim fit options then casual fit
    if suit_color_temp == "Light Grey":

        for val in cs.items():
            for temp_jacket_size_array in val[1]:
                for temp_jacket_size_category, temp_jacket_size_score_array in temp_jacket_size_array.items():
                    if temp_jacket_size_category == "Size":
                        if chest == temp_jacket_size_score_array:

                            low_coat_waist = temp_jacket_size_array["Coat Waist"] - 8
                            high_coat_waist = temp_jacket_size_array["Coat Waist"] - 2

                            if low_coat_waist <= coat_waist <= high_coat_waist:

                                # jacket is a match
                                jacketSize = chest
                                jacket_fit = "Slim"
                                return jacketSize, jacket_fit

                            # Coat waist is smaller than the jacket
                            elif low_coat_waist > coat_waist:

                                small_chest = chest - 2

                                for val2 in cs.items():
                                    for temp_jacket_size_array2 in val2[1]:
                                        for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                            if temp_jacket_size_category2 == "Size":
                                                if small_chest == temp_jacket_size_score_array2:

                                                    high_chest = small_chest + 2

                                                    if chest_input < high_chest:
                                                        jacketSize = small_chest
                                                        jacket_fit = "Slim"
                                                        return jacketSize, jacket_fit
                                                    else:
                                                        jacketSize = small_chest + 2
                                                        jacket_fit = "Slim"
                                                        return jacketSize, jacket_fit
                                return jacketSize, jacket_fit

                            # coat Waist is larger than the jacket
                            elif coat_waist > high_coat_waist:

                                fit_status = False

                                big_chest = chest

                                while fit_status == False:

                                    if big_chest in cassual_array:

                                        for val2 in cs.items():
                                            if val2[0] == "Jacket_size_Casual":
                                                for temp_jacket_size_array2 in val2[1]:
                                                    for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                        if temp_jacket_size_category2 == "Size":
                                                            if big_chest == temp_jacket_size_score_array2:

                                                                high_coat_waist = temp_jacket_size_array2[
                                                                                      "Coat Waist"] - 2

                                                                if coat_waist <= high_coat_waist:
                                                                    # jacket is a match
                                                                    jacketSize = big_chest
                                                                    jacket_fit = "Casual"
                                                                    fit_status = True
                                                                    return jacketSize, jacket_fit

                                                                else:

                                                                    big_chest = chest + 2

                                                                    for val3 in cs.items():
                                                                        for temp_jacket_size_array3 in val3[1]:
                                                                            for temp_jacket_size_category3, temp_jacket_size_score_array3 in temp_jacket_size_array3.items():
                                                                                if temp_jacket_size_category3 == "Size":
                                                                                    if big_chest == temp_jacket_size_score_array3:

                                                                                        if coat_waist <= high_coat_waist:
                                                                                            # jacket is a match
                                                                                            jacketSize = big_chest
                                                                                            jacket_fit = "Slim"
                                                                                            fit_status = True
                                                                                            return jacketSize, jacket_fit

                                                                                        else:
                                                                                            big_chest += 2
                                                                                            fit_status = False

                                    else:
                                        for val2 in cs.items():
                                            for temp_jacket_size_array2 in val[1]:
                                                for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                    if temp_jacket_size_category2 == "Size":
                                                        if big_chest == temp_jacket_size_score_array2:

                                                            high_coat_waist = temp_jacket_size_array2["Coat Waist"] - 2

                                                            if coat_waist <= high_coat_waist:
                                                                # jacket is a match
                                                                jacketSize = chest
                                                                jacket_fit = "Slim"
                                                                fit_status = True
                                                                return jacketSize, jacket_fit

                                                            else:
                                                                fit_status = False

    # looks for euro, slim and casual options
    if suit_color_temp == "Charcoal":

        high_chest = 0

        for val in cs.items():
            for temp_jacket_size_array in val[1]:
                for temp_jacket_size_category, temp_jacket_size_score_array in temp_jacket_size_array.items():
                    if temp_jacket_size_category == "Size":
                        if chest == temp_jacket_size_score_array:

                            low_coat_waist = temp_jacket_size_array["Coat Waist"] - 8
                            high_coat_waist = temp_jacket_size_array["Coat Waist"] - 2

                            if low_coat_waist <= coat_waist <= high_coat_waist:

                                # jacket is a match
                                jacketSize = chest
                                jacket_fit = "Slim"
                                return jacketSize, jacket_fit

                            elif low_coat_waist > coat_waist:

                                if chest in euro_array:

                                    for val2 in cs.items():
                                        if val2[0] == "Jacket_size_Euro":
                                            for temp_jacket_size_array2 in val2[1]:
                                                for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                    if temp_jacket_size_category2 == "Size":
                                                        if chest == temp_jacket_size_score_array2:

                                                            high_coat_waist = temp_jacket_size_array2["Coat Waist"] - 2

                                                            if coat_waist <= high_coat_waist:

                                                                # jacket is a match
                                                                jacketSize = chest
                                                                jacket_fit = "Euro"
                                                                return jacketSize, jacket_fit

                                                            else:

                                                                small_chest = chest - 2

                                                                for val3 in cs.items():
                                                                    for temp_jacket_size_array3 in val3[1]:
                                                                        for temp_jacket_size_category3, temp_jacket_size_score_array3 in temp_jacket_size_array3.items():
                                                                            if temp_jacket_size_category3 == "Size":
                                                                                if small_chest == temp_jacket_size_score_array3:

                                                                                    high_chest = \
                                                                                        temp_jacket_size_array3[
                                                                                            "Size"] + 2

                                                                                    if chest_input <= high_chest:
                                                                                        # jacket is a match
                                                                                        jacketSize = small_chest
                                                                                        jacket_fit = "Slim"
                                                                                        return jacketSize, jacket_fit

                                                                                    else:
                                                                                        jacketSize = chest
                                                                                        jacket_fit = "Slim"
                                                                                        return jacketSize, jacket_fit
                                else:

                                    small_chest = chest - 2

                                    for val2 in cs.items():
                                        for temp_jacket_size_array2 in val2[1]:
                                            for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                if temp_jacket_size_category2 == "Size":
                                                    if small_chest == temp_jacket_size_score_array2:

                                                        high_chest = temp_jacket_size_array2["Size"] + 2

                                                        if chest_input <= high_chest:
                                                            # jacket is a match
                                                            jacketSize = small_chest
                                                            jacket_fit = "Slim"
                                                            return jacketSize, jacket_fit

                                                        else:
                                                            jacketSize = chest
                                                            jacket_fit = "Slim"
                                                            return jacketSize, jacket_fit

                            elif coat_waist > high_coat_waist:

                                fit_status = False

                                big_chest = chest

                                while fit_status == False:

                                    if big_chest in cassual_array:

                                        for val2 in cs.items():
                                            if val2[0] == "Jacket_size_Casual":
                                                for temp_jacket_size_array2 in val2[1]:
                                                    for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                        if temp_jacket_size_category2 == "Size":
                                                            if big_chest == temp_jacket_size_score_array2:

                                                                high_coat_waist = temp_jacket_size_array2[
                                                                                      "Coat Waist"] - 2

                                                                if coat_waist <= high_coat_waist:
                                                                    # jacket is a match
                                                                    jacketSize = big_chest
                                                                    jacket_fit = "Casual"
                                                                    fit_status = True
                                                                    return jacketSize, jacket_fit

                                                                else:

                                                                    big_chest = chest + 2

                                                                    for val3 in cs.items():
                                                                        for temp_jacket_size_array3 in val3[1]:
                                                                            for temp_jacket_size_category3, temp_jacket_size_score_array3 in temp_jacket_size_array3.items():
                                                                                if temp_jacket_size_category3 == "Size":
                                                                                    if big_chest == temp_jacket_size_score_array3:

                                                                                        if coat_waist <= high_coat_waist:
                                                                                            # jacket is a match
                                                                                            jacketSize = big_chest
                                                                                            jacket_fit = "Slim"
                                                                                            fit_status = True
                                                                                            return jacketSize, jacket_fit

                                                                                        else:
                                                                                            big_chest += 2
                                                                                            fit_status = False

                                    else:

                                        big_chest = chest + 2

                                        for val2 in cs.items():
                                            for temp_jacket_size_array2 in val2[1]:
                                                for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                    if temp_jacket_size_category2 == "Size":
                                                        if big_chest == temp_jacket_size_score_array2:

                                                            high_coat_waist = temp_jacket_size_array2["Coat Waist"] - 2

                                                            if coat_waist <= high_coat_waist:
                                                                # jacket is a match
                                                                jacketSize = chest
                                                                jacket_fit = "Slim"
                                                                fit_status = True
                                                                return jacketSize, jacket_fit

                                                            else:
                                                                big_chest += 2
                                                                fit_status = False

    # looks for euro, slim and casual options
    if suit_color_temp == "Black":

        high_chest = 0

        for val in cs.items():
            for temp_jacket_size_array in val[1]:
                for temp_jacket_size_category, temp_jacket_size_score_array in temp_jacket_size_array.items():
                    if temp_jacket_size_category == "Size":
                        if chest == temp_jacket_size_score_array:

                            low_coat_waist = temp_jacket_size_array["Coat Waist"] - 8
                            high_coat_waist = temp_jacket_size_array["Coat Waist"] - 2

                            if low_coat_waist <= coat_waist <= high_coat_waist:

                                # jacket is a match
                                jacketSize = chest
                                jacket_fit = "Slim"
                                return jacketSize, jacket_fit

                            elif low_coat_waist > coat_waist:

                                if chest in euro_array:

                                    for val2 in cs.items():
                                        if val2[0] == "Jacket_size_Euro":
                                            for temp_jacket_size_array2 in val2[1]:
                                                for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                    if temp_jacket_size_category2 == "Size":
                                                        if chest == temp_jacket_size_score_array2:

                                                            high_coat_waist = temp_jacket_size_array2["Coat Waist"] - 2

                                                            if coat_waist <= high_coat_waist:

                                                                # jacket is a match
                                                                jacketSize = chest
                                                                jacket_fit = "Euro"
                                                                return jacketSize, jacket_fit

                                                            else:

                                                                small_chest = chest - 2

                                                                for val3 in cs.items():
                                                                    for temp_jacket_size_array3 in val3[1]:
                                                                        for temp_jacket_size_category3, temp_jacket_size_score_array3 in temp_jacket_size_array3.items():
                                                                            if temp_jacket_size_category3 == "Size":
                                                                                if small_chest == temp_jacket_size_score_array3:

                                                                                    high_chest = \
                                                                                        temp_jacket_size_array3[
                                                                                            "Size"] + 2

                                                                                    if chest_input <= high_chest:
                                                                                        # jacket is a match
                                                                                        jacketSize = small_chest
                                                                                        jacket_fit = "Slim"
                                                                                        return jacketSize, jacket_fit

                                                                                    else:
                                                                                        jacketSize = chest
                                                                                        jacket_fit = "Slim"
                                                                                        return jacketSize, jacket_fit
                                else:

                                    small_chest = chest - 2

                                    for val2 in cs.items():
                                        for temp_jacket_size_array2 in val2[1]:
                                            for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                if temp_jacket_size_category2 == "Size":
                                                    if small_chest == temp_jacket_size_score_array2:

                                                        high_chest = temp_jacket_size_array2["Size"] + 2

                                                        if chest_input <= high_chest:
                                                            # jacket is a match
                                                            jacketSize = small_chest
                                                            jacket_fit = "Slim"
                                                            return jacketSize, jacket_fit

                                                        else:
                                                            jacketSize = chest
                                                            jacket_fit = "Slim"
                                                            return jacketSize, jacket_fit

                            elif coat_waist > high_coat_waist:

                                fit_status = False

                                big_chest = chest

                                while fit_status == False:

                                    if big_chest in cassual_array:

                                        for val2 in cs.items():
                                            if val2[0] == "Jacket_size_Casual":
                                                for temp_jacket_size_array2 in val2[1]:
                                                    for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                        if temp_jacket_size_category2 == "Size":
                                                            if big_chest == temp_jacket_size_score_array2:

                                                                high_coat_waist = temp_jacket_size_array2[
                                                                                      "Coat Waist"] - 2

                                                                if coat_waist <= high_coat_waist:
                                                                    # jacket is a match
                                                                    jacketSize = big_chest
                                                                    jacket_fit = "Casual"
                                                                    fit_status = True
                                                                    return jacketSize, jacket_fit

                                                                else:

                                                                    big_chest = chest + 2

                                                                    for val3 in cs.items():
                                                                        for temp_jacket_size_array3 in val3[1]:
                                                                            for temp_jacket_size_category3, temp_jacket_size_score_array3 in temp_jacket_size_array3.items():
                                                                                if temp_jacket_size_category3 == "Size":
                                                                                    if big_chest == temp_jacket_size_score_array3:

                                                                                        if coat_waist <= high_coat_waist:
                                                                                            # jacket is a match
                                                                                            jacketSize = big_chest
                                                                                            jacket_fit = "Slim"
                                                                                            fit_status = True
                                                                                            return jacketSize, jacket_fit

                                                                                        else:
                                                                                            big_chest += 2
                                                                                            fit_status = False

                                    else:

                                        big_chest = chest + 2

                                        for val2 in cs.items():
                                            for temp_jacket_size_array2 in val2[1]:
                                                for temp_jacket_size_category2, temp_jacket_size_score_array2 in temp_jacket_size_array2.items():
                                                    if temp_jacket_size_category2 == "Size":
                                                        if big_chest == temp_jacket_size_score_array2:

                                                            high_coat_waist = temp_jacket_size_array2["Coat Waist"] - 2

                                                            if coat_waist <= high_coat_waist:
                                                                # jacket is a match
                                                                jacketSize = chest
                                                                jacket_fit = "Slim"
                                                                fit_status = True
                                                                return jacketSize, jacket_fit

                                                            else:
                                                                fit_status = False

    # suit color not selected
    else:
        print("Select a suit color")


# Finds Pant size and fit
def find_pant_size_and_fit(jacketSize2, jacketFit, waist, seat):
    pantStartSize = int(jacketSize2) - 6
    pantSize = 0

    if jacketFit == "Slim":
        pantFit = "Pant_Size_Slim"
    if jacketFit == "Casual":
        pantFit = "Pant_Size_Casual"
    if jacketFit == "Euro":
        pantFit = "Pant_Size_Euro"

    for val in cs.items():
        if val[0] == pantFit:
            for temp_pant_size_array in val[1]:
                for temp_pant_size_category, temp_pant_size_score_array in temp_pant_size_array.items():
                    if temp_pant_size_category == "Size":
                        if waist == temp_pant_size_score_array:

                            low_seat = temp_pant_size_array["Seat"] - 5
                            high_seat = temp_pant_size_array["Seat"] + 2

                            if low_seat <= seat <= high_seat:
                                pantSize = waist
                                return pantSize
                            if low_seat > seat:
                                pantSize = waist - 2
                                return pantSize
                            if high_seat < seat:

                                doPantsFit = False

                                while doPantsFit is False:

                                    waist += 2

                                    for val2 in cs.items():
                                        if val2[0] == pantFit:
                                            for temp_pant_size_array2 in val2[1]:
                                                for temp_pant_size_category2, temp_pant_size_score_array2 in temp_pant_size_array2.items():
                                                    if temp_pant_size_category2 == "Size":
                                                        if waist == temp_pant_size_score_array2:

                                                            high_seat = temp_pant_size_array2["Seat"] + 2

                                                            if seat <= high_seat:
                                                                pantSize = waist
                                                                doPantsFit = True
                                                                return pantSize

                                                            if high_seat < seat:
                                                                waist += 2
                                                                doPantsFit = False


# Checks to see if it is ok to split the pants
def is_it_ok_to_split(firstPantSize, jacketSize2, seat, jacketFit):
    pantStartSize = int(jacketSize2) - 6
    finalPantSize = 0

    if jacketFit == "Slim":
        pantFit = "Pant_Size_Slim"
    if jacketFit == "Casual":
        pantFit = "Pant_Size_Casual"
    if jacketFit == "Euro":
        pantFit = "Pant_Size_Euro"

    okToSplitLow = pantStartSize - 4
    okToSplitBig = pantStartSize + 4

    if int(firstPantSize) == pantStartSize:
        finalPantSize = firstPantSize
        return finalPantSize
    if int(firstPantSize) == pantStartSize - 2:
        finalPantSize = pantStartSize
        return finalPantSize
    if int(firstPantSize) <= okToSplitLow:
        finalPantSize = firstPantSize
        return finalPantSize
    if int(firstPantSize) >= okToSplitBig:
        finalPantSize = firstPantSize
        return finalPantSize
    if int(firstPantSize) > pantStartSize:
        for val in cs.items():
            if val[0] == pantFit:
                for temp_pant_size_array in val[1]:
                    for temp_pant_size_category, temp_pant_size_score_array in temp_pant_size_array.items():
                        if temp_pant_size_category == "Size":
                            if pantStartSize == temp_pant_size_score_array:

                                high_seat = temp_pant_size_array["Seat"] + 2

                                if seat <= high_seat:
                                    finalPantSize = pantStartSize
                                    return finalPantSize
                                else:
                                    finalPantSize = firstPantSize
                                    return finalPantSize

        return finalPantSize


# finds shirt size
def find_shirt_size(neck, chest, coat_waist):
    shirtScore = neck + sleeve + chest + coat_waist
    sleeve_length = 0
    shirt_size = 0

    for val in cs.items():
        if val[0] == "Shirt_Size":
            for temp_shirt_size_array in val[1]:
                for temp_shirt_size_category, temp_shirt_size_score_array in temp_shirt_size_array.items():
                    if temp_shirt_size_category == "Neck":
                        if neck == temp_shirt_size_score_array:

                            low_chest = temp_shirt_size_array["Chest"] - 8
                            high_chest = temp_shirt_size_array["Chest"] - 2

                            low_coat_waist = temp_shirt_size_array["Coat Waist"] - 8
                            high_coat_waist = temp_shirt_size_array["Coat Waist"] - 2

                            # Check for chest fit
                            if chest <= high_chest:
                                if low_coat_waist <= coat_waist <= high_coat_waist:
                                    shirt_size = neck
                                    return shirt_size

                                if low_coat_waist > coat_waist:
                                    shirt_size = neck
                                    return shirt_size

                                if high_coat_waist < coat_waist:
                                    shirt_fit = False
                                    while shirt_fit == False:
                                        big_neck = neck + .5
                                        for val2 in cs.items():
                                            if val2[0] == "Shirt_Size":
                                                for temp_shirt_size_array2 in val2[1]:
                                                    for temp_shirt_size_category2, temp_shirt_size_score_array2 in temp_shirt_size_array2.items():
                                                        if temp_shirt_size_category2 == "Neck":
                                                            if big_neck == temp_shirt_size_score_array2:

                                                                high_coat_waist = temp_shirt_size_array2[
                                                                                      "Coat Waist"] - 2

                                                                if coat_waist <= high_coat_waist:
                                                                    shirt_size = big_neck
                                                                    shirt_fit = True
                                                                    return shirt_size
                                                                else:
                                                                    big_neck += .5
                                                                    shirt_fit = False
                                                                    break

                            if low_chest > chest:
                                shirt_size = neck
                                return shirt_size

                            if high_chest < chest:
                                shirt_fit = False
                                while shirt_fit == False:
                                    new_neck = neck + .5
                                    for val2 in cs.items():
                                        if val2[0] == "Shirt_Size":
                                            for temp_shirt_size_array2 in val2[1]:
                                                for temp_shirt_size_category2, temp_shirt_size_score_array2 in temp_shirt_size_array2.items():
                                                    if temp_shirt_size_category2 == "Neck":
                                                        if new_neck == temp_shirt_size_score_array2:

                                                            low_chest = temp_shirt_size_array2["Chest"] - 8
                                                            high_chest = temp_shirt_size_array2["Chest"] - 2

                                                            low_coat_waist = temp_shirt_size_array2["Coat Waist"] - 8
                                                            high_coat_waist = temp_shirt_size_array2["Coat Waist"] - 2

                                                            if low_chest <= chest <= high_chest:
                                                                if low_coat_waist <= coat_waist <= high_coat_waist:
                                                                    shirt_size = new_neck
                                                                    shirt_fit = True
                                                                    return shirt_size

                                                            if low_chest > chest:
                                                                if low_coat_waist <= coat_waist <= high_coat_waist:
                                                                    shirt_size = new_neck
                                                                    shirt_fit = True
                                                                    return shirt_size

                                                                if low_coat_waist > coat_waist:
                                                                    shirt_size = new_neck - .5
                                                                    shirt_fit = True
                                                                    return shirt_size
                                                            else:
                                                                new_neck += .5
                                                                shirt_fit = False


# Find Shirt Sleeve Length
def find_shirt_sleeve_Length(shirt_size, sleeve):
    if sleeve < 32:
        sleeve = 33
    elif sleeve == 32:
        sleeve = 33
    elif sleeve == 33:
        sleeve = 33
    elif sleeve == 34:
        sleeve = 35
    elif sleeve == 35:
        sleeve = 35
    elif sleeve == 36:
        sleeve = 37
    elif sleeve == 37:
        sleeve = 37
    elif sleeve == 38:
        sleeve = 39
    elif sleeve == 39:
        sleeve = 39
    elif sleeve > 39:
        sleeve = 39

    for val in cs.items():
        if val[0] == "Shirt_Size":
            for temp_shirt_size_array in val[1]:
                for temp_shirt_size_category, temp_shirt_size_score_array in temp_shirt_size_array.items():
                    if temp_shirt_size_category == "Neck":
                        if shirt_size == temp_shirt_size_score_array:

                            shortest_sleeve = min(temp_shirt_size_array["Sleeve Length"])
                            longest_sleeve = max(temp_shirt_size_array["Sleeve Length"])

                            if sleeve in temp_shirt_size_array["Sleeve Length"]:
                                return shirt_size, sleeve
                            if sleeve < shortest_sleeve:
                                sleeve = shortest_sleeve
                                return shirt_size, sleeve
                            if sleeve > longest_sleeve:

                                shirt_size + .5

                                for val2 in cs.items():
                                    if val2[0] == "Shirt_Size":
                                        for temp_shirt_size_array2 in val2[1]:
                                            for temp_shirt_size_category2, temp_shirt_size_score_array2 in temp_shirt_size_array2.items():
                                                if temp_shirt_size_category2 == "Neck":
                                                    if shirt_size == temp_shirt_size_score_array2:

                                                        shortest_sleeve = min(temp_shirt_size_array2["Sleeve Length"])
                                                        longest_sleeve = max(temp_shirt_size_array2["Sleeve Length"])

                                                        if sleeve in temp_shirt_size_array["Sleeve Length"]:
                                                            return shirt_size, sleeve
                                                        if sleeve < shortest_sleeve:
                                                            sleeve = shortest_sleeve
                                                            return shirt_size, sleeve
                                                        if sleeve > longest_sleeve:
                                                            sleeve = longest_sleeve
                                                            return shirt_size, sleeve


# Red Flags
def red_flags(feet, inches, weight, chest_input, chest, coat_waist, waist, waist_input, seat, shirt_size, sleeve, finalPantSize, jacketSize2):
    shouldShirtSleeveLength = []

    red_flags = ""

    # Checks for Splits
    if (jacketSize2 - finalPantSize) == 6:
        print("")
    else:
        pant_split_flag = "\n Double check that pant split is necessary"

        red_flags += pant_split_flag

    # Checks for red flags with shirt sleeve length
    if feet == 4:

        # initialize sleeve array
        shouldShirtSleeveLength = [28, 29, 30, 31, 32, 33]

        if sleeve in shouldShirtSleeveLength:
            print("")
        else:
            # redflag
            shirt_sleeve_dont_match_height = "\n height does not match shirt sleeve length "
            red_flags += shirt_sleeve_dont_match_height
    elif feet == 5 and inches < 10:
        # initialize sleeve array
        shouldShirtSleeveLength = [28, 29, 30, 31, 32, 33]

        if sleeve in shouldShirtSleeveLength:
            print("")
        else:
            # redflag
            shirt_sleeve_dont_match_height = "\n height does not match shirt sleeve length "
            red_flags += shirt_sleeve_dont_match_height
    elif feet == 5 and inches >= 10:
        # initialize sleeve array
        shouldShirtSleeveLength = [34, 35]

        if sleeve in shouldShirtSleeveLength:
            print("")
        else:
            # redflag
            shirt_sleeve_dont_match_height = "\n height does not match shirt sleeve length "
            red_flags += shirt_sleeve_dont_match_height
    elif feet == 6 and inches <= 1:
        # initialize sleeve array
        shouldShirtSleeveLength = [34, 35]

        if sleeve in shouldShirtSleeveLength:
            print("")
        else:
            # redflag
            shirt_sleeve_dont_match_height = "\n height does not match shirt sleeve length "
            red_flags += shirt_sleeve_dont_match_height
    elif feet == 6 and inches > 2:
        # initialize sleeve array
        shouldShirtSleeveLength = [36, 37]

        if sleeve in shouldShirtSleeveLength:
            print("")
        else:
            # redflag
            shirt_sleeve_dont_match_height = "\n height does not match shirt sleeve length "
            red_flags += shirt_sleeve_dont_match_height
    elif feet == 7:
        # initialize sleeve array
        shouldShirtSleeveLength = [36, 37]

        if sleeve in shouldShirtSleeveLength:
            print("")
        else:
            # redflag
            shirt_sleeve_dont_match_height = "\n height does not match shirt sleeve length "
            red_flags += shirt_sleeve_dont_match_height

    # Checks if user input for the pants is within spec
    if seat < waist:
        seat_greater_then_waist_flag = "\n Customer measured incorrectly please double check"
        red_flags += seat_greater_then_waist_flag
    if seat - waist < 2:
        seat_too_small_flag = "\n Waist and seat measurements are to close please double check"
        red_flags += seat_too_small_flag
    if seat - waist > 8:
        seat_too_big_flag = "\n Waist and seat measurements are to far apart please double check"
        red_flags += seat_too_big_flag

    # Checks if user input for jackets is within spec
    if abs(chest_input - coat_waist) > 8:
        coat_waist_too_small_flag = "\n chest and coat waist measurements are to far apart please double check"
        red_flags += coat_waist_too_small_flag

    # Checks height amd weight and compares to jacket

    # checks shirt size and compares to jacket
    if shirt_size == 14 or 14.5:
        if jacketSize2 == 34 or 36 or 38:
            print("")
        else:
            shirt_and_jacket_flag = "\n Shirt size and Jacket size dont match please double check"
            red_flags += shirt_and_jacket_flag
    elif shirt_size == 15 or 15.5:
        if jacketSize2 == 36 or 38 or 40:
            print("")
        else:
            shirt_and_jacket_flag = "\n Shirt size and Jacket size dont match please double check"
            red_flags += shirt_and_jacket_flag
    elif shirt_size == 16 or 16.5:
        if jacketSize2 == 38 or 40 or 42 or 44:
            print("")
        else:
            shirt_and_jacket_flag = "\n Shirt size and Jacket size dont match please double check"
            red_flags += shirt_and_jacket_flag
    elif shirt_size == 17 or 17.5:
        if jacketSize2 == 42 or 44 or 46 or 48:
            print("")
        else:
            shirt_and_jacket_flag = "\n Shirt size and Jacket size dont match please double check"
            red_flags += shirt_and_jacket_flag
    elif shirt_size == 18 or 18.5:
        if jacketSize2 == 46 or 48 or 50 or 52:
            print("")
        else:
            shirt_and_jacket_flag = "\n Shirt size and Jacket size dont match please double check"
            red_flags += shirt_and_jacket_flag
    elif shirt_size == 19 or 19.5:
        if jacketSize2 == 52 or 54 or 56:
            print("")
        else:
            shirt_and_jacket_flag = "\n Shirt size and Jacket size dont match please double check"
            red_flags += shirt_and_jacket_flag
    elif shirt_size == 20 or 20.5:
        if jacketSize2 == 54 or 56 or 58:
            print("")
        else:
            shirt_and_jacket_flag = "\n Shirt size and Jacket size dont match please double check"
            red_flags += shirt_and_jacket_flag
    elif shirt_size == 22 or 22.5:
        if jacketSize2 == 58 or 60 or 62:
            print("")
        else:
            shirt_and_jacket_flag = "\n Shirt size and Jacket size dont match please double check"
            red_flags += shirt_and_jacket_flag
    elif shirt_size == 23:
        if jacketSize2 == 58 or 60 or 62 or 64:
            print("")
        else:
            shirt_and_jacket_flag = "\n Shirt size and Jacket size dont match please double check"
            red_flags += shirt_and_jacket_flag
    # Email Logic
    if red_flags != "":

        red_flags_Measurements = ""
        red_flags_Measurements += "Feet: " + str(feet) + " " + str(inches) + "\n " + "Jacket: " + str(jacketSize2) + " " + "Chest: " + str(chest_input) + " " + "Coat Waist: " + str(coat_waist) + "\n " + "Pant: " + str(finalPantSize) + " " + "Waist: " + str(waist_input) + " " + "Seat: " + str(seat) + "\n " + "Shirt " + str(shirt_size) + " " + str(sleeve) + "\n "

        red_flags_Measurements += red_flags

        email_sender = "redflagedfittings@nicksmenswear.com"
        email_password = "nxegcuitbodukkwb"
        email_receiver = "rico@nicksmenswear.com"

        subject = "Red Flag Fitting"
        body = red_flags_Measurements

        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

