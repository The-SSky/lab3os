try: 
    import os
except:
    pass

def lab3_cd(screen, *args):

    if args[0]:
        path = ' '.join(args[0])
        if os.path.isdir(path):
            screen.current_screen = '\n'
            screen.cwd = path
        else:
            screen.current_screen = "Системе не удается найти указанный путь."
           
    else:
        screen.current_screen = screen.cwd
