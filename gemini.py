import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=('example api key')

genai.configure(api_key='example api key')



import PIL.Image

def gemini():

  img = PIL.Image.open('image.jpg')
  img

  model = genai.GenerativeModel('gemini-1.5-flash')


  response = model.generate_content(img)

  to_markdown(response.text)

  response = model.generate_content(["I want you to analyse the image and figure out the color of the clothing, and what colour would match the color of the cloth. color: clothing type: matching pant color: matching accessories: . give the response in the json format", img], stream=True)
  response.resolve()

  to_markdown(response.text)
  print(response)

  print(response.text)


  model = genai.GenerativeModel('gemini-1.5-flash')
  chat = model.start_chat(history=[])
  chat

  response = chat.send_message("can you tell what color of pant will suit the shirt.")
  to_markdown(response.text)
  chat.history
