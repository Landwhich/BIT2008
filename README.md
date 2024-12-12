This is a realtime text app with (almost) full profile customization.

It is possible to upload images from the profile customization screen, though not possible to see them not sure why and would love to know.
Aside from profile customization, there is a user registry and login page. 

The main focus of the project is a real time text app using channels and websockets which displays a timestamp and user.
Open up two windows and login to two different user accounts to see how it works. 
You'll also need to start the server with daphne instead of manage.py for ws to work.

use `pip install -r requirement.txt` to download all necessary packages

launch with:
may need to alter localhost ip or ports depending on your platform
`daphne -b 127.0.0.1 -p 8000 termproject.asgi:application`


