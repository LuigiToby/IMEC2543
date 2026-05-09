import serial
import tkinter as tk

PORT = "COM10"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

a1, a2, a3 = 90, 90, 90

def send():
    msg = f"{a1},{a2},{a3}\n"
    ser.write(msg.encode())
    label.config(text=f"S1:{a1}°  S2:{a2}°  S3:{a3}°")

def update_sliders():
    slider1.set(a1)
    slider2.set(a2)
    slider3.set(a3)

def on_slider(val=None):
    global a1, a2, a3
    a1 = slider1.get()
    a2 = slider2.get()
    a3 = slider3.get()
    send()

def set_manual():
    global a1, a2, a3
    try:
        a1 = int(entry1.get())
        a2 = int(entry2.get())
        a3 = int(entry3.get())
        a1 = max(0, min(180, a1))
        a2 = max(0, min(180, a2))
        a3 = max(0, min(180, a3))
        update_sliders()
        send()
    except:
        pass

def key_control(event):
    global a1, a2, a3

    if event.keysym == "Up":
        a2 += 1
    elif event.keysym == "Down":
        a2 -= 1
    elif event.keysym == "Left":
        a1 -= 1
    elif event.keysym == "Right":
        a1 += 1
    elif event.keysym == "w":
        a3 += 1
    elif event.keysym == "s":
        a3 -= 1

    a1 = max(0, min(180, a1))
    a2 = max(0, min(180, a2))
    a3 = max(0, min(180, a3))

    update_sliders()
    send()

root = tk.Tk()
root.title("Control 3 Servos ESP32")

root.bind("<Key>", key_control)

slider1 = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, label="Servo 1", command=on_slider)
slider1.set(a1)
slider1.pack()

slider2 = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, label="Servo 2", command=on_slider)
slider2.set(a2)
slider2.pack()

slider3 = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, label="Servo 3 (Garra)", command=on_slider)
slider3.set(a3)
slider3.pack()

frame = tk.Frame(root)
frame.pack()

entry1 = tk.Entry(frame, width=5)
entry1.pack(side="left")
entry2 = tk.Entry(frame, width=5)
entry2.pack(side="left")
entry3 = tk.Entry(frame, width=5)
entry3.pack(side="left")

btn = tk.Button(frame, text="Set", command=set_manual)
btn.pack(side="left")

label = tk.Label(root, text="S1:90°  S2:90°  S3:90°")
label.pack()

send()

root.mainloop()