

print("==============Lending Calculator=================")


loanAmount = float(input("Enter loan amount:"))
loanInterest = float(input("Enter loan interest:"))/100
loanNumPayments = int(input("Enter number of loan payments:"))

print("\ncalculating loan amount per pay period\n")

amountPerPay = loanAmount/loanNumPayments * \
    loanInterest+loanAmount/loanNumPayments

print("\n number of payents:", loanNumPayments)
print("\n amount per pay:", round(amountPerPay, 2))
print("\n interest charged:", round(loanAmount/loanNumPayments*loanInterest, 2))
print("\n total payout:", round(amountPerPay*loanNumPayments, 2))

