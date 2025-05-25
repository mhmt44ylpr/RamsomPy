import os
from cryptography.fernet import Fernet,InvalidToken
from colorama import Fore,init
from pyfiglet import Figlet
from rich.console import Console
from optparse import OptionParser

console = Console()
init(autoreset=True)

class Decrpyt():
    def __init__(self):
        self.path = ''
        self.key = ''
        self.list_file = list()
        self.get_user_input()
        self.add_file_list()
        self.crypt()
        
    def get_user_input(self):
        parser = OptionParser()
        parser.add_option('-p', '--path', dest='path',
                          help='Şifrelenecek dosyaların bulunduğu klasör yolu')
        parser.add_option('-k','--key',dest='key',help='key girilecek alan')
        options, _ = parser.parse_args()  # ← Burada tuple olarak al
        if options.key:
            self.key = options.key
        else:
            console.log('[red]Key alanı boş geçilemez.[/red]')
            exit()
        if options.path:
            if os.path.isdir(options.path):
                self.path = options.path
            else:
                console.log('[red]Geçersiz path, klasör bulunamadı.[/red]')
                exit()
        else:
            self.path = os.path.dirname(os.path.abspath(__file__))
            console.log(f"[yellow]Path belirtilmedi, script dizini kullanılacak: {self.path}[/yellow]")
            
               
    def add_file_list(self):
        try:
            for file in os.listdir(self.path):
                if file == 'generated.key' or file == 'encrypgraph.py' or file == 'decrypgraph.py':
                    continue
                
                full_path = os.path.join(self.path, file)
                
                if not os.path.isdir(full_path):
                    self.list_file.append(file)
                    
        except FileNotFoundError:
            console.log('[red]Lütfen doğru bir path yolu giriniz.[/red]')
            exit()
    
    def crypt(self):
        try:
            console.log('[yellow]Şifreleme çözülüyor....[/yellow]')
            for file in self.list_file:
                full_path = os.path.join(self.path, file)
                with open(full_path,'rb') as f:
                    original_txt = f.read()
                with open(full_path,'wb') as ff:
                    crypt_txt = Fernet(self.key).decrypt(original_txt)
                    ff.write(crypt_txt)
            console.log('[green]Şifreleme çözüldü....[/green]')
            
        except InvalidToken:
            console.log('[red]Hatalı key girdiniz veya bu dosya şifreli değil.[/red]')
            exit()

        except Exception as e:
            
            exit()
if __name__ == '__main__':
    
    figlet = Figlet(font='slant')
    print(Fore.CYAN +figlet.renderText('RamsomPy'))
    Decrpyt()

