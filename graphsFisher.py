#%%
import fisherMarket as m
import matplotlib.pyplot as plt
import numpy as np



############################### Example 1 ######################################

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1, 2, 3], [3, 2, 1]])

# Budgets of buyers: |buyers|
budgets = np.array([0.0, 10.0])

iter = 0
prices = []
budgets0 = []
budgets1 = []
while(iter <= 100):
    iter += 1


    # Create Market
    market1 = m.FisherMarket(valuations, budgets)

    # Solve for market prices and allocations for desired utility function structure.

    # Current Options are 'quasi-linear' and 'linear'
    Q, p = market1.solveMarket("linear", printResults = False)

    prices.append(p)
    budgets0.append(budgets[0])
    budgets1.append(budgets[1])

    # print(f"budget[0] = {budgets[0]}\nbudget[1] = {budgets[1]}")
    budgets[0] += 0.1
    budgets[1] -= 0.1

prices = np.array(prices)
fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets0, prices[:,0], "-g", label = "Good 1")
ax1.plot(budgets0, prices[:,1], "-b", label = "Good 2")
ax1.plot(budgets0, prices[:,2], "-r", label = "Good 3")
plt.title("Linear: Prices vs Budget of Buyer 1\nValuations: [1, 2, 3]")
plt.xlabel("Budget of Buyer 1")
plt.ylabel("Prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets1, prices[:,0], "-g", label = "Good 1")
ax2.plot(budgets1, prices[:,1], "-b", label = "Good 2")
ax2.plot(budgets1, prices[:,2], "-r", label = "Good 3")
plt.title("Linear: Prices vs Budget of Buyer 2\nValuations: [3, 2, 1]")
plt.xlabel("Budget of Buyer 2")
plt.ylabel("Prices")
plt.legend()
plt.savefig("graph1.png")






############################### Example 2 ######################################

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[5, 2, 1], [4, 2, 3]])

# Budgets of buyers: |buyers|
budgets = np.array([0.0, 10.0])

iter = 0
prices = []
budgets0 = []
budgets1 = []
while(iter <= 100):
    iter += 1


    # Create Market
    market1 = m.FisherMarket(valuations, budgets)

    # Solve for market prices and allocations for desired utility function structure.

    # Current Options are 'quasi-linear' and 'linear'
    Q, p = market1.solveMarket("linear", printResults = False)

    prices.append(p)
    budgets0.append(budgets[0])
    budgets1.append(budgets[1])

    # print(f"budget[0] = {budgets[0]}\nbudget[1] = {budgets[1]}")
    budgets[0] += 0.1
    budgets[1] -= 0.1

prices = np.array(prices)
fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets0, prices[:,0], "-g", label = "Good 1")
ax1.plot(budgets0, prices[:,1], "-b", label = "Good 2")
ax1.plot(budgets0, prices[:,2], "-r", label = "Good 3")
plt.title("Linear: Prices vs Budget of Buyer 1\nValuations: [5 , 2, 1]")
plt.xlabel("Budget of Buyer 1")
plt.ylabel("Prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets1, prices[:,0], "-g", label = "Good 1")
ax2.plot(budgets1, prices[:,1], "-b", label = "Good 2")
ax2.plot(budgets1, prices[:,2], "-r", label = "Good 3")
plt.title("Linear: Prices vs Budget of Buyer 2\nValuations: [4 , 2, 3]")
plt.xlabel("Budget of Buyer 2")
plt.ylabel("Prices")
plt.legend()
plt.savefig("graph2.png")



############################### Example 3 : When goods are not good ######################################

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[2, 0, 1], [0, 2, 1]])

# Budgets of buyers: |buyers|
budgets = np.array([0.0, 10.0])

