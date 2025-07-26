# First install: pip install customtkinter
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random

class ModernInteractiveWindow:
    def __init__(self):
        # Set appearance mode and color theme
        ctk.set_appearance_mode("dark")  # "light" or "dark"
        ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("Modern Interactive Window")
        self.root.geometry("500x400")
        
        # Variables
        self.name_var = ctk.StringVar()
        self.counter = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title_label = ctk.CTkLabel(
            self.root, 
            text="🚀 Modern Interactive App", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)
        
        # Main frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Name input section
        name_frame = ctk.CTkFrame(main_frame)
        name_frame.pack(pady=15, padx=20, fill="x")
        
        ctk.CTkLabel(name_frame, text="Enter your name:", font=ctk.CTkFont(size=14)).pack(pady=5)
        
        self.name_entry = ctk.CTkEntry(
            name_frame, 
            textvariable=self.name_var,
            placeholder_text="Your name here...",
            width=200,
            height=35
        )
        self.name_entry.pack(pady=5)
        
        # Buttons section
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(pady=15, padx=20, fill="x")
        
        # First row of buttons
        btn_row1 = ctk.CTkFrame(button_frame)
        btn_row1.pack(pady=5, fill="x")
        
        greet_btn = ctk.CTkButton(
            btn_row1, 
            text="👋 Greet Me!", 
            command=self.greet_user,
            width=120,
            height=35
        )
        greet_btn.pack(side="left", padx=5)
        
        counter_btn = ctk.CTkButton(
            btn_row1, 
            text="📊 Count Up!", 
            command=self.increment_counter,
            width=120,
            height=35
        )
        counter_btn.pack(side="left", padx=5)
        
        # Counter display
        self.counter_label = ctk.CTkLabel(
            button_frame, 
            text=f"Counter: {self.counter}", 
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.counter_label.pack(pady=10)
        
        # Text area
        text_frame = ctk.CTkFrame(main_frame)
        text_frame.pack(pady=15, padx=20, fill="both", expand=True)
        
        ctk.CTkLabel(text_frame, text="📝 Output:", font=ctk.CTkFont(size=14)).pack(pady=5, anchor="w")
        
        self.text_area = ctk.CTkTextbox(
            text_frame,
            height=150,
            font=ctk.CTkFont(family="Courier", size=12)
        )
        self.text_area.pack(pady=5, fill="both", expand=True)
        
        # Bottom buttons
        bottom_frame = ctk.CTkFrame(main_frame)
        bottom_frame.pack(pady=15, padx=20, fill="x")
        
        # Button row
        btn_row2 = ctk.CTkFrame(bottom_frame)
        btn_row2.pack(fill="x")
        
        random_btn = ctk.CTkButton(
            btn_row2, 
            text="🎲 Random Quote", 
            command=self.show_random_quote,
            width=110,
            height=35
        )
        random_btn.pack(side="left", padx=5)
        
        clear_btn = ctk.CTkButton(
            btn_row2, 
            text="🗑️ Clear", 
            command=self.clear_output,
            width=80,
            height=35,
            fg_color="red",
            hover_color="darkred"
        )
        clear_btn.pack(side="left", padx=5)
        
        # Theme toggle
        theme_btn = ctk.CTkButton(
            btn_row2, 
            text="🌓 Theme", 
            command=self.toggle_theme,
            width=80,
            height=35
        )
        theme_btn.pack(side="left", padx=5)
        
        quit_btn = ctk.CTkButton(
            btn_row2, 
            text="❌ Quit", 
            command=self.quit_app,
            width=80,
            height=35,
            fg_color="gray",
            hover_color="darkgray"
        )
        quit_btn.pack(side="right", padx=5)
    
    def greet_user(self):
        name = self.name_var.get().strip()
        if name:
            greeting = f"🎉 Hello, {name}! Welcome to the modern interactive window!\n"
            self.add_to_output(greeting)
        else:
            messagebox.showwarning("Warning", "Please enter your name first!")
    
    def increment_counter(self):
        self.counter += 1
        self.counter_label.configure(text=f"Counter: {self.counter}")
        self.add_to_output(f"📈 Counter increased to {self.counter}\n")
    
    def show_random_quote(self):
        quotes = [
            "💡 The only way to do great work is to love what you do. - Steve Jobs",
            "🚀 Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "🌟 Life is what happens to you while you're busy making other plans. - John Lennon",
            "✨ The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "🌅 It is during our darkest moments that we must focus to see the light. - Aristotle"
        ]
        quote = random.choice(quotes)
        self.add_to_output(f"{quote}\n\n")
    
    def add_to_output(self, text):
        self.text_area.insert("end", text)
        self.text_area.see("end")  # Auto-scroll to bottom
    
    def clear_output(self):
        self.text_area.delete("1.0", "end")
        self.add_to_output("🧹 Output cleared.\n")
    
    def toggle_theme(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = "light" if current_mode == "dark" else "dark"
        ctk.set_appearance_mode(new_mode)
        self.add_to_output(f"🎨 Theme changed to {new_mode} mode\n")
    
    def quit_app(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.quit()
    
    def run(self):
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    app = ModernInteractiveWindow()
    app.run()
