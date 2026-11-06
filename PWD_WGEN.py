import customtkinter as ctk
import secrets
import string

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PWD_WGEN // electric")
        self.geometry("640x360")
        self.resizable(False, False)
        self.configure(fg_color="#0A0A0B")
        self.ELECTRIC = "#00E5FF"
        self.ELECTRIC_HOVER = "#00B8CC"
        self.main = ctk.CTkFrame(self, fg_color="#141416", corner_radius=14, border_width=1, border_color="#1E1E20")
        self.main.pack(padx=16, pady=16, fill="both", expand=True)
        header = ctk.CTkFrame(self.main, fg_color="transparent")
        header.pack(fill="x", padx=18, pady=(14, 8))
        ctk.CTkLabel(header, text="PWD.WGEN", font=("Segoe UI", 16, "bold"), text_color="#FFFFFF").pack(side="left")
        ctk.CTkLabel(header, text="ELECTRIC // 16:9", font=("Consolas", 10), text_color=self.ELECTRIC).pack(side="left", padx=(10,0))
        self.pwd_box = ctk.CTkFrame(self.main, fg_color="#0A0A0B", corner_radius=10, border_width=1, border_color="#252529")
        self.pwd_box.pack(fill="x", padx=18, pady=8)
        self.pwd_var = ctk.StringVar(value="••••••••••••••••••••")
        self.pwd_label = ctk.CTkLabel(self.pwd_box, textvariable=self.pwd_var, font=("Consolas", 16), text_color="#FFFFFF", anchor="w")
        self.pwd_label.pack(side="left", padx=14, pady=12, fill="x", expand=True)
        self.copy_btn = ctk.CTkButton(self.pwd_box, text="COPIAR", command=self.copiar, width=68, height=30, corner_radius=7, font=("Segoe UI", 10, "bold"), fg_color="#0A0A0B", border_width=1, border_color=self.ELECTRIC, text_color=self.ELECTRIC, hover_color="#1A1A1E")
        self.copy_btn.pack(side="right", padx=8, pady=8)
        controls = ctk.CTkFrame(self.main, fg_color="transparent")
        controls.pack(fill="x", padx=18, pady=8)
        left = ctk.CTkFrame(controls, fg_color="transparent")
        left.pack(side="left", fill="both", expand=True, padx=(0,10))
        ctk.CTkLabel(left, text="LONGITUD", font=("Segoe UI", 9, "bold"), text_color="#8A8A93").pack(anchor="w")
        self.length_var = ctk.IntVar(value=16)
        self.slider = ctk.CTkSlider(left, from_=8, to=32, number_of_steps=24, command=self.update_length, fg_color="#252529", progress_color=self.ELECTRIC, button_color="#FFFFFF", button_hover_color=self.ELECTRIC)
        self.slider.pack(fill="x", pady=(4,2))
        self.length_label = ctk.CTkLabel(left, text="16 caracteres", font=("Segoe UI", 10), text_color="#FFFFFF")
        self.length_label.pack(anchor="w")
        right = ctk.CTkFrame(controls, fg_color="transparent")
        right.pack(side="left", fill="both", expand=True)
        ctk.CTkLabel(right, text="INCLUIR", font=("Segoe UI", 9, "bold"), text_color="#8A8A93").pack(anchor="w")
        chk_frame = ctk.CTkFrame(right, fg_color="transparent")
        chk_frame.pack(fill="x", pady=(4,0))
        self.upper_var = ctk.BooleanVar(value=True)
        self.num_var = ctk.BooleanVar(value=True)
        self.sym_var = ctk.BooleanVar(value=True)
        self.chk1 = ctk.CTkCheckBox(chk_frame, text="A-Z", variable=self.upper_var, font=("Segoe UI", 11), text_color="#D1D1D6", fg_color=self.ELECTRIC, border_color="#2A2A2E", checkmark_color="#000000", corner_radius=3, checkbox_width=18, checkbox_height=18)
        self.chk1.pack(side="left", padx=(0,12))
        self.chk2 = ctk.CTkCheckBox(chk_frame, text="0-9", variable=self.num_var, font=("Segoe UI", 11), text_color="#D1D1D6", fg_color=self.ELECTRIC, border_color="#2A2A2E", checkmark_color="#000000", corner_radius=3, checkbox_width=18, checkbox_height=18)
        self.chk2.pack(side="left", padx=(0,12))
        self.chk3 = ctk.CTkCheckBox(chk_frame, text="!@#", variable=self.sym_var, font=("Segoe UI", 11), text_color="#D1D1D6", fg_color=self.ELECTRIC, border_color="#2A2A2E", checkmark_color="#000000", corner_radius=3, checkbox_width=18, checkbox_height=18)
        self.chk3.pack(side="left")
        btn_center = ctk.CTkFrame(self.main, fg_color="transparent")
        btn_center.pack(fill="x", padx=18, pady=(12, 14))
        self.gen_btn = ctk.CTkButton(btn_center, text="GENERAR NUEVA CONTRASEÑA", command=self.generar, width=400, height=38, corner_radius=9, font=("Segoe UI", 11, "bold"), fg_color=self.ELECTRIC, text_color="#000000", hover_color=self.ELECTRIC_HOVER)
        self.gen_btn.pack(anchor="center")
        self.generar()
    def update_length(self, val):
        v = int(val)
        self.length_var.set(v)
        self.length_label.configure(text=f"{v} caracteres")
    def generar(self):
        # --- PARCHE 10/10 ---
        length = self.length_var.get()
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase if self.upper_var.get() else ""
        digits = string.digits if self.num_var.get() else ""
        symbols = "!@#$%_-.+="
        symbols = symbols if self.sym_var.get() else ""

        chars = lowercase
        must_have = [secrets.choice(lowercase)]
        if uppercase:
            chars += uppercase
            must_have.append(secrets.choice(uppercase))
        if digits:
            chars += digits
            must_have.append(secrets.choice(digits))
        if symbols:
            chars += symbols
            must_have.append(secrets.choice(symbols))

        remaining = length - len(must_have)
        pwd_list = must_have + [secrets.choice(chars) for _ in range(remaining)]
        secrets.SystemRandom().shuffle(pwd_list)
        self.pwd_var.set("".join(pwd_list))
    def copiar(self):
        self.clipboard_clear()
        self.clipboard_append(self.pwd_var.get())
        self.copy_btn.configure(text="¡COPIADO!", fg_color=self.ELECTRIC, text_color="#000000")
        self.after(1200, lambda: self.copy_btn.configure(text="COPIAR", fg_color="#0A0A0B", text_color=self.ELECTRIC))
if __name__ == "__main__":
    app = App()
    app.mainloop()