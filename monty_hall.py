import random

input_choice = input()


def run(input_choice, doors):
    chosen_door = random.randint(1, doors)
    if input_choice:
        revealed_door = 3 if chosen_door==2 else 2
        available_doors = [dnum for dnum in range(1,doors+1)
                                if dnum not in (chosen_door, revealed_door)]
        chosen_door = random.choice(available_doors)
    return chosen_door == 1

def run_trials(trials, input_choice , doors):

    wins = 0
    for i in range(trials):
        if run(input_choice, doors):
            wins += 1
    return (wins/trials)*100



print(run_trials(10000,input_choice,3))




