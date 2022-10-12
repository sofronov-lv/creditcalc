import argparse

import creditcalc


def type_of_loan_calculation(t: str, a: float, p: float, n: int, i: float) -> None:
    """
    Selecting a loan using the type and other input parameters
    :param t: payment type
    :param a: annuity payment
    :param p: loan principal
    :param n: number of payments
    :param i: nominal interest rate
    :return: None
    """
    if t == "annuity":
        if all((p, n)):
            a = creditcalc.calculation_of_annuity_payment(p, n, i)
        elif all((a, n)):
            p = creditcalc.calculation_of_loan_principal(a, n, i)
        elif all((a, p)):
            n = creditcalc.calculate_the_number_of_payments(a, p, i)
            creditcalc.calculation_of_the_period(n)
        else:
            checking_args()

        creditcalc.calculating_overpayment(p, n, a)

    elif t == "diff" and all((p, n)):
        creditcalc.calculating_differentiated_payments(p, n, i)  # overpayment is calculated separately
    else:
        checking_args()


def checking_args():
    print("Incorrect parameters")
    exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description='''
                                                 Gets information about the loan using the following parameters:
                                                    differentiated payments = (-t="diff", -pl, -ps, -i);
                                                    loan principal = (-t="annuity", -pt, -ps, -i);
                                                    annuity payment = (-t="annuity",-pl, -ps, -i);
                                                    number of payments = (-t="annuity",-pt, -pl, -i);
                                                 ''')
    parser.add_argument("-t", "--type", choices=["annuity", "diff"], type=str)
    parser.add_argument("-pt", "--payment", type=float, help='Accepts the "float" data type '
                                                             'and is a annuity payment')
    parser.add_argument("-pl", "--principal", type=float, help='Accepts the "float" data type '
                                                               'and is a loan principal')
    parser.add_argument("-ps", "--periods", type=int, help='Accepts the "int" data type '
                                                           'and is a number of payments')
    parser.add_argument("-i", "--interest", type=float, help='Accepts the "float" data type '
                                                             'is specified without a percent sign!')

    args = parser.parse_args()

    payment_type = args.type
    annuity_payment = args.payment
    loan_principal = args.principal
    number_of_payments = args.periods

    if args.interest is not None:
        nominal_interest_rate = creditcalc.get_a_nominal_interest_rate(args.interest)
        type_of_loan_calculation(payment_type, annuity_payment, loan_principal,
                                 number_of_payments, nominal_interest_rate)
    else:
        checking_args()


if __name__ == "__main__":
    main()
