import tkinter
from tkinter import *
import customtkinter as ctk
from pygame import mixer
from customtkinter import *
from tkinter import filedialog
from typing import List, Optional

files: List[str] = []

file_index: Optional[str] = None

mixer.init()

is_playing = False

########################################################

#def current_time():
#    mixer.music.get_pos()
#    progressBar.configure(text=current_time) # anything mentioning progressBar is currently not in use


def play_sound():
    global is_playing
    mixer.music.play()
    if file_index:
        is_playing = True
        play_status.configure(text=f"playing: {os.path.basename(file_index)}")

    else:
        play_status.configure(text="no file selected")


def openfile():
    global file_index
    selected_file = filedialog.askopenfilename(
        filetypes=[("Audio files", "*.mp3")])

    if selected_file:
        file_index = selected_file
        mixer.music.load(file_index)
        play_status.configure(text=f"loaded: {os.path.basename(file_index)}. press play!")
    else:
        print("no file selected")


def back_button():
    if mixer.music.get_busy():
        mixer.music.rewind()


def play_update():
    if not file_index:
        play_status.configure(text="no file selected")
    play_status.configure(text=f"Playing: {file_index}")


def stop_button():
    play_status.configure(text="track stopped")
    if is_playing == is_playing:
        playButton.configure(state="active")


def get_current_value():
    return '{:.2f}'.format(current_value.get())


def mute_button():
    if is_playing == is_playing:
        mixer.music.set_volume(0)
    else:
        play_status.configure(text="nothing to mute; load an mp3")


def slider_change(_):
    volume = current_value.get() / 100
    mixer.music.set_volume(volume)

def stop_and_close():
    try:
        mixer.music.stop()
    except Exception as e:
        print(f"Error stopping sound: {e}")
    finally:
        root.quit()
        root.destroy()
########################################################

root = CTk()
frame = Frame(root)
frame.grid()
root.minsize(500,500)
root.maxsize(500,500)
root.title('walkingharlem MP3 player')

current_value = tkinter.DoubleVar(value=50)
mixer.music.set_volume(current_value.get() / 100)

label = ctk.CTkLabel(root, text="0.1.9 mp3 filenames now show in label upon load + when hitting play")

label.grid(row = 1, column = 2)

########################################################

play_status = ctk.CTkLabel(root, text="nothing playing")

play_status.grid(row = 2, column = 2)


playButton = ctk.CTkButton(root, text="▶", width=10, command = play_sound, hover_color="#005c14", fg_color="#ffffff", text_color="#000000")

playButton.grid(row = 3, column = 2, padx = 10)


backButton = ctk.CTkButton(root, text="⏮", width=10, hover_color="#005c14", fg_color="#ffffff", text_color="#000000", command=back_button)

backButton.grid(row = 3, column = 1, sticky = NE)


skipButton = ctk.CTkButton(root, text="⏭", width=10, hover_color="#005c14", fg_color="#ffffff", text_color="#000000")

skipButton.grid(row = 3, column = 3)


stopButton = ctk.CTkButton(root, text="■", width=10, command=lambda: [mixer.music.stop(), stop_button()], hover_color="#005c14", fg_color="#ffffff", text_color="#000000")

stopButton.grid(row = 6, column = 2, padx=10, pady=5)


muteButton = ctk.CTkButton(root, text="mute", width=10, command=mute_button, hover_color="#005c14", fg_color="#ffffff", text_color="#000000")

muteButton.grid(row = 7, column = 2)


volumeSlider = (

    ctk.CTkSlider(master=root,
              from_=0, to = 100,
              orientation='horizontal',
              command=slider_change,
              variable=current_value,
              fg_color="#ffffff",
              button_color="#147a2a",
              button_hover_color="#005c14",
              button_length=3,
              progress_color="#005c14",
              button_corner_radius = 2
              ))

volumeSlider.grid(row=9, column=2, pady = 25)





open_file = ctk.CTkButton(root, text="open file", command=openfile, corner_radius = 0, fg_color = "#147a2a", hover_color = "#005c14")
open_file.grid(column = 2, row = 10, pady = 15)



#volumeSlider.get() # use this to show volume level in label in future

########################################################
########################################################
########################################################

root.protocol("WM_DELETE_WINDOW", stop_and_close)

root.mainloop()
