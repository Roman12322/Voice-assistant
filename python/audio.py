# import speech_recognition as sr
#
#
# def get_text_from_audiofile(path):
#     response = ""  # function output
#
#     # Создаем объект Recognizer
#     r = sr.Recognizer()
#
#     # Записываем аудио с микрофона
#     audio = sr.AudioFile(path)
#
#     with audio as source:
#         audio = r.listen(source)
#     try:
#         # Преобразуем записанный звук в текст
#         response = r.recognize_google(audio, language="ru")
#
#     except sr.UnknownValueError:
#         response = "Извините, не удалось распознать речь."
#
#     except sr.RequestError as e:
#         response = "Ошибка сервиса распознавания речи; {0}".format(e)
#
#     return response
#
