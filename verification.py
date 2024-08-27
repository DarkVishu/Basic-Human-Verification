import random
import os
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

def check(text, image_name, canvas):
    text = text + ".jpg"
    if text == image_name:
        verify(canvas)
    else:
        failed_to_verify(canvas)

def verify(canvas):
    canvas.delete("all")
    canvas.create_rectangle(20, 20, 380, 280, fill="lightgreen")
    canvas.create_rectangle(60, 80, 340, 120, fill="green", outline="black")
    custom_font = font.Font(family="Baskerville Old Face", size=16, weight="bold")
    canvas.create_text(200, 100, text="Verified Successfully", font=custom_font)

def failed_to_verify(canvas):
    canvas.delete("all")
    canvas.create_rectangle(20, 20, 380, 280, fill="lightpink")
    canvas.create_rectangle(60, 80, 340, 120, fill="red", outline="black")
    custom_font = font.Font(family="Baskerville Old Face", size=16, weight="bold")
    canvas.create_text(200, 100, text="Failed to verify", font=custom_font)

    button_try_again = tk.Button(canvas, text="Try again", bg="navy", fg="white", font=custom_font,
                                 command=lambda: on_verify_click(canvas))
    canvas.create_window(200, 200, window=button_try_again)

def display_image(canvas, image_path, image_name):
    canvas.delete("all")
    
    img = Image.open(image_path)
    img = img.resize((230, 160))
    img_tk = ImageTk.PhotoImage(img)
    
    canvas.create_rectangle(20, 20, 380, 280, fill="white")
    canvas.create_image(200, 110, image=img_tk)
    canvas.create_image(45, 110, image=img_tk)
    canvas.create_image(350, 110, image=img_tk)
    canvas.create_rectangle(160, 30, 165, 190, fill="white", outline="white")
    canvas.create_rectangle(235, 30, 240, 190, fill="white", outline="white")
    canvas.create_rectangle(85, 75, 315, 80, fill="white", outline="white")
    canvas.create_rectangle(85, 130, 315, 135, fill="white", outline="white")
    canvas.create_rectangle(0,0,400,25,outline="black",fill="black")
    canvas.create_rectangle(0,0,20,300,outline="black",fill="black")
    canvas.create_rectangle(380,0,400,300,outline="black",fill="black")
    canvas.create_rectangle(0,280,400,300,outline="black",fill="black")
    canvas.create_rectangle(20,26,84,280,outline="lightblue",fill="lightblue")
    canvas.create_rectangle(315,26,380,280,outline="lightblue",fill="lightblue")
    canvas.create_rectangle(50,190,320,280,outline="lightblue",fill="lightblue")
    canvas.create_rectangle(80, 20, 320, 195, outline="black")

    # Shuffle and assign random texts to buttons
    options = ["flower", "car", "world"]
    random.shuffle(options)
    custom_font = font.Font(family="Baskerville Old Face", size=12, weight="bold")

    b1 = tk.Button(canvas, text=options[0], bg="navy", fg="white", font="arial", command=lambda: check(options[0], image_name, canvas))
    b2 = tk.Button(canvas, text=options[1], bg="navy", fg="white", font="arial", command=lambda: check(options[1], image_name, canvas))
    b3 = tk.Button(canvas, text=options[2], bg="navy", fg="white", font="arial", command=lambda: check(options[2], image_name, canvas))
    
    canvas.create_window(90, 250, window=b1)
    canvas.create_window(200, 250, window=b2)
    canvas.create_window(310, 250, window=b3)
    
    canvas.image = img_tk

def on_verify_click(canvas):
    directory = "C:\\Users\\vishu\\Desktop\\VERIFY"
    files = [f for f in os.listdir(directory) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    
    if files:
        random_file = random.choice(files)
        image_path = os.path.join(directory, random_file)
        display_image(canvas, image_path, random_file)
    else:
        print("No image files found in the specified directory.")

def create_main_window():
    root = tk.Tk()
    root.title("Human Verification")
    root.geometry("400x300")
    root.configure(bg="black")

    canvas = tk.Canvas(root, width=400, height=300, bg="black")
    canvas.pack()

    canvas.create_rectangle(20, 20, 380, 280, fill="pink")
    canvas.create_rectangle(60, 80, 340, 120, fill="lightblue")
    custom_font = font.Font(family="Baskerville Old Face", size=16, weight="bold")
    canvas.create_text(200, 100, text="Verify that you are a human?", font=custom_font, fill="black")

    button = tk.Button(root, text="Click here to verify", bg="navy", fg="white", font=custom_font,
                       command=lambda: on_verify_click(canvas))
    canvas.create_window(200, 200, window=button)

    root.mainloop()

create_main_window()

