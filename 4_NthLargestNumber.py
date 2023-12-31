from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    # List of Integers
    numbers = [90, 10, 23, 55, 44, 25, 50, 70]
 
    #Sorting list of Integers
    numbers.sort()
    return "Input List is [90, 10, 23, 55, 44, 25, 50, 70]"+" Sorted List: "+ str(numbers) + "Fifth (5th) largest number of list is: " + str(numbers[len(numbers)-4])


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
