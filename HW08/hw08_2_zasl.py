def transform2words(amount):
    units = [
        "",
        "одна",
        "дві",
        "три",
        "чотири",
        "п'ять",
        "шість",
        "сім",
        "вісім",
        "дев'ять",
    ]
    teens = [
        "",
        "одинадцять",
        "дванадцять",
        "тринадцять",
        "чотирнадцять",
        "п'ятнадцять",
        "шістнадцять",
        "сімнадцять",
        "вісімнадцять",
        "дев'ятнадцять",
    ]
    tens = [
        "",
        "десять",
        "двадцять",
        "тридцять",
        "сорок",
        "п'ятдесят",
        "шістдесят",
        "сімдесят",
        "вісімдесят",
        "дев'яносто",
    ]
    hundreds = [
        "",
        "сто",
        "двісті",
        "триста",
        "чотириста",
        "п'ятсот",
        "шістсот",
        "сімсот",
        "вісімсот",
        "дев'ятсот",
    ]

    hryvnas, coins = str(amount).split(".")
    hryvnas = int(hryvnas)
    coins = int(coins)

    result = ""
    if hryvnas == 0:
        result += "нуль гривень"
    elif hryvnas == 1:
        result += "одна гривня"
    elif hryvnas < 10 and hryvnas == 2 or hryvnas == 3 or hryvnas == 4:
        result += units[hryvnas] + " гривні"
    elif hryvnas < 10:
        result += units[hryvnas] + " гривень"

    elif hryvnas < 20:
        result += teens[hryvnas % 10] + " гривень"
    elif hryvnas < 100 and (hryvnas % 10) in [2, 3, 4]:
        result += tens[hryvnas // 10] + " " + units[hryvnas % 10] + " гривні"
    else:
        result += (
            hundreds[hryvnas // 100]
            + " "
            + tens[(hryvnas % 100) // 10]
            + " "
            + units[(hryvnas % 100) % 10]
            + " гривень"
        )

    if coins == 0:
        result += ""
    elif coins == 1:
        result += " одна копійка"
    elif coins < 10 and (coins == 2 or coins == 3 or coins == 4):
        result += " " + units[coins] + " копійки"
    elif coins < 10:
        result += " " + units[coins] + " копійок"
    elif coins < 20:
        result += " " + teens[coins % 10] + " копійок"
    elif coins < 100 and coins % 10 in [2, 3, 4]:
        result += " " + tens[coins // 10] + " " + units[coins % 10] + " копійки"
    elif coins < 100 and coins % 10 == 0:
        result = " " + tens[coins // 10] + " копійок"
    else:
        ten_num = coins // 10
        one_num = coins % 10
        if one_num == 0:
            result += " " + tens[ten_num] + " копійок"
        else:
            result += " " + tens[ten_num] + " " + units[one_num] + " копійок"

    ####        result += " " + str(coins) + " копійок"

    return result


# Тестування програми
amount = float(input("Введіть суму: "))
words = transform2words(amount)
print(words)
