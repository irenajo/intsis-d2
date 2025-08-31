
class MinimaxABAgent(Agent):

    def minimax(self, player_max, curr_depth, state, max_depth, root_player, alpha, beta):
        if state.is_goal_state() or curr_depth == max_depth:
            # reached end - get score
            if root_player == 'A':
                return (state.get_score('A') - state.get_score('B'))
            else:
                return (state.get_score('B') - state.get_score('A'))

        # have not reached end
        possible_actions = state.get_legal_actions()

        if player_max == True:
            score = float('-inf')
            for my_action in possible_actions:
                possible_state = state.generate_successor_state(my_action)
                score = max(score, MinimaxAgent.minimax(self,False, curr_depth + 1, possible_state, max_depth, root_player, alpha, beta))
                alpha = max(alpha, score)
                if alpha >= beta: 
                    break 
            return score
        else:
            score = float('inf')
            for my_action in possible_actions:
                possible_state = state.generate_successor_state(my_action)
                score = min(score, MinimaxAgent.minimax(self,True, curr_depth + 1, possible_state, max_depth, root_player,alpha,beta))
                beta = min(beta, score)
                if alpha >= beta:
                    break 
        return score

    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        possible_actions = state.get_legal_actions()

        if len(possible_actions) == 0:
            return None

        alpha = float('-inf')
        beta = float('inf')
        best_score = float('-inf')
        next_action = possible_actions[0]
        root_player = state.get_on_move_chr()
        # starting as a MAX player, this is first iteration because we want to return the action associated with it
        for action in possible_actions:
            possible_state = state.generate_successor_state(action)
            curr_score = MinimaxAgent.minimax(self, False, 1, possible_state, max_depth, root_player, alpha, beta)
            if curr_score > best_score:
                best_score = curr_score
                next_action = action
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break # beta-cut
        return next_action
