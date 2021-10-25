from easygui import *

    #use the set to compare to a set of user tags. Then pull common tags to provide the recommendation.
user_choice_set = set()
user_tally_list = set(....)

def main():
    def quest_d_1(): 
        msg ="What genre game do you want to play?"
        title = "Steam Recommendations Tool"
        choices = ["Action", "Survival", "RPG", "Simulation", "Sports"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)
        
    def quest_d_2(): 
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Open World", "Indie", "First Person Shooter"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)
        
    def quest_b_1():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Massively Multiplayer", "Online Co-op", "Historical", "Horror"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)
        
    def quest_b_2():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Casual", "Colony Sim", "Automation", "Building"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)
        
    def quest_b_3():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Farming Sim", "Life Sim", "Mod", "Realistic"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)
        
    def quest_b_4():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Medieval", "PvE", "Utilities", "Mature"]
        choice = choicebox(msg, title, choices)
        user_choioce_set.add(choice)

    def quest_b_5():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Hack and Slash", "Difficult", "Music", "Exploration"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)
        
    def quest_b_6():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Music", "Sci-fi", "Basketball", "Looter Shooter", "Action RPG"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)
        
    def quest_a_1():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Soccer", "Adventure", "Shooter", "MMORPG"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)

    def quest_a_2():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Story Rich", "Crafting", "Fantasy", "Hero Shooter"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)

    def quest_a_3():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["MOBA", "Battle Royale", "World War II", "Grand Strategy"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)
        
    def quest_a_4():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Early Access", "City Builder", "Turn-Based Strategy", "Indie"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)

    def quest_a_5():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Base Building", "3D", "2D", "Driving"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)
        
    def quest_a_6():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Sandbox", "Funny", "Competitive", "Martial Arts"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)

    def quest_a_7():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Memes", "Management", "Racing", "eSports"]
        choice = choicebox(msg, title, choices)
        user_choice_set.add(choice)
        
#print(user_choice_set)
#compare user_choice_set to user_tally_set
#Then need to figure out how to use the tags that are common to both lists to select a game most similar
        
    quest_d_1()
    quest_d_2()
    quest_b_1()
    quest_b_2()
    quest_b_3()
    quest_b_4()
    quest_b_5()
    quest_b_6()
    quest_a_1()
    quest_a_2()
    quest_a_3()
    quest_a_4()
    quest_a_5()
    quest_a_6()
    quest_a_7()
    
main()
