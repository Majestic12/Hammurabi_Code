import utility
# -- introducing the game
def game_intro(number_of_years, oracles, bushels_consumed_per_person, acres_farmed_per_person, bushels_planted_per_acre):
    # in effect clear screen
    utility.push_screen(30)
    # intro display
    print("                                 HAMMURABI")
    print("__________________________________________________________________________________")
    print()
    print("O great Hammurabi. Ruler of Babylon")
    print("The people are in need of your leadership")
    if oracles > 0:
        print("Oracles have prophesied your * " + str(number_of_years) + "-year * rule")
    else:
        print("Guide your people through the next *", number_of_years,"years *")
    print()
    print("As your humble advisor, I will guide you as you consider your duties to:")
    print(" - Dispense and store food")
    print(" - Direct farming")
    print(" - Buy and sell our fertile land")
    print("All life and land is supported by the harvest, measured in bushels")
    print()
    print("Things you should know before you proceed:")
    print("........................................................................")
    print("          Each person needs", bushels_consumed_per_person ,"bushels per year to survive")
    print("        Each person can farm", acres_farmed_per_person ,"acres of fertile land per year")
    print("             To plant one acre of land requires", bushels_planted_per_acre ,"bushels")
    print()
    print("       Consult the Oracles to gain insights into the future") if oracles > 0 else 0
    print("  Beware of rat infestations that affect bushels planted and in storage")
    print("  Watching lives squadered due to bad planning can turn even loyal minds")
    print("........................................................................")
    print("- History will judge your rule -")
    print("- But people will decide your fate -")
    print()
    print(" Enter 'q' or 'quit' when prompted to exit game at any time")
    print("__________________________________________________________________________________")
    print()
    # -- utility.keyword_check - checks for quit command
    utility.keyword_check(input("Press [ENTER] to start..."))
# TODO - improve failure state
def game_lost(people_total, people_starved_total):
    # in effect clear screen
    utility.push_screen(30)
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print()
    print(" ((( FAILED )))")
    if people_total <= 0:
        print("Your land is devoid of life!")
        print("You now command no one and everyone!")
    else:
        print("You fool! Your failed policies has led to the death of", people_starved_total,"people!")
        print("The people have taken to the streets in revolt!")
        print("You no longer command their loyalty!")
    print()
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print()
    print("                           <<< GAME OVER - FAILED >>>")
    quit()
# TODO - Evaluate success
def game_won(number_of_years, people_total, bushels_total, acres_owned, people_starved_total, people_plague_deaths_total):
    # in effect clear screen
    utility.push_screen(30)
    print("*******************************")
    print(" ((( SUCCESS )))")
    print("You have successfully led Babylon through the past", number_of_years,"years")
    print("__________________________________________________________________________________")
    print()
    print("                      [ GAME OVER - THANK YOU FOR PLAYING ]")
    print("__________________________________________________________________________________")
