CONFIG = _config.yml,_config.local.yml

.PHONY: serve draft build install clean preview

serve:
	bundle exec jekyll serve --config $(CONFIG)

# Build, then serve _site/ with a range-capable server so video (mp4) plays
# correctly. Jekyll's WEBrick mishandles HTTP Range requests and stalls/resets
# video in Chrome. Open http://localhost:4001
preview: build
	python3 scripts/preview.py

draft:
	bundle exec jekyll serve --config $(CONFIG) --drafts

build:
	bundle exec jekyll build --config $(CONFIG)

install:
	bundle install

clean:
	rm -rf _site .jekyll-cache
