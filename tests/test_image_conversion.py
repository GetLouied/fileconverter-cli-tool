import os
from conversions.image_converter import image_conversion_command
from click.testing import CliRunner

def test_image_conversion_png_to_jpeg():
    runner = CliRunner()
    input_path = 'exampleinputfolder/png_test_image.png'
    output_path = 'exampleoutputfolder/png_test_image.jpeg'
    result = runner.invoke(image_conversion_command, [input_path, output_path, 'jpeg'])
    assert result.exit_code == 0
    assert os.path.exists(output_path)

def test_image_conversion_jpeg_to_png():
    runner = CliRunner()
    input_path = 'exampleinputfolder/jpg_test_image.jpeg'
    output_path = 'exampleoutputfolder/jpg_test_image.png'
    result = runner.invoke(image_conversion_command, [input_path, output_path, 'png'])
    assert result.exit_code == 0
    assert os.path.exists(output_path)