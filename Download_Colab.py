import os
import base64
from IPython.display import HTML, display

def download(path, filename=None):
    """
    Create a clickable download link for a file in the Colab/remote environment.
    
    path: full path to the file in the kernel (e.g. '/content/logfile.txt')
    filename: optional name that will appear in the download (defaults to basename)
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    filename = filename or os.path.basename(path)

    with open(path, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode("utf-8")
    href = f'data:application/octet-stream;base64,{b64}'
    html = f'<a download="{filename}" href="{href}">Download {filename}</a>'

    display(HTML(html))
