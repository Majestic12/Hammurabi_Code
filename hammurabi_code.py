import random, string
import utility
import prompt
import state
# this is ashwin's comment
# -- main game function to call
def game_main():
    # -------------------------------------- initializing variables
    # -- turns
    number_of_years = 10
    # -- turn orcales off (0) and on (1) -- oracles helps reduce player issue with a lot of randomness
    oracles = 0
    # -- starting population
    people_total = 100
    # -- starting grain in storage
    bushels_total = 2850
    # -- starting land
    acres_owned = 1000
    # -- initial yeild and harvest for display
    initial_bushel_yeild = 1
    initial_bushel_harvest = 1000
    # ------------------------------------------------------------ requirements
    # -- amount in bushels one person needs to survive the year
    bushels_consumed_per_person = 20
    # -- amount in acres one person can farm for the year
    acres_farmed_per_person = 10
    # -- amount in bushels that needs to be used to farm one acre of land
    bushels_planted_per_acre = 1
    # ------------------------------------------ randoms
    # -- range of values
    # -- bushel yeild range
    bushels_yeild_low = 0
    bushels_yeild_high = 4
    # -- land value range
    acres_price_low = 10
    acres_price_high = 25
    # -- number of immigrants range
    immigrants_low = 0
    immigrants_high = 20
    # ----------------------------------------------------- percent range
    # -- percentage range rats can affect total bushels
    rat_infestation_perc_low = 10
    rat_infestation_perc_high = 50
    # -- percentage range plague can affect population
    plague_deaths_perc_low = 25
    plague_deaths_perc_high = 50
    # ----------------------------------------- failure limit
    # -- percentage of population lost will result in fail state
    people_revolt_perc_loss = 50
    # -------------------------------------------------------- chance variables
    # -- chance of a rat infestation
    rat_infestation_chance = 50
    # -- chance of a plague
    plague_chance = 15
    # -- array for requirments, so that they can be passed to other functions
    requirements = [bushels_consumed_per_person, acres_farmed_per_person, bushels_planted_per_acre]
    # -- array for the randoms, so that they can be passed to other functions
    randoms = [bushels_yeild_low, bushels_yeild_high, acres_price_low, acres_price_high, immigrants_low, immigrants_high]
    # -- array for percent variables, so that they can be passed to other functions
    percents = [rat_infestation_perc_low, rat_infestation_perc_high, plague_deaths_perc_low, plague_deaths_perc_high, rat_infestation_chance, plague_chance, people_revolt_perc_loss]
    # --------------------------------- functions
    # -- display introductory text
    state.game_intro(number_of_years, oracles, bushels_consumed_per_person, acres_farmed_per_person, bushels_planted_per_acre)
    # -- loop through the years
    game_loop(number_of_years, oracles, people_total, bushels_total, acres_owned, requirements, randoms, percents, initial_bushel_yeild, initial_bushel_harvest)
    quit()
