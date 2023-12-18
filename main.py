from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/en-us/')
@app.route('/en-us/home/')
def home_en():
    return """
    
<!DOCTYPE HTML>
<html>
    <head>
        <title>UkrOS - Home</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="https://ukros2022.github.io/oswebsite/images/icons/icon.png">
    </head>
    <body>
        <style>
            body {
                margin: 0px;
                background-color: white;
            }

            .menu {
                height: 35px;
                width: auto;
                background-color: gray;
                display: flex;
            }

            .button-menu {
                text-decoration: none;
            }

            .button-menu:hover {
                text-decoration: none;
                background-color: silver;
            }

            .home-text-menu {
                margin: 0px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: white;
                text-align: none;
                font-size: 15px;
            }

            .home-text-menu:hover {
                margin: 0px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: black;
                text-align: none;
                font-size: 15px;
            }

            .page {
                width: 500px;
                padding: 15px;
            }

            .left-bar {
                width: 500;
                vertical-align: top;
            }

            .right-bar {
                width: 135px;
                background-color: gray;
            }

            .main {
                background-color: silver;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .about {
                background-color: silver;
                margin-top: 5px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .language {
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-decoration: none;
            }

            .language:hover {
                background-color: silver;
                color: black;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-decoration: none;
            }

            * {box-sizing:border-box}

        .slideshow-container {
            max-width: 1000px;
            position: relative;
            margin: auto;
        }

        .mySlides {
            display: none;
        }

        .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            margin-top: -22px;
            padding: 16px;
            color: white;
            font-weight: bold;
            font-size: 18px;
            transition: 0.6s ease;
            user-select: none;
        }

        .next {
            right: 0;
        }

        .prev:hover, .next:hover {
            background-color: rgba(128,128,128,0.8);
        }

        .text {
            color: #f2f2f2;
            font-size: 15px;
            padding: 8px 12px;
            position: absolute;
            bottom: 8px;
            width: 100%;
            text-align: center;
            vertical-align: bottom;
        }

        .dot {
            cursor: pointer;
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #f2f2f2;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
        }

        .active, .dot:hover {
            background-color: #717171;
        }

        /* Fading animation */
        .fade {
            animation-name: fade;
            animation-duration: 1.5s;
        }

        @keyframes fade {
            from {opacity: .4}
            to {opacity: 1}
        }

        button {
            border-radius: 0px;
            background-color: gray;
            border: none;
            font-size: 20px;
        }

        button:hover {
            border-radius: 0px;
            background-color: black;
            border: none;
            font-size: 20px;
            color: white;
        }

        td {
            padding: 0px;
        }

        </style>
        <div width="100%" align="CENTER">
            <div class="menu">
                <table width="100%">
                    <tbody>
                        <tr>
                            <td class="button-menu" align="LEFT" width="70px">
                                <a href="/en-us/home" class="button-menu">
                                    <div style="display:flex">
                                        <img src="https://ukros2022.github.io/oswebsite/images/icons/icon.png" width="27px" height="27px">
                                        <p class="home-text-menu">UkrOS</p>
                                    </div>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT" width="80px">
                                <a href="/en-us/downloads" class="button-menu">
                                    <p class="home-text-menu">Downloads</p>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT"width="95px">
                                <a href="/en-us/ukrosweb" class="button-menu">
                                    <p class="home-text-menu">UkrOS Web</p>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT"width="50px">
                                <a href="/en-us/about" class="button-menu">
                                    <p class="home-text-menu">About</p>
                                </a>
                            </td>
                            <td width="auto" align="CENTER"></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="page" align="CENTER">
                <table width="100%">
                    <tbody>
                        <td class="left-bar">
                            <div class="main">
                                <h1>What's new:</h1>
                                
                                <div class="slideshow-container">

                                <div class="mySlides fade">
                                <img src="images/news/1.png" style="width:100%">
                                <div class="text">Caption Text</div>
                                </div>

                                <div class="mySlides fade">
                                <img src="images/news/2.png" style="width:100%">
                                <div class="text">Caption Two</div>
                                </div>

                                <div class="mySlides fade">
                                <img src="images/news/3.png" style="width:100%">
                                <div class="text">Caption Three</div>
                                </div>

                                <a class="prev" onclick="plusSlides(-1)">❮</a>
                                <a class="next" onclick="plusSlides(1)">❯</a>

                                </div>
                                <br>

                                <div style="text-align:center">
                                <span class="dot" onclick="currentSlide(1)"></span> 
                                <span class="dot" onclick="currentSlide(2)"></span> 
                                <span class="dot" onclick="currentSlide(3)"></span> 
                                </div>

                                <script>
                                let slideIndex = 1;
                                showSlides(slideIndex);

                                function plusSlides(n) {
                                showSlides(slideIndex += n);
                                }

                                function currentSlide(n) {
                                showSlides(slideIndex = n);
                                }

                                function showSlides(n) {
                                let i;
                                let slides = document.getElementsByClassName("mySlides");
                                let dots = document.getElementsByClassName("dot");
                                if (n > slides.length) {slideIndex = 1}    
                                if (n < 1) {slideIndex = slides.length}
                                for (i = 0; i < slides.length; i++) {
                                    slides[i].style.display = "none";  
                                }
                                for (i = 0; i < dots.length; i++) {
                                    dots[i].className = dots[i].className.replace(" active", "");
                                }
                                slides[slideIndex-1].style.display = "block";  
                                dots[slideIndex-1].className += " active";
                                }
                                </script>
                            </div>
                            <div class="about">
                                <h3 align="CENTER">UkrOS @2022-2023</h3>
                            </div>
                        </td>
                        
                        <td class="right-bar" valign=TOP>
                            <ul>
                                <li class="language"><a href="/en-us/downloads" class="language">English</a></li>
                                <li class="language"><a href="/de-de/downloads" class="language">German</a></li>
                                <li class="language"><a href="/fr-fr/downloads" class="language">French</a></li>
                                <li class="language"><a href="/ru-ru/downloads" class="language">Russian</a></li>
                                <li class="language"><a href="/uk-ua/downloads" class="language">Ukrainian</a></li>
                                <li class="language"><a href="/be-by/downloads" class="language">Belarussian</a></li>
                            </ul>
                            <img src="https://ukros2022.github.io/oswebsite/images/baners/1.png">
                            <img src="https://ukros2022.github.io/oswebsite/images/baners/2.png">
                        </td>
                    </tbody>
                </table>
            </div>
        </div>
    </body>
</html>

"""

