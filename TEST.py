max_depth = 3

# start with player_max == TRUE!
# todo what is start depth?? ajde recimo da je 1 za sad...
def minimax(player_max : bool, curr_depth : int, state):
    if curr_depth == max_depth:
        # reached end - get score
        return state.get_score(state.get_on_move_char())

    # have not reached end
    possible_actions = state.get_legal_actions()

    if player_max == True:
        score = float('-inf')
        for my_action in possible_actions:
            possible_state = state.generate_successor_state(my_action)
            score = max(score, minimax(False, curr_depth + 1, possible_state))
        return score
    else:
        score = float('inf')
    for my_action in possible_actions:
        possible_state = state.generate_successor_state(my_action)
        score = min(score, minimax(True, curr_depth + 1, possible_state))
    return score


def get_chosen_action(state, max_depth):
    time.sleep(0.5)
    possible_actions = state.get_legal_actions()
    score = float('-inf')
    next_action = [] # todo what is a valid no-action?
    # starting as a MAX player, this is first iteration because we want to return the action associated with it
    for action in possible_actions:
        possible_state = state.generate_successor_state(action)
        possible_score = self.minimax(False, 1, possible_state, max_depth)
        if possible_score > score:
            score = possible_score
            next_action = action

    return next_action