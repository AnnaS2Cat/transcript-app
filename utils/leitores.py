from pypdf import PdfReader
from docx import Document


def ler_pdf(arquivo_pdf):
    """Extrai texto do PDF"""

    texto = ""

    leitor = PdfReader(arquivo_pdf)
    for pagina in leitor.pages:

        texto += pagina.extract_text() + "\n"

    return texto


def ler_txt(arquivo_txt):
    """Lê TXT"""

    return arquivo_txt.read().decode("utf-8")


def ler_docx(arquivo_docx):
    """Lê DOCX"""

    documento = Document(arquivo_docx)

    texto = ""

    for paragrafo in documento.paragraphs:

        texto += paragrafo.text + "\n"

    return texto