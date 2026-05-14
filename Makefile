.PHONY: start check

start:
	python3 scripts/start_day.py

check:
	python3 -m py_compile scripts/start_day.py