@app.route('/downloads/')
@app.route('/en-us/downloads/')
def downloads_en():
    return """
    
<!DOCTYPE HTML>
<html>
    <head>
        <title>UkrOS - Downloads</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="https://ukros2022.github.io/oswebsite/images/icons/icon.png">
    </head>
    <body>
        <style>
            body {
                margin: 0px;
                background-color: white;
            }

            .menu {
                height: 35px;
                width: auto;
                background-color: gray;
                display: flex;
            }

            .button-menu {
                text-decoration: none;
            }

            .button-menu:hover {
                text-decoration: none;
                background-color: silver;
            }

            .home-text-menu {
                margin: 0px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: white;
                text-align: none;
                font-size: 15px;
            }

            .home-text-menu:hover {
                margin: 0px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: black;
                text-align: none;
                font-size: 15px;
            }

            .page {
                width: 500px;
                padding: 15px;
            }

            .left-bar {
                width: 500;
                vertical-align: top;
            }

            .right-bar {
                width: 135px;
                background-color: gray;
            }

            .main {
                background-color: silver;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .about {
                background-color: silver;
                margin-top: 5px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .language {
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-decoration: none;
            }

            .language:hover {
                background-color: silver;
                color: black;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-decoration: none;
            }

            * {box-sizing:border-box}

        .slideshow-container {
            max-width: 1000px;
            position: relative;
            margin: auto;
        }

        .mySlides {
            display: none;
        }

        .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            margin-top: -22px;
            padding: 16px;
            color: white;
            font-weight: bold;
            font-size: 18px;
            transition: 0.6s ease;
            user-select: none;
        }

        .next {
            right: 0;
        }

        .prev:hover, .next:hover {
            background-color: rgba(128,128,128,0.8);
        }

        .text {
            color: #f2f2f2;
            font-size: 15px;
            padding: 8px 12px;
            position: absolute;
            bottom: 8px;
            width: 100%;
            text-align: center;
            vertical-align: bottom;
        }

        .dot {
            cursor: pointer;
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #f2f2f2;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
        }

        .active, .dot:hover {
            background-color: #717171;
        }

        /* Fading animation */
        .fade {
            animation-name: fade;
            animation-duration: 1.5s;
        }

        @keyframes fade {
            from {opacity: .4}
            to {opacity: 1}
        }

        button {
            border-radius: 0px;
            background-color: gray;
            border: none;
            font-size: 20px;
        }

        button:hover {
            border-radius: 0px;
            background-color: black;
            border: none;
            font-size: 20px;
            color: white;
        }

        td {
            padding: 0px;
        }

        </style>
        <div width="100%" align="CENTER">
            <div class="menu">
                <table width="100%">
                    <tbody>
                        <tr>
                            <td class="button-menu" align="LEFT" width="70px">
                                <a href="/en-us/home" class="button-menu">
                                    <div style="display:flex">
                                        <img src="https://ukros2022.github.io/oswebsite/images/icons/icon.png" width="27px" height="27px">
                                        <p class="home-text-menu">UkrOS</p>
                                    </div>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT" width="80px">
                                <a href="/en-us/downloads" class="button-menu">
                                    <p class="home-text-menu">Downloads</p>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT"width="95px">
                                <a href="/en-us/ukrosweb" class="button-menu">
                                    <p class="home-text-menu">UkrOS Web</p>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT"width="50px">
                                <a href="/en-us/about" class="button-menu">
                                    <p class="home-text-menu">About</p>
                                </a>
                            </td>
                            <td width="auto" align="CENTER"></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="page" align="CENTER">
                <table width="100%">
                    <tbody>
                        <td class="left-bar">
                            <div class="main">
                                <h1>Downloads:</h1>
                                
                                <div class="slideshow-container">

                                <div class="mySlides fade">
                                <img src="images/news/1.png" style="width:100%">
                                <div class="text">Caption Text</div>
                                </div>

                                <div class="mySlides fade">
                                <img src="images/news/2.png" style="width:100%">
                                <div class="text">Caption Two</div>
                                </div>

                                <div class="mySlides fade">
                                <img src="images/news/3.png" style="width:100%">
                                <div class="text">Caption Three</div>
                                </div>

                                <a class="prev" onclick="plusSlides(-1)">❮</a>
                                <a class="next" onclick="plusSlides(1)">❯</a>

                                </div>
                                <br>

                                <div style="text-align:center">
                                <span class="dot" onclick="currentSlide(1)"></span> 
                                <span class="dot" onclick="currentSlide(2)"></span> 
                                <span class="dot" onclick="currentSlide(3)"></span> 
                                </div>

                                <script>
                                let slideIndex = 1;
                                showSlides(slideIndex);

                                function plusSlides(n) {
                                showSlides(slideIndex += n);
                                }

                                function currentSlide(n) {
                                showSlides(slideIndex = n);
                                }

                                function showSlides(n) {
                                let i;
                                let slides = document.getElementsByClassName("mySlides");
                                let dots = document.getElementsByClassName("dot");
                                if (n > slides.length) {slideIndex = 1}    
                                if (n < 1) {slideIndex = slides.length}
                                for (i = 0; i < slides.length; i++) {
                                    slides[i].style.display = "none";  
                                }
                                for (i = 0; i < dots.length; i++) {
                                    dots[i].className = dots[i].className.replace(" active", "");
                                }
                                slides[slideIndex-1].style.display = "block";  
                                dots[slideIndex-1].className += " active";
                                }
                                </script>

                                <b>About:</b>
                                <p>UkrOS - ukrainin operite system, who was created for nationality of Ukraine.</p>

                                <b>Requirement:</b>

                                <br>
                                <br>
                                <b><i>Minimum:</i></b>
                                <p>Disk: 30 GB<br>RAM:  2 GB<br>CPU: 1 CPU<br>Type: 64-bit (x64)<br>VRAM: 16 MB</p>

                                <br>
                                <br>
                                <b><i>Recommended:</i></b>
                                <p>Disk: 64 GB<br>RAM:  2 GB<br>CPU: 2 CPU<br>Type: 64-bit (x64)<br>VRAM: 128 MB (Support of 3D acceleration)</p>

                                <b>Software:</b>

                                <br>
                                <br>
                                <b><i>Messangers:</i></b>
                                <ul>
                                    <li>Viber</li>
                                    <li>Telegram</li>
                                    <li>Skype</li>
                                    <li>Teams</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Collaborations:</i></b>
                                <ul>
                                    <li>Zoom</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Office packages:</i></b>
                                <ul>
                                    <li>LibreOfiice</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Video editor:</i></b>
                                <ul>
                                    <li>Kdenlive</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Image editor:</i></b>
                                <ul>
                                    <li>Krita</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Programs for developing:</i></b>
                                <ul>
                                    <li>QTCreator</li>
                                    <li>SQLiteBrowser</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Document viewer:</i></b>
                                <ul>
                                    <li>Okular</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Browser:</i></b>
                                <ul>
                                    <li>Konqueror</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Mail clients:</i></b>
                                <ul>
                                    <li>KMail</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Calendar:</i></b>
                                <ul>
                                    <li>KOrganizer</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Image viewer:</i></b>
                                <ul>
                                    <li>Gwenview</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Media player:</i></b>
                                <ul>
                                    <li>Dragon</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Programs for run to virtual machines:</i></b>
                                <ul>
                                    <li>VirtualBox</li>
                                </ul>

                                <br>
                                <br>
                                <b><i>Libraries:</i></b>
                                <ul>
                                    <li>Glib1.0</li>
                                    <li>Glib2.0</li>
                                    <li>Glib3.0</li>
                                    <li>Glib3.1</li>
                                    <li>LLVM</li>
                                </ul>

                                <b>Downloads:</b>
                                <br>
                                <a href=""><button id="downloads_button" width="100px">Downloads</button></a>
                                <br>
                                <br>

                                <b>Donation:</b>
                                <br>
                                <a href="https://www.paypal.com/myaccount/transfer?from=Header"><button id="paypal_button" width="100px">PayPal</button></a>
                                <br>
                                <p>Email for donation: vadimsavenko2008@outlook.com</p>
                                <br>

                                <b>Feedback:</b>
                                <br>
                                <p>If you don't like in our operite system UkrOS or if you want, that we add in operite system UkrOS. You can to write feedback or mail to <a href="mail:ukros2022@gmail.com" style="color: black">ukros2022@gmail.com</a></p>
                                <input id="email_input" placeholder="Your email" style="width: 315px;"></input>
                                <input id="text_input" placeholder="Text" style="width: 315px; height: 100px;"></input>
                                <br>
                                <a href=""><button id="send_button" width="100px">Send </button></a>
                            </div>
                            <div class="about">
                                <h3 align="CENTER">UkrOS @2022-2023</h3>
                            </div>
                        </td>
                        
                        <td class="right-bar" valign=TOP>
                            <ul>
                                <li class="language"><a href="/en-us/downloads" class="language">English</a></li>
                                <li class="language"><a href="/de-de/downloads" class="language">German</a></li>
                                <li class="language"><a href="/fr-fr/downloads" class="language">French</a></li>
                                <li class="language"><a href="/ru-ru/downloads" class="language">Russian</a></li>
                                <li class="language"><a href="/uk-ua/downloads" class="language">Ukrainian</a></li>
                                <li class="language"><a href="/be-by/downloads" class="language">Belarussian</a></li>
                            </ul>
                            <img src="https://ukros2022.github.io/oswebsite/images/baners/1.png">
                            <img src="https://ukros2022.github.io/oswebsite/images/baners/2.png">
                        </td>
                    </tbody>
                </table>
            </div>
        </div>
    </body>
</html>
"""

