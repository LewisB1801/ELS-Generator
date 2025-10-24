import os
import sys
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

# === DETERMINE BASE DIR ===
# Use exe folder if frozen, else script folder
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# === GLOBAL SETTINGS ===
NAMES_FILE = os.path.join(BASE_DIR, "names.txt")
EXAMPLES_FOLDER_NAME = "Example_Files"
COMPLETE_FOLDER = os.path.join(BASE_DIR, "Complete")
ALLOWED_EXTENSIONS = (".ytd", ".yft", ".meta")

# === RESOURCE PATH HELPERS ===
def resource_path(relative_path):
    """Get absolute path to resource (works for PyInstaller)."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# === EXAMPLES EXTRACTION ===
def extract_examples():
    """Extract bundled example files to the disk if not already present."""
    target_folder = os.path.join(BASE_DIR, EXAMPLES_FOLDER_NAME)
    if os.path.exists(target_folder):
        return  # already exists

    examples_source = resource_path(EXAMPLES_FOLDER_NAME)
    if not os.path.exists(examples_source):
        print("⚠️ No examples folder found in resources.")
        return

    os.makedirs(target_folder, exist_ok=True)

    for root, _, files in os.walk(examples_source):
        for file in files:
            src = os.path.join(root, file)
            rel_path = os.path.relpath(src, examples_source)
            dst = os.path.join(target_folder, rel_path)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
    messagebox.showinfo("Examples Installed", f"✅ Example files extracted to:\n{target_folder}")

# === CORE FUNCTIONS ===
def ensure_names_file():
    if not os.path.exists(NAMES_FILE):
        with open(NAMES_FILE, "w", encoding="utf-8") as f:
            f.write("")
        messagebox.showinfo("File Created", f"✅ Created blank names file:\n{NAMES_FILE}")
    else:
        messagebox.showinfo("Already Exists", "names.txt already exists.")

def browse_source():
    path = filedialog.askopenfilename(title="Select Source File")
    if path:
        source_entry.delete(0, "end")
        source_entry.insert(0, path)

def browse_output():
    path = filedialog.askdirectory(title="Select Output Folder")
    if path:
        output_entry.delete(0, "end")
        output_entry.insert(0, path)

def grab_folder_names():
    parent_folder = filedialog.askdirectory(title="Select Folder to Scan")
    if not parent_folder:
        return

    qualifying = set()
    for current_dir, _, files in os.walk(parent_folder):
        for file in files:
            if file.lower().endswith(ALLOWED_EXTENSIONS):
                qualifying.add(os.path.basename(current_dir))
                break

    if not qualifying:
        messagebox.showwarning("No Matches", f"No folders found with {ALLOWED_EXTENSIONS}")
        return

    with open(NAMES_FILE, "w", encoding="utf-8") as f:
        for name in sorted(qualifying):
            f.write(name + "\n")

    messagebox.showinfo("Done", f"✅ Found {len(qualifying)} folders.\nSaved to:\n{NAMES_FILE}")

def run_copy():
    source_file = source_entry.get().strip()
    output_folder = output_entry.get().strip()

    if not os.path.isfile(source_file):
        messagebox.showerror("Error", "Please select a valid source file.")
        return
    if not os.path.isdir(output_folder):
        messagebox.showerror("Error", "Please select a valid output folder.")
        return
    if not os.path.exists(NAMES_FILE):
        messagebox.showerror("Error", "names.txt not found. Create or generate it first.")
        return

    with open(NAMES_FILE, "r", encoding="utf-8") as f:
        new_names = [line.strip() for line in f if line.strip()]

    if not new_names:
        messagebox.showerror("Error", "names.txt is empty.")
        return

    os.makedirs(output_folder, exist_ok=True)
    _, ext = os.path.splitext(source_file)

    for name in new_names:
        new_file_path = os.path.join(output_folder, f"{name}{ext}")
        shutil.copy(source_file, new_file_path)

    messagebox.showinfo("Success", f"✅ Copied and renamed {len(new_names)} files.")

# === INITIAL SETUP ===
os.makedirs(COMPLETE_FOLDER, exist_ok=True)
extract_examples()

# === APP WINDOW ===
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🚓 ELS Generator")
app.geometry("700x480")

# Set taskbar & window icon
icon_path = os.path.join(BASE_DIR, "assets", "app.ico")
if os.path.exists(icon_path):
    app.iconbitmap(icon_path)

# === HEADER ===
header = ctk.CTkFrame(app, corner_radius=12)
header.pack(fill="x", padx=10, pady=10)
ctk.CTkLabel(header, text="🚓 ELS Generator", font=("Segoe UI", 20, "bold")).pack(side="left", padx=20, pady=10)
ctk.CTkLabel(header, text="Version 1.0", font=("Segoe UI", 12), text_color="#888").pack(side="right", padx=20)

# === TAB VIEW ===
tabs = ctk.CTkTabview(app, width=650, height=360)
tabs.pack(padx=10, pady=10, fill="both", expand=True)

tab_manual = tabs.add("📄 Copy & Rename")
tab_auto = tabs.add("⚙️ Name Finder")

# === MANUAL TAB CONTENT ===
ctk.CTkLabel(tab_manual, text="Select a source file and output folder to duplicate and rename files.",
             font=("Segoe UI", 12)).pack(pady=(10, 15))

frame_manual = ctk.CTkFrame(tab_manual, corner_radius=10)
frame_manual.pack(padx=20, pady=10, fill="x")

# Source row
source_row = ctk.CTkFrame(frame_manual)
source_row.pack(fill="x", pady=5)
ctk.CTkLabel(source_row, text="Source File:", width=100).pack(side="left", padx=10)
source_entry = ctk.CTkEntry(source_row, width=400)
source_entry.pack(side="left", padx=5)
ctk.CTkButton(source_row, text="📁 Browse", width=100, command=browse_source).pack(side="left", padx=5)

# Output row
output_row = ctk.CTkFrame(frame_manual)
output_row.pack(fill="x", pady=5)
ctk.CTkLabel(output_row, text="Output Folder:", width=100).pack(side="left", padx=10)
output_entry = ctk.CTkEntry(output_row, width=400)
output_entry.insert(0, COMPLETE_FOLDER)
output_entry.pack(side="left", padx=5)
ctk.CTkButton(output_row, text="📂 Browse", width=100, command=browse_output).pack(side="left", padx=5)

# Action buttons
ctk.CTkButton(tab_manual, text="▶️ Run Copy & Rename", width=250, height=35, command=run_copy).pack(pady=15)
ctk.CTkButton(tab_manual, text="📝 Create Blank names.txt", width=250, height=35, command=ensure_names_file).pack(pady=5)

ctk.CTkLabel(tab_manual, text=f"names.txt location:\n{NAMES_FILE}", text_color="#888").pack(pady=10)

# === AUTO TAB CONTENT ===
ctk.CTkLabel(tab_auto, text="Automatically detect folders containing .meta, .ytd, or .yft files.",
             font=("Segoe UI", 12)).pack(pady=(20, 10))
ctk.CTkButton(tab_auto, text="🔍 Scan Folder", width=250, height=40, command=grab_folder_names).pack(pady=20)
ctk.CTkLabel(tab_auto, text=f"Filtered by: {', '.join(ALLOWED_EXTENSIONS)}", text_color="#888").pack(pady=10)

# === FOOTER ===
footer = ctk.CTkLabel(app, text="© 2025 Three Peaks Studio",
                      font=("Segoe UI", 10), text_color="#777")
footer.pack(pady=(0, 10))

app.mainloop()
