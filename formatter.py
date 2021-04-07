import subprocess
import pprint

def format_output(command):
    getVersion =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    version =  getVersion.read()

    result = version.decode(encoding="cp866")
    return result

arguments = {
    "/?" : "",
    "CD" : "",
    "CHDIR" : "",
    "CLS" : "",
    "COPY" : "",
    "DIR" : "",
    "DEL" : "",
    "ECHO" : "",
    "ERASE" : "",
    "HELP" : "",
    "MD" : "",
    "MKDIR" : "",
    "MOVE" : "",
    "RD" : "",
    "REN" : "",
    "RENAME" : "",
    "REPLACE" : "",
    "RMDIR" : "",
    "TYPE" : ""
}
