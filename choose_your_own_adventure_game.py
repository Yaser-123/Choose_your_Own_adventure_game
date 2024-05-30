print("Welcome to the Fighting Adventure!")
print("You are a brave warrior on a quest to save the kingdom from an evil dragon.")
print("Choose your weapon:")
print("For choosing Sword select 1 and enter, for Bow and Arrow select 2 and enter and for choosing Magic Staff select 3 and enter.")
print("1. Sword")
print("2. Bow and Arrow")
print("3. Magic Staff")

while True:
    weapon_choice = input("Enter the number of your choice: ")
    if weapon_choice in ['1', '2', '3']:
        break
    else:
        print("Invalid choice, please choose 1, 2, or 3.")

if weapon_choice == '1':
    print("You chose the Sword! A wise choice for a close combat fighter.")
    print("You march into the dark forest where the dragon is hiding.")
    print("Suddenly, a group of bandits attack you!")
    print("Do you:")
    print("1. Fight the bandits")
    print("2. Try to sneak past them")
    print("3. Attempt to scare them off")

    while True:
        action_choice = input("Enter the number of your choice: ")
        if action_choice in ['1', '2', '3']:
            break
        else:
            print("Invalid choice, please choose 1, 2, or 3.")

    if action_choice == '1':
        print("You bravely fight the bandits with your sword and emerge victorious!")
        print("You continue your journey and reach the dragon's lair.")
        print("The dragon awakens and attacks you with fiery breath.")
        print("Do you:")
        print("1. Block with your shield")
        print("2. Roll to dodge")
        print("3. Use a reflective surface to deflect the fire")

        while True:
            dragon_choice = input("Enter the number of your choice: ")
            if dragon_choice in ['1', '2', '3']:
                break
            else:
                print("Invalid choice, please choose 1, 2, or 3.")

        if dragon_choice == '1':
            print("You block the fire with your shield, but the dragon's power is overwhelming.")
            print("You are defeated by the dragon.")
            print("Game Over. Try again.")
        elif dragon_choice == '2':
            print("You roll to dodge the fire but the dragon is too fast and catches you.")
            print("You are defeated by the dragon.")
            print("Game Over. Try again.")
        elif dragon_choice == '3':
            print("You use a reflective surface to deflect the fire back at the dragon.")
            print("The dragon is momentarily stunned, giving you a chance to strike it down!")
            print("The kingdom is saved and you are hailed as a hero.")
            print("Congratulations! You achieved a happy ending.")
    elif action_choice == '2':
        print("You sneak past the bandits successfully and continue your journey.")
        print("As you approach the dragon's lair, you find a wounded knight.")
        print("Do you:")
        print("1. Help the knight")
        print("2. Continue without helping")
        print("3. Search the area for supplies")

        while True:
            knight_choice = input("Enter the number of your choice: ")
            if knight_choice in ['1', '2', '3']:
                break
            else:
                print("Invalid choice, please choose 1, 2, or 3.")

        if knight_choice == '1':
            print("You help the knight, who in return assists you in the battle against the dragon.")
            print("Together, you defeat the dragon and save the kingdom.")
            print("The knight becomes your loyal ally. Congratulations! You achieved a happy ending.")
        elif knight_choice == '2':
            print("You continue alone and face the dragon.")
            print("The dragon proves too powerful for a lone warrior.")
            print("You are defeated by the dragon.")
            print("Game Over. Try again.")
        elif knight_choice == '3':
            print("You find a powerful potion and some weapons.")
            print("With these new supplies, you face the dragon.")
            print("The enhanced weapons and potion give you an edge and you defeat the dragon!")
            print("The kingdom is saved and you are hailed as a hero.")
            print("Congratulations! You achieved a happy ending.")
    elif action_choice == '3':
        print("You attempt to scare the bandits off by brandishing your sword and shouting fiercely.")
        print("The bandits, intimidated by your display, flee into the forest.")
        print("You continue your journey and reach the dragon's lair.")
        print("The dragon is sleeping. Do you:")
        print("1. Sneak up and attack")
        print("2. Set a trap")
        print("3. Wake the dragon and challenge it to a duel")

        while True:
            dragon_choice = input("Enter the number of your choice: ")
            if dragon_choice in ['1', '2', '3']:
                break
            else:
                print("Invalid choice, please choose 1, 2, or 3.")

        if dragon_choice == '1':
            print("You sneak up and attack, but the dragon wakes up and overpowers you.")
            print("You are defeated by the dragon.")
            print("Game Over. Try again.")
        elif dragon_choice == '2':
            print("You set a trap and lure the dragon into it, then finish it off with your sword.")
            print("The kingdom is saved and you are hailed as a hero.")
            print("Congratulations! You achieved a happy ending.")
        elif dragon_choice == '3':
            print("You wake the dragon and challenge it to a duel.")
            print("The dragon, amused by your bravery, accepts.")
            print("After a fierce battle, you find a weak spot and strike the dragon down.")
            print("The kingdom is saved and you are hailed as a hero.")
            print("Congratulations! You achieved a happy ending.")

