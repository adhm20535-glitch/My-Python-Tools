import tkinter as tk

def main():
    root = tk.Tk()
    root.title("مشروع جديد")
    root.geometry("400x300")
    tk.Label(root, text="مرحباً بك في مشروعك!", font=("Segoe UI", 14)).pack(pady=50)
    root.mainloop()

if __name__ == "__main__":
    main()
