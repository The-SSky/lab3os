try: 
    from tester import format_output
    import os
except:
    pass

def lab3_rmdir(screen, *args):
    command = "RMDIR"
    if args[0]:
        command += ' ' + ' '.join(args[0])

    result = format_output(command)
           
    screen.current_screen = result
    