@app.route('/ukrosweb/')
@app.route('/en-us/ukrosweb/')
def ukrosweb_en():
    return """

<!DOCTYPE HTML>
<html>
    <head>
        <title>UkrOS - UkrOS Web</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="https://ukros2022.github.io/oswebsite/images/icons/icon.png">
    </head>
    <body>
        <style>
            body {
                margin: 0px;
                background-color: white;
            }

            .menu {
                height: 35px;
                width: auto;
                background-color: gray;
                display: flex;
            }

            .button-menu {
                text-decoration: none;
            }

            .button-menu:hover {
                text-decoration: none;
                background-color: silver;
            }

            .home-text-menu {
                margin: 0px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: white;
                text-align: none;
                font-size: 15px;
            }

            .home-text-menu:hover {
                margin: 0px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: black;
                text-align: none;
                font-size: 15px;
            }

            .page {
                width: 500px;
                padding: 15px;
            }

            .left-bar {
                width: 500;
                vertical-align: top;
            }

            .right-bar {
                width: 135px;
                background-color: gray;
            }

            .main {
                background-color: silver;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .about {
                background-color: silver;
                margin-top: 5px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .language {
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-decoration: none;
            }

            .language:hover {
                background-color: silver;
                color: black;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-decoration: none;
            }

            * {box-sizing:border-box}

        .slideshow-container {
            max-width: 1000px;
            position: relative;
            margin: auto;
        }

        .mySlides {
            display: none;
        }

        .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            margin-top: -22px;
            padding: 16px;
            color: white;
            font-weight: bold;
            font-size: 18px;
            transition: 0.6s ease;
            user-select: none;
        }

        .next {
            right: 0;
        }

        .prev:hover, .next:hover {
            background-color: rgba(128,128,128,0.8);
        }

        .text {
            color: #f2f2f2;
            font-size: 15px;
            padding: 8px 12px;
            position: absolute;
            bottom: 8px;
            width: 100%;
            text-align: center;
            vertical-align: bottom;
        }

        .dot {
            cursor: pointer;
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #f2f2f2;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
        }

        .active, .dot:hover {
            background-color: #717171;
        }

        /* Fading animation */
        .fade {
            animation-name: fade;
            animation-duration: 1.5s;
        }

        @keyframes fade {
            from {opacity: .4}
            to {opacity: 1}
        }

        button {
            border-radius: 0px;
            background-color: gray;
            border: none;
            font-size: 20px;
        }

        button:hover {
            border-radius: 0px;
            background-color: black;
            border: none;
            font-size: 20px;
            color: white;
        }

        td {
            padding: 0px;
        }

        </style>
        <div width="100%" align="CENTER">
            <div class="menu">
                <table width="100%">
                    <tbody>
                        <tr>
                            <td class="button-menu" align="LEFT" width="70px">
                                <a href="/en-us/home" class="button-menu">
                                    <div style="display:flex">
                                        <img src="https://ukros2022.github.io/oswebsite/images/icons/icon.png" width="27px" height="27px">
                                        <p class="home-text-menu">UkrOS</p>
                                    </div>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT" width="80px">
                                <a href="/en-us/downloads" class="button-menu">
                                    <p class="home-text-menu">Downloads</p>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT"width="95px">
                                <a href="/en-us/ukrosweb" class="button-menu">
                                    <p class="home-text-menu">UkrOS Web</p>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT"width="50px">
                                <a href="/en-us/about" class="button-menu">
                                    <p class="home-text-menu">About</p>
                                </a>
                            </td>
                            <td width="auto" align="CENTER"></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="page" align="CENTER">
                <table width="100%">
                    <tbody>
                        <td class="left-bar">
                            <div class="main">
                                <img src="https://ukros2022.github.io/oswebsite/images/ukrosweb/icon.png" width="128px" height="128px">

                                <h1>UkrOS Web:</h1>
                                
                                <b><i>About:</i></b>
                                <p>UkrOS Web - this is web operite system, who can to working in browser. This web operite system isn't for free. For using, you must to registration and buy a license of UkrOS Web for 1 month. This license cost of 10$(USD) or 360₴(UAH).</p>
                                
                                <p><i>UkrOS Company is developing of this operite system now.</i></p>
                            </div>

                            <div class="about">
                                <h3 align="CENTER">UkrOS @2022-2023</h3>
                            </div>
                        </td>
                        
                        <td class="right-bar" valign=TOP>
                            <ul>
                                <li class="language"><a href="/en-us/ukrosweb" class="language">English</a></li>
                                <li class="language"><a href="/de-de/ukrosweb" class="language">German</a></li>
                                <li class="language"><a href="/fr-fr/ukrosweb" class="language">French</a></li>
                                <li class="language"><a href="/ru-ru/ukrosweb" class="language">Russian</a></li>
                                <li class="language"><a href="/uk-ua/ukrosweb" class="language">Ukrainian</a></li>
                                <li class="language"><a href="/be-by/ukrosweb" class="language">Belarussian</a></li>
                            </ul>
                            <img src="https://ukros2022.github.io/oswebsite/images/baners/1.png">
                            <img src="https://ukros2022.github.io/oswebsite/images/baners/2.png">
                        </td>
                    </tbody>
                </table>
            </div>
        </div>
        
        <!--
                <a href="/pl-pl/about" class="text-a">Polish</a>
                <a href="/ro-ro/about" class="text-a">Romainian</a>
                <a href="/hu-hu/about" class="text-a">Hungarian</a>
                <a href="/ko-kr/about" class="text-a">Korean</a>
                <a href="/ja-jp/about" class="text-a">Japanese</a>
                <a href="/zh-ch/about" class="text-a">Chinese (Simplified)</a>
                <a href="/zh-tw/about" class="text-a">Chinese (Traditional)</a>
                <a href="/hy-am/about" class="text-a">Armenian</a>
                <a href="/az-az/about" class="text-a">Azerbaijani</a>
                <a href="/ka-ge/about" class="text-a">Georgian</a>
                <a href="/ar-sa/about" class="text-a">Arabic</a>
                <a href="/fa-ir/about" class="text-a">Persian</a>
        -->
    </body>
</html>
"""

