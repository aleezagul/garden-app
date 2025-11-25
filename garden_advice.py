# Gardening advice program with user input and dictionaries

# Advice dictionaries
season_advice = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n"
}

plant_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}

def main():
    # Get user input
    season = input("Enter the season (summer/winter): ").lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").lower()

    # Get advice from dictionaries, with defaults
    advice = season_advice.get(season, "No advice for this season.\n")
    advice += plant_advice.get(plant_type, "No advice for this type of plant.")

    print(advice)

main()
