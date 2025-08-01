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
        print("✅ ffmpeg encontrado e funcionando.")
    except FileNotFoundError:
        print("❌ Erro: ffmpeg não encontrado no caminho especificado.")
        sys.exit(1)

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        filename = os.path.basename(d.get('filename', ''))
        print(f"⏬ Baixando: {filename} - {percent}")
    elif d['status'] == 'finished':
        print("✅ Download finalizado, iniciando processamento...")

def montar_opcoes(url, tipo_download, output_path):
    if tipo_download == "audio":
        return {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'ffmpeg_location': FFMPEG_PATH,
            'progress_hooks': [progress_hook],
            'quiet': False,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
    else:  # vídeo
        return {
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

def main():
    check_ffmpeg()

    # Define o caminho da pasta base
    base_path = r"C:\\H.E.L.I.X"
    print("🎬 Bem-vindo ao H.E.L.I.X — Download Inteligente de Mídias!\n")

    while True:
        url = input("\n🔗 Insira o link do vídeo (ou digite 'sair' para encerrar): ").strip()
        if url.lower() == "sair":
            print("Programa encerrado. Até mais!")
            break

        tipo = input("🎧 Deseja baixar (1) Vídeo ou (2) Apenas Áudio (MP3)? ").strip()
        tipo_download = "audio" if tipo == "2" else "video"

        # Define subpasta
        output_path = os.path.join(base_path, "audios" if tipo_download == "audio" else "videos")
        os.makedirs(output_path, exist_ok=True)

        try:
            ydl_opts = montar_opcoes(url, tipo_download, output_path)

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\nBaixando {tipo_download}... Aguarde.")
                ydl.download([url])

            print(f"\n✅ Download de {tipo_download} concluído com sucesso. Verifique a pasta:\n{output_path}")

        except Exception as e:
            print(f"\n❌ Erro ao baixar o conteúdo: {e}\nTente novamente.")

if __name__ == "__main__":
    main()



