import os
import time
import whisper
from email.message import EmailMessage
import ssl
import smtplib
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

sentence_transformer_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
def calculate_embedding(text):
    return sentence_transformer_model.encode(text)

email_sender = 'animesh.m2202@gmail.com'
email_pass = 'syrx bizy dtfs tsgp'
send_to = 'aniaero22@gmail.com'
body = "Emergency for Mr Joseph!"
model = whisper.load_model("base")
#result = model.transcribe("audio_2.wav")
#print(result["text"])
em = EmailMessage()
em['From'] = email_sender
em['To'] = send_to
em['Subject'] = "Emergency"
em.set_content(body)
context = ssl.create_default_context()

# if(result["text"] == " Emergency. Call the doctor."):
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(email_sender, email_pass)
#         smtp.sendmail(email_sender, send_to, em.as_string())
folder_path = "D:\Hackathon\Axxess"
def get_audio_files_in_folder(folder_path):
    audio_files = [file for file in os.listdir(folder_path) if file.endswith('.m4a')]
    return audio_files

while True:
    audio_files = get_audio_files_in_folder(folder_path)
    if audio_files:
        for audio_file in audio_files:
            audio_file_path = os.path.join(folder_path, audio_file)
            result = model.transcribe(audio_file_path)
            embedding_result = calculate_embedding(result["text"])
            embedding_expected = calculate_embedding("Emergency. Call the doctor.")
            similarity = cosine_similarity([embedding_result], [embedding_expected])[0][0]
            print(result["text"])
            print(similarity)
            if similarity > 0.5:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_pass)
                    smtp.sendmail(email_sender, send_to, em.as_string())
            # Remove processed audio file
            #os.remove(audio_file_path)
    time.sleep(5)