@app.route('/about/')
@app.route('/en-us/about/')
def about_en():
    return """

<!DOCTYPE HTML>
<html>
    <head>
        <title>UkrOS - About</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="https://ukros2022.github.io/oswebsite/images/icons/icon.png">
    </head>
    <body>
    <body>
        <style>
            body {
                margin: 0px;
                background-color: white;
            }

            .menu {
                height: 35px;
                width: auto;
                background-color: gray;
                display: flex;
            }

            .button-menu {
                text-decoration: none;
            }

            .button-menu:hover {
                text-decoration: none;
                background-color: silver;
            }

            .home-text-menu {
                margin: 0px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: white;
                text-align: none;
                font-size: 15px;
            }

            .home-text-menu:hover {
                margin: 0px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: black;
                text-align: none;
                font-size: 15px;
            }

            .page {
                width: 500px;
                padding: 15px;
            }

            .left-bar {
                width: 500;
                vertical-align: top;
            }

            .right-bar {
                width: 135px;
                background-color: gray;
            }

            .main {
                background-color: silver;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .about {
                background-color: silver;
                margin-top: 5px;
                padding: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .language {
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-decoration: none;
            }

            .language:hover {
                background-color: silver;
                color: black;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-decoration: none;
            }

            * {box-sizing:border-box}

        .slideshow-container {
            max-width: 1000px;
            position: relative;
            margin: auto;
        }

        .mySlides {
            display: none;
        }

        .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            margin-top: -22px;
            padding: 16px;
            color: white;
            font-weight: bold;
            font-size: 18px;
            transition: 0.6s ease;
            user-select: none;
        }

        .next {
            right: 0;
        }

        .prev:hover, .next:hover {
            background-color: rgba(128,128,128,0.8);
        }

        .text {
            color: #f2f2f2;
            font-size: 15px;
            padding: 8px 12px;
            position: absolute;
            bottom: 8px;
            width: 100%;
            text-align: center;
            vertical-align: bottom;
        }

        .dot {
            cursor: pointer;
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #f2f2f2;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
        }

        .active, .dot:hover {
            background-color: #717171;
        }

        /* Fading animation */
        .fade {
            animation-name: fade;
            animation-duration: 1.5s;
        }

        @keyframes fade {
            from {opacity: .4}
            to {opacity: 1}
        }

        button {
            border-radius: 0px;
            background-color: gray;
            border: none;
            font-size: 20px;
        }

        button:hover {
            border-radius: 0px;
            background-color: black;
            border: none;
            font-size: 20px;
            color: white;
        }

        td {
            padding: 0px;
        }

        </style>
        <div width="100%" align="CENTER">
            <div class="menu">
                <table width="100%">
                    <tbody>
                        <tr>
                            <td class="button-menu" align="LEFT" width="70px">
                                <a href="/en-us/home" class="button-menu">
                                    <div style="display:flex">
                                        <img src="https://ukros2022.github.io/oswebsite/images/icons/icon.png" width="27px" height="27px">
                                        <p class="home-text-menu">UkrOS</p>
                                    </div>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT" width="80px">
                                <a href="/en-us/downloads" class="button-menu">
                                    <p class="home-text-menu">Downloads</p>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT"width="95px">
                                <a href="/en-us/ukrosweb" class="button-menu">
                                    <p class="home-text-menu">UkrOS Web</p>
                                </a>
                            </td>
                            <td class="button-menu" align="LEFT"width="50px">
                                <a href="/en-us/about" class="button-menu">
                                    <p class="home-text-menu">About</p>
                                </a>
                            </td>
                            <td width="auto" align="CENTER"></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="page" align="CENTER">
                <table width="100%">
                    <tbody>
                        <td class="left-bar">
                            <div class="main">
                                <h1>About:</h1>
                                
                                <b><i>About company:</i></b>
                                <p>Company UkrOS was created in the 18th of December 2022. The company is developing of operite system UkrOS.<br>The 29th of December 2022 was created 2 edition of operite system UkrOS. This is Home (H) and Professional (P).</p>
                                
                                <b><i>About operite system UkrOS:</i></b>
                                <p>Developing of operite system UkrOS was started in the 18th of December 2022. The operite system was created for nationality of Ukraine. Was created 2 edition of operite system UkrOS. This is Home (H) and Professional (P). First version of operite system UkrOS was created on the basis of operite system Debian with GNOME GUI (Thus operite system Ubuntu was created).<br></p>
                            </div>

                            <div class="about">
                                <h3 align="CENTER">UkrOS @2022-2023</h3>
                            </div>
                        </td>
                        
                        <td class="right-bar" valign=TOP>
                            <ul>
                                <li class="language"><a href="/en-us/about" class="language">English</a></li>
                                <li class="language"><a href="/de-de/about" class="language">German</a></li>
                                <li class="language"><a href="/fr-fr/about" class="language">French</a></li>
                                <li class="language"><a href="/ru-ru/about" class="language">Russian</a></li>
                                <li class="language"><a href="/uk-ua/about" class="language">Ukrainian</a></li>
                                <li class="language"><a href="/be-by/about" class="language">Belarussian</a></li>
                            </ul>
                            <img src="https://ukros2022.github.io/oswebsite/images/baners/1.png">
                            <img src="https://ukros2022.github.io/oswebsite/images/baners/2.png">
                        </td>
                    </tbody>
                </table>
            </div>
        </div>
        
        <!--
                <a href="/pl-pl/about" class="text-a">Polish</a>
                <a href="/ro-ro/about" class="text-a">Romainian</a>
                <a href="/hu-hu/about" class="text-a">Hungarian</a>
                <a href="/ko-kr/about" class="text-a">Korean</a>
                <a href="/ja-jp/about" class="text-a">Japanese</a>
                <a href="/zh-ch/about" class="text-a">Chinese (Simplified)</a>
                <a href="/zh-tw/about" class="text-a">Chinese (Traditional)</a>
                <a href="/hy-am/about" class="text-a">Armenian</a>
                <a href="/az-az/about" class="text-a">Azerbaijani</a>
                <a href="/ka-ge/about" class="text-a">Georgian</a>
                <a href="/ar-sa/about" class="text-a">Arabic</a>
                <a href="/fa-ir/about" class="text-a">Persian</a>
        -->
    </body>
</html>
"""

app.run()