iter = 0
prices = []
budgets0 = []
budgets1 = []
while(iter <= 100):
    iter += 1


    # Create Market
    market1 = m.FisherMarket(valuations, budgets)

    # Solve for market prices and allocations for desired utility function structure.

    # Current Options are 'quasi-linear' and 'linear'
    Q, p = market1.solveMarket("linear", printResults = False)

    prices.append(p)
    budgets0.append(budgets[0])
    budgets1.append(budgets[1])

    # print(f"budget[0] = {budgets[0]}\nbudget[1] = {budgets[1]}")
    budgets[0] += 0.1
    budgets[1] -= 0.1

prices = np.array(prices)
fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets0, prices[:,0], "-g", label = "Good 1")
ax1.plot(budgets0, prices[:,1], "-b", label = "Good 2")
ax1.plot(budgets0, prices[:,2], "-r", label = "Good 3")
plt.title("Linear: Prices vs Budget of Buyer 1\nValuations: [2, 0, 1]")
plt.xlabel("Budget of Buyer 1")
plt.ylabel("Prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets1, prices[:,0], "-g", label = "Good 1")
ax2.plot(budgets1, prices[:,1], "-b", label = "Good 2")
ax2.plot(budgets1, prices[:,2], "-r", label = "Good 3")
plt.title("Linear: Prices vs Budget of Buyer 2\nValuations: [0, 2, 1]")
plt.xlabel("Budget of Buyer 2")
plt.ylabel("Prices")
plt.legend()
plt.savefig("graph3.png")


####################### Quasilinear #######################

############################### Example 1 ######################################

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1, 2, 3], [3, 2, 1]])

# Budgets of buyers: |buyers|
budgets = np.array([0.0, 10.0])

iter = 0
prices = []
budgets0 = []
budgets1 = []
while(iter <= 100):
    iter += 1


    # Create Market
    market1 = m.FisherMarket(valuations, budgets)

    # Solve for market prices and allocations for desired utility function structure.

    # Current Options are 'quasi-linear' and 'linear'
    Q, p = market1.solveMarket("quasi-linear", printResults = False)

    prices.append(p)
    budgets0.append(budgets[0])
    budgets1.append(budgets[1])

    # print(f"budget[0] = {budgets[0]}\nbudget[1] = {budgets[1]}")
    budgets[0] += 0.1
    budgets[1] -= 0.1

prices = np.array(prices)
fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets0, prices[:,0], "-g", label = "Good 1")
ax1.plot(budgets0, prices[:,1], "-b", label = "Good 2")
ax1.plot(budgets0, prices[:,2], "-r", label = "Good 3")
plt.title("Quasi: Prices vs Budget of Buyer 1\nValuations: [1, 2, 3]")
plt.xlabel("Budget of Buyer 1")
plt.ylabel("Prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets1, prices[:,0], "-g", label = "Good 1")
ax2.plot(budgets1, prices[:,1], "-b", label = "Good 2")
ax2.plot(budgets1, prices[:,2], "-r", label = "Good 3")
plt.title("Prices vs Budget of Buyer 2\nValuations: [3, 2, 1]")
plt.xlabel("Budget of Buyer 2")
plt.ylabel("Prices")
plt.legend()
plt.savefig("graph4.png")




############################### Example 2 ######################################

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[5, 2, 1], [4, 2, 3]])

# Budgets of buyers: |buyers|
budgets = np.array([0.0, 10.0])

iter = 0
prices = []
budgets0 = []
budgets1 = []
while(iter <= 100):
    iter += 1


    # Create Market
    market1 = m.FisherMarket(valuations, budgets)

    # Solve for market prices and allocations for desired utility function structure.

    # Current Options are 'quasi-linear' and 'linear'
    Q, p = market1.solveMarket("quasi-linear", printResults = False)

    prices.append(p)
    budgets0.append(budgets[0])
    budgets1.append(budgets[1])

    # print(f"budget[0] = {budgets[0]}\nbudget[1] = {budgets[1]}")
    budgets[0] += 0.1
    budgets[1] -= 0.1

