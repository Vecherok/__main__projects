import textwrap as tw


str_width = input(f'input width of the string:\n')
while not str_width.isdigit() or not int(str_width) > 35: 
    str_width = input('wrong input, give me only digits and width should be more than 35\n')
    continue
else:
    with open ('text.txt', 'r') as text:
        t = text.read()
    with open ('text_new', 'w') as text_new:
        text_new.write(tw.fill(t, width = int(str_width)))

    
        