elif weapon_choice == '2':
    print("You chose the Bow and Arrow! Perfect for a skilled marksman.")
    print("You head towards the dragon's lair in the mountains.")
    print("On the way, you encounter a wild beast blocking your path.")
    print("Do you:")
    print("1. Shoot the beast with your bow")
    print("2. Try to tame the beast")
    print("3. Avoid the beast by taking a different path")

    while True:
        action_choice = input("Enter the number of your choice: ")
        if action_choice in ['1', '2', '3']:
            break
        else:
            print("Invalid choice, please choose 1, 2, or 3.")

    if action_choice == '1':
        print("You shoot the beast with your bow and it flees.")
        print("You proceed to the dragon's lair and see it sleeping.")
        print("Do you:")
        print("1. Take a stealthy shot")
        print("2. Set a trap")
        print("3. Create a distraction")

        while True:
            dragon_choice = input("Enter the number of your choice: ")
            if dragon_choice in ['1', '2', '3']:
                break
            else:
                print("Invalid choice, please choose 1, 2, or 3.")

        if dragon_choice == '1':
            print("You take a stealthy shot and hit the dragon's weak spot, defeating it silently.")
            print("The kingdom is saved and you are hailed as a hero.")
            print("Congratulations! You achieved a happy ending.")
        elif dragon_choice == '2':
            print("You set a trap and lure the dragon into it, then finish it off with your arrows.")
            print("The kingdom is saved and you are hailed as a hero.")
            print("Congratulations! You achieved a happy ending.")
        elif dragon_choice == '3':
            print("You create a distraction to confuse the dragon and take a shot, but miss.")
            print("The dragon wakes up and defeats you.")
            print("You are defeated by the dragon.")
            print("Game Over. Try again.")
    elif action_choice == '2':
        print("You successfully tame the beast and it becomes your loyal companion.")
        print("With the beast's help, you reach the dragon's lair.")
        print("Do you:")
        print("1. Send the beast to distract the dragon")
        print("2. Attack together with the beast")
        print("3. Use the beast to scout ahead")

        while True:
            dragon_choice = input("Enter the number of your choice: ")
            if dragon_choice in ['1', '2', '3']:
                break
            else:
                print("Invalid choice, please choose 1, 2, or 3.")

        if dragon_choice == '1':
            print("You send the beast to distract the dragon and take advantage of the distraction to defeat it.")
            print("The kingdom is saved and you are hailed as a hero.")
            print("Congratulations! You achieved a happy ending.")
        elif dragon_choice == '2':
            print("You and the beast attack together, but the dragon overpowers both of you.")
            print("You are defeated by the dragon.")
            print("Game Over. Try again.")
        elif dragon_choice == '3':
            print("You use the beast to scout ahead and discover a hidden entrance to the dragon's lair.")
            print("You sneak in and take a shot at the dragon's weak spot, defeating it.")
            print("The kingdom is saved and you are hailed as a hero.")
            print("Congratulations! You achieved a happy ending.")
    elif action_choice == '3':
        print("You avoid the beast by taking a different path, but it leads you into a bandit ambush.")
        print("Do you:")
        print("1. Fight the bandits")
        print("2. Try to negotiate with the bandits")
        print("3. Attempt to escape")

        while True:
            bandit_choice = input("Enter the number of your choice: ")
            if bandit_choice in ['1', '2', '3']:
                break
            else:
                print("Invalid choice, please choose 1, 2, or 3.")

        if bandit_choice == '1':
            print("You fight the bandits but they outnumber and defeat you.")
            print("You are defeated by the bandits.")
            print("Game Over. Try again.")
        elif bandit_choice == '2':
            print("You successfully negotiate with the bandits, promising them a share of the dragon's treasure.")
            print("They let you pass and you reach the dragon's lair.")
            print("Do you:")
            print("1. Take a stealthy shot")
            print("2. Set a trap")
            print("3. Wait for the bandits to catch up and attack together")

            while True:
                dragon_choice = input("Enter the number of your choice: ")
                if dragon_choice in ['1', '2', '3']:
                    break
                else:
                    print("Invalid choice, please choose 1, 2, or 3.")

            if dragon_choice == '1':
                print("You take a stealthy shot and hit the dragon's weak spot, defeating it silently.")
                print("The kingdom is saved and you are hailed as a hero.")
                print("Congratulations! You achieved a happy ending.")
            elif dragon_choice == '2':
                print("You set a trap and lure the dragon into it, then finish it off with your arrows.")
                print("The kingdom is saved and you are hailed as a hero.")
                print("Congratulations! You achieved a happy ending.")
            elif dragon_choice == '3':
                print("You wait for the bandits to catch up, but they betray you and attack.")
                print("You are defeated by the bandits.")
                print("Game Over. Try again.")
        elif bandit_choice == '3':
            print("You attempt to escape but the bandits catch and defeat you.")
            print("You are defeated by the bandits.")
            print("Game Over. Try again.")

