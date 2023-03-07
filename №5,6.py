plus = int(input('Profit: '))
minus = int(input('Costs: '))
people = int(input('Users: '))
if plus > minus:
    print('Revenue is more than costs:')
    clear_plus = plus - minus
    rent = clear_plus/plus
    print('Profitability {} revenue {}: {:.2f}' .format('our','made up',rent))
    clear_for_person = float(clear_plus/people)
    print('The companys profit per employee: %s'%clear_for_person)
else:
    print('The company operates at a loss')