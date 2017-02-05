import pyaudio
import wave
import time

def s_p(): # start parking
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/sp.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)
    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)
        
    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()

def f_p(): # finish parking
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/fp.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()

def s_d(): # start driving
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/sd.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()

def f_d(): # finish driving
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/fd.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()

def p_a(): # parking available
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/pa.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()

def wel(): # parking available
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/we.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()

def bt_error(): # parking available
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/bt_error.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()

def serial_error(): # parking available
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/serial_error.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()

def alarm(): # parking available
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/alarm.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()

def off_led(): # parking available
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/off_led.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()
    
def bt_success(): # start parking
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/bt_success.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)
    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)
        
    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()
    
def serial_success(): # start parking
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"/home/jarvis/Dropbox/WAV/serial_success.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)
    #play stream
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)
        
    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()
