import json
import random
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk
import os

# ---------- File Paths ----------
PROMPTS_FILE = r"C:\Users\laxmi\OneDrive\Desktop\30\Day29\writing_prompts.json"
LOG_FILE = r"C:\Users\laxmi\OneDrive\Desktop\30\Day29\prompt_log.txt"
BG_IMAGE_PATH = r"C:\Users\laxmi\OneDrive\Desktop\30\Day29\Background.png"
WAND_ICON_PATH = r"C:\Users\laxmi\OneDrive\Desktop\30\Day29\wand.png"

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
        result_text.insert(tk.END, f"➤ {current_prompt}")
        result_text.config(state='disabled')
    else:
        messagebox.showerror("Invalid", "No prompts found.")

# ---------- Save Prompt ----------
def save_prompt():
    if current_prompt:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {current_prompt}\n\n")
        messagebox.showinfo("Saved", "✅ Prompt saved to prompt_log.txt")
    else:
        messagebox.showwarning("⚠️ No Prompt", "Please generate a prompt before saving.")

# ---------- View Saved ----------
def show_saved_prompts():
    if not os.path.exists(LOG_FILE):
        messagebox.showinfo("No Logs", "No saved prompts found yet.")
        return

    top = tk.Toplevel(root)
    top.title("Saved Prompts")
    top.geometry("600x400")
    top.config(bg=theme['bg'])

    text = tk.Text(top, wrap=tk.WORD, font=FONT_MAIN, bg=theme['textbox'], fg=theme['fg'])
    text.pack(expand=True, fill="both", padx=10, pady=10)

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        text.insert(tk.END, f.read())
    text.config(state='disabled')

# ---------- Toggle Theme ----------
def toggle_theme():
    global is_dark_mode, theme
    is_dark_mode = not is_dark_mode
    theme = dark_theme if is_dark_mode else light_theme
    root.configure(bg=theme['bg'])

    for widget in all_widgets:
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.config(bg=theme['bg'], fg=theme['fg'])
        elif isinstance(widget, tk.Text):
            widget.config(bg=theme['textbox'], fg=theme['fg'])

    generate_button.config(bg=theme['button_bg'], fg=theme['button_fg'], activebackground=theme['active_bg'])
    save_button.config(bg=theme['save_bg'], fg=theme['button_fg'], activebackground=theme['active_bg'])
    view_button.config(bg=theme['view_bg'], fg=theme['button_fg'], activebackground=theme['active_bg'])
    theme_button.config(text="🌞 Light Mode" if is_dark_mode else "🌙 Dark Mode")

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("✨ PromptWand")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# ---------- Fonts ----------
FONT_HEADER = ("Georgia", 24, "bold")
FONT_MAIN = ("Georgia", 15)
FONT_COMBO = ("Segoe UI", 16)
FONT_BUTTON = ("Segoe UI", 14, "bold")

# ---------- Theme Config ----------
light_theme = {
    'bg': "SystemButtonFace",
    'fg': "black",
    'textbox': "#FBFBFB",
    'button_bg': "#16A085",
    'save_bg': "#884EA0",
    'view_bg': "#5D6D7E",
    'button_fg': "white",
    'active_bg': "#138D75"
}
dark_theme = {
    'bg': "#1E1E1E",
    'fg': "#F0F0F0",
    'textbox': "#2D2D2D",
    'button_bg': "#229954",
    'save_bg': "#7D3C98",
    'view_bg': "#34495E",
    'button_fg': "white",
    'active_bg': "#196F3D"
}
is_dark_mode = False
theme = light_theme

# ---------- Background ----------
if os.path.exists(BG_IMAGE_PATH):
    bg_image = Image.open(BG_IMAGE_PATH).resize((screen_width, screen_height))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ---------- Load Prompts ----------
data = load_prompts()
if not data:
    root.destroy()
    exit()
current_prompt = None

# ---------- Theme Button ----------
theme_button = tk.Button(root, text="🌙 Dark Mode", command=toggle_theme,
                         font=("Segoe UI", 12), bg="#D0D3D4", fg="black", relief="raised")
theme_button.pack(pady=(10, 5))

# ---------- Header ----------
header_frame = tk.Frame(root, bg=theme['bg'])
header_frame.pack(pady=(5, 10))

if os.path.exists(WAND_ICON_PATH):
    wand_img = Image.open(WAND_ICON_PATH).resize((32, 32), Image.Resampling.LANCZOS)
    wand_photo = ImageTk.PhotoImage(wand_img)
    wand_label = tk.Label(header_frame, image=wand_photo, bg=theme['bg'])
    wand_label.image = wand_photo
    wand_label.pack(side="left", padx=(0, 10))
else:
    print("❌ wand.png not found!")

label_text = tk.Label(header_frame, text="Select Your Category", font=FONT_HEADER,
                      bg=theme['bg'], fg=theme['fg'])
label_text.pack(side="left")

# ---------- Dropdown ----------
category_var = tk.StringVar()
category_menu = ttk.Combobox(root, textvariable=category_var, state="readonly",
                             font=FONT_COMBO, width=40)
category_menu['values'] = [cat.capitalize() for cat in data.keys()]
category_menu.pack(pady=(0, 15))

# ---------- Buttons ----------
generate_button = tk.Button(root, text="⚒️ Generate Prompt", command=show_prompt,
                            font=FONT_BUTTON, bg=theme['button_bg'], fg=theme['button_fg'],
                            activebackground=theme['active_bg'], relief="flat", padx=20, pady=10)
generate_button.pack(pady=5)

# ---------- Prompt Display ----------
result_frame = tk.Frame(root, bg=theme['textbox'], bd=2, relief="groove")
result_frame.pack(pady=25, padx=100, fill="x")

result_text = tk.Text(result_frame, wrap=tk.WORD, height=8,
                      font=FONT_MAIN, bg=theme['textbox'], fg=theme['fg'],
                      state='disabled', padx=15, pady=10, bd=0)
result_text.pack(expand=True, fill="both")

# ---------- Save & View Buttons ----------
save_button = tk.Button(root, text="💾 Save Prompt", command=save_prompt,
                        font=FONT_BUTTON, bg=theme['save_bg'], fg=theme['button_fg'],
                        activebackground=theme['active_bg'], relief="flat", padx=20, pady=10)
save_button.pack(pady=(0, 10))

view_button = tk.Button(root, text="📖 View Saved Prompts", command=show_saved_prompts,
                        font=FONT_BUTTON, bg=theme['view_bg'], fg=theme['button_fg'],
                        activebackground=theme['active_bg'], relief="flat", padx=20, pady=10)
view_button.pack(pady=(0, 10))

# ---------- Footer ----------
footer = tk.Label(root, text="⚙️ Designed by Laxmi Prasanna", font=("Segoe UI", 11),
                  bg="#0F2027", fg="#E0E0E0")
footer.pack(side="bottom", pady=10)

# ---------- Register Widgets ----------
all_widgets = [label_text, result_text, footer, generate_button, save_button, view_button, theme_button]

# ---------- Main Loop ----------
root.mainloop()
