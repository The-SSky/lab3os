try: 
    import subprocess
except:
    pass

def lab3_cd(screen, *args):
    result = subprocess.Popen("CD", shell=True, stdout=subprocess.PIPE).stdout
    screen.current_screen = result
