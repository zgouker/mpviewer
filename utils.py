import ctypes, configparser
from mem_edit import Process

def get_pid64():
    pid = Process.get_pid_by_name('Project64-MPN.exe')
    return pid
    
def get_offsets(game):
    offset_dict = {}
    config = configparser.ConfigParser()
    config.read('offsets.ini')
    
    offset_dict = dict(config.items(game))
    
    return offset_dict

def init(game):
    pid = get_pid64()
    offsets = get_offsets(game)
    return (pid,offsets)
