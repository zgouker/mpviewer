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

def calibrate(coins,offsets,pid):
    buffer0 = (ctypes.c_byte * 1)(0)
    player_offset = int(offsets['player_offset'])
    
    with Process.open_process(pid) as p:
        addrs = p.search_all_memory(ctypes.c_int(coins[0]))
        new_addrs = []
        for addr in addrs:
            p2_addr = addr+player_offset
            p.read_memory(p2_addr,buffer0)
            if(buffer0[0]==coins[1]):
                new_addrs.append(addr)

        addrs = new_addrs.copy()
        new_addrs = []
        for addr in addrs:
            p3_addr = addr+(player_offset*2)
            p.read_memory(p3_addr,buffer0)
            if(buffer0[0]==coins[2]):
                new_addrs.append(addr)

        addrs = new_addrs.copy()
        new_addrs = []
        for addr in addrs:
            p4_addr = addr+(player_offset*3)
            p.read_memory(p4_addr,buffer0)
            if(buffer0[0]==coins[3]):
                new_addrs.append(addr)

        if(len(new_addrs)==0):
            pass #no addresses found error
        elif(len(new_addrs)>1):
            pass #too many addresses found error
        elif(len(new_addrs)==1):
            address = new_addrs[0]
    return address

def init(game,coins):
    pid = get_pid64()
    offsets = get_offsets(game)
    address = calibrate(coins,offsets,pid)
    return (pid,offsets,address)