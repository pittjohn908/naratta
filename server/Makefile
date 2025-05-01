default: help

help:
	@echo Developer commands:
	@echo
	@echo " run				Run narrata server"
	@echo " add-migration	Add migration file"
	

run:
	fastapi dev app/server.py

add-migration:
	alembic revision -m "$(MSG)"