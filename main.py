from flask import Flask, url_for, request, redirect

import os

app = Flask(__name__)


@app.route('/carousel')
def load_photo():
    return f''' <!doctype html>
<html lang="en">
<head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">

                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align='center'>Пейзажи Марса</h1>
                            <br>


    <div id="carouselExampleControls" class="carousel slide d-inline-block" data-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img class="d-block w-100" src="{url_for('static', filename='img/mars4.jpg')}" data-holder-rendered="true">
            </div>
            <div class="carousel-item">
                <img class="d-block w-100" src="{url_for('static', filename='img/mars1.jpg')}" data-holder-rendered="true">
            </div>
            <div class="carousel-item">
                <img class="img-fluid" src="{url_for('static', filename='img/mars3.jpg')}" alt="...">
            </div>
        </div>
        <!-- Элементы управления -->
        <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev" >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>

        </a>
        <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide-to="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>

        </a>
    </div>

</div>


</body>
</html>'''


def main():
    app.run(host='localhost', port=8080)


if __name__ == '__main__':
    main()
