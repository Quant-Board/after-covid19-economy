docker build -t test_flask_app .
docker run -p 80:80 -t test_flask_app