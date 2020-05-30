#%%
# Import libraries
import numpy as np
import cvxpy as cp
import fisherMarket as m
import test.fisherVerifier as fv



#%% [markdown]
# # Example: Linear

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [1,  2], [2, 1], [2, 1]])


# Budgets of buyers: |buyers|
budgets = np.array([100, 100, 100, 100])

# Vector with quantity of goods: |goods|
# numGoodsVec = np.array([1,2,6,4,3])

# Create Market
market = m.FisherMarket(valuations, budgets)

# Solve for market prices and allocations for desired utility function structure.

# Current Options are 'quasi-linear' and 'linear'

X, p = market.solveMarket("linear", printResults=True)

fv.verify(X, p, valuations, budgets, utility = "linear")

#%% [markdown]
# # Example: Leontief

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [1,  2], [2, 1], [2, 1]])


# Budgets of buyers: |buyers|
budgets = np.array([100, 100, 100, 100])

# Vector with quantity of goods: |goods|
# numGoodsVec = np.array([1,2,6,4,3])

# Create Market
market = m.FisherMarket(valuations, budgets)

# Solve for market prices and allocations for desired utility function structure.

# Current Options are 'quasi-linear' and 'linear'

X, p = market.solveMarket("leontief", printResults=True)

fv.verify(X, p, valuations, budgets, utility = "leontief")


#%% [markdown]
# # Example: CES utilities with rho = .5

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [1,  2], [2, 1], [2, 1]])


# Budgets of buyers: |buyers|
budgets = np.array([100, 100, 100, 100])

# Vector with quantity of goods: |goods|
# numGoodsVec = np.array([1,2,6,4,3])

# Create Market
market = m.FisherMarket(valuations, budgets)

# Solve for market prices and allocations for desired utility function structure.

# Current Options are 'quasi-linear' and 'linear'

X, p = market.solveMarket("ces", printResults=True, rho = 0.5)

fv.verify(X, p, valuations, budgets, utility = "ces", rho = 0.5)



#%% [markdown]
# # Example 4: Cobb-Douglas

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [1,  2], [2, 1], [2, 1]])/3


# Budgets of buyers: |buyers|
budgets = np.array([100, 100, 100, 100])

# Vector with quantity of goods: |goods|
# numGoodsVec = np.array([1,2,6,4,3])

# Create Market
market = m.FisherMarket(valuations, budgets)

# Solve for market prices and allocations for desired utility function structure.

# Current Options are 'quasi-linear' and 'linear'

X, p = market.solveMarket("cobb-douglas", printResults=True)

fv.verify(X, p, valuations, budgets, utility = "cobb-douglas")






# %%
