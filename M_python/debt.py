from math import ceil


def debt(balance, annualInterestRate):
    monthlyPaymentRate = 0.01
    new_balance = balance
    
    while new_balance > 0:
        new_balance = balance
        for _ in range(12):
            monthly_interest_rate = annualInterestRate / 12.0
            monthly_unpaid_balance = new_balance - balance*monthlyPaymentRate
            new_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        
        monthlyPaymentRate = monthlyPaymentRate + 0.0001
    
    payment = monthlyPaymentRate*balance
    payment_round = ceil(payment/10) * 10
    print(f"Lowest payment: {str(payment_round)}")


debt(3329, 0.20)