

.PHONY: default

default: TADA.tmLanguage

%.tmLanguage: %.YAML-tmLanguage
	./scripts/yaml-to-plist $< $@
