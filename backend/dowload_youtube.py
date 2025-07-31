import yt_dlp
import subprocess
import os
import sys

# Caminho absoluto do ffmpeg
FFMPEG_PATH = r"C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"

def check_ffmpeg():
    try:
        result = subprocess.run([FFMPEG_PATH, "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print("Erro: ffmpeg não retornou código zero.")
            print(result.stderr)
            sys.exit(1)
        print("ffmpeg encontrado e funcionando.")
    except FileNotFoundError:
        print("Erro: ffmpeg não encontrado no caminho especificado.")
        sys.exit(1)

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        filename = os.path.basename(d.get('filename', ''))
        print(f"Baixando: {filename} - {percent}")
    elif d['status'] == 'finished':
        print("Download finalizado, iniciando processamento...")

def main():
    check_ffmpeg()

    output_path = r"C:\\Users\\H.E.L.I.X"
    os.makedirs(output_path, exist_ok=True)
    print("Bem-vindo ao programa de baixar vídeos do YouTube!")

    while True:
        url = input("\nInsira o link do vídeo (ou digite 'sair' para encerrar): ").strip()
        if url.lower() == "sair":
            print("Programa encerrado. Até mais!")
            break

        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
                'ffmpeg_location': FFMPEG_PATH,
                'progress_hooks': [progress_hook],
                'postprocessors': [{
                    'key': 'FFmpegMerger',
                }],
                'quiet': False,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print("\nBaixando o vídeo... Aguarde.")
                ydl.download([url])

            # Checagem do arquivo final
            # Extraímos o título para montar o caminho do arquivo (não é 100% seguro, mas funciona na maioria dos casos)
            info = ydl.extract_info(url, download=False)
            filename = ydl.prepare_filename(info)
            final_file = os.path.splitext(filename)[0] + ".mp4"

            if os.path.exists(final_file) and os.path.getsize(final_file) > 0:
                print(f"\nDownload e merge concluídos com sucesso! Arquivo salvo em:\n{final_file}")
            else:
                print("\nErro: arquivo final não encontrado ou está vazio após o download e merge.")

        except Exception as e:
            print(f"\nErro ao baixar o vídeo: {e}\nTente novamente.")

if __name__ == "__main__":
    main()


