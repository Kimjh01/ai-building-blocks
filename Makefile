PYTHON ?= python
UV ?= uv

install-shared:
	$(UV) pip install -e ./shared

test:
	$(PYTHON) scripts/run_all_tests.py

clean:
	$(PYTHON) scripts/clean_cache.py

create-module:
	$(if $(NAME),,$(error NAME is required. Example: make create-module NAME=18-new-ai-module))
	$(PYTHON) scripts/create_module.py $(NAME)
