from docx import Document
import markdown
from markdown2 import markdown as md2
from typing import Literal
import click
import os

def text_conversion(input_path: str, output_path: str, output_format: Literal['docx', 'md', 'html', 'pdf', 'txt', 'rtf']) -> None:
    try:
        with open(input_path, 'r') as file:
            content = file.read()

        if output_format == 'docx':
            doc = Document()
            doc.add_paragraph(content)
            doc.save(output_path)
        elif output_format == 'md':
            with open(output_path, 'w') as file:
                file.write(content)
        elif output_format == 'html':
            html_content = md2(content)
            with open(output_path, 'w') as file:
                file.write(html_content)
        elif output_format == 'pdf':
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, content)
            pdf.output(output_path)
        elif output_format == 'txt':
            with open(output_path, 'w') as file:
                file.write(content)
        elif output_format == 'rtf':
            from pyth.plugins.rtf15.reader import Rtf15Reader
            from pyth.plugins.plaintext.writer import PlaintextWriter
            doc = Rtf15Reader.read(file)
            text = PlaintextWriter.write(doc).getvalue()
            with open(output_path, 'w') as file:
                file.write(text)
        else:
            click.echo("Invalid output format.")
            return

        click.echo(f'Text converted and saved to {output_path}')
    except Exception as e:
        click.echo(f"An error occurred: {e}")

@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.argument('output_format', type=click.Choice(['docx', 'md', 'html', 'pdf', 'txt', 'rtf'], case_sensitive=False))
def convert_text_command(input_path: str, output_path: str, output_format: str) -> None:
    """
    Convert a text file to the specified format. 

    INPUT_PATH: Path to the input text file.
    OUTPUT_PATH: Path to the output text file. 
    OUTPUT_FORMAT: Desired text format (docx, md, html, pdf, txt, rtf).
    """
    text_conversion(input_path, output_path, output_format)
