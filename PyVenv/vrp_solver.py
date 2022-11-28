
import vrp_solver_lp
import vrp_solver_ortools

def solve_lp(vrp):
    return vrp_solver_lp.solve(vrp)

def solve_ortools(vrp):
    return vrp_solver_ortools.solve(vrp)