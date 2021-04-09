try: 
    from format_ou import format_output
    import os
except:
    pass

def lab3_echo(screen, *args):
    command = "ECHO"
    if args[0]:
        command += ' ' + ' '.join(args[0])

    result = format_output(command)
           
    screen.current_screen = result