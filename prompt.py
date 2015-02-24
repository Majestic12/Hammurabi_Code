import utility

def oracles(bushels_yeild, acres_price_current, acres_price_next, plague, bushels_planted_per_acre):
    print("..................................................................................")
    print(" ((( Oracles )))")
    print()
    while True:
        print("What do you want to know about the time that has not passed?")
        print("0 - Nothing, 1 - Should I Farm?, 2 - Value of land?, 3 - Expect the plague?")
        future_result = utility.convert_to_int(": ")
        if future_result == 0:
            print()
            print("Very well! But you will need us someday. Pray that we may help you then!")
            return
        elif future_result == 1:
            # -- if the return on bushel is not good
            if bushels_yeild <= bushels_planted_per_acre:
                print()
                print("We forsee a terrible farming season!")
                return
            else:
                print()
                print("Expect a good farming season ahead")
                return
        elif future_result == 2:
            if acres_price_next < acres_price_current:
                print()
                print("We forsee the value of land decreasing!")
                return
            else:
                print()
                print("Expect the value of land to NOT decrease")
                return
        elif future_result == 3:
            if plague > 0:
                print()
                print("Prepare for the ugly hand of plague!")
                return
            else:
                print()
                print("Plague is not a possiblity, at least for a year")
                return
        else:
            print(">>> Enter a number between 0 and 3")
            print()
    print()

def land_buy(people_total, bushels_total, acres_owned, acres_price_current, bushels_consumed_per_person):
    print()
    print("..................................................................................")
    print(" ((( Buy Land )))")
    if bushels_total <= 0:
        print("You have no bushels in storage to buy land this year!")
        return [bushels_total, acres_owned]
    elif bushels_total < acres_price_current: # -- if bushels is not 0 but still not enough to buy even one acre of land
        print("You don't have enough bushels(" + str(bushels_total) + ") in storage to buy land this year!")
        return [bushels_total, acres_owned]
    while True:
        print("An acre of land is worth", acres_price_current,"bushels")
        # -- if enough bushels in storage to feel all people
        if (people_total*bushels_consumed_per_person) < bushels_total:
            # -- extra bushels after feeding everyone
            bushels_extra = bushels_total - (people_total*bushels_consumed_per_person)
            # -- land that can be bought with the extra bushels
            acre_afford = int(bushels_extra/acres_price_current)
            print("You can feed all your people and still buy", acre_afford,"acres, OR")
            print("You can feed all your people and have", bushels_extra,"bushels remaining for farming")
        else:
            print("You cannot afford to buy even an acre of land if you plan on feeding all your people!")
        print()
        print("How many acres of land would you like to BUY? (0 to decline)")
        land_result = utility.convert_to_int(": ")
        if bushels_total - (land_result * acres_price_current) >= 0:
            if land_result != 0:
                acres_owned += land_result
                bushels_total -= land_result * acres_price_current
                print(" <<< Transaction - Land Bought >>>")
                print(" You now have", acres_owned,"acres of land")
                print(" You now have", bushels_total,"bushels in storage")
            return [bushels_total, acres_owned]
        else:
            print(">>> But you only have", bushels_total,"bushels, enough to buy", int(bushels_total/acres_price_current),"acres!")

def land_sell(people_total, bushels_total, acres_owned, acres_price_current, bushels_consumed_per_person):
    print()
    print("..................................................................................")
    print(" ((( Sell Land )))")
    if acres_owned <= 0:
        print("You have no land to sell this year!")
        return [bushels_total, acres_owned]
    while True:
        print("An acre of land is worth", acres_price_current,"bushels and you have", acres_owned,"acres of land")
        # -- if feeding all people is not possible
        if (people_total*bushels_consumed_per_person) > bushels_total:
            # -- get deficit bushels and calculate land to sell in order to cover it
            # -- use 0.99999 to get ceiling from decimal acres needed
            land_sell = int((((people_total*bushels_consumed_per_person) - bushels_total)/acres_price_current) + 0.99999)
            if acres_owned > land_sell:
                print("Consider selling at least", land_sell,"acres of our land to have enough to feed all your people!")
            elif acres_owned == land_sell:
                print("Consider selling all of our land to have none of your people starve!")
        print()
        print("How many acres of land would you like to SELL? (0 to decline)")
        land_result = utility.convert_to_int(": ")
        if acres_owned - land_result >= 0:
            if land_result != 0:
                acres_owned -= land_result
                bushels_total += land_result * acres_price_current
                print(" <<< Transaction - Land Sold >>>")
                print(" You now have", acres_owned,"acres of land")
                print(" You now have", bushels_total,"bushels in storage")
            return [bushels_total, acres_owned]
        else:
            print(">>> But you only have", acres_owned,"acres of land!")