elif weapon_choice == '3':
    print("You chose the Magic Staff! Ideal for a wizard.")
    print("You travel to the dragon's lair through the enchanted forest.")
    print("A mystical barrier blocks your path.")
    print("Do you:")
    print("1. Use a dispel spell")
    print("2. Try to find a way around it")
    print("3. Use your staff to break the barrier")

    while True:
        barrier_choice = input("Enter the number of your choice: ")
        if barrier_choice in ['1', '2', '3']:
            break
        else:
            print("Invalid choice, please choose 1, 2, or 3.")

    if barrier_choice == '1':
        print("You successfully dispel the barrier and continue your journey.")
        print("You reach the dragon's lair and find it guarded by enchanted creatures.")
        print("Do you:")
        print("1. Use a sleep spell on the creatures")
        print("2. Fight the creatures with magic")
        print("3. Try to sneak past the creatures")

        while True:
            creature_choice = input("Enter the number of your choice: ")
            if creature_choice in ['1', '2', '3']:
                break
            else:
                print("Invalid choice, please choose 1, 2, or 3.")

        if creature_choice == '1':
            print("You use a sleep spell on the creatures and they fall asleep.")
            print("You quietly enter the dragon's lair and prepare for battle.")
            print("Do you:")
            print("1. Use a powerful fire spell")
            print("2. Use an ice spell to freeze the dragon")
            print("3. Summon a protective shield")

            while True:
                dragon_choice = input("Enter the number of your choice: ")
                if dragon_choice in ['1', '2', '3']:
                    break
                else:
                    print("Invalid choice, please choose 1, 2, or 3.")

            if dragon_choice == '1':
                print("You use a powerful fire spell, but the dragon is immune to fire.")
                print("The dragon defeats you.")
                print("You are defeated by the dragon.")
                print("Game Over. Try again.")
            elif dragon_choice == '2':
                print("You use an ice spell to freeze the dragon, making it vulnerable.")
                print("You then shatter the frozen dragon with your staff.")
                print("The kingdom is saved and you are hailed as a hero.")
                print("Congratulations! You achieved a happy ending.")
            elif dragon_choice == '3':
                print("You summon a protective shield, but it isn't strong enough to withstand the dragon's attack.")
                print("The dragon defeats you.")
                print("You are defeated by the dragon.")
                print("Game Over. Try again.")
        elif creature_choice == '2':
            print("You fight the creatures with magic but are overwhelmed by their numbers.")
            print("You are defeated by the creatures.")
            print("Game Over. Try again.")
        elif creature_choice == '3':
            print("You try to sneak past the creatures, but they detect you and attack.")
            print("You are defeated by the creatures.")
            print("Game Over. Try again.")
    elif barrier_choice == '2':
        print("You find a way around the barrier but it takes longer.")
        print("As night falls, you encounter a group of hostile wizards.")
        print("Do you:")
        print("1. Fight the wizards")
        print("2. Try to negotiate with them")
        print("3. Use an invisibility spell to escape")

        while True:
            wizard_choice = input("Enter the number of your choice: ")
            if wizard_choice in ['1', '2', '3']:
                break
            else:
                print("Invalid choice, please choose 1, 2, or 3.")

        if wizard_choice == '1':
            print("You fight the wizards with your staff and defeat them.")
            print("You continue your journey and reach the dragon's lair.")
            print("Do you:")
            print("1. Use a powerful lightning spell")
            print("2. Summon a magical creature to help you")
            print("3. Use an invisibility spell to surprise the dragon")

            while True:
                dragon_choice = input("Enter the number of your choice: ")
                if dragon_choice in ['1', '2', '3']:
                    break
                else:
                    print("Invalid choice, please choose 1, 2, or 3.")

            if dragon_choice == '1':
                print("You use a powerful lightning spell, but the dragon absorbs the energy and becomes stronger.")
                print("The dragon defeats you.")
                print("You are defeated by the dragon.")
                print("Game Over. Try again.")
            elif dragon_choice == '2':
                print("You summon a magical creature to help you and together you defeat the dragon.")
                print("The kingdom is saved and you are hailed as a hero.")
                print("Congratulations! You achieved a happy ending.")
            elif dragon_choice == '3':
                print("You use an invisibility spell to surprise the dragon and launch a surprise attack, defeating it.")
                print("The kingdom is saved and you are hailed as a hero.")
                print("Congratulations! You achieved a happy ending.")
        elif wizard_choice == '2':
            print("You try to negotiate with the wizards but they are not interested and attack you.")
            print("You are defeated by the wizards.")
            print("Game Over. Try again.")
        elif wizard_choice == '3':
            print("You use an invisibility spell to escape and continue your journey.")
            print("You reach the dragon's lair and find it unguarded.")
            print("Do you:")
            print("1. Use a powerful lightning spell")
            print("2. Summon a magical creature to help you")
            print("3. Use an invisibility spell to surprise the dragon")

            while True:
                dragon_choice = input("Enter the number of your choice: ")
                if dragon_choice in ['1', '2', '3']:
                    break
                else:
                    print("Invalid choice, please choose 1, 2, or 3.")

            if dragon_choice == '1':
                print("You use a powerful lightning spell, but the dragon absorbs the energy and becomes stronger.")
                print("The dragon defeats you.")
                print("You are defeated by the dragon.")
                print("Game Over. Try again.")
            elif dragon_choice == '2':
                print("You summon a magical creature to help you and together you defeat the dragon.")
                print("The kingdom is saved and you are hailed as a hero.")
                print("Congratulations! You achieved a happy ending.")
            elif dragon_choice == '3':
                print("You use an invisibility spell to surprise the dragon and launch a surprise attack, defeating it.")
                print("The kingdom is saved and you are hailed as a hero.")
                print("Congratulations! You achieved a happy ending.")
    elif barrier_choice == '3':
        print("You use your staff to break the barrier, but the magic backfires and injures you.")
        print("You are unable to continue your journey.")
        print("Game Over. Try again.")