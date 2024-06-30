import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conversions.audio_converter import audio_conversion_command
from click.testing import CliRunner

def test_audio_conversion_wav_to_mp3():
    runner = CliRunner()
    input_path = 'exampleinputfolder/test_audio.wav'
    output_path = 'exampleoutputfolder/test_audio.mp3'
    result = runner.invoke(audio_conversion_command, [input_path, output_path, 'mp3'])
    print(result.output)
    assert result.exit_code == 0
    assert os.path.exists(output_path)

def test_audio_conversion_mp3_to_wav():
    runner = CliRunner()
    input_path = 'exampleinputfolder/test_audio.mp3'
    output_path = 'exampleoutputfolder/test_audio.wav'
    result = runner.invoke(audio_conversion_command, [input_path, output_path, 'wav'])
    print(result.output)
    assert result.exit_code == 0
    assert os.path.exists(output_path)

def test_audio_conversion_wav_to_ogg():
    runner = CliRunner()
    input_path = 'exampleinputfolder/test_audio.wav'
    output_path = 'exampleoutputfolder/test_audio.ogg'
    result = runner.invoke(audio_conversion_command, [input_path, output_path, 'ogg'])
    print(result.output)
    assert result.exit_code == 0
    assert os.path.exists(output_path)

def test_audio_conversion_mp3_to_flv():
    runner = CliRunner()
    input_path = 'exampleinputfolder/test_audio.mp3'
    output_path = 'exampleoutputfolder/test_audio.flv'
    result = runner.invoke(audio_conversion_command, [input_path, output_path, 'flv'])
    print(result.output)
    assert result.exit_code == 0
    assert os.path.exists(output_path)
