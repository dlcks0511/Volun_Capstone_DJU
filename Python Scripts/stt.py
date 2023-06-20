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

    # 마이크로 음성 데이터 추출
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    frames = []

    print("말하세요")

    # 일정 시간 녹음
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)): 
        data = stream.read(CHUNK)
        frames.append(data)

    print("음성 인식 끝")

    # 마이크 스트림 종료
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # WAV 파일 저장
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close() 

    # 오디오 파일 입력
    filename = "output.wav"
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
    # google 엔진으로 음성 변환
    text = r.recognize_google(audio_data, language="ko-KR")

    return text 