from math import ceil, floor, log


def calculating_overpayment(p: float, n: int, a: float) -> None:
    """
    Calculating overpayment as follows: the amount of interest paid over the whole term of the loan
    :param p: loan principal
    :param n: number of payments
    :param a: annuity payment
    :return: overpayment
    """
    overpayment = a * n - p
    print(f"Overpayment = {ceil(overpayment)}")


def calculating_differentiated_payments(p: float, n: int, i: float) -> None:
    """
    Calculating differentiated payments by the formula:
    d = p / n + i * (p - p * (m - 1) / n)
    :param p: loan principal
    :param n: number of payments
    :param i: nominal interest rate
    :return: differentiated payments
    """
    total_of_all_payments = 0
    for current_repayment_month in range(1, n + 1):
        m = current_repayment_month
        differentiated_payments = ceil(p / n + i * (p - p * (m - 1) / n))
        total_of_all_payments += differentiated_payments
        print(f"Month {current_repayment_month}: payment is {differentiated_payments}")

    print(f"\nOverpayment = {int(total_of_all_payments - p)}")


def calculation_of_loan_principal(a: float, n: int, i: float) -> int:
    """
    Calculation of loan principal by the formula:
    p = a * ((1 + i)^n - 1) / (i * (1 + i)^n)
    :param a: annuity payment
    :param n: number of payments
    :param i: nominal interest rate
    :return: loan principal
    """
    i_n = (1 + i) ** n
    loan_principal = floor(a * (i_n - 1) / (i * i_n))
    print(f"Your loan principal = {loan_principal}!")

    return loan_principal


def calculation_of_annuity_payment(p: float, n: int, i: float) -> int:
    """
    Calculation of annuity payments by the formula:
    a = p * (i * (1 + i)^n) / ((1 + i)^n - 1)
    :param p: loan principal
    :param n: number of payments
    :param i: nominal interest rate
    :return: annuity payment
    """
    i_n = (1 + i) ** n
    annuity_payment = ceil(p * (i * i_n) / (i_n - 1))
    print(f"Your annuity payment = {annuity_payment}!")

    return annuity_payment


def calculation_of_the_period(months: int) -> None:
    years = months // 12
    number_of_months = months % 12

    if months == 1:
        print(f"It will take {months} month to repay the loan")
    elif years == 0:
        print(f"It will take {months} months to repay the loan")
    elif number_of_months == 0:
        print(f"It will take {years} years to repay this loan!")
    elif number_of_months == 1:
        print(f"It will take {years} years and {number_of_months} month to repay this loan!")
    else:
        print(f"It will take {years} years and {number_of_months} months to repay this loan!")


def calculate_the_number_of_payments(a: float, p: float, i: float) -> int:
    """
    Calculation of number of payments by the formula:
    n = log_1+i_(a / (a - i * p))
    :param a: annuity payment
    :param p: loan principal
    :param i: nominal interest rate
    :return: number of payments
    """
    base_log = 1 + i
    number = a / (a - i * p)
    logarithm = log(number, base_log)

    return ceil(logarithm)


def get_a_nominal_interest_rate(interest: float) -> float:
    i = 12 * 100

    return interest / i