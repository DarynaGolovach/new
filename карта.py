import tkinter as tk
from tkinter import messagebox

def luhn_algorithm(card_number):
    digits = [int(x) for x in card_number]
    checksum = sum(digits[::-2] + [sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return checksum % 10 == 0

def validate_card():
    card_number = entry_card_number.get().replace(" ", "") 
    if card_number.isdigit():
        if luhn_algorithm(card_number):
            messagebox.showinfo("���������", "����� ������ �������.")
        else:
            messagebox.showwarning("���������", "����� ������ �� �������.")
    else:
        messagebox.showerror("�������", "������� ������������ ����� ������.")


root = tk.Tk()
root.title("�������� �������� ������ �������� ������")


label_card_number = tk.Label(root, text="����� ������:")
label_card_number.grid(row=0, column=0, padx=10, pady=5)

entry_card_number = tk.Entry(root)
entry_card_number.grid(row=0, column=1, padx=10, pady=5)

button_validate = tk.Button(root, text="���������", command=validate_card)
button_validate.grid(row=1, column=0, columnspan=2, padx=10, pady=5)


root.mainloop()
