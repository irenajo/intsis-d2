def max_n(self,curr_depth, max_depth, state):

    if state.is_goal_state() or curr_depth == max_depth:
        return state.get_scores()
    
    score_list = {chr(ord('A')+i): float('-inf') for i in range(state.get_num_of_players())}
    possible_moves = state.get_legal_actions()
    player_chr = state.get_on_move_chr()

    for action in possible_moves:
        child_score_list = max_n(curr_depth+1, max_depth, state.generate_successor_state(action))
        score_list = score_list if score_list[player_chr] >= child_score_list[player_chr] else child_score_list   
    return score_list 


def get_chosen_action(self, state, max_depth):
    time.sleep(0.5)
    possible_actions = state.get_legal_actions()

    if len(possible_actions) == 0:
        return None
    
    score_list = {chr(ord('A')+i): float('-inf') for i in range(state.get_num_of_players())}
    next_action = possible_actions[0]
    player_chr = state.get_on_move_chr()

    for action in possible_actions:    
        child_score_list = max_n(1, max_depth, state.generate_successor_state(action))
        if child_score_list[player_chr] > score_list[player_chr]:
            next_action = action
            score_list = child_score_list

    return next_action