# -- game update loop
def game_loop(number_of_years, oracles, people_total, bushels_total, acres_owned, requirements, randoms, percents, initial_bushel_yeild, initial_bushel_harvest):
    # -------------------------------------------------------------------------- initializing loop
    # --------------------------------------------------- requirements - passed
    bushels_consumed_per_person = requirements[0]
    acres_farmed_per_person = requirements[1]
    bushels_planted_per_acre = requirements[2]
    # --------------------------------------------- randoms - passed
    bushels_yeild_low = randoms[0]
    bushels_yeild_high = randoms[1]
    acres_price_low = randoms[2]
    acres_price_high = randoms[3]
    immigrants_low = randoms[4]
    immigrants_high = randoms[5]
    # --------------------------------------------- percents - passed
    rat_infestation_perc_low = percents[0]
    rat_infestation_perc_high = percents[1]
    plague_deaths_perc_low = percents[2]
    plague_deaths_perc_high = percents[3]
    rat_infestation_chance = percents[4]
    plague_chance = percents[5]
    people_revolt_perc_loss = percents[6]
    # ----------------------------------------------------------------- population
    # -- total number of people starved - accumulates each turn
    people_starved_total = 0
    # -- number of people starved - resets/calculated each turn
    people_starved = 0
    # -- number of people immigrating - generated each turn
    people_immigrated = 0
    # -- total number of people killed because of plague - accumulates each turn
    people_plague_deaths_total = 0
    # -- number of people that died through plague - resets/calculated each turn
    people_plague_deaths = 0
    # ------------------------------------------------------------------------------- bushels
    bushels_harvested = initial_bushel_harvest
    bushels_yeild = initial_bushel_yeild
    bushels_rats_stole = 0
    # ------------------------ land
    acres_price_previous = random.randint(acres_price_low, acres_price_high)
    acres_price_current = 0
    acres_price_next = random.randint(acres_price_low, acres_price_high)
    # -- variable to check if player had farmed previously (0- no, 1- yes)
    farming = 1
    # -------------------------------------------------------------------- loop through the years
    for year in range(1, number_of_years+1):
        # in effect clear screen
        utility.push_screen(30)
        # -- updating land price to display
        acres_price_current = acres_price_next
        # -- start dialogue and prompts
        print("__________________________________________________________________________________")
        print()
        print("==========================[ Year", year, "of", number_of_years,"]==========================")
        # -- check to see if there is important info to display
        if (people_immigrated + people_starved + people_plague_deaths + farming + bushels_rats_stole) > 0:
            print("  <<< During the Previous Year >>>")
            print()
            print(" *", people_immigrated,"new people have settled in our lands * (" + str(people_total) + " total)") if people_immigrated > 0 else 0
            print(" !!!", people_starved,"people starved to death !!!") if people_starved > 0 else 0
            print(" !!!", people_plague_deaths,"people died from the plague !!!") if people_plague_deaths > 0 else 0
            if farming > 0:
                if bushels_yeild <= 0:
                    print("!!! All planted bushels were lost because of drought !!!")
                else:
                    print(" ", bushels_harvested,"bushels were harvested at the rate of", bushels_yeild,"bushels per acre")
            print(" !!!", bushels_rats_stole,"bushels were lost to rat infestations !!!") if bushels_rats_stole > 0 else 0
            print()
        print("  <<< Current Status >>>")
        print()
        print(" ", acres_owned,"acres of land are under your rule")
        print(" ", people_total,"people are now part of our lands")
        print(" ", bushels_total,"bushels are in storage")
        print()
        print(" ", acres_price_current,"bushels is the worth of an acre of land (previously " + str(acres_price_previous) +")")
        # -- generating variables for the next year (for use by Oracles)
        # -- generating grain yeild for next year
        bushels_yeild = random.randint(bushels_yeild_low, bushels_yeild_high)
        # -- generating land price
        acres_price_next = random.randint(acres_price_low, acres_price_high)
        # -- figure out if plague (0 - no, 1 - yes)
        plague = 1 if random.randint(0, 99) < plague_chance else 0
        # ------------------------------------------------------------------------ Oracles
        if oracles > 0:
            # -- oracles advice - self contained function
            prompt.oracles(bushels_yeild, acres_price_current, acres_price_next, plague, bushels_planted_per_acre)
        print()
        utility.keyword_check(input("Press [ENTER] to start planning..."))
        # -- buy or sell land and update variables
        bushels_total, acres_owned = prompt.land_buy(people_total, bushels_total, acres_owned, acres_price_current, bushels_consumed_per_person)
        bushels_total, acres_owned = prompt.land_sell(people_total, bushels_total, acres_owned, acres_price_current, bushels_consumed_per_person)
        # -- feed people and update people starved and remaining
        # -- update people starved and bushels total depending on number of people feed and bushels consumed
        people_starved, bushels_total = prompt.food(people_total, bushels_total, bushels_consumed_per_person)
        # -- update bushels total, bushels harvested and if farming took place depending on acres chosen to farm and bushels consumed
        bushels_total, bushels_harvested, farming = prompt.farm(people_total, bushels_total, acres_owned, acres_farmed_per_person, bushels_planted_per_acre, bushels_yeild)
        print()
        utility.keyword_check(input("Press [ENTER] to advance time..."))
        # ----------------------------------------------------------------- updating variables
        # -- update total bushels by the number of bushels harvested
        bushels_total += bushels_harvested
        # ------------------------------------------------------------------------ rat attack
        if bushels_total > 0 and random.randint(0, 99) < rat_infestation_chance:
            bushels_rats_stole = int(random.randint(rat_infestation_perc_low, rat_infestation_perc_high) / 100 * bushels_total)
            bushels_total -= bushels_rats_stole
            print()
            print(" ((( Rats )))")
            print("!!! We lost", bushels_rats_stole, "bushels to rat infestation and we now have", bushels_total,"bushels in storage !!!")
            print()
            utility.keyword_check(input("Press [ENTER] to advance time..."))
        else:
            bushels_rats_stole = 0
        # ------------------------------------------------- plague attack
        if people_total > 0 and plague > 0:
            people_plague_deaths = int(random.randint(plague_deaths_perc_low, plague_deaths_perc_high) / 100 * people_total)
            people_plague_deaths_total += people_plague_deaths
            people_total -= people_plague_deaths
            if people_starved > 0:
                potential_starved_deaths = people_starved - people_plague_deaths
                if potential_starved_deaths < 0:
                    people_starved = 0
                else:
                    people_starved = potential_starved_deaths
            print()
            print(" ((( Plague )))")
            print("!!! Grave news, we lost", people_plague_deaths,"people to the plague and we now have", people_total,"people under your rule !!!")
            print()
            utility.keyword_check(input("Press [ENTER] to advance time..."))
        else:
            people_plague_deaths = 0
        # ------------------------------------------------------------ status of current population
        # -- update current population if people were starved
        people_total -= people_starved
        # -- update starved total variable
        people_starved_total += people_starved
        # -- if some percent of the population is lost - end game - failure state
        if people_starved >= (people_total * (people_revolt_perc_loss/100)):
            state.game_lost(people_total, people_starved_total)
        # ----------------------------------------------------------- immigration
        people_immigrated = random.randint(immigrants_low, immigrants_high)
        people_total += people_immigrated
        acres_price_previous = acres_price_current
        print("__________________________________________________________________________________")
    # -- game won
    state.game_won(number_of_years, people_total, bushels_total, acres_owned, people_starved_total, people_plague_deaths_total)

if __name__ == "__main__":
    game_main()
