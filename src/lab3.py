try:
    import os
except:
    pass

def parse_path(path_str):
    """
    """
    path_str = path_str.replace('\\', '/', -1)
    if len(path_str[path_str.rfind('/') + 1:]):
        foldername = path_str[:path_str.rfind('/') + 1]
        filename = path_str[path_str.rfind('/') + 1:]
    else:
        filename = path_str[:-1]
        foldername = filename[:filename.rfind('/') + 1]
        filename = filename[filename.rfind('/') + 1:]
    return foldername, filename

def correct_file_length(path_str):
    foldername, filename = parse_path(path_str)
    if len(filename) > 255:
        if filename.rfind('.') == -1:
            filename = filename[:255] + '~'
        else:
            name = filename[:filename.rfind('.')] 
            ext = filename[filename.rfind('.'):]
            length = 255 - len(ext)
            filename = name[:length] + '~' + ext
    return foldername + filename


def get_folder_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size // 1024