prices = np.array(prices)
fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets0, prices[:,0], "-g", label = "Good 1")
ax1.plot(budgets0, prices[:,1], "-b", label = "Good 2")
ax1.plot(budgets0, prices[:,2], "-r", label = "Good 3")
plt.title("Quasi: Prices vs Budget of Buyer 1\nValuations: [5, 2, 1]")
plt.xlabel("Budget of Buyer 1")
plt.ylabel("Prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets1, prices[:,0], "-g", label = "Good 1")
ax2.plot(budgets1, prices[:,1], "-b", label = "Good 2")
ax2.plot(budgets1, prices[:,2], "-r", label = "Good 3")
plt.title("Quasi: Prices vs Budget of Buyer 2\nValuations: [4, 2, 3]")
plt.xlabel("Budget of Buyer 2")
plt.ylabel("Prices")
plt.legend()
plt.savefig("graph5.png")




############################### Example 3 : When goods are not good ######################################

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[2, 0, 1], [0, 2, 1]])

# Budgets of buyers: |buyers|
budgets = np.array([0.0, 10.0])

iter = 0
prices = []
budgets0 = []
budgets1 = []
while(iter <= 100):
    iter += 1


    # Create Market
    market1 = m.FisherMarket(valuations, budgets)

    # Solve for market prices and allocations for desired utility function structure.

    # Current Options are 'quasi-linear' and 'linear'
    Q, p = market1.solveMarket("quasi-linear", printResults = False)

    prices.append(p)
    budgets0.append(budgets[0])
    budgets1.append(budgets[1])

    # print(f"budget[0] = {budgets[0]}\nbudget[1] = {budgets[1]}")
    budgets[0] += 0.1
    budgets[1] -= 0.1

prices = np.array(prices)
fig = plt.figure(figsize = (12,10))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets0, prices[:,0], "-g", label = "Good 1")
ax1.plot(budgets0, prices[:,1], "-b", label = "Good 2")
ax1.plot(budgets0, prices[:,2], "-r", label = "Good 3")
plt.title("Quasi: Prices vs Budget of Buyer 1\nValuations: [2, 0, 1]")
plt.xlabel("Budget of Buyer 1")
plt.ylabel("Prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets1, prices[:,0], "-g", label = "Good 1")
ax2.plot(budgets1, prices[:,1], "-b", label = "Good 2")
ax2.plot(budgets1, prices[:,2], "-r", label = "Good 3")
plt.title("Quasi: Prices vs Budget of Buyer 2\nValuations: [0, 2, 1]")
plt.xlabel("Budget of Buyer 2")
plt.ylabel("Prices")
plt.legend()
plt.savefig("graph6.png")



############################### Example 4 : More than 2 buyers ######################################

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])

# Budgets of buyers: |buyers|
budgets = np.array([10.0, 0.0, 0.0])

iter = 0
prices = []
budgets0 = []
budgets1 = []
budgets2 = []
while(iter <= 100):
    iter += 1


    # Create Market
    market1 = m.FisherMarket(valuations, budgets)

    # Solve for market prices and allocations for desired utility function structure.

    # Current Options are 'quasi-linear' and 'linear'
    Q, p = market1.solveMarket("quasi-linear", printResults = False)

    prices.append(p)
    budgets0.append(budgets[0])
    budgets1.append(budgets[1])
    budgets2.append(budgets[2])

    # print(f"budget[0] = {budgets[0]}\nbudget[1] = {budgets[1]}")
    budgets[0] -= 0.1
    budgets[1] += 0.05
    budgets[2] += 0.05

prices = np.array(prices)
fig = plt.figure(figsize = (12,4))
ax1 = plt.subplot(1, 3, 1)
ax1.plot(budgets0, prices[:,0], "-g", label = "Good 1")
ax1.plot(budgets0, prices[:,1], "-b", label = "Good 2")
ax1.plot(budgets0, prices[:,2], "--r", label = "Good 3")
plt.title("Quasi: Prices vs Budget of Buyer 1\nValuations: [2, 1, 1]")
plt.xlabel("Budget of Buyer 1")
plt.ylabel("Prices")

