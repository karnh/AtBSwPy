#! python3
# mcb.pyw - Saves and load pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipbaord to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyowrd to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Delete saved keyword.
#        py.exe mcb.pyw delete - delete all saved keywords.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print('saved: ' + str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # TODO: List keywords and load contents
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()