import os
from detection.detect import detect_boxes
from recognition.recognition import recognize
from flask import Flask, request


UPLOAD_FOLDER = './data'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'

        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)

        try:
            detect_boxes(source=UPLOAD_FOLDER)
        except (AssertionError, FileNotFoundError):
            os.remove(path)
            return " НАЗВАНИЯ ФАЙЛОВ НА КИРИЛЛИЦЕ НЕ ПОДДЕРЖИВАЮТСЯ :("

        os.remove(path)

        result = recognize(UPLOAD_FOLDER)
        return result
    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''


if __name__ == '__main__':
    app.run()
