import os
from flask import Flask, request, render_template, send_from_directory, send_file, flash


import combine as combine
import ocr_functions as ocr

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# route for home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    # target = os.path.join(APP_ROOT, 'data/')
    # os.mkdir(target)

    if(request.method == "POST"):
        if(request.form['upload_button'] == "Generate tax form"):
            files = request.files.getlist("upload_button")
            for file in files:
                print(file)
                if not file.filename == '':

                    file.save("./images/{}".format(file.filename))

            combine.create_csv()
            print("Tax return generated!")
            return send_file("./filled/return.pdf", attachment_filename='return.pdf')
    return render_template('upload.html')


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("data", filename)


if __name__ == "__main__":
    app.secret_key = 'some secret key'
    app.run(port=4555, debug=True)

# import os

# from flask import Flask, request, render_template, send_from_directory

# __author__ = 'ibininja'

# app = Flask(__name__)

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# @app.route("/")
# def index():
#     return render_template("upload.html")


# @app.route("/upload", methods=['POST'])
# def upload():

#     target = os.path.join(APP_ROOT, 'data/')
#     print(target)
#     if not os.path.isdir(target):
#         os.mkdir(target)
#     for upload in request.files.getlist("file"):
#         print(upload)
#         print("{} is the file name".format(upload.filename))
#         filename = upload.filename
#         # This is to verify files are supported
#         ext = os.path.splitext(filename)[1]
#         if (ext == ".jpg") or (ext == ".png"):
#             print("File supported moving on...")
#         else:
#             render_template("Error.html", message="Files uploaded are not supported...")
#         destination = "/".join([target, filename])
#         print("Accept incoming file:", filename)
#         print("Save it to:", destination)
#         upload.save(destination)

#     # return send_from_directory("data", filename, as_attachment=True)
#     return render_template("complete.html", image_name=filename)


# @app.route('/upload/<filename>')
# def send_image(filename):
#     return send_from_directory("data", filename)


# if __name__ == "__main__":
#     app.run(port=4555, debug=True)
