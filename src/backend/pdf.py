import fitz  # PyMuPDF

def split_pdf_vertically_text(input_pdf_path, output_pdf_path):
    original = fitz.open(input_pdf_path)
    result = fitz.open()

    for page in original:
        rect = page.rect
        mid_x = rect.x0 + rect.width / 2

        # Metade esquerda
        left = result.new_page(width=rect.width/2, height=rect.height)
        left.show_pdf_page(
            fitz.Rect(0, 0, rect.width/2, rect.height),
            original,
            page.number,
            clip=fitz.Rect(rect.x0, rect.y0, mid_x, rect.y1)
        )

        # Metade direita
        right = result.new_page(width=rect.width/2, height=rect.height)
        right.show_pdf_page(
            fitz.Rect(0, 0, rect.width/2, rect.height),
            original,
            page.number,
            clip=fitz.Rect(mid_x, rect.y0, rect.x1, rect.y1)
        )

    result.save(output_pdf_path)
    result.close()
    original.close()

if __name__ == "__main__":
    input_pdf = "entrada.pdf"
    output_pdf = "saida.pdf"
    split_pdf_vertically_text(input_pdf, output_pdf)
    print("PDF dividido ao meio com sucesso! (mantendo texto pesquisável)")
