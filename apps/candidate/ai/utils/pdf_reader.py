import pdfplumber


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract all readable text from a PDF file.
    """

    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        raise Exception(f"Unable to read PDF: {e}")

    return text.strip()