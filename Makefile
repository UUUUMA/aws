RUN = python3
ENV =
SUFFIX =
EXTENTION = py
DEPLOY_TARGET = script/deploy.$(EXTENTION)

build:
	@:

deploy:
	$(RUN) $(DEPLOY_TARGET) $(ENV) $(SUFFIX)
