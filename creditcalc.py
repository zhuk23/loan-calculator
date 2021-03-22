import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--interest")
parser.add_argument("--periods")
parser.add_argument("--payment")

args = parser.parse_args()
if args.type == 'diff' and args.payment is not None:
    print('Incorrect parameters')
elif args.interest is None:
    print('Incorrect parameters')
elif args.type is None or (args.type != "annuity" and args.type != "diff"):
    print('Incorrect parameters')
else:
    i = float(args.interest) / (12 * 100)

    if args.type == 'diff':
        principal = int(args.principal)
        periods = int(args.periods)
        sum = 0
        for m in range(periods):
            result = int(math.ceil((principal / periods) + i * (principal - ((principal * m) / periods))))
            sum += int(result)
            print('Month {}: payment is {}'.format(m + 1, result))
        print('\nOverpayment = {}'.format(sum - principal))

    if args.type == 'annuity':
        if args.principal is None:
            periods = int(args.periods)
            ann = int(args.payment)
            result = int(ann / ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1)))
            print('Your loan principal = {}!'.format(result))
            print('Overpayment = {}'.format((ann * periods) - result))
        elif args.periods is None:
            loan = int(args.principal)
            pay = int(args.payment)
            n = math.ceil(math.log(pay / (pay - (i * loan)), 1 + i))
            if n % 12 == 0:
                print('It will take {} years to repay this loan!'.format(int(n / 12)))
            elif int(n) < 12:
                print('It will take {} months to repay this loan!'.format(int(n)))
            elif int(n) <= 1:
                print('It will take 1 month to repay this loan!')
            elif int(n) == 12:
                print('It will take 1 year to repay this loan!')
            else:
                print('It will take {} years and {} months to repay this loan!'.format(int(n / 12), math.ceil(n % 12)))
            print('Overpayment = {}'.format((pay * n) - loan))
        elif args.payment is None:
            periods = int(args.periods)
            loan = int(args.principal)
            result = loan * ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1))
            print('Your annuity payment = {}!'.format((math.ceil(result) * periods) - loan))
            print('Overpayment = {}'.format(math.ceil(result)))



