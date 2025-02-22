import tkinter as tk
import random
import time

TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Typing fast requires practice and patience.",
    "Accuracy is more important than speed in typing."
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.text_to_type = random.choice(TEXTS)
        self.start_time = None
        
        self.label = tk.Label(root, text=self.text_to_type, wraplength=400, font=("Arial", 14))
        self.label.pack(pady=20)
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.calculate_speed)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
    
    def start_test(self):
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.start_time = time.time()
        self.result_label.config(text="")
    
    def calculate_speed(self, event):
        end_time = time.time()
        time_taken = end_time - self.start_time
        typed_text = self.entry.get()
        words = len(typed_text.split())
        wpm = round((words / time_taken) * 60)
        accuracy = self.calculate_accuracy(typed_text)
        self.result_label.config(text=f"Speed: {wpm} WPM | Accuracy: {accuracy}%")
    
    def calculate_accuracy(self, typed_text):
        correct_chars = sum(1 for a, b in zip(typed_text, self.text_to_type) if a == b)
        accuracy = (correct_chars / len(self.text_to_type)) * 100
        return round(accuracy, 2)

if __name__ == "__main__":
    root = tk.Tk()
    TypingSpeedTest(root)
    root.mainloop()
