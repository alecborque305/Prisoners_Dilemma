####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'ABID' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
import random
    
def move(my_history, their_history, my_score, their_score):

    if 'b' in their_history[-10:]: # If the other player has betrayed within last 10 rounds, 
        return 'b'               # Betray.
    else:
        if random.random()<0.1: # 10% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'         # but 90% of the time collude
