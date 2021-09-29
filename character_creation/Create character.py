import random
def roll_sort():
     d6_1 = random.randint(1,6)
     d6_2 = random.randint(1,6)
     d6_3 = random.randint(1,6)
     d6_4 = random.randint(1,6)
     stats = [d6_1, d6_2, d6_3, d6_4]
     stats.sort()
     return stats

def stat_finder():
    #First stat roll
     stats = roll_sort()
     del stats[0]
     print(stats)
     total_1 = sum(stats)
     print(total_1)
     print("This is your first stat! You rolled these three numbers and at the end of all you rolls you can place them how you want!")
     print("\n")
     con_1 = input("Press Y key to keep rolling!")
     if con_1 == "Y" or "y":
        #This rolls for the second stat
         stats = roll_sort()
         del stats[0]
         print(stats)
         total_2 = sum(stats)
         print(total_2)
         print("Here is your second stat!")
         print("\n")
         con_2 = input("Press Y key to keep rolling!")
         if con_2 == "Y" or "y":
            #Third stat
            stats = roll_sort()
            del stats[0]
            print(stats)
            total_3 = sum(stats)
            print(total_3)
            print("Here is your third stat roll!")
            print("\n")
            con_3 = input("Press Y key to keep rolling!")
            if con_3 == "Y" or "y":
                #fourth stat
                stats = roll_sort()
                del stats[0]
                print(stats)
                total_4 = sum(stats)
                print(total_4)
                print("Here is your fourth stat roll!")
                print("\n")
                con_4 = input("Press Y key to keep rolling!")
                if con_4 == "Y" or "y":
                #fifth stat
                    stats = roll_sort()
                    del stats[0]
                    print(stats)
                    total_5 = sum(stats)
                    print(total_5)
                    print("Here is your fifth stat roll!")
                    print("\n")
                    con_5 = input("Press Y key to keep rolling!")
                    if con_5 == "Y" or "y":
                    #sixth stat
                        stats = roll_sort()
                        del stats[0]
                        print(stats)
                        total_6 = sum(stats)
                        print(total_6)
                        print("Alright adventurer here is your sixth adn final stat!")
                        print("\n\n\n")
     #This next segment take all the saved statistics that were randomly rolled and allows the player to assign them to skills of their choosing
     print("Those are some mighty fine rolls there might I say, but the question lies...Where will you put them?")
    
     print(total_1)
     print(total_2)
     print(total_3)
     print(total_4)
     print(total_5)
     print(total_6)
     print("\n")
     #Allows selected skill to be removed from the list for user convinence
     #Needs code in instance input doesnt match items in the list
     list_1 = ["Str", "Dex", "Con", "Int", "Wis", "Char"]
     print(list_1)
     print("Where would you like the " + str(total_1) + " ?: ")
     first_stat = input()
     list_1.remove(first_stat)
     print("\n")
     print(list_1)
     print("Where would you like " + str(total_2) + " ?: ")
     second_stat = input()
     list_1.remove(second_stat)
     print("\n")
     print(list_1)
     print("Where would you like " + str(total_3) + " ?: ")
     third_stat = input()
     list_1.remove(third_stat)
     print("\n")
     print(list_1)
     print("Where would you like " + str(total_4) + " ?: ")
     fourth_stat = input()
     list_1.remove(fourth_stat)
     print("\n")
     print(list_1)
     print("Where would you like " + str(total_5) + " ?: ")
     fifth_stat = input()
     list_1.remove(fifth_stat)
     print("\n")
     print(list_1)
     print("Where would you like " + str(total_6) + " ?: ")
     sixth_stat = input()
     list_1.remove(sixth_stat)
     print("\n")
     print("Alright adventurer lets take a look at those stats you've placed!")
     print(first_stat + " " + str(total_1))
     print(second_stat + " " + str(total_2))
     print(third_stat + " " + str(total_3))
     print(fourth_stat + " " + str(total_4))
     print(fifth_stat + " " + str(total_5))
     print(sixth_stat + " " + str(total_6))
     


                       





 #Starts the program, i want to add a input that takes player name to make program more personal   
start_rolls = input("Press Y key to start rolling!: ")
if start_rolls == "Y" or "y":
    stat_finder()






    


