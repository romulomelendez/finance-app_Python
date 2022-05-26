import yfinance as yf


def set_line(size=50):
    return '-' * size


def header(text):
    print(set_line())
    print(text.center(50))
    print(set_line())


def menu(list_menu, mensage):
    header(mensage)
    print('Choose a Option:')
    c = 1
    for item in list_menu:
        print(f'{c}) {item}')
        c += 1
    print('\n{}'.format(set_line()))


menu(['SHOW ACTIONS', 'SHOW SPLITS ONLY', 'SHOW DIVIDENDS ONLY', 'SHOW CASHFLOW'], 'Finance Console App')


def get_stock_info(action):
    return yf.Ticker(action)


def show_splits(action):
    response = get_stock_info(action)
    print(response.splits)


def show_dividens(action):
    response = get_stock_info(action)
    print(response.dividends)


def show_cashflow(action):
    response = get_stock_info(action)
    print(response.cashflow)


def show_actions(action):
    # historical = actions.history(period="max")
    action_info = get_stock_info(action)
    print(action_info.actions)


def switch(selected_option):
    global array_actions

    match selected_option:

        case 1:
            menu(array_actions, 'ACTIONS')
            action = int(input('Choose your actions: '))
            show_actions(array_actions[action - 1])

        case 2:
            menu(array_actions, 'ACTIONS')
            action = int(input('Choose your actions: '))
            show_splits(array_actions[action - 1])

        case 3:
            menu(array_actions, 'ACTIONS')
            action = int(input('Choose your actions: '))
            show_dividens(array_actions[action - 1])

        case 4:
            menu(array_actions, 'ACTIONS')
            action = int(input('Choose your actions: '))
            show_cashflow(array_actions[action - 1])


if __name__ == '__main__':
    menu_item = int(input('Your option here: '))
    array_actions = ['MSFT', 'AAPL', 'SONY', 'DIS', 'PBR']

    # building a Switch Case
    switch(menu_item)
