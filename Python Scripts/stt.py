import pyaudio
import wave
import speech_recognition as sr


def stt( ):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024 
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"


    audio = pyaudio.PyAudio()

    # 마이크로부터 음성 데이터를 캡처합니다.
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    print("녹음을 시작합니다.")

    # 지정한 시간 동안 음성 데이터를 캡처합니다.
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)): 
        data = stream.read(CHUNK)
        frames.append(data)

    print("녹음이 완료되었습니다.")

    # 마이크 스트림을 정리하고 종료합니다.
    stream.stop_stream()
    stream.close()
    audio.terminate()


    # WAV 파일로 저장합니다.
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


    # 오디오 파일 읽기
    filename = "output.wav"
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
    # 음성 인식
    text = r.recognize_google(audio_data, language="ko-KR")

# 결과 출력
    print(text)

    return text 