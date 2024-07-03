install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py
lint:
	#flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker
	#docker run -p 127.0.0.1:8080:8080
deploy:
	#deploy
	aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 211125627614.dkr.ecr.eu-north-1.amazonaws.com
	docker build -t sentiment-analysis .
	docker tag sentiment-analysis:latest 211125627614.dkr.ecr.eu-north-1.amazonaws.com/sentiment-analysis:latest
	docker push 211125627614.dkr.ecr.eu-north-1.amazonaws.com/sentiment-analysis:latest
	
all: install format lint test deploy