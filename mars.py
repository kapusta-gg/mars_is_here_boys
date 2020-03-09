from flask import Flask, url_for, request, render_template, abort

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = 'Марс'
    return render_template('base.html', title=title)

@app.route('/list_prof/<list>')
def list_prof(list):
    if list == 'ul':
        return render_template('blockul.html')
    elif list == 'ol':
        return render_template('blockol.html')
    else:
        abort(404)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
