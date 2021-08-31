from modules.algorithms.metaheuristics.slime_mould_based.slimeMouldSolution import SlimeMouldSolution
from modules.algorithms.metaheuristics.metaheuristic import Metaheuristic

class SlimeMould(Metaheuristic):
    """docstring for SlimeMould."""
    
    def __init__(self, max_efos):
        super(SlimeMould, self).__init__()        
        self.max_efos = max_efos
    
    def execute(self, the_knapsack, the_aleatory, debug):
        self.my_knapsack = the_knapsack
        self.my_aleatory = the_aleatory
        self.current_efos = 0
        s = SlimeMouldSolution.init_owner(self)
        s.random_initialization()
        self.curve.append(s.fitness)
        while self.current_efos < self.max_efos and abs(s.fitness - self.my_knapsack.objective) > 1e-10: