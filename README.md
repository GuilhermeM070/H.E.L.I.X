# H.E.L.I.X. — Handler Eficiente para Log de Integração e eXtração

> ⚙️ Um sistema modular para download inteligente de mídias com futura interface gráfica e suporte a múltiplas fontes.

---

## 📌 Visão Geral

O **H.E.L.I.X.** é um script Python de extração automatizada de vídeos com foco em modularidade, escalabilidade e usabilidade futura via GUI. A base utiliza `yt_dlp` e `ffmpeg`, permitindo baixar mídias com qualidade personalizada, suporte a áudio/vídeo separados e lógica preparada para expansão.

--- 

## Stacks
🔹 Frontend:
- HTML5 + CSS3: A landing page foi completamente estilizada com foco em design responsivo e visual limpo. Foram aplicadas boas práticas de semântica, acessibilidade e organização estrutural.
- JavaScript Vanilla: Em andamento, a integração de scripts para manipulação dinâmica da interface — como validação de links, animações e interações em tempo real.

🔹 Backend:
- Python + FastAPI: O backend será responsável por orquestrar os downloads via yt_dlp, oferecendo uma API REST robusta, rápida e fácil de escalar.
- Integração com yt_dlp: Será utilizado para realizar o download e o merge de vídeo e áudio, com suporte a múltiplos formatos e tratamento de erros.
- Execução assíncrona: A FastAPI permitirá requisições simultâneas com alto desempenho, ideal para processos que envolvem I/O pesado como downloads.

---

## 🚀 Funcionalidades

- ✅ Download de vídeos via link direto
- ✅ Conversão automatizada com `ffmpeg`
- 🚧 Interface gráfica em construção (Tkinter/Qt)
- 🚧 Configurações via JSON em breve

---

## 🛠️ Requisitos

- Python 3.10+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/) (no PATH)

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/helix-downloader.git
cd helix-downloader
pip install -r requirements.txt
```
---

▶️ Uso
bash
Copiar
Editar
python helix.py
Por enquanto, o script solicita a URL e realiza o download direto com qualidade pré-definida.

---

🧭 Roadmap
- Modularização por camadas (core, interface, config)

- Suporte a múltiplos formatos (mp3, mp4, webm)

- Sistema de logs e histórico de downloads

- Configuração via arquivo externo

- Interface gráfica com progress bar

---

🧠 Nome & Filosofia
H.E.L.I.X. representa a espiral evolutiva da automação:
"De um script simples, nasce um motor híbrido, lógico e poderoso."

---

📄 Licença
MIT License © 2025 Guilherme Matos
