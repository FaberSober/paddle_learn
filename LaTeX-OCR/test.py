import PIL

if int(PIL.__version__[0]) < 9:
    print('Mandatory restart: Execute this cell again!')
    import os
    os.kill(os.getpid(), 9)

def upload_files():
  from google.colab import files
  from io import BytesIO
  uploaded = files.upload()
  return [(name, BytesIO(b)) for name, b in uploaded.items()]

from pix2tex import cli as pix2tex
from PIL import Image
model = pix2tex.LatexOCR()

from IPython.display import HTML, Math
display(HTML("<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/"
             "latest.js?config=default'></script>"))
table = r'\begin{array} {l|l} %s  \end{array}'