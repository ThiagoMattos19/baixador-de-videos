from pytube import YouTube
from tkinter import Tk, filedialog, Label, Entry, Button

def choose_directory():
    # Abre uma janela de diálogo para o usuário selecionar o diretório de download
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

def download_video():
    try:
        # Obtenha o link do vídeo fornecido pelo usuário
        video_url = video_url_entry.get()

        # Crie um objeto da classe YouTube usando a URL do vídeo
        video = YouTube(video_url)

        # Abra a janela de diálogo para o usuário escolher o diretório de download
        output_path = choose_directory()

        # Baixe o vídeo na melhor resolução disponível
        video.streams.get_highest_resolution().download(output_path)

        status_label.config(text="Download concluído com sucesso!")
    except Exception as e:
        status_label.config(text="Ocorreu um erro durante o download: " + str(e))

# Criar a janela principal
root = Tk()
root.title("Baixador de Vídeo")
root.geometry("400x150")

# Rótulo e campo de entrada para o link do vídeo
video_url_label = Label(root, text="Insira o link do vídeo:")
video_url_label.pack(pady=10)

video_url_entry = Entry(root, width=50)
video_url_entry.pack(pady=5)

# Botão para iniciar o download
download_button = Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=10)

# Rótulo para exibir o status do download
status_label = Label(root, text="")
status_label.pack()

# Iniciar o loop da interface
root.mainloop()