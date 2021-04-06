try: 
    from tester import format_output
    import os
except:
    pass

def lab3_ren(screen, *args):
    command = "REN"
    if args[0]:
        command += ' ' + ' '.join(args[0])

    result = format_output(command)
           
    screen.current_screen = result
