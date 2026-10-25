import tkinter as tk
from PIL import Image, ImageTk
import os

class Ominitirix:
    def __init__(self, root):
        self.root = root 
        self.root.title("Omnitrix beta teste")
        self.root.geometry("400x550")
        self.root.configure(bg = "#111111")
        self.root.resizable(False,False)

        self.titulo_label = tk.Label(
            root, text = "OMNITRIX", font=("Helvetica",22,"bold"),
            fg = "#00FF00", bg="#111111"
        )
        self.titulo_label.pack(pady=15)

        self.visor_frame = tk.Frame(
            root, bg="#0A330A", bd= 6, relief="raised",
            width= 250, height=250
        )
        self.visor_frame.pack(pady=10)
        self.visor_frame.pack_propagate(False)

        self.imagem_label = tk.Label(self.visor_frame, bg= "#0A330A")
        self.imagem_label.pack(pady= 10)

        self.alien_label = tk.Label(
            root, text = "Modo : Selacao de alien ativa", font=("Helvetica",14,"bold"),
            fg = "#FFFFFF", bg= "#111111"
        )
        self.alien_label.pack(pady=20)
        
        self.botao_ativar = tk.Button(
            root, text="SELECIONE O ALIEN", font= ("Helvetica", 12,"bold"),
            bg = "#00FF00", fg = "#111111",activebackground = "#00CC00",
            command= self.iniciar_transicao, relief = "flat", padx = 10, pady = 8

        )
        self.botao_ativar.pack(pady=10)
        self. dados_aliens = [
            {"nome" : " Chama", "arquivo":"app/imagem/ChamaOmni.png"},
            {"nome" : "Bala De Canhao ", "arquivo":"app/imagem/Arte_oficial_de_Bala_de_Canh.png"},
            {"nome" : "Ultra T ", "arquivo":"app/imagem/Ben_10_-_Ultra_T.png"},
            {"nome" : "Massa Cinzenta", "arquivo":"app/imagem/MassaFrente.png"},
            {"nome" : " Diamante", "arquivo":"app/imagem/Diamondhead.png"}

        ]
        self.alien_index = -1

    def iniciar_transicao(self):
        self.botao_ativar.config(state= "disabled")
        self.alien_label.config(text="E A HORA DO HEROI ",
        fg = "#00FF00" )
        cores_flash = [
            "#00FF00",
            "#0A330A",
            "#00FF00",
            "#111111",
            "#00FF00",
            "#0A330A"
        ]
        self.executar_flash(cores_flash,0)
    def executar_flash(self, cores, passo):
        if passo < len (cores):
            cor_atual = cores[passo]
            self.visor_frame.config(bg=cor_atual)
            self.imagem_label.config(bg=cor_atual)
            self.root.after(
                80, lambda:
                self.executar_flash(cores,passo + 1)

        )
        else:
            self.visor_frame.config(bg="#0A330A")
            self.imagem_label.config(bg="#0A330A")
            self.mostrar_alien_final()
    def mostrar_alien_final(self):
        self.alien_index=(self.alien_index+1)% len(self.dados_aliens)
        alien_atual = self.dados_aliens[self.alien_index]
        self.alien_label.config(
            text = f"ALIEN: {alien_atual['nome'].upper()}",
            fg= "#00FF00"
            )
        alien_atual = self.dados_aliens[self.alien_index]
        print(os.path.abspath(alien_atual["arquivo"]))
        print(os.path.abspath(alien_atual["arquivo"]))
        if os.path.exists(alien_atual["arquivo"]):
            try:
                img = Image.open(alien_atual["arquivo"])
                img = img.resize((160,160), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img)
                self.imagem_label.config(image = img_tk)
                self.imagem_label.image =img_tk
            except Exception:
                self.alien_label.config(text= "Erro na imagem" ,
                                        fg = "red"
                )
                
        else:
            self.alien_label.config(
            text= f"{alien_atual['nome']}(Pronto!)",
                fg = "#00FF00"
                )
        self.botao_ativar.config(state="normal")
if __name__== "__main__":
    app_root = tk.Tk()
    app = Ominitirix(app_root)
    app_root.mainloop()

        
    