# Simple Makefile for some common tasks.
.PHONY: test dist upload

clean:
	find . -name "*.pyc" |xargs rm || true
	rm -r dist || true
	rm -r build || true
	rm -r *.egg-info || true
	rm tiddlyweb.log || true
	rm lifestream.log || true
	rm -r htmlcov || true
	rm .coverage || true		

clean-bags:
	rm -r store/bags/blogs/tiddlers/* || true
	rm -r store/bags/tweets/tiddlers/* || true
	rm -r store/bags/github/tiddlers/* || true

test:
	py.test -x test

test-cov:
	py.test --cov-report term-missing --cov tiddlywebplugins test

test-cov-html:
	py.test --cov-report html --cov tiddlywebplugins test

install:
	python setup.py install

dist:
	python setup.py sdist

release: clean pypi

pypi:
	python setup.py sdist upload

deploy: heroku-stop heroku-push

heroku-stop:
	heroku ps:stop web=1

heroku-push:
	git push heroku master

heroku-open:
	heroku open
