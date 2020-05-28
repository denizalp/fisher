#%%
# Import libraries
import numpy as np
import cvxpy as cp
import fisherMarket as m
import test.fisherVerifier as fv


#%% [markdown]
# # Example

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1, 2, 3], [3, 2, 1]])

# Budgets of buyers: |buyers|
budgets = np.array([1, 1])

# Vector with quantity of goods: |goods|
# numGoodsVec = np.array([1,2,6,4,3])

# Create Market
market = m.FisherMarket(valuations, budgets)

# Solve for market prices and allocations for desired utility function structure.

# Current Options are 'quasi-linear' and 'linear'

X, p = market.solveMarket("linear", printResults=False)

fv.verify(X, p, valuations, budgets, utility = "linear")







# %%
