from pytube import YouTube
from tkinter import Tk, filedialog, Label, Entry, Button
import os

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
        status_label.config(text="Download concluído com sucesso. O vídeo foi salvo em:!\n" + output_path)
    except Exception as e:
        status_label.config(text="Ocorreu um erro durante o download: " + str(e))


def download_youtube_audio():
    video_url = video_url_entry.get()
    output_path = choose_directory()
    output_filename = video_url_entry.get()

    try:
        youtube = YouTube(video_url)
        audio_stream = youtube.streams.filter(only_audio=True).first()
        save_path = os.path.join(output_path, output_filename)

        status_label.config(text=f"Baixando áudio de \"{youtube.title}\"...")
        audio_stream.download(output_path)
        status_label.config(text="Download concluído. O áudio foi salvo em:\n" + save_path)
    except Exception as e:
        status_label.config(text="Ocorreu um erro durante o download:\n" + str(e))


root = Tk()
root.title("Baixador de Vídeo")
root.geometry("430x200")
video_url_label = Label(root, text="Insira o link do vídeo:")
video_url_label.pack(pady=10)
video_url_entry = Entry(root, width=50)
video_url_entry.pack(pady=5)
download_button = Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=10)
download_button = Button(root, text="baixar áudio", command=download_youtube_audio)
download_button.pack(pady=10)
status_label = Label(root, text="")
status_label.pack()

root.mainloop()