# 🎙️ App Transcript

Aplicação feita com Streamlit + Groq para transcrever áudios e vídeos utilizando IA.
O projeto permite:

- transcrição automática de áudio
- transcrição de vídeos grandes
- geração de resumo inteligente
- exportação em TXT
- exportação em DOCX
- exportação em PDF
- interface moderna com HTML + CSS

---

# Tecnologias utilizadas

- Python
- Streamlit
- Groq API
- Whisper Large V3
- Llama 3.3 70B
- MoviePy
- Pydub
- ReportLab
- Python-Docx

---

# Funcionalidades

## Transcrição de áudio

Suporta:

- MP3
- WAV
- M4A
- OGG

---

## Transcrição de vídeo

Suporta:

- MP4
- MOV
- AVI
- MKV

O sistema:

1. extrai o áudio do vídeo
2. divide em partes
3. transcreve cada parte
4. junta tudo automaticamente

---

## Resumo inteligente com ia

Após a transcrição, a ia gera automaticamente:

- resumo geral
- principais pontos
- decisões importantes
- nomes citados
- ações mencionadas
- datas importantes

---

# Exportação

A transcrição pode ser baixada em:

- TXT
- DOCX
- PDF

---

# Interface personalizada

O projeto utiliza:

- HTML
- CSS
- componentes personalizados no Streamlit

para deixar a interface mais moderna e agradável.

---

# ⚙️ Como rodar o projeto

## 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

---

## 2. Entre na pasta

```bash
cd transcript
```

---

## 3. Crie o ambiente virtual

### Windows

```bash
python -m venv .venv
```

---

## 4. Ative o ambiente virtual

### PowerShell

```bash
.\.venv\Scripts\Activate.ps1
```

---

## 5. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 6. Configure o arquivo .env

Crie um arquivo chamado:

```txt
.env
```

e adicione:

```env
GROQ_API_KEY= sua chave
```

---

## 7. Rode o projeto

```bash
streamlit run transcricao_video.py
```

---

# Estrutura do projeto

```txt
transcript/
│
├── components/
│   └── header.html
│
├── temp/
│
├── .env
├── style.css
├── transcricao_video.py
├── README.md
└── requirements.txt
```

---

# Obs

- vídeos grandes são divididos automaticamente
- os arquivos temporários são removidos após o processamento
- o resumo é gerado utilizando LLM da Groq

---

# Projeto desenvolvido para estudos de IA aplicada

Aplicação focada em automação de transcrição e processamento inteligente de mídia utilizando modelos modernos de linguagem.