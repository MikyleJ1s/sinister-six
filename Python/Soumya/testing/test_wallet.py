import unittest
import wallet

class Test_Wallet(unittest.TestCase):
    def test_initialisation(self):
        wall = wallet.Wallet()
        self.assertEqual(wall.balance, 0)
    def test_add_cash(self):
        wall = wallet.Wallet()
        wall.add_cash(10)
        self.assertEqual(wall.balance, 10)
    def test_spending(self):
        wall = wallet.Wallet()
        wall.add_cash(10)
        wall.spend_cash(2)
        self.assertEqual(wall.balance, 8)

if __name__ == '__main__':
    unittest.main()
    
    
'''
import pytest
import wallet
@pytest.mark.parametrize("earned, spend, expected", [
    (10,5,5),
    (23,3,20),
    (4,2,4),
    (30,28,2),
    ])
def test_transaction(earned, spent, expected):
    wallet = wallet.Wallet()
    wallet.add_cash(earned)
    wallet.spend_cash(spent)
    assert wallet.balance == expected
'''



'''

import wallet
import unittest
class Test_TestWallet(unittest.TestCase):
    def test_walletInitNone(self):
        desireeWallet = wallet.Wallet()
        self.assertEqual(desireeWallet.balance,0)
    def test_walletInitVal(self):
        kyleWallet = wallet.Wallet(1000)
        self.assertEqual(kyleWallet.balance,1000)
    def test_walletSpendValid(self):
        desireeWallet = wallet.Wallet(500)
        desireeWallet.spend_cash(50)
        self.assertEqual(desireeWallet.balance, 450)
    def test_walletSpendInvalid(self):
        vukosiWallet = wallet.Wallet(500)
        with self.assertRaises(wallet.InsufficientAmount):
            vukosiWallet.spend_cash(501)
    def test_walletDep(self):
        desireeWallet = wallet.Wallet()
        desireeWallet.deposit(1000)
        self.assertEqual(desireeWallet.balance, 1000)

if __name__ == '__main__':
    unittest.main()

'''