from flask import Flask, render_template
import queries as query

app = Flask(__name__)
conn = None


@app.route('/')
def hello_world():
    data = dict(
        title="nani",
        greet="nesze neked random szavak"
    )
    word = get_daily_word()
    data["daily"] = dict(word=word[0], meaning=word[1])
    if not data.keys().__contains__("daily"):
        pass
    return render_template("index.html", data=data)


def get_daily_word():
    word = query.get_daily_word()
    if word is not None:
        return word
    get_daily_word()


if __name__ == '__main__':
    app.run()
