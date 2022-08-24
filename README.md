# Robot-Control-Task-4
This project uses Python Flask microframework, Javascript, CSS,HTML and Firebase realtime database

### Prerequisite:
1-Install Python.

2-PyCharm IDE.

3-Install Flask.

4-Firebase account.

### Steps:
1-Build `home.html` page, that contains five buttons, then design it using CSS, to be shown as below:

![2022-08-24](https://user-images.githubusercontent.com/73133501/186491597-43d7bcd4-4c1c-4113-926d-bb69edeec94e.png)

this page will get the pressed button, along the date and time of pressing it and store it in Firebase database. We choosed Firebase
because it is a web platform and suitable to store data of a web page.

2-Create Firebase Project, add web application to it, then follow steps mentiond in Task-3 to link Firebase to Python:
In `main.py` we will import three libraries:
```

from flask import Flask,render_template,request
import pyrebase
from datetime import datetime

```
`pyrebase` is a simple python interface for the Firebase API, it is better than `firebase-admin` in term of easiness, BUT, be carefull that we will install `pyrebase4` which is the consistant version of this library, otherwise you will fell in endless errors.

`pyrebase4` on github here: https://github.com/nhorvath/Pyrebase4

3-In our firebase tree structre database, we will have this hairacy:

`date > 'Current date' > 'Current time' = 'Pressed btn value'`

Pressed btn value can be:  (Forward: f, Backward: b, Stop: s, Left: l,Right: r)

![Capture](https://user-images.githubusercontent.com/73133501/186492843-5f1a4edd-b5bb-4907-83c5-2445ad88b00a.PNG)


5-Create `report.html` file to display this information inside table, design it with CSS

![2022-08-24 (2)](https://user-images.githubusercontent.com/73133501/186510420-741c6e81-7c65-4c32-920d-d64cbf85e3fa.png)


