import os
import requests
import base64

def d(t, s):
    r = ""
    for c in t:
        r += chr(ord(c) - s)
    return r

def download_file():
    # FLAG{balta} (Base64)
    e_f = "RkxBR3tiYWx0YX0="
    # Caesar shift +1 nuorodai: https://storage.googleapis.com/sparkyazure/Image20260122172021.png
    s_u = "iuuqt;00tupsbhf/hpphmfbqjt/dpn0tqbslza{vsf0Jnbhf313711332831322/qnh"

    c_f = base64.b64decode(e_f).decode('utf-8')
    url = d(s_u, 1)
    
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    target_dir = os.path.join(desktop, "Pusmetinis Projektas", "Užduotis", "3 Uzduotis")
    file_path = os.path.join(target_dir, "Image20260122172021.png")

    user_input = input("Įveskite flagą: ")

    if user_input == c_f:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        try:
            print("Flagas teisingas. Siunčiamas failas...")
            r = requests.get(url, stream=True)
            r.raise_for_status()
            
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"Baigta. Failas išsaugotas: {file_path}")
        except Exception as e:
            print(f"Klaida siunčiant: {e}")
    else:
        print("Neteisingas flagas.")

if __name__ == "__main__":
    download_file()