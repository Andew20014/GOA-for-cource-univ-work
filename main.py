import numpy as np

# GOA
from pyMetaheuristic.algorithm import grasshopper_optimization_algorithm
from pyMetaheuristic.algorithm.goa import target_function
from pyMetaheuristic.utils import graphs


# Target Function - It can be any function that needs to be minimize, However it has to have only one argument: 'variables_values'. This Argument must be a list of variables.
# For Instance, suppose that our Target Function is the Easom Function (With two variables x1 and x2. Global Minimum f(x1, x2) = -1 for, x1 = 3.14 and x2 = 3.14)

# Target Function: Easom Function
##lims(-5, 5) step 0.1
#def easom(variables_values = [0, 0]):
#    x1, x2     = variables_values
#    func_value = -(-np.cos(x1) * np.sin(x2) * np.exp(-(x2 - np.pi) ** 2 - (x1 - np.pi) ** 2))
#    return func_value
##lims(-6, 6) step 0.1
#def easom(x):
#    x = x[0]
#    func_value = np.sin(x - 8) ** 2 + (x / 5) ** 2 - 5
#    return func_value
#lims(-2 2), step 0.05
def easom(variable_values = [0, 0]):
    x1, x2 = variable_values
    func_value = -20 * np.exp(-0.2 * np.sqrt(1/2 * (x1 ** 2 + x2 ** 2)))- np.exp(1/2 * (np.cos(2 * np.pi * x1) +np.cos(2 * np.pi * x2)))+ 20 + np.exp(1)
    return func_value

# Limits and dimensions
dims = 3
min_v = (-4, -4)
max_v = (4, 4)
step = (0.05, 0.05)
dim = '3D'
iters = 100

# Target Function - Values
plot_parameters = {
    'min_values': min_v,
    'max_values': max_v,
    'step': step,
    'solution': [],
    'proj_view': dim,
    'view': 'notebook'
}
graphs.plot_single_function(target_function = easom, **plot_parameters)

# GOA - Parameters
parameters = {
    'grasshoppers': 50,
    'min_values': min_v,
    'max_values': max_v,
    'iterations': iters,
    'c_min': 0.00004,
    'c_max': 1,
    'F': 0.5,
    'L': 1.5,
    'verbose': True
}

# GOA - Algorithm
goa = grasshopper_optimization_algorithm(target_function = easom, **parameters)

# GOA - Solution
variables = goa[-1][0][:-1]
minimum   = goa[-1][0][ -1]
sol = goa[0]

print('Variables: ', np.around(variables, 4) , ' Minimum Value Found: ', round(minimum, 4) )

# GOA - Plot Solution
#for sol in goa[:-1]:
#    plot_parameters = {
#        'min_values': min_v,
#        'max_values': max_v,
#        'step': step,
#        'solution': [sol],
#        'proj_view': dim,
#        'view': 'notebook'
#    }
#    graphs.my_plot_single_function(target_function = easom, **plot_parameters)


sol = goa[-1]
goa = np.array(goa[:-1])
steps = goa.reshape((goa.shape[0] * goa.shape[1], dims))

plot_parameters = {
    'min_values': min_v,
    'max_values': max_v,
    'step': step,
    'steps': steps,
    'solution': [sol],
    'proj_view': dim,
    'view': 'notebook'
    }
graphs.full_plot(target_function = easom, **plot_parameters)