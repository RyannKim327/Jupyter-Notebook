import os;

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.allow_origin = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' https://replit.com"
  }
}
c.NotebookApp.notebook_dir = "notebooks"
c.NotebookApp.password = os.environ['NOTEBOOK_PASSWORD']
