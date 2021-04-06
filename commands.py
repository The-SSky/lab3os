from cmd.lab3_type import lab3_type
from cmd.lab3_rmdir import lab3_rmdir
from cmd.lab3_replace import lab3_replace
from cmd.lab3_ren import lab3_ren
from cmd.lab3_rd import lab3_rd
from cmd.lab3_move import lab3_move
from cmd.lab3_md import lab3_md
from cmd.lab3_exit import lab3_exit
from cmd.lab3_erase import lab3_erase
from cmd.lab3_echo import lab3_echo
from cmd.lab3_dir import lab3_dir
from cmd.lab3_del import lab3_del
from cmd.lab3_copy import lab3_copy
from cmd.lab3_help import lab3_help
from cmd.lab3_cls import lab3_cls
from cmd.lab3_cd import lab3_cd


commands = {
    "CD" : lab3_cd,
    "CHDIR" : lab3_cd,
    "CLS" : lab3_cls,
    "COPY" : lab3_copy,
    "DEL" : lab3_del,
    "DIR" : lab3_dir,
    "ECHO" : lab3_echo,
    "ERASE" : lab3_erase,
    "EXIT" : lab3_exit,
    "HELP" : lab3_help,
    "MD" : lab3_md,
    "MKDIR" : lab3_md,
    "MOVE" : lab3_move,
    "RD" : lab3_rd,
    "REN" : lab3_ren,
    "RENAME" : lab3_ren,
    "REPLACE" : lab3_replace,
    "RMDIR" : lab3_rmdir,
    "TYPE" : lab3_type,
}

