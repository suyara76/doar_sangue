import tkinter as tk
from tkinter import ttk, messagebox
from pyswip import Prolog


class BloodDonationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Doação de Sangue")
        self.root.geometry("400x500")
        self.root.configure(bg="#f5f5f5")

        #inicializacao do prolog
        self.prolog = Prolog()
        self.prolog.consult("base_conhecimento.pl")

        #titulo principal
        tk.Label(root, text="Sistema de Doação de Sangue", fg="#8B0000", bg="#f5f5f5", font=("Arial", 18, "bold")).pack(pady=10)

        #consultar quem pode doar
        self.donation_frame = ttk.LabelFrame(root, text="Verificar Doação", padding=(10, 10))
        self.donation_frame.pack(fill="x", padx=20, pady=10)

        ttk.Label(self.donation_frame, text="Doador:").grid(row=0, column=0, padx=5, pady=5)
        self.doador_entry = ttk.Entry(self.donation_frame)
        self.doador_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.donation_frame, text="Receptor:").grid(row=1, column=0, padx=5, pady=5)
        self.receptor_entry = ttk.Entry(self.donation_frame)
        self.receptor_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.donation_frame, text="Quem pode doar?", bg="#8B0000", fg="white", font=("Arial", 10, "bold"),
                  command=self.check_donation).grid(row=2, column=0, columnspan=2, pady=10)

        #consultar tipo sanguíneo
        self.blood_type_frame = ttk.LabelFrame(root, text="Consultar Tipo Sanguíneo", padding=(10, 10))
        self.blood_type_frame.pack(fill="x", padx=20, pady=10)

        ttk.Label(self.blood_type_frame, text="Pessoa:").grid(row=0, column=0, padx=5, pady=5)
        self.person_entry = ttk.Entry(self.blood_type_frame)
        self.person_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.blood_type_frame, text="Consultar", bg="#8B0000", fg="white", font=("Arial", 10, "bold"),
                  command=self.check_blood_type).grid(row=1, column=0, columnspan=2, pady=10)

        #consultar fator RH
        self.rh_frame = ttk.LabelFrame(root, text="Consultar Fator RH", padding=(10, 10))
        self.rh_frame.pack(fill="x", padx=20, pady=10)

        ttk.Label(self.rh_frame, text="Pessoa:").grid(row=0, column=0, padx=5, pady=5)
        self.rh_person_entry = ttk.Entry(self.rh_frame)
        self.rh_person_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.rh_frame, text="Consultar", bg="#8B0000", fg="white", font=("Arial", 10, "bold"),
                  command=self.check_rh).grid(row=1, column=0, columnspan=2, pady=10)

        tk.Button(root, text="Fechar", bg="#333333", fg="white", font=("Arial", 10, "bold"),
                  command=root.quit).pack(pady=20)

    def check_donation(self):
        doador = self.doador_entry.get().strip().lower()
        receptor = self.receptor_entry.get().strip().lower()

        query = f"podedoar({doador}, {receptor})."
        result = list(self.prolog.query(query))

        if result:
            messagebox.showinfo("Resultado", f"{doador.capitalize()} pode doar para {receptor.capitalize()}.")
        else:
            messagebox.showinfo("Resultado", f"{doador.capitalize()} não pode doar para {receptor.capitalize()}.")

    def check_blood_type(self):
        person = self.person_entry.get().strip().lower()

        query = f"tiposanguineo({person}, Tipo)."
        result = list(self.prolog.query(query))

        if result:
            blood_type = result[0]["Tipo"].upper()
            messagebox.showinfo("Resultado", f"{person.capitalize()} tem tipo sanguíneo {blood_type}.")
        else:
            messagebox.showinfo("Resultado", f"Tipo sanguíneo de {person.capitalize()} não encontrado.")

    def check_rh(self):
        person = self.rh_person_entry.get().strip().lower()

        query = f"fatorrh({person}, Rh)."
        result = list(self.prolog.query(query))

        if result:
            rh_factor = "+" if result[0]["Rh"] == "positivo" else "-"
            messagebox.showinfo("Resultado", f"{person.capitalize()} tem fator RH {rh_factor}.")
        else:
            messagebox.showinfo("Resultado", f"Fator RH de {person.capitalize()} não encontrado.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BloodDonationApp(root)
    root.mainloop()
