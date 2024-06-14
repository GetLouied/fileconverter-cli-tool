from pydub import AudioSegment
from typing import Literal
import click

def audio_conversion(input_path: str, output_path: str, output_format: Literal['wav', 'mp3', 'ogg', 'flv']) -> None:
    try: 
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format=output_format)

        click.echo(f"Audio converted and saved to {output_path}")
    
    except Exception as e:
        click.echo(f"An error occurred: {e}")


@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.argument('output_format', type=click.Choice(['wav', 'mp3', 'ogg', 'flv'], case_sensitive=False))
def audio_conversion_command(input_path: str, output_path: str, output_format: str) -> None:
    """
    Convert an audio file to the specified format. 

    INPUT_PATH: Path to the input audio file.
    OUTPUT_PATH: Path to the output audio file. 
    OUTPUT_FORMAT: Desired audio format (wav, mp3, ogg, flv).
    """

    audio_conversion(input_path, output_path, output_format)