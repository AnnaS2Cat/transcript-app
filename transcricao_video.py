import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from moviepy.video.io.VideoFileClip import VideoFileClip

load_dotenv()

client = Groq()

# pasta temporária
folder_temp = "temp"
os.makedirs(folder_temp, exist_ok=True)

# arquivos temporários
file_audio_temp = f"{folder_temp}/audio.mp3"
file_video_temp = f"{folder_temp}/video.mp4"


def transcrever_audio(file_audio, prompt=None):
    """Função para transcrever áudio"""

    try:

        if file_audio:

            transcription = client.audio.transcriptions.create(
                file=file_audio,
                model="whisper-large-v3",
                language="pt",
                response_format="text",
                prompt=prompt
            )

            return transcription

    except Exception as erro:

        st.error(f"Erro no áudio: {erro}")

    return None


def transcrever_video(file_video, prompt=None):
    """Função para transcrever vídeo"""

    try:

        if file_video:

            # salva vídeo temporariamente
            with open(file_video_temp, "wb") as f_video:
                f_video.write(file_video.read())

            # converte vídeo para áudio
            video_convert = VideoFileClip(file_video_temp)

            # verifica se existe áudio
            if video_convert.audio is None:

                st.error("O vídeo não possui áudio.")

                return None

            # extrai áudio
            video_convert.audio.write_audiofile(
                file_audio_temp,
                logger=None
            )

            # fecha arquivo do vídeo
            video_convert.close()

            # abre áudio convertido
            with open(file_audio_temp, "rb") as file_audio:

                transcription = client.audio.transcriptions.create(
                    file=file_audio,
                    model="whisper-large-v3",
                    language="pt",
                    response_format="text",
                    prompt=prompt
                )

            return transcription

    except Exception as erro:

        st.error(f"Erro no vídeo: {erro}")

    return None


def exibir_transcricao(texto):
    """Mostra transcrição na tela"""

    st.success("Transcrição concluída!")

    st.text_area(
        "Texto transcrito",
        texto,
        height=300
    )

    st.download_button(
        label="Baixar transcrição",
        data=texto,
        file_name="transcricao.txt",
        mime="text/plain"
    )


def main():
    """Função principal"""

    st.set_page_config(
        page_title="App Transcript",
        page_icon="🎙️",
        layout="centered"
    )

    st.header("🎙️ App Transcript", divider=True)

    st.subheader(
        "Transcreva áudios e vídeos"
    )

    # abas
    tabs = ["Vídeo", "Áudio"]

    tab_video, tab_audio = st.tabs(tabs)

    # aba áudio
    with tab_audio:

        st.markdown("### Transcrição de áudio")

        prompt_audio = st.text_input(
            "Prompt do áudio (opcional)",
            key="audio_prompt",
            placeholder="Ex: reunião médica, podcast, aula..."
        )

        file_audio = st.file_uploader(
            "Adicione um arquivo de áudio",
            type=["mp3", "wav", "m4a", "ogg"]
        )

        if file_audio:

            st.audio(file_audio)

            with st.spinner("Transcrevendo áudio..."):

                transcricao_audio = transcrever_audio(
                    file_audio,
                    prompt_audio
                )

            if transcricao_audio:

                exibir_transcricao(transcricao_audio)

    # aba vídeo
    with tab_video:

        st.markdown("### Transcrição de vídeo")

        prompt_video = st.text_input(
            "Prompt do vídeo (opcional)",
            key="video_prompt",
            placeholder="Ex: entrevista, aula, palestra..."
        )

        file_video = st.file_uploader(
            "Adicione um arquivo de vídeo",
            type=["mp4", "mov", "avi", "mkv"]
        )

        if file_video:

            st.video(file_video)

            with st.spinner("Transcrevendo vídeo..."):

                transcricao_video = transcrever_video(
                    file_video,
                    prompt_video
                )

            if transcricao_video:

                exibir_transcricao(transcricao_video)


if __name__ == "__main__":
    main()

#streamlit run .\transcricao_video.py