def minimax_alpha_beta(node, player, alpha, beta):
    if is_terminal_node(node):
        return node_evaluation(node)
    
    if player == Player.MAX:
        score = -math.inf
        for succ in node.successors():
            score = max(score, minimax_alpha_beta(succ, Player.MIN, alpha, beta))
            alpha = max(alpha, score)
            if alpha >= beta: 
                break # alpha-cut
        return score
    else:
        score = +math.inf
        for succ in node.successors():
            score = min(score, minimax_alpha_beta(succ, Player.MAX, alpha, beta))
            beta = min(beta, score)
            if alpha >= beta:
                break # beta-cut
    return score

