import os

def searchlines(start,search_keyword, lines=0, header=True, begin_start=None):
    if header:
        print('{:>10} |{:>10} | {:<20} | {:<20}'.format('ADDED', 'TOTAL', 'FILE', 'FOUND'))
        print('{:->11}|{:->11}|{:->20}|{:->20}'.format('', '', '',''))

    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isfile(thing):
            if thing.endswith('.py'):
                with open(thing, 'r') as f:
                    newlines = f.readlines()
                    temp_str=' '.join(newlines)
                    
                    newlines = len(newlines)
                    lines += newlines

                    found=False

                    if search_keyword in temp_str:
                        found=True
                        
                    if begin_start is not None:
                        reldir_of_thing = '.' + thing.replace(begin_start, '')
                    else:
                        reldir_of_thing = '.' + thing.replace(start, '')

                    print('{:>10} |{:>10} | {:<20} | {:<20}'.format(
                            newlines, lines, reldir_of_thing,str(found)))


    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isdir(thing):
            lines = countlines(thing, lines, header=False, begin_start=start)

    return lines
a=searchlines('.','name')
print('\n\nTotal Lines in this folder is: ',a)
