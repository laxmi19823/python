import json
import random
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk
import os

# ---------- Paths ----------
PROMPTS_FILE = r"C:\Users\laxmi\OneDrive\Desktop\30\Day29\writing_prompts.json"
LOG_FILE = r"C:\Users\laxmi\OneDrive\Desktop\30\Day29\prompt_log.txt"
BG_IMAGE_PATH = r"C:\Users\laxmi\OneDrive\Desktop\30\Day29\Background.png"
WAND_IMAGE_PATH = r"C:\Users\laxmi\OneDrive\Desktop\30\Day29\wand.png"

# ---------- Load Prompts ----------
def load_prompts():
    if not os.path.exists(PROMPTS_FILE):
        messagebox.showerror("File Not Found", f"❌ Cannot find:\n{PROMPTS_FILE}")
        return None
    with open(PROMPTS_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

# ---------- Show Prompt ----------
def show_prompt():
    category = category_var.get()
    if not category:
        messagebox.showwarning("⚠️ No Category", "Please select a category.")
        return
    prompts = data.get(category.lower())
    if prompts:
        global current_prompt
        current_prompt = random.choice(prompts)
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"\u27a4 {current_prompt}")
        result_text.config(state='disabled')
        save_button.config(state='normal')
    else:
        messagebox.showerror("Invalid", "No prompts found.")

# ---------- Save Prompt ----------
def save_prompt():
    if current_prompt:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {current_prompt}\n\n")
        messagebox.showinfo("Saved", "✅ Prompt saved to prompt_log.txt")
        save_button.config(state='disabled')

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("PromptWand")

# Fullscreen setup
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Canvas with background
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)

bg_image = Image.open(BG_IMAGE_PATH).resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Fonts
FONT_HEADER = ("Georgia", 24, "bold")
FONT_MAIN = ("Georgia", 15)
FONT_COMBO = ("Segoe UI", 14)
FONT_BUTTON = ("Segoe UI", 13)

# Load prompts
data = load_prompts()
if not data:
    root.destroy()
    exit()

current_prompt = None

# ---------- UI Elements ----------
header_frame = tk.Frame(root, bg="SystemButtonFace")

# 🪄 Load wand image if exists
if os.path.exists(WAND_IMAGE_PATH):
    wand_img = Image.open(WAND_IMAGE_PATH).resize((32, 32))
    wand_photo = ImageTk.PhotoImage(wand_img)
    wand_label = tk.Label(header_frame, image=wand_photo, bg="SystemButtonFace")
    wand_label.image = wand_photo
    wand_label.pack(side="left", padx=(0, 10))
else:
    tk.Label(header_frame, text="🪄", font=("Segoe UI Emoji", 26), bg="SystemButtonFace").pack(side="left", padx=(0, 10))

tk.Label(header_frame, text="Select Your Category", font=FONT_HEADER, bg="SystemButtonFace", fg="black").pack(side="left")
canvas.create_window(screen_width // 2, 80, window=header_frame)

# Dropdown menu
category_var = tk.StringVar()
category_menu = ttk.Combobox(root, textvariable=category_var, state="readonly", font=FONT_COMBO, width=40)
category_menu['values'] = [category.capitalize() for category in data.keys()]
category_menu.set('')  # Default to empty
canvas.create_window(screen_width // 2, 140, window=category_menu)

# Generate button
generate_button = tk.Button(root, text="⚒️ Generate Prompt", command=show_prompt,
                            font=FONT_BUTTON, bg="#16A085", fg="white",
                            activebackground="#138D75", relief="flat",
                            padx=20, pady=10)
canvas.create_window(screen_width // 2, 200, window=generate_button)

# Prompt display box
result_frame = tk.Frame(root, bg="#FBFBFB", bd=2, relief="groove")
result_text = tk.Text(result_frame, wrap=tk.WORD, height=8,
                      font=FONT_MAIN, bg="#FBFBFB", fg="#1C1C1C",
                      state='disabled', padx=15, pady=10, bd=0)
result_text.pack(expand=True, fill="both")
canvas.create_window(screen_width // 2, 360, window=result_frame, width=screen_width - 200, height=200)

# Save Button (always visible, but disabled until prompt generated)
save_button = tk.Button(root, text="💾 Save Prompt", command=save_prompt,
                        font=FONT_BUTTON, bg="#884EA0", fg="white",
                        activebackground="#633974", relief="flat",
                        padx=15, pady=8, state='disabled')
canvas.create_window(screen_width // 2, 490, window=save_button)

# Footer
footer = tk.Label(root, text="⚙️ Designed by Laxmi Prasanna", font=("Segoe UI", 11),
                  bg="#0F2027", fg="#E0E0E0")
canvas.create_window(screen_width // 2, screen_height - 40, window=footer)

# ---------- Main Loop ----------
root.mainloop()
