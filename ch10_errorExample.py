import traceback, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def spam():
    bacon()

def bacon():
    try:
        raise Exception('This is error.')
    except:
        errorFile = open('hello.txt', 'a')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('Traceback written to hello.txt')

spam()