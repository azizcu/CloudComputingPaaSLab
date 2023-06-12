from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    # Program to multiply two matrices using nested loops

    # 3x3 matrix
    X = [[123,70,30],
        [40 ,50,66],
        [78 ,80,99]]
    # 3x4 matrix
    Y = [[54,58,16,27],
        [66,78,83,90],
        [44,56,94,61]]
    # result is 3x4
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

    # iterate through rows of X
    for i in range(len(X)):
     # iterate through columns of Y
     for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

    return "Matrix Multiplication of 3X3 and 4X3 matrixs. So result is 3x4 :  " + str(result)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
