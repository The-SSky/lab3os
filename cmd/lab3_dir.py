try: 
    from tester import format_output
    import os
except:
    pass

def lab3_dir(screen, *args):
    command = "DIR"
    if args[0]:
        command += ' ' + ' '.join(args[0])
    else:
        command += screen.cwd

    result = format_output(command)
           
    screen.current_screen = result