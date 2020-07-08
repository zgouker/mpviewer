import ctypes
from mem_edit import Process

def find_pj64():
    pid = Process.get_pid_by_name('Project64-MPN.exe')
    return pid