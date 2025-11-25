# Gardening advice program (refactored into functions)

def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    # Hardcoded values still here (Input will be handled in Issue 2)
    season = "summer"
    plant_type = "flower"

    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)

    print(advice)


main()
