import os
import click
from docx import Document
from markdown2 import markdown as md2
from markdown import markdown as md
from fpdf import FPDF

def read_input_file(input_path: str, input_format: str) -> str:
    content = ""
    if input_format == 'docx':
        doc = Document(input_path)
        content = '\n'.join([para.text for para in doc.paragraphs])
    elif input_format == 'md':
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
    elif input_format == 'html':
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
    elif input_format == 'txt':
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
    return content

def text_conversion(input_path: str, output_path: str, output_format: str) -> None:
    try:
        input_format = os.path.splitext(input_path)[1][1:]
        content = read_input_file(input_path, input_format)

        if output_format == 'docx':
            doc = Document()
            doc.add_paragraph(content)
            doc.save(output_path)
        elif output_format == 'md':
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(content)
        elif output_format == 'html':
            html_content = md(content)
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(html_content)
        elif output_format == 'pdf':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, content)
            pdf.output(output_path)
        elif output_format == 'txt':
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(content)
        else:
            click.echo("Invalid output format.")
            return

        click.echo(f'Text converted and saved to {output_path}')
    except Exception as e:
        click.echo(f"An error occurred: {e}")

@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.argument('output_format', type=click.Choice(['docx', 'md', 'html', 'pdf', 'txt'], case_sensitive=False))
def convert_text_command(input_path: str, output_path: str, output_format: str) -> None:
    """
    Convert a text file to the specified format.

    INPUT_PATH: Path to the input text file.
    OUTPUT_PATH: Path to the output text file.
    OUTPUT_FORMAT: Desired text format (docx, md, html, pdf, txt).
    """
    text_conversion(input_path, output_path, output_format)

if __name__ == '__main__':
    convert_text_command()
