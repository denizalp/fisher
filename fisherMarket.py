import cvxpy as cp
import numpy as np
import sys

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

class FisherMarket:
    """
    This is a class that models a Fisher Market

    Attributes:
        valutations (numpy: double x double):
            matrix of valuations of buyer i for good j.
        budgets (numpy: double): vector of buyer budgets.
        numGoodsVec (numpy: double): vector of number of each good.

    """

    def __init__(self, V, B, M = None):
        """
        The constructor for the fisherMarket class.

        Parameters:
        valuations (numpy: double x double): matrix of valuations of buyer i for good j.
        budgets (numpy: double): vector of buyer budgets.
        numGoodsVec (numpy: double): vector of number of each good.
        """
        self.budgets = B
        self.valuations = V

        if(M is None):
            self.numGoodsVec = np.ones(self.valuations.shape[1])
        else:
            self.numGoodsVec = M
            # # Add each copy of a good as a new good with the same valuation to the
            # # valuations matrix
            # self.valuations = np.empty((0,self.numberOfBuyers()))
            # for item, itemNumber in enumerate(self.numGoodsVec):
            #     self.valuations = np.append(self.valuations, np.tile(V[:,item], (itemNumber, 1)), axis =0)
            # self.valuations = self.valuations.T


    def getBudgets(self):
        """
        Returns:
        The budgets of the buyers in the market
        """
        return self.budgets

    def getValuations(self):
        """
        Returns:
        The valuation of buyers in the market
        """
        return self.valuations

    def numberOfGoods(self):
        """
        Returns:
        Number of goods in the market
        """
        return self.numGoodsVec.size

    def numberOfBuyers(self):
        """
        Returns:
        Number of buyers in the market
        """
        return self.budgets.size

    def getCache(self):
        """
        Returns:
        The cached alocation values (X, p)
        """
        return (self.optimalX, self.optimalp)

    def getDS(self, utilities = "quasi-linear"):
        """
        Takes as input the utility structure and returns the demand and supply
        (in dollars) of all goods in the economy.

        Parameters:
        utilities(string): Denotes the utilities used to solve market
            Currently options are 'quasi-linear' and 'linear'

        Returns:
        A tuple (D, S) of vector of demand and supply for each good.
        """
        # Find optimal allocation and cache it
        X,p = self.solveMarket(utilities, printResults = False)
        self.optimalX = X
        self.optimalp = p

        D = np.sum(X*p, axis = 0)
        assert D.size == self.numberOfGoods()

        S = np.multiply(self.numGoodsVec, p)
        if(S.size != self.numberOfGoods()):
            print(f"Size of supply: {S.size}\nNumber of Goods: {self.numberOfGoods()}")
        assert S.size == self.numberOfGoods()

        if((np.sum(np.abs(D-S)) > np.sum(np.abs(D))*0.001)):
            print(f"Demand: {D}\nSupply: {S}")
        assert (np.sum(np.abs(D-S)) < np.sum(np.abs(D))*0.001)

        if(((np.sum(D) - np.sum(self.getBudgets())) > np.sum(self.getBudgets())*0.001) or ((np.sum(X @ p) - np.sum(self.getBudgets())) > np.sum(self.getBudgets())*0.001)):
            print(f"Model money spent: {np.sum(D)}\nActual Money Present: {np.sum(self.getBudgets())}")

        assert  np.sum(D) - np.sum(self.getBudgets()) < np.sum(D)*0.001
        assert np.sum(X @ p) - np.sum(self.getBudgets()) < np.sum(X @ p)*0.001

        return (D, S)

    def solveMarket(self, utilities = "linear", printResults = True, rho = 1):
        """
        Parameters:
        utilities(string): Denotes the utilities used to solve market
            Currently options are 'quasi-linear' and 'linear'

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """
        if (utilities == "quasi-linear"):
            alloc, prices = self.solveQuasiLinear(printResults)
        elif (utilities == "linear"):
            alloc, prices = self.solveLinear(printResults)
        elif (utilities == "leontief"):
            alloc, prices = self.solveLeontief(printResults)
        elif (utilities == "cobb-douglas"):
            alloc, prices = self.solveCobbDouglas(printResults)
        elif (utilities == "ces"):
            alloc, prices = self.solveCES(rho, printResults)
        else:
            print(f"Invalid Utility Model : '{utilities}'")
            sys.exit()

        p = np.multiply(prices, (1/self.numGoodsVec))

        X = alloc * self.numGoodsVec

        numberOfEachGood = np.sum(X, axis = 0)

        if(printResults):
            print(f"Budgets of Consumers: {self.budgets}\nSpending of Consumers: {X @ p}")


        ##### Sanity Checks ##### 

        # Check that the market clears
        if(np.sum(np.abs(self.numGoodsVec - numberOfEachGood)) > 0.0001):
            print(f"Supply of Goods Vector: {self.numGoodsVec}\nNumber of Goods\
             Allocated: {numberOfEachGood}")


        # Check that the money spent by each buyer is less than their budget
        if(np.sum(X @ p - self.budgets) > np.sum(self.budgets)*0.0001):
            print(f"Money spent by buyers: {X @ p}\nBuyers' budgets: {self.budgets}")
        assert np.sum(X @ p - self.budgets) < np.sum(self.budgets)*0.0001


        return (X,p)


    def solveLinear(self, printResults = True):
        """
        Solves Fisher Market with Linear utilities

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """

        numberOfGoods = self.numberOfGoods()
        numberOfBuyers = self.numberOfBuyers()

        ########### Primal: Output => Allocation #########

        # Variables of program
        alloc = cp.Variable((numberOfBuyers, numberOfGoods))
        utils = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Maximize(self.budgets.T @ cp.log(utils))

        constraints = [utils <= cp.sum(cp.multiply(self.valuations, alloc), axis = 1),
                        cp.sum(alloc, axis = 0) <= 1,
                        alloc >= 0]

        # Convex Program for primal
        primal = cp.Problem(obj, constraints)


        # Solve Program
        primal.solve()  # Returns the optimal value.

        X = alloc.value

        # Get dual value directly from CVXPY
        p = constraints[1].dual_value
        if(printResults):
            print("Primal Status (Allocation):", primal.status)
            print(f"Allocation: {X}\nPrices: {p}")
            print(f"Value of Supply = {np.dot(self.numGoodsVec, p)}")

        return (X, p)


    def solveQuasiLinear(self, printResults = True):
        """
        Solves Fisher Market with Quasi-Linear utilities

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """
        numberOfGoods = self.numberOfGoods()
        numberOfBuyers = self.numberOfBuyers()

        ########### Primal: Output => Allocation #########

        # Variables of program
        alloc = cp.Variable((numberOfBuyers, numberOfGoods))
        values = cp.Variable(numberOfBuyers)
        utils = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Maximize(self.budgets.T @ cp.log(utils) - cp.sum(values))

        constraints = [utils <= (cp.sum(cp.multiply(self.valuations, alloc), axis = 1) + values),
                        cp.sum(alloc, axis = 0) <= 1,
                        alloc >= 0,
                        values >= 0]


        # Convex Program for dual
        dual = cp.Problem(obj, constraints)


        # Solve Program
        dual.solve()  # Returns the optimal value.

        # Get primal maximizer (allocations)
        X = alloc.value
        # Get dual maximizer (prices) directly from CVXPY
        p = constraints[1].dual_value
        
        
        if(printResults):
            print("Status of program:", dual.status)
            print(f"Allocation = {X}\nPrices = {p}")
            print(f"Sum of prices =  {np.sum(p)}\nPrices * Supply of goods = {np.dot(self.numGoodsVec, p)}")

        return (X, p)

    def solveLeontief(self, printResults):
        """
        Solves Fisher Market with Leontief utilities

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """
        numberOfGoods = self.numberOfGoods()
        numberOfBuyers = self.numberOfBuyers()

        ########### Primal: Output => Allocation #########

        # Variables of program
        alloc = cp.Variable((numberOfBuyers, numberOfGoods))
        utils = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Maximize(self.budgets.T @ cp.log(utils))

        utilConstraints = [(utils[buyer] <= ( alloc[buyer,good] / self.valuations[numberOfBuyers - buyer -1,good])) for good in range(numberOfGoods) for buyer in range(numberOfBuyers)]
        constraints = [ cp.sum(alloc, axis = 0) <= 1,
                        alloc >= 0]
        constraints =  constraints + utilConstraints

        # Convex Program for dual
        primal = cp.Problem(obj, constraints)

        # Solve Program
        primal.solve()  # Returns the optimal value.

        # Get primal maximizer
        X = alloc.value
        # Get dual value (for prices) directly from CVXPY
        p = constraints[0].dual_value
        
        #### Print Option ####
        if(printResults):
            print("Status of program:", primal.status)
            print(f"Allocation = {X}\nPrices = {p}")
            print(f"Sum of prices =  {np.sum(p)}\nPrices * Supply of goods = {np.dot(self.numGoodsVec, p)}")
    
        return (X,p)

    def solveCobbDouglas(self, printResults):
        """
        Solves Fisher Market with Cobb-Douglas utilities

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """

        numberOfGoods = self.numberOfGoods()
        numberOfBuyers = self.numberOfBuyers()

        ########### Primal: Output => Allocation #########

        # Variables of program
        alloc = cp.Variable((numberOfBuyers, numberOfGoods))

        # Objective
        obj = cp.Maximize(self.budgets.T @ cp.sum(cp.multiply(self.valuations, cp.log(alloc)), axis = 1))

        constraints = [ cp.sum(alloc, axis = 0) <= 1,
                        alloc >= 0]

        # Convex Program for primal
        primal = cp.Problem(obj, constraints)


        # Solve Program
        primal.solve()  # Returns the optimal value.

        X = alloc.value

        # Get dual value directly from CVXPY
        p = constraints[0].dual_value
        if(printResults):
            print("Primal Status (Allocation):", primal.status)
            print(f"Allocation: {X}\nPrices: {p}")
            print(f"Value of Supply = {np.dot(self.numGoodsVec, p)}")

        return (X, p)


    def solveCES(self, rho, printResults = True):
        """
        Solves Fisher Market with Linear utilities

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """

        numberOfGoods = self.numberOfGoods()
        numberOfBuyers = self.numberOfBuyers()

        ########### Primal: Output => Allocation #########

        # Variables of program
        alloc = cp.Variable((numberOfBuyers, numberOfGoods))

        # Objective
        obj = cp.Maximize(self.budgets.T @ ((1/rho)*cp.log(cp.sum(cp.multiply(self.valuations, cp.power(alloc, rho)), axis = 1))))

        constraints = [ cp.sum(alloc, axis = 0) <= 1,
                        alloc >= 0]

        # Convex Program for primal
        primal = cp.Problem(obj, constraints)


        # Solve Program
        primal.solve()  # Returns the optimal value.

        X = alloc.value

        # Get dual value directly from CVXPY
        p = constraints[0].dual_value
        if(printResults):
            print("Primal Status (Allocation):", primal.status)
            print(f"Allocation: {X}\nPrices: {p}")
            print(f"Value of Supply = {np.dot(self.numGoodsVec, p)}")

        return (X, p)