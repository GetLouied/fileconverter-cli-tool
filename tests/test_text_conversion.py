import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conversions.text_converter import convert_text_command
from click.testing import CliRunner

def test_text_conversion_txt_to_pdf():
    runner = CliRunner()
    input_path = 'exampleinputfolder/test_text.txt'
    output_path = 'exampleoutputfolder/test_text.pdf'
    result = runner.invoke(convert_text_command, [input_path, output_path, 'pdf'])
    print(result.output)
    assert result.exit_code == 0
    assert os.path.exists(output_path)

def test_text_conversion_pdf_to_txt():
    runner = CliRunner()
    input_path = 'exampleinputfolder/test_text.pdf'
    output_path = 'exampleoutputfolder/test_text.txt'
    result = runner.invoke(convert_text_command, [input_path, output_path, 'txt'])
    print(result.output)
    assert result.exit_code == 0
    assert os.path.exists(output_path)

def test_text_conversion_txt_to_docx():
    runner = CliRunner()
    input_path = 'exampleinputfolder/test_text.txt'
    output_path = 'exampleoutputfolder/test_text.docx'
    result = runner.invoke(convert_text_command, [input_path, output_path, 'docx'])
    print(result.output)
    assert result.exit_code == 0
    assert os.path.exists(output_path)

def test_text_conversion_docx_to_txt():
    runner = CliRunner()
    input_path = 'exampleinputfolder/test_text.docx'
    output_path = 'exampleoutputfolder/test_text1.txt'
    result = runner.invoke(convert_text_command, [input_path, output_path, 'txt'])
    print(result.output)
    assert result.exit_code == 0
    assert os.path.exists(output_path)
