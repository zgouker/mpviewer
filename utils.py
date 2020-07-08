import ctypes, configparser
from mem_edit import Process

def get_pid64():
    pid = Process.get_pid_by_name('Project64-MPN.exe')
    return pid
    
def get_offsets(game):
    offset_dict = {}
    config = configparser.ConfigParser()
    config.read('offsets.ini')
    
    offset_dict['chara_list'] = config[game]['chara_list'].split(',')
    offset_dict['chara_offset'] = int(config[game]['char_offset'])
    offset_dict['coin_offset'] = int(config[game]['coin_offset'])
    offset_dict['max_offset'] =  = int(config[game]['max_offset'])
    offset_dict['minigame_offset'] =  = int(config[game]['minigame_offset'])
    offset_dict['happening_offset'] =  = int(config[game]['happening_offset'])
    offset_dict['player_offset'] =  = int(config[game]['player_offset'])
    
    return offset_dict

def init(game):
    pid = get_pid64()
    offsets = get_offsets(game)
    return (pid,offsets)
