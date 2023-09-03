from flask import Flask, request, jsonify
import requests

app = Flask(_name_)

@app.route('/numbers',methods=['GET'])
def fun():
    final_numbers = []
    query = request.args.getlist('url')
    print(query)
    for url in query:
        numbers = requests.get(url).json()['numbers']
        print(numbers)
        for number in numbers:
            if number not in final_numbers:
                final_numbers.append(number)
    final_numbers.sort()
    return f'numbers : {final_numbers}'


if _name_ == '_main_':
    app.run(debug=True)
