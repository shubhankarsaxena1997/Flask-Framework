# from flask import Flask
# app = Flask(__name__)
#
# # print(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
# if __name__ == "__main__":
#     app.run()

def outer_func():
    print("I'm Outer")

    def inner_func():
        print("I'm Inner")

    return inner_func

nested = outer_func()
nested()
