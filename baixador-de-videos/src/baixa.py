from pytube import YouTube
from tkinter import Tk, filedialog, Label, Entry, Button

def choose_directory():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

def download_video():
    try:
        video_url = video_url_entry.get()
        video = YouTube(video_url)
        output_path = choose_directory()
        video.streams.get_highest_resolution().download(output_path)
        status_label.config(text="Download concluído com sucesso!")
    except Exception as e:
        status_label.config(text="Ocorreu um erro durante o download: " + str(e))


root = Tk()
root.title("Baixador de Vídeo")
root.geometry("400x150")
video_url_label = Label(root, text="Insira o link do vídeo:")
video_url_label.pack(pady=10)
video_url_entry = Entry(root, width=50)
video_url_entry.pack(pady=5)
download_button = Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=10)
status_label = Label(root, text="")
status_label.pack()

root.mainloop()