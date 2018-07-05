import pyperclip

text = pyperclip.paste()
print('Received text: ' + text)

input_text_lines = text.split('\n')

output_text = ''
for i in range(len(input_text_lines)):
    if input_text_lines[i].strip() != '':
        input_text_lines[i] = '* ' + input_text_lines[i]
    else:
        input_text_lines[i] = input_text_lines[i]

text = '\n'.join(input_text_lines)
print('Pasting to clipboard: ' + text)

pyperclip.copy(text)
print('Formatted text is now available clipboard.')
