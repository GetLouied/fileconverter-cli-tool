from PIL import Image
import click
import os

def image_conversion(input_path: str, output_path: str, output_format: str) -> None:
    try:
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        img = Image.open(input_path)

        if output_format.lower() == 'png':
            if not output_path.lower().endswith('.png'):
                output_path += '.png'
            img.save(output_path, 'PNG')
        elif output_format.lower() == 'jpeg':
            if not output_path.lower().endswith('.jpeg') and not output_path.lower().endswith('.jpg'):
                output_path += '.jpg'
            img.save(output_path, 'JPEG')
        else:
            click.echo("Invalid output format.")
            return
        click.echo(f"Image converted and saved to {output_path}")
    except Exception as e:
        click.echo(f"An error occurred: {e}")

@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.argument('output_format', type=click.Choice(['png', 'jpeg'], case_sensitive=False))
def image_conversion_command(input_path: str, output_path: str, output_format: str) -> None:
    """
    Convert an image file to the specified format.

    INPUT_PATH: Path to the input image file.
    OUTPUT_PATH: Path to the output image file.
    OUTPUT_FORMAT: Desired output format (png or jpeg).
    """
    image_conversion(input_path, output_path, output_format)