def food(people_total, bushels_total, bushels_consumed_per_person):
    print()
    print("..................................................................................")
    print(" ((( Feed )))")
    if bushels_total <= 0:
        print("All of your people will starve since you have no bushels in storage!")
        return [people_total, bushels_total]
    while True:
        print("Each person needs", bushels_consumed_per_person ,"bushels per year to survive")
        # -- calculate extra bushels
        bushels_extra = bushels_total - (people_total*bushels_consumed_per_person)
        if bushels_extra > 0:
            print("You can feed all of your people (" + str(people_total) + ") and have", bushels_extra,"bushels remaining for farming")
        elif bushels_extra == 0:
            print("You can feed all of your people (" + str(people_total) + ") but you will have no bushels left over for farming!")
        else:
            people_fed = int(bushels_total/bushels_consumed_per_person)
            print("You can only feed", people_fed,"people and", people_total - people_fed,"people will starve!")
        print()
        print("How many people would you like to feed?")
        feed_result = utility.convert_to_int(": ")
        if feed_result <= people_total and (feed_result * bushels_consumed_per_person) <= bushels_total:
            bushels_total -= feed_result * bushels_consumed_per_person
            print(" <<< Order >>>")
            print(" Approved plan to feed", feed_result,"out of", people_total,"people")
            print(" You now have", bushels_total,"bushels in storage")
            return [(people_total - feed_result), bushels_total]
        elif feed_result > people_total:
            print(">>> But you only have", people_total,"people!")
        elif (feed_result * bushels_consumed_per_person) > bushels_total:
            print(">>> But you only have", bushels_total,"bushels, enough to feed", int(bushels_total/bushels_consumed_per_person),"people!")

def farm(people_total, bushels_total, acres_owned, acres_farmed_per_person, bushels_planted_per_acre, bushels_yeild_previous):
    print()
    print("..................................................................................")
    print(" ((( Farm )))")
    if acres_owned <= 0:
        print("You have no land to farm on this year!")
        return [bushels_total, 0, 0]
    elif bushels_total <= 0:
        print("You have no bushels in storage to farm this year!")
        return [bushels_total, 0, 0]
    elif int(bushels_total/bushels_planted_per_acre) <= 0:
        print()
        print("You don't have enough bushels to farm this year!")
        return [bushels_total, 0, 0]
    while True:
        print("To plant one acre of land requires", bushels_planted_per_acre ,"bushels and you have", bushels_total,"bushels in storage")
        # -- find minimum acres that can be farmed -- limiting land, people and bushels
        people_limit = people_total*acres_farmed_per_person
        bushels_limit = int(bushels_total/bushels_planted_per_acre)
        minimum_of_resources = min(acres_owned, people_limit, bushels_limit)
        print("You can plant", minimum_of_resources,"acres out of", acres_owned,"total acres")
        print()
        print("How many acres of land do you want to plant with bushels?")
        acres_result = utility.convert_to_int(": ")
        if acres_result == 0:
            return [bushels_total, 0, 0]
        elif acres_result <= minimum_of_resources:
            bushels_total -= (acres_result*bushels_planted_per_acre)
            print(" <<< Plan >>>")
            print(" Farming is underway on", acres_result,"out of", acres_owned,"acres of our fertile land")
            print(" You now have", bushels_total,"bushels in storage")
            return [bushels_total, acres_result*bushels_yeild_previous, 1]
        else: # -- if entered land is more than minimum possible
            # -- if people is more limiting than bushels
            if people_limit < bushels_limit:
                # -- if people is more limiting than land
                if people_limit < acres_owned:
                    print(">>> But you only have", people_total,"people, enough to farm", people_total*acres_farmed_per_person,"acres!")
                elif people_limit > acres_owned: # -- if land is more limiting than people
                    print(">>> But you only have", acres_owned,"acres of land!")
                else: # -- if both people and land are equally limiting
                    print(">>> But you don't have enough people and land to farm", acres_result,"acres!")
            elif people_limit > bushels_limit: # -- if bushels is more limiting than people
                if bushels_limit < acres_owned: # -- if bushels is more limiting than land
                    print(">>> But you only have", bushels_total,"bushels, enough to farm", int(bushels_total/bushels_planted_per_acre),"acres!")
                elif bushels_limit > acres_owned: # -- if land is more limiting than bushels
                    print(">>> But you only have", acres_owned,"acres of land!")
                elif bushels_limit == acres_owned: # -- if bushels and land are equally limiting
                    print(">>> But you don't have enough bushels and land to farm", acres_result,"acres!")
            elif people_limit == bushels_limit: # -- if people and bushels are equally limiting
                print(">>> But you don't have enough people and bushels to farm", acres_result,"acres!")
            else: # if all three resources are equally limiting
                print(">>> But you don't have enough of any resources to farm", acres_result,"acres!")
