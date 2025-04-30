default: help

help:
	@echo Developer commands:
	@echo
	@echo " run				Run narrata server"

run:
	fastapi dev server/app/server.py