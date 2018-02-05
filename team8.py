####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Integer' # Only 10 chars displayed.
strategy_name = 'Colude first rounds, then betray if no betrayed.'
strategy_description = ''
''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'.
    '''
    
def number_rounds(history):
    if len(history) >= 100:
        hundred = True
        return hundred
    
    
def move(my_history, their_history, my_score, their_score):
    if 'cc' in their_history:
        return 'b'
    elif 'b' in their_history:
        return 'b'
    else:
        return 'c'
    if 'bc' in their_history:
        return 'c'
    number_rounds(my_history)
        
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    


              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.

              
              