ax2 = plt.subplot(1, 3, 2)
ax2.plot(budgets1, prices[:,0], "-g", label = "Good 1")
ax2.plot(budgets1, prices[:,1], "-b", label = "Good 2")
ax2.plot(budgets1, prices[:,2], "--r", label = "Good 3")
plt.title("Quasi: Prices vs Budget of Buyer 2\nValuations: [1, 2, 1]")
plt.xlabel("Budget of Buyer 2")
plt.ylabel("Prices")

ax3 = plt.subplot(1, 3, 3)
ax3.plot(budgets2, prices[:,0], "-g", label = "Good 1")
ax3.plot(budgets2, prices[:,1], "-b", label = "Good 2")
ax3.plot(budgets2, prices[:,2], "--r", label = "Good 3")
plt.title("Quasi: Prices vs Budget of Buyer 3\nValuations: [1, 1, 2]")
plt.xlabel("Budget of Buyer 3")
plt.ylabel("Prices")
plt.legend()
plt.savefig("graph7.png")

############## Individual Markets of The economy example  ##################

############################### Example 1 ######################################

# Matrix of valuations: |buyers| x |goods|
# Matrix of valuations of buyers/workers: |buyers| x |goods|
demandV = np.array([[8.0, 2.0], [2.0, 5.0]])

# Matrix of valuations of firms: |firms| x |workers|
supplyV = np.array([[5.0, 3.0], [1.0, 5.0]])

# Budgets of firms: |buyers|
budgets = np.array([0.0, 10.0])

iter = 0
prices = []
wages = []
budgets0 = []
budgets1 = []
while(iter <= 100):
    iter += 1


    # Create Market
    demand = m.FisherMarket(demandV, budgets)
    supply =  m.FisherMarket(supplyV, budgets)
    # Solve for market prices and allocations for desired utility function structure.

    # Current Options are 'quasi-linear' and 'linear'
    Q, p = demand.solveMarket("linear", printResults = False)
    X, w = supply.solveMarket("linear", printResults = False)
    wages.append(w)
    prices.append(p)
    budgets0.append(budgets[0])
    budgets1.append(budgets[1])

    # print(f"budget[0] = {budgets[0]}\nbudget[1] = {budgets[1]}")
    budgets[0] += 0.1
    budgets[1] -= 0.1

prices = np.array(prices)
fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets0, prices[:,0], "-g", label = "Good 1")
ax1.plot(budgets0, prices[:,1], "-b", label = "Good 2")
plt.title("Linear: Prices vs Budget of Buyer 1\nValuations: [8.0, 2.0], [2.0, 5.0]")
plt.xlabel("Budget of Buyer 1")
plt.ylabel("Prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets1, prices[:,0], "-g", label = "Good 1")
ax2.plot(budgets1, prices[:,1], "-b", label = "Good 2")
plt.title("Linear: Prices vs Budget of Buyer 2\nValuations: [8.0, 2.0], [2.0, 5.0]")
plt.xlabel("Budget of Buyer 2")
plt.ylabel("Wages")
plt.legend()

wages = np.array(wages)
fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets0, wages[:,0], "-g", label = "Good 1")
ax1.plot(budgets0, wages[:,1], "-b", label = "Good 2")
plt.title("Linear: Wages vs Budget of Firms 1\nValuations: [5.0, 3.0], [1.0, 5.0]")
plt.xlabel("Budget of firm 1")
plt.ylabel("Prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets1, wages[:,0], "-g", label = "Good 1")
ax2.plot(budgets1, wages[:,1], "-b", label = "Good 2")
plt.title("Linear: Wages vs Budget of Firms 2\nValuations: [5.0, 3.0], [1.0, 5.0]")
plt.xlabel("Budget of firm 2")
plt.ylabel("Prices")
plt.legend()


# %%
