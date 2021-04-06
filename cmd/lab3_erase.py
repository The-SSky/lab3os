try: 
    from tester import format_output
    import os
except:
    pass

def lab3_erase(screen, *args):
    command = "ERASE"
    if args[0]:
        command += ' ' + ' '.join(args[0])

    result = format_output(command)
           
    screen.current_screen = result
    