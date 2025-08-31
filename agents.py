import random
import time


class Agent:
    ident = 0

    def __init__(self):
        self.id = Agent.ident
        Agent.ident += 1

    def get_chosen_action(self, state, max_depth):
        pass


class RandomAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        actions = state.get_legal_actions()
        return actions[random.randint(0, len(actions) - 1)]


class GreedyAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        actions = state.get_legal_actions()
        best_score, best_action = None, None
        for action in actions:
            new_state = state.generate_successor_state(action)
            score = new_state.get_score(state.get_on_move_chr())
            if (best_score is None and best_action is None) or score > best_score:
                best_action = action
                best_score = score
        return best_action

# todo implement here 
class MinimaxAgent(Agent):

    def minimax(self, player_max, curr_depth, state, max_depth, root_player):
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
                score = max(score, MinimaxAgent.minimax(self,False, curr_depth + 1, possible_state, max_depth, root_player))
            return score
        else:
            score = float('inf')
        for my_action in possible_actions:
            possible_state = state.generate_successor_state(my_action)
            score = min(score, MinimaxAgent.minimax(self,True, curr_depth + 1, possible_state, max_depth, root_player))
        return score

    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        possible_actions = state.get_legal_actions()

        if len(possible_actions) == 0:
            return None

        best_score = float('-inf')
        next_action = possible_actions[0]
        root_player = state.get_on_move_chr()
        # starting as a MAX player, this is first iteration because we want to return the action associated with it
        for action in possible_actions:
            possible_state = state.generate_successor_state(action)
            curr_score = MinimaxAgent.minimax(self, False, 1, possible_state, max_depth, root_player)
            if curr_score > best_score:
                best_score = curr_score
                next_action = action

        return next_action


# start with player_max == TRUE!
# todo what is start depth?? ajde recimo da je 1 za sad...
