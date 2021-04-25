#
# Makefile

defaut: help

install: unityyamlnormalize/*.py ## install self
	python setup.py install

install-test-deps: ## install test dependencies
	pip install -e.[test]

test: install ## commands test
	unity-yaml-normalize sample/SampleScene.unity -o tmp/SampleScene.unity

one:
	python -c "import sys; from unityparser import UnityDocument; doc = UnityDocument.load_yaml(sys.argv[1]); [(d := dict(sorted(x.__dict__.items())), x.__dict__.clear(), x.__dict__.update(d)) for x in doc.entries]; doc.dump_yaml(sys.argv[2]);" sample/SampleScene.unity tmp/SampleScene.unity

pytest: ## python test
	python setup.py test

tox: install-test-deps
	tox .

flake8: install-test-deps
	tox -e flake8 .

help: ## Display this help screen
	@grep -E '^[a-zA-Z][a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sed -e 's/^GNUmakefile://' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

docker:
	docker run -it --rm -v ${PWD}:/work -w /work python:3.8-alpine sh
	# apk add make
