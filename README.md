# Fisher Market Solver 
Fisher markets and associated solvers. A market is built in fisherMarket.py. You can declare parameters of the market in fisherExample.py and solve for market prices depending on the type of utility function you would like to use using the structure in fisherExample.py.

The project currently supports "linear" and "quasi-linear" utilities. You can solve the market with the function solveMarket() and passing it as argument the utility structure you desire as a string:

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,3,5,1,2], [2,5,6,2,6],
    [6,3,5,1,4], [3,3,4,2,6]])

# Budgets of buyers: |buyers|
budgets = np.array([20, 23, 54, 12])

# Vector with quantity of goods: |goods|
numGoodsVec = np.array([1,2,6,4,3])

# Create Market
market1 = m.Market(valuations, budgets, numGoodsVec)

# Solve for market prices and allocations for
# desired utility function structure.

# Current Options are 'quasi-linear' and 'linear'
market1.solveMarket("quasi-linear")
market1.solveMarket("linear")

