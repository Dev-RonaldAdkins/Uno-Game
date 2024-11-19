
def main():
    sales = get_sales()

    advanced_pay = get_advanced_pay()

    comm_rate = determine_commission_rate(sales)

    pay = sales * comm_rate - advanced_pay

    print("The pay is $", format(pay, ',.2f'), sep='')

    if pay < 0:
        print("The Salesperon must reimburse the company.")


def get_sales():
    monthly_sales = float(input("Enter the monthly sales: "))
    return monthly_sales

def get_advanced_pay():
    print("Enter the amount of advanced pay, or enter 0 if no advanced pay was given.")
    advanced = float(input("Advanced pay: "))
    return advanced

def determine_commission_rate(sales):
    if sales < 10000.00:
        rate = 0.1
    elif sales >= 10000 and sales < 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales < 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales < 21999.99:
        rate = 0.16
    else:
        rate = 0.18
    return rate

main()





                                 



