import pytest


def test_account(sol):
    """B1-B3: account construction, valid operations and rejected amounts preserve balance."""
    account = sol.Account("A1")
    assert account.GetAccountNumber() == "A1"
    assert account.GetBalance() == pytest.approx(0.0, abs=1e-9)
    assert account.Deposit(100.0) is True
    assert account.Withdraw(30.0) is True
    assert account.GetBalance() == pytest.approx(70.0, abs=1e-9)
    assert account.Withdraw(80) is False
    assert account.Deposit(0) is False
    assert account.Deposit(-5) is False
    assert account.Withdraw(0) is False
    assert account.GetBalance() == pytest.approx(70.0, abs=1e-9)


def test_interest_and_withdrawal_limit(sol):
    """B4-B5: inherited deposit, interest and two successful withdrawals, then rejection."""
    account = sol.SavingsAccount("S1", 0.05)
    assert account.Deposit(200) is True
    account.AddInterest()
    assert account.GetBalance() == pytest.approx(210.0, abs=1e-9)
    assert [account.Withdraw(10) for _ in range(3)] == [True, True, False]
    assert account.GetBalance() == pytest.approx(190.0, abs=1e-9)
    assert account.GetWithdrawalsLeft() == 0


def test_failed_withdrawal_keeps_allowance(sol):
    """B6: insufficient funds consume no allowance; subsequent two withdrawals succeed."""
    account = sol.SavingsAccount("S2", 0.1)
    assert account.Deposit(50) is True
    assert account.Withdraw(100) is False
    assert account.GetWithdrawalsLeft() == 2
    assert [account.Withdraw(10) for _ in range(3)] == [True, True, False]
    assert account.GetBalance() == pytest.approx(30.0, abs=1e-9)


def test_zero_interest(sol):
    """B7: zero balance yields zero interest without error."""
    account = sol.SavingsAccount("S3", 0.05)
    account.AddInterest()
    assert account.GetBalance() == pytest.approx(0.0, abs=1e-9)


def test_inheritance_and_attributes(sol):
    """B8: savings account is an Account with exactly the specified parent/child private fields."""
    account = sol.SavingsAccount("S1", 0.05)
    assert isinstance(account, sol.Account)
    assert set(vars(account)) == {"_Account__AccountNumber", "_Account__Balance", "_SavingsAccount__InterestRate", "_SavingsAccount__WithdrawalsLeft"}
