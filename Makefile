prepare:
	@poetry export -f requirements.txt --output requirements.txt

container:
	docker build -t vk_chat_bot .
run:
	docker run vk_chat_bot



.PHONY: install run container prepare