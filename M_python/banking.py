
def banking(balance, annualInterestRate, monthlyPaymentRate):
    
    for i in range(12):
        
        monthly_interest_rate = annualInterestRate / 12.0
        monthly_unpaid_balance = balance - balance*monthlyPaymentRate
        balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        print(f"{i+1}: {round(balance, 2)}")

banking(484, 0.2, 0.04)