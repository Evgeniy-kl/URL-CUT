# URL-CUT
1) localhost:8000/api/v1/login to create access and refresh token (LOGIN)
2) localhost:8000/api/v1/registration to register user
3) localhost:8000/api/v1/short to create short url by jwt token
4) localhost:8000/api/v1/short_my_urls to get all generated user's urls 

5) localhost:8000/<generated-key>/ use to redirect to target resource


to run this application use:
docker-compose up --build
