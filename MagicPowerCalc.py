import requests
import math
def request_profile():
    name = input("ign: ")
    try:
        data = requests.get( url = "https://sky.shiiyu.moe/api/v2/talismans/" + name).json()
        names = [data['profiles'][x]['cute_name'] for x in data['profiles']]
        internal_name = [data['profiles'][x] for x in data['profiles']]
        names_dict = {}
        for i, j in enumerate(names):
            names_dict[j] = i
        print(names)
        profile = input("profile: ")
        if (not profile in names):
            print("That is not a profile")
            request_profile()
        profile_data = internal_name[names_dict[profile]];
        power_chart = {"common":3, "uncommon":5, "rare":8, "epic":12, "legendary":16, "mythic":22, "special":3, "very_special":5}  
        magic_power = 0
        for accessory in profile_data['accessories']:
            if (not accessory['isInactive']): 
                magic_power += power_chart[accessory['rarity']]
        if (magic_power == 0):
            print("Api disabled or this profile has no talismans.")
        stats_mult = 29.97 * ((math.log(0.0019 * (magic_power) + 1)) ** 1.2)
        print(name + "'s magical power on profile " + profile + " is " + str(magic_power) + " with a stats boost of " + str(round(stats_mult*100, 2)) + " %")
        request_profile()
    except KeyError:
        print("This player does not exist!")
        request_profile()
request_profile()
