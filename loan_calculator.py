def calculate_loan_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    if monthly_rate == 0:
        monthly_payment = principal / num_payments
    else:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
    return monthly_payment


def main():
    print("=== Loan Calculator ===")
    principal = float(input("Enter the loan amount (£): "))
    annual_rate = float(input("Enter the annual interest rate (%): "))
    years = int(input("Enter the loan term (in years): "))

    payment = calculate_loan_payment(principal, annual_rate, years)
    total_payment = payment * years * 12

    print(f"\nMonthly payment: £{payment:.2f}")
    print(f"Total payment over {years} years: £{total_payment:.2f}")


if __name__ == "__main__":
    main()
