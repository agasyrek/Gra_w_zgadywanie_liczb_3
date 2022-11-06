from flask import Flask, request

app = Flask(__name__)

html_main = """

<!DOCTYPE html>
<html lang = 'en'>
    <head>
        <meta charset="UTF-8">
        <title> Main page </title>
    </head>
    <body>
        <h1>Think a number from 0 to 1000 and I'll guess it in max. 10 tries</h1>
        <form action ='' method = 'POST'>
        <input type = 'hidden' name = 'min' value = '{}'></input>
        <input type = 'hidden' name = 'max' value = '{}'></input>
        <input type = 'submit' value = 'submit'>
        </form>
    </body>
</html>
"""

html_with_form = """
<!DOCTYPE html>
<html lang ='en'>
    <head>
        <meta charset="UTF-8">
        <title> Game </title>
    </head>
    <body>
        <h1> It is {guess} ? <h2>
        <form action = '' method = 'POST'>
            <input type = 'submit' name = 'answer' value = 'too big'>
            <input type = 'submit' name = 'answer' value = 'too small'>
            <input type = 'submit' name = 'answer' value = 'You win'>
            <input type = 'hidden' name = 'min' value = '{min}'>
            <input type = 'hidden' name = 'max' value = '{max}'>
            <input type = 'hidden' name = 'guess' value = '{guess}'>
        </form>
    </body>
</html>
"""

html_final = """
<!DOCTYPE html>
<html lang ='en'>
    <head>
        <meta charset="UTF-8">
        <title> Final </title>
    </head>
    <body>
        <h1>I won ! Your number is {guess}<h1>
    </body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def guess_game():
    if request.method == 'GET':
        return html_main.format(0, 1000)
    else:
        min_num = int(request.form.get('min'))
        max_num = int(request.form.get('max'))
        answer = request.form.get('answer')
        guess = int(request.form.get('guess', 500))

        if answer == "too big":
            max_num = guess
        elif answer == "too small":
            min_num = guess
        elif answer == "You win":
            print("I win")
            return html_final.format(guess=guess)
        else:
            print("Don't cheat")
        guess = (max_num - min_num) // 2 + min_num

        return html_with_form.format(guess=guess, min=min_num, max=max_num)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
