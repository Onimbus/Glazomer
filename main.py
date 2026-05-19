import tkinter as tk
import random

class LetterEyeTrainer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Угадай букву')
        self.root.geometry("700x700")
        self.root.resizable(False, False)
        
        self.letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У']
        self.correct = self.wrong = 0
        self.current_size = 180
        self.current_letter = ''
        
        # Интерфейс
        self.score_frame = tk.Frame(self.root)
        self.score_frame.pack(pady=10)
        self.correct_label = tk.Label(self.score_frame, text=f"V {self.correct}", font=("Arial", 14), fg="green")
        self.correct_label.pack(side=tk.LEFT, padx=20)
        self.wrong_label = tk.Label(self.score_frame, text=f"X {self.wrong}", font=("Arial", 14), fg="red")
        self.wrong_label.pack(side=tk.LEFT, padx=20)
        
        self.size_label = tk.Label(self.root, text=f"Размер: {self.current_size}px", font=("Arial", 10))
        self.size_label.pack()
        
        self.letter_display = tk.Label(self.root, font=("Arial", self.current_size, "bold"))
        self.letter_display.pack(pady=30)
        
        self.entry = tk.Entry(self.root, font=("Arial", 14), width=10, justify='center')
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.check)
        
        self.check_btn = tk.Button(self.root, text="Проверить", command=self.check, bg="#4CAF50", fg="white")
        self.check_btn.pack()
        
        self.next_btn = tk.Button(self.root, text="Следующая →", command=self.next, state=tk.DISABLED, bg="#2196F3", fg="white")
        self.next_btn.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack()
        
        self.new_letter()
        self.root.mainloop()
    
    def new_letter(self):
        self.current_letter = random.choice(self.letters)
        if self.current_size <= 0:
            self.letter_display.config(text="•", font=("Arial", 20))
            self.size_label.config(text=f"Размер: {self.current_size}px (невидимо)")
        else:
            self.letter_display.config(text=self.current_letter, font=("Arial", self.current_size, "bold"))
            self.size_label.config(text=f"Размер: {self.current_size}px")
        
        self.entry.delete(0, tk.END)
        self.entry.config(state=tk.NORMAL)
        self.check_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.DISABLED)
        self.result_label.config(text="")
        self.entry.focus()
    
    def check(self, event=None):
        user_input = self.entry.get().strip().upper()
        if not user_input:
            self.result_label.config(text="Введите букву!", fg="orange")
            return
        
        if user_input == self.current_letter:
            self.correct += 1
            self.current_size -= 30
            self.result_label.config(text="Правильно! +1", fg="green")
        else:
            self.wrong += 1
            self.result_label.config(text=f"Неверно! Была '{self.current_letter}'", fg="red")
        
        self.correct_label.config(text=f"V {self.correct}")
        self.wrong_label.config(text=f"X {self.wrong}")
        
        self.entry.config(state=tk.DISABLED)
        self.check_btn.config(state=tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL)
    
    def next(self):
        self.new_letter()

game = LetterEyeTrainer()