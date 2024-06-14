import click
from conversions.audio_converter import audio_conversion
from conversions.image_converter import image_conversion
from conversions.text_converter import text_conversion

@click.command()
@click.option('--type', '-t', type=click.Choice(['audio', 'image', 'text']), help='Type of conversion: audio, image, or text.')
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.argument('output_format', type=click.Choice(['wav', 'mp3', 'ogg', 'flv', 'png', 'jpeg', 'docx', 'md', 'html', 'pdf', 'txt', 'rtf'], case_sensitive=False))
def convert(type, input_path, output_path, output_format):
    """
    Convert files between different formats.
    """
    if type == 'audio':
        audio_conversion(input_path, output_path, output_format)
    elif type == 'image':
        image_conversion(input_path, output_path, output_format)
    elif type == 'text':
        text_conversion(input_path, output_path, output_format)
    else:
        click.echo('Invalid conversion type. Use --help for more information.')

if __name__ == '__main__':
    convert()
