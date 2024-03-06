import requests, json, random

while True:
    # Get the list of pokemon from the API
    url = "https://pokeapi.co/api/v2/pokemon"
    response = requests.get(url)
    pokemon_list = json.loads(response.text)["results"]

    pokemon_names = []
    for pokemon in pokemon_list:
        pokemon_names.append(pokemon["name"])

    ### Show list of pokemon
    print("Pokemon List:", pokemon_names)

    # Get the user's choice ### Combined 2 lines to 1 - choice variable
    choice = input("Enter your pokemon: ").lower()

    ### Get a random Pokemon for the computer (aka the cpu)
    computer = random.choice(pokemon_list)["name"]

    # Get the pokemon's data from the API ### Original url doesn't work 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
    url = f"https://pokeapi.co/api/v2/pokemon/{choice}"
    response = requests.get(url)
    pokemon_data = json.loads(response.text)

    # Get the computer's data from the API - similar to previous section
    url = f"https://pokeapi.co/api/v2/pokemon/{computer}"
    response = requests.get(url)
    computer_data = json.loads(response.text)

    print("----------------------------------------------------------")
    # to get ability
    abilities = pokemon_data['abilities'][0]
    ability = abilities['ability']

    # to format height and weight properly
    height = int(pokemon_data['height'])
    weight = int(pokemon_data['weight'])

    height_formatted = height / 10
    weight_formatted = weight / 10

    # Print the pokemon's data
    print('Name: {}'.format(pokemon_data['name']))
    print('Weight: {}'.format(weight_formatted) + "(kgs)")
    print('Height: {}'.format(height_formatted) + "(m)")
    print('Ability: {}'.format(ability['name']))
    print("----------------------------------------------------------")

    # Power = height + weight
    pokemon_power = int(pokemon_data["height"]) + int(pokemon_data["weight"])
    computer_power = int(computer_data["height"]) + int(computer_data["weight"])

    # Print their powers
    print(f"The power of {choice} is: {pokemon_power}")
    print(f"The power of {computer} is: {computer_power}")

    # Determine the winner
    if pokemon_power > computer_power:
        print("You win!")
    elif pokemon_power < computer_power:
        print("Computer wins!")
    else:
        print("It's a tie!")

    # Option to play again
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again == "no":
        break
