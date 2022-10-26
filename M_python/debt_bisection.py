
def debt_bisection(balance, annualInterestRate):
    monthlyPaymentRate = 0.5
    new_balance = balance
    low = 0.0
    high = 1.0
    
    while abs(new_balance - 0) > 0.001:
        for i in range(12):
            monthly_interest_rate = annualInterestRate / 12.0
            monthly_unpaid_balance = new_balance - balance*monthlyPaymentRate
            new_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        
        if abs(new_balance - 0) < 0.001:
            break
        
        elif new_balance > 0:
            new_balance = balance
            low = monthlyPaymentRate
            monthlyPaymentRate = (low + high) / 2
    
        elif new_balance < 0:
            new_balance = balance
            high = monthlyPaymentRate
            monthlyPaymentRate = (low + high) / 2
        
    
    payment = round(monthlyPaymentRate*balance, 2)
    print(f"Lowest payment: {str(payment)}")


debt_bisection(999999, 0.18)