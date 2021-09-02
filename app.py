from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def handler():
    word = request.args.get('word')
    dictionary = {
        'cat': 'кошка',
        'dog': 'собака',
        'table': 'стол',
    }
    translation = dictionary.get(word, 'не найдено в словаре')
    return render_template(
        'form.html',
        word=word,
        translation=translation
    )
