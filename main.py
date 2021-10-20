from easygui import *

def main():
    pvp_tally = 0
    anime_tally = 0
    zombies_tally = 0
    soccer_tally = 0
    adventure_tally = 0
    coop_tally = 0
    shooter_tally = 0
    mmorpg_tally = 0
    story_rich_tally = 0
    crafting_tally = 0
    fantasy_tally = 0
    hero_shooter_tally = 0
    moba_tally = 0
    battle_royale_tally = 0
    ww2_tally = 0
    grand_strategy_tally = 0
    early_access_tally = 0
    city_builder_tally = 0
    turn_based_strategy_tally = 0
    indie_tally = 0
    base_building_tally = 0
    threeD_tally = 0
    twoD_tally = 0
    driving_tally = 0
    sandbox_tally = 0
    funny_tally = 0
    competitive_tal = 0ly = 0
    martial_arts_tally = 0
    memes_tally = 0
    management_tally = 0
    racing_tally = 0
    eSports_tally = 0
    massive_multiplayer_tally = 0
    online_coop_tally = 0
    historical_tally = 0
    horror_tally = 0
    casual_tally = 0
    colony_sim_tally = 0
    automation_tally = 0
    building_tally = 0
    farming_sim_tally = 0
    life_sim_tally = 0
    mod_tally = 0
    realistic_tally = 0
    medieval_tally = 0
    pve_tally = 0
    utilities_tally = 0
    mature_tally = 0
    hacknslash_tally = 0
    difficult_tally = 0
    music_tally = 0
    exploration_tally = 0
    scifi_tally = 0
    basketball_tally = 0
    looter-shooter_tally = 0
    actionRPG_tally = 0
    multiplayer_tally = 0
    free_tally = 0
    rpg_tally = 0
    openworld_tally = 0
    action_tally = 0
    survival_tally = 0
    openworld_survival_tally = 0
    simulation_tally = 0
    fps_tally = 0
    sports_tally = 0
    
    
    def quest_d_1(): 
        msg ="What genre game do you want to play?"
        title = "Steam Recommendations Tool"
        choices = ["Action", "Survival", "RPG", "Simulation", "Sports"]
        choice = choicebox(msg, title, choices)
        if choice == "Action":
            action_tally = action_tally + 1
        elif choice == "Survival":
            survival_tally = survival_tally + 1
        elif choice == "Simulation":
             simulation_tally =  simulation_tally + 1
        elif choice == "RPG":
            rpg_tally = rpg_tally + 1
        elif choice == "Sports":
            sports_tally = sports_tally + 1

        
    def quest_d_2(): 
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Open World", "Indie", "First Person Shooter"]
        choice = choicebox(msg, title, choices)
        if choice == "Open World":
            open_world_tally = open_world_tally + 1
        elif choice == "Indie":
            indie_tally = indie_tally + 1
        elif choice == "First Person Shooter":
            fps_tally = fps_tally + 1     
        
    def quest_b_1():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Massively Multiplayer", "Online Co-op", "Historical", "Horror"]
        choice = choicebox(msg, title, choices)
        if choice == "Massively Multiplayer":
            massively_multiplayer_tally = massively_multiplayer_tally + 1
        elif choice == "Online Co-op":
            online_coop_tally = x + 1
        elif choice == "Historical":
            historical_tally = historical_tally + 1
        elif choice == "Horror":
            horror_tally = horror_tally + 1
        
    def quest_b_2():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Casual", "Colony Sim", "Automation", "Building"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        
    def quest_b_3():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Farming Sim", "Life Sim", "Mod", "Realistic"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1 

    def quest_b_4():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Medieval", "PvE", "Utilities", "Mature"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        
    def quest_b_5():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Hack and Slash", "Difficult", "Music", "Exploration"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        
    def quest_b_6():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Music", "Sci-fi", "Basketball", "Looter Shooter", "Action RPG"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1 

    def quest_a_1():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Soccer", "Adventure", "Shooter", "MMORPG"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        
    def quest_a_2():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Story Rich", "Crafting", "Fantasy", "Hero Shooter"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        
    def quest_a_3():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["MOBA", "Battle Royale", "World War II", "Grand Strategy"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1 

    def quest_a_4():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Early Access", "City Builder", "Turn-Based Strategy", "Indie"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        
    def quest_a_5():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Base Building", "3D", "2D", "Driving"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1 

    def quest_a_6():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Sandbox", "Funny", "Competitive", "Martial Arts"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        
    def quest_a_7():
        msg ="Select your choices."
        title = "Steam Recommendations Tool"
        choices = ["Memes", "Management", "Racing", "eSports"]
        choice = choicebox(msg, title, choices)
        if choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        elif choice == "":
            x = x + 1
        
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
