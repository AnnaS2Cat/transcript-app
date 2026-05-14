import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

def transcrever_audio(file_audio, prompt=None):
    """Função para transcrever o áudio usando a API da Groq"""

    if file_audio:

        transcription = client.audio.transcriptions.create(
            file=(
                file_audio.name,
                file_audio,
            ),
            model="whisper-large-v3",
            language="pt",
            prompt=prompt,
            response_format="text"
        )

        return transcription

    return None


def transcrever_video(file_video, prompt=None):
    """Função para transcrever vídeo"""

    st.warning("Funcionalidade de vídeo ainda não implementada.")
    return None


def transcrever_microfone(prompt=None):
    """Função para transcrever entrada do microfone"""

    st.warning(
        "A funcionalidade de microfone "
        "ainda não está implementada."
    )

    return None


def main():
    """Função principal"""

    st.header(
        "🎙️ App Transcript",
        divider=True
    )

    st.subheader(
        "Transcreva áudios, vídeos e voz por microfone"
    )

    #criação das abas
    tabs = ["Microfone", "Vídeo", "Áudio"]

    tab_mic, tab_video, tab_audio = st.tabs(tabs)

    #microfone
    with tab_mic:

        st.markdown("Teste microfone")

    # aba áudio
    with tab_audio:

        st.markdown("Teste áudio")

        prompt_audio = st.text_input(
            "Digite o seu prompt para o áudio"
        )

        file_audio = st.file_uploader(
            "Adicione um arquivo de áudio",
            type=["mp3", "wav", "m4a", "ogg"]
        )

        if file_audio:

            with st.spinner("Transcrevendo áudio..."):

                transcricao_audio = transcrever_audio(
                    file_audio,
                    prompt_audio
                )

            if transcricao_audio:

                st.success("Transcrição concluída!")

                st.write(transcricao_audio)

            else:
                st.error("Erro ao transcrever o áudio.")

    #vídeo
    with tab_video:

        st.markdown("Teste vídeo")


if __name__ == "__main__":
    main()

#streamlit run .\transcricao_audio.py