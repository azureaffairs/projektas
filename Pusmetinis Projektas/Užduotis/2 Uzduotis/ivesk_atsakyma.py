import base64
import webbrowser

def get_download_link():
    e_f = "RkxBR3tiYWx0YX0="
    e_u = "aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3NwYXJreWF6dXJlL0ltYWdlMjAyNjAxMjIxNzIwMjEucG5n"

    user_input = input("Įveskite flagą: ")

    c_f = base64.b64decode(e_f).decode('utf-8')

    if user_input == c_f:
        url = base64.b64decode(e_u).decode('utf-8')
        
        print("\nFlagas teisingas! Atidaroma nuoroda...")
        webbrowser.open(url)
    else:
        print("Neteisingas flagas. Prieiga uždrausta.")

if __name__ == "__main__":
    get_download_link()
