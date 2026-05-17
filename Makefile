CONFIG = _config.yml,_config.local.yml

.PHONY: serve draft build install clean

serve:
	bundle exec jekyll serve --config $(CONFIG)

draft:
	bundle exec jekyll serve --config $(CONFIG) --drafts

build:
	bundle exec jekyll build --config $(CONFIG)

install:
	bundle install

clean:
	rm -rf _site .jekyll-cache
