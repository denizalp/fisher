import cvxpy as cp
import numpy as np


def verify(X, p, V, b, utility, M = None):
    """
    Given and allocation of goods, prices, valuations and utility types, check if
    a pair of allocation and prices satisfy conditions for a competitive
    equilibrium, that is 1) supply_j * p_j >= demand_j * p_j and 2) the
    allocation is envy free.
    Inputs:
    X : A matrix of allocations (size: |buyers| x |goods|)
    p : A vector of prices for goods (size: |goods|)
    V : A matrix of valuations (size: |buyers| x |goods| )
    b : A vector of budgets (size: |buyers|)
    utility: The type of utilty function
    M : Number of goods
    Returns:
    Boolean: True if (X, p) form a CE for valuations V and budgets b,
    false otherwise
    """
    numberOfBuyers, numberOfGoods = V.shape

    alloc = np.zeros((numberOfBuyers, numberOfGoods))
    for i in range(numberOfBuyers):
        alloc[i,:] = compute_util_max_bundle(V[i,:], p, b[i], utility)
        
    print(f"Input Allocation:\n{X}\nVerifier Allocation:\n{alloc}")

def compute_util_max_bundle(valuation, prices, budget, utility = "linear"):
    """
    Given a vector of consumer valuations, v, a price vector, p, and a budget, compute the utility
    of a utility-maximizing bundle. Mathematically, solve the linear program:
    max_{x} xv
    s.t. xp <= budget
    :param valuation: a consumer's valuation for goods.
    :param prices: prices of goods.
    :param budget: the consumer's budget
    :return:
    """
  
    num_items = len(valuation)
    x = cp.Variable(num_items)
    
    if (utility == "linear"):
        obj = cp.Maximize(x.T @ valuation)

    else:
        obj = cp.Maximize(x.T @ (valuation - prices))

    prob = cp.Problem(obj,
                      [x.T @ prices <= budget,
                       x >= 0])
    prob.solve()
    return x.value
