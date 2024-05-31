import time
import os
import subprocess
import threading
import json
from datetime import datetime



def load_config():
    with open('config.json', encoding='utf-8') as config_file:
        return json.load(config_file)

def read_chat_log():
    config = load_config()
    chat_log_path = os.path.expanduser(config["CHAT_LOG_PATH"])
    
    # Verifica se o arquivo de log existe
    if not os.path.exists(chat_log_path):
        print(f"Arquivo de log não encontrado: {chat_log_path}")
        return
    
    # Abre o arquivo de log de chat
    with open(chat_log_path, 'r') as file:
        # Move o ponteiro do arquivo para o fim do arquivo
        file.seek(0, os.SEEK_END)
        
        while True:
            # Lê novas linhas do arquivo de log
            line = file.readline()
            if line:
                if "CHAT" in line:
                    # Verifica se a linha contém a palavra "Overpowerr"
                    if "Sua vara está quebrada, você precisa repará-la antes de usar." in line:
                        check_condition_and_run_ahk("Quebrada")
                    elif "Você pescou um peixe mais pesado do que sua vara suporta, portanto sua vara quebrou." in line:
                        check_condition_and_run_ahk("Quebrada")
                    elif "Sua sacola de peixes está cheia, venda os peixes antes de pescar novamente." in line:
                        check_condition_and_run_ahk("Cheia")
                        
            else:
                # Se não há novas linhas, espera um pouco antes de tentar novamente
                time.sleep(0.1)

def check_condition_and_run_ahk(condition):
    config = load_config()
    autohotkey_exe_path = config["AUTOHOTKEY_PATH"]
    script_RepairFishRod = config["SCRIPT_REPAIR_FISH_ROD"]
    script_SellFishFull = config["SCRIPT_SELL_FISH_FULL"]
    script_SellFish = config["SCRIPT_SELL_FISH"]
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if condition == "Quebrada":
        subprocess.run([autohotkey_exe_path, script_RepairFishRod])
        print(f"{current_time} - Script AutoHotkey de Reparar Vara executado.")
    elif condition == "Cheia":
        subprocess.run([autohotkey_exe_path, script_SellFishFull])
        print(f"{current_time} - Script AutoHotkey de Vender Peixes executado.")
    elif condition == "SellFish":
        subprocess.run([autohotkey_exe_path, script_SellFish])
        print(f"{current_time} - Script AutoHotkey de Vender Peixes executado.")

def schedule_sell_fish():
    check_condition_and_run_ahk("SellFish")
    threading.Timer(10 * 60, schedule_sell_fish).start()

if __name__ == "__main__":
    schedule_sell_fish()
    read_chat_log()
