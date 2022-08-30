container:
	poetry export -f requirements.txt --output requirements.txt
	poetry run docker build -t vk_chat_bot .
run:
	poetry run docker run vk_chat_bot