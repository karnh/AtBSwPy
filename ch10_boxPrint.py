def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol should be 1 char long.')
    if width <= 2:
        raise Exception('Widthe must be > 2')
    if height <=2:
        raise Exception('Height must be > 2')

    print((symbol + ' ') * width)
    for i in range((height - 2)):
        print(symbol + (' ' * (2 * (width -2) + 1)) + symbol)
    print((symbol + ' ') * width)

for sym, w, h in (('*', 4, 4),('0',20,5),('x',1,3),('ZZ',3,3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception occurred: {}'.format(str(err)))