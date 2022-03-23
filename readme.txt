Go into pythonTask Directory and open the settings.py file,
scroll down and enter email id and password in these fields
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
API -> http://localhost:8000/sendMail
API uses multipart form with two required fields (recipient email, message) and 
one optional field (subject).

This server also keeps track of all the sent emails, 
one can check this my making a superuser and redirecting to 
http://localhost:8000/admin
