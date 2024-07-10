
# OpenCV Telegram Bot

This is a Telegram bot that processes images using OpenCV. It can perform various operations like converting to black and white, applying blur, detecting edges, and more.

## Features

- **/start**: Start the bot and receive a welcome message.
- **/help**: Display help message with available commands.
- **/blackwhite**: Convert the received image to black and white.
- **/blur**: Apply Gaussian blur to the received image.
- **/edge**: Detect edges in the received image using Canny edge detection.
- **/contour**: Detect contours in the received image.
- **/erosion**: Apply erosion to the received image.
- **/dilation**: Apply dilation to the received image.
- **/histogram**: Equalize the histogram of the received image.
- **/sampling**: Sample the received image (reduce resolution).

## Requirements

- Python 3.x
- Telegram Bot API token (you can get this by creating a bot on Telegram using BotFather)
- OpenCV
- Python Telegram Bot library
- dotenv for managing environment variables

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Asazin007/opencv_telegram_bot.git
    cd opencv-telegram-bot
    ```

2. Install the required packages:

    ```sh
    pip install python-telegram-bot python-dotenv opencv-python-headless numpy
    ```

3. Create a `.env` file in the root directory of the project and add your Telegram Bot API token:

    ```sh
    echo "TOKEN=your-telegram-bot-token" > .env
    ```

4. Run the bot:

    ```sh
    python bot.py
    ```

## Usage

1. Start a chat with your bot on Telegram.
2. Use the `/start` command to initiate the conversation.
3. Send an image to the bot.
4. Use any of the available commands to process the image:

    - `/blackwhite`
    - `/blur`
    - `/edge`
    - `/contour`
    - `/erosion`
    - `/dilation`
    - `/histogram`
    - `/sampling`

## Contributing

Feel free to submit issues, fork the repository and send pull requests!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
