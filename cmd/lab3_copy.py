try: 
    from format_ou import format_output
    import os
except:
    pass

def lab3_copy(screen, *args):
    command = "COPY"
    if args[0]:
        command += ' ' + ' '.join(args[0])

    result = format_output(command)
           
    screen.current_screen = result