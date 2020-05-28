import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir) 
sys.path.insert(0,parentdir) 
import unittest
import cvxpy as cp
import numpy as np
import fisherVerifier
import fisherMarket

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        """
        Example in the Eisenberg-Gale paper:
        Consensus of Subjective Probabilities: The Pari-Mutuel Method on JSTOR
        https://www.jstor.org/stable/2237130?casa_token=O576M6_fWzsAAAAA:QqMHo9vTXEQa1Q7X-dUkPDaNSneFLzhTmChI6XWKVFMgh6GE8iwI4x-vmezbE1fe4-KDKcsVPJBK1OmcSCgIVYmQ8Uv2SljiTxTp3Ur264Pwmn8Kzp0g&socuuid=8a7880bd-edae-4c49-b540-73ea19e69fba&socplat=twitter
        """
        valuations = np.array([[10.85, 10.5], [0.5, 0.5]])
        budgets = np.array([1, 1])
        m1 = fisherMarket.FisherMarket(valuations, budgets)
        X, p = m1.solveMarket("linear", printResults=False)
        print(X)
        print(p)

    def test_markets(self, num_consumers=20, num_goods=20, num_trials=10, tolerance=1e-2):
        """
        Test num_trials many i.i.d. random markets with num_consumers many consumers and num_goods many goods.
        For each market, compute its equilibria as a fisher (linear) market. Then, fixing the equilibria price vector,
        compute for each consumer its utility maximizing bundle. The utility of the later computation should equal
        the utility of the equilibria computation. We check equality up to given tolerance.
        :param num_consumers: the number of consumers. Default is 20.
        :param num_goods: the number of goods. Default is 20.
        :param num_trials: the number of random, i.i.d. markets.
        """
        for trial in range(num_trials):
            try:
                # Matrix of valuations: |buyers| x |goods|
                valuations = np.random.rand(num_consumers, num_goods)

                # Budgets of buyers: |buyers|
                budgets = np.random.rand(num_consumers)

                # Create Market
                market = fisherMarket.FisherMarket(valuations, budgets)
                X, p = market.solveMarket("linear", printResults=False)
                print(f"\n ***** Trial {trial} *****")
                print(f"Input market: \n U \n {valuations} \n budgets \n  {budgets}")
                print(f"\nSolution: \n X \n {X}  \n p \n {p}")
                print(f"\nUtilities: \n ")
                consumer_eq_utility = {}
                for consumer_index, u in enumerate(np.sum(np.multiply(X, valuations), axis=1)):
                    print(f"{consumer_index}'s optimal utility is {u}")
                    consumer_eq_utility[consumer_index] = u

                for consumer_index in range(0, num_consumers):
                    u = valuations[consumer_index]
                    budget = budgets[consumer_index]
                    max_u = fisherVerifer.compute_util_max_bundle(u, p, budget, "linear")
                    error = abs(max_u - consumer_eq_utility[consumer_index])
                    print(f"{consumer_index}'s consumer error is {error:.12f}")
                    assert error <= tolerance

            except cp.error.SolverError:
                print("IGNORING")


if __name__ == '__main__':
    unittest.main()
