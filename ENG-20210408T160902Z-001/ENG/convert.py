def translate(filepath):
    import speech_recognition as sr
    r = sr.Recognizer()
    p = sr.AudioFile(filepath)
    with p as source:
        audio = r.record(source)
        
    audio = r.recognize_google(audio)
        
    return(audio)