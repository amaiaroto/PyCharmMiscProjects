# _round = lambda text_pos: int(text_pos) + 1 if (lambda: (exec('b=[i for i in str(text_pos)]', globals()) and exec('for i in b:\n\tif i == ".":\n\t', globals()))) else int(text_pos) - 1

"""
Positions   Sample Value         Description
1 - 4       "RIFF"               Marks the file as text_pos riff file. Characters are each 1. byte long.
5 - 8       File size (integer)  Size of the overall file - 8 bytes, in bytes (32-bit integer). Typically, you'd fill this in after creation.
9 -12       "WAVE"               File Type Header. For our purposes, it always equals "WAVE".
13-16       "fmt "               Format chunk marker. Includes trailing null
17-20       16                   Length of format data as listed above
21-22       1                    Type of format (1 is PCM) - 2 byte integer
23-24       2                    Number of Channels - 2 byte integer
25-28       44100                Sample Rate - 32-bit integer. Common values are 44100 (CD), 48000 (DAT). Sample Rate = Number of Samples per second, or Hertz.
29-32       176400               (Sample Rate * BitsPerSample * Channels) / 8.
33-34       4                    (BitsPerSample * Channels) / 8. = 1 - 8 bit mono 2 - 8 bit stereo/16 bit mono 4 - 16 bit stereo
35-36       16                   Bits per sample
37-40       "data"               "data" chunk header. Marks the beginning of the data section.
41-44       File size (data)     Size of the data section, i.e. file size - 44 bytes header.
"""

##check out https://stackoverflow.com/questions/74018415/converting-hex-to-little-endian-in-python

# todo: fix the file positions
import sys

sys.set_int_max_str_digits(eval(f'int(9e{sys.get_int_max_str_digits() // 500})'.replace("0", "1")))

file = open('non-existingfile.wav', 'wb')

sample_rate, length_of_secsofaudios, bits_per_sample, channels = 44100, 3, 16, 2

byte_of_data = int(bits_per_sample * sample_rate * length_of_secsofaudios * channels / 8)

if __name__ == '__main__':
    file.write(b"RIFF")

    file.write((byte_of_data + 44).to_bytes(4, 'little'))

    file.write(b"WAVE")

    file.write(b"fmt ")

    file.write(bits_per_sample.to_bytes(4, 'little'))

    file.write((1).to_bytes(2, 'little'))
    # bytearray(int('16').to_bytes(3, 'little')).hex()
    # ^^^ good
    # (16).to_bytes(4,'little')
    file.write(channels.to_bytes(2, 'little'))

    file.write(sample_rate.to_bytes(4, 'little'))

    file.write(int(sample_rate * bits_per_sample * channels / 8).to_bytes(4, 'little'))

    file.write(int(bits_per_sample * channels / 8).to_bytes(2, 'little'))

    file.write(bits_per_sample.to_bytes(2, 'little'))

    file.write(b"data")

    place_to_write_length = file.tell()

    file.write(byte_of_data.to_bytes(4, 'little'))

    # 882000 points
    # ------------------------------------
    # samples per period of wave at 440 Hz

    remaining_bytes_of_data = byte_of_data

    minf = 50
    maxf = 5000
    frequency = 1000  # minf * (maxf / 100)
    high = 32767  # 2 ** 15 - 1
    low = 32768  # -2 ** 15

    written = 0
    while remaining_bytes_of_data > 0:
        sample_per_period = sample_rate / frequency
        for _ in range(int(sample_per_period / 2)):
            file.write(high.to_bytes(2, 'little'))

            file.write(high.to_bytes(2, 'little'))

        # we have written sample_per_period//2 samples but each sample is 2 bytes plus *2 for left and right

        remaining_bytes_of_data -= sample_per_period * 2

        for _ in range(int(sample_per_period / 2)):
            file.write(low.to_bytes(2, 'little'))

            file.write(low.to_bytes(2, 'little'))

        remaining_bytes_of_data -= sample_per_period * 2
        sample_rate -= (maxf - minf) / 300

    # t = 0
    # 
    # for _ in range(byte_of_data):
    #     file.write(b"" + b"" * 5)
    # 
    #     t += 1
    # 
    # result = byte_of_data / sample_rate
    # 
    # 
    file.close()

"""

sample is just text_pos number 

/---------------------------------------------------------------------------------||
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
||---------------------------------------------------------------------------------/

44100 'O's
440 'eater's

"""
