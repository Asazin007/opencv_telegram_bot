import telegram.ext
from dotenv import load_dotenv
import os
import cv2
import numpy as np
import logging

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hello! Welcome to opencv_bot')

def help(update, context):
    update.message.reply_text("""
    Send an image and choose an option:
    /blackwhite - Convert to black and white
    /blur - Apply blur
    /edge - Detect edges
    /contour - Detect contours
    /erosion - Apply erosion
    /dilation - Apply dilation
    /histogram - Equalize histogram
    /sampling - Sample image (reduce resolution)
    """)

def handle_image(update, context):
    try:
        file = update.message.photo[-1].get_file()
        file_path = 'input_image.jpg'
        file.download(file_path)
        logger.info("Image downloaded successfully")

        # Load image using OpenCV
        image = cv2.imread(file_path)
        context.user_data['image'] = image
        update.message.reply_text('Image received! Choose an option using the commands.')
    except Exception as e:
        logger.error("Error handling image: %s", e)
        update.message.reply_text('Failed to process image.')

def convert_black_white(update, context):
    try:
        image = context.user_data.get('image')
        if image is not None:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            output_path = 'output_image.jpg'
            cv2.imwrite(output_path, gray_image)
            update.message.reply_photo(photo=open(output_path, 'rb'))
            logger.info("Black and white image sent")
        else:
            update.message.reply_text('No image found. Please send an image first.')
    except Exception as e:
        logger.error("Error converting image to black and white: %s", e)
        update.message.reply_text('Failed to convert image to black and white.')

def apply_blur(update, context):
    try:
        image = context.user_data.get('image')
        if image is not None:
            blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
            output_path = 'output_image.jpg'
            cv2.imwrite(output_path, blurred_image)
            update.message.reply_photo(photo=open(output_path, 'rb'))
            logger.info("Blurred image sent")
        else:
            update.message.reply_text('No image found. Please send an image first.')
    except Exception as e:
        logger.error("Error applying blur: %s", e)
        update.message.reply_text('Failed to apply blur.')

def detect_edges(update, context):
    try:
        image = context.user_data.get('image')
        if image is not None:
            edges = cv2.Canny(image, 100, 200)
            output_path = 'output_image.jpg'
            cv2.imwrite(output_path, edges)
            update.message.reply_photo(photo=open(output_path, 'rb'))
            logger.info("Edge-detected image sent")
        else:
            update.message.reply_text('No image found. Please send an image first.')
    except Exception as e:
        logger.error("Error detecting edges: %s", e)
        update.message.reply_text('Failed to detect edges.')

def detect_contours(update, context):
    try:
        image = context.user_data.get('image')
        if image is not None:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray_image, 127, 255, 0)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
            output_path = 'output_image.jpg'
            cv2.imwrite(output_path, image)
            update.message.reply_photo(photo=open(output_path, 'rb'))
            logger.info("Contours-detected image sent")
        else:
            update.message.reply_text('No image found. Please send an image first.')
    except Exception as e:
        logger.error("Error detecting contours: %s", e)
        update.message.reply_text('Failed to detect contours.')

def apply_erosion(update, context):
    try:
        image = context.user_data.get('image')
        if image is not None:
            kernel = np.ones((5, 5), np.uint8)
            erosion = cv2.erode(image, kernel, iterations=1)
            output_path = 'output_image.jpg'
            cv2.imwrite(output_path, erosion)
            update.message.reply_photo(photo=open(output_path, 'rb'))
            logger.info("Eroded image sent")
        else:
            update.message.reply_text('No image found. Please send an image first.')
    except Exception as e:
        logger.error("Error applying erosion: %s", e)
        update.message.reply_text('Failed to apply erosion.')

def apply_dilation(update, context):
    try:
        image = context.user_data.get('image')
        if image is not None:
            kernel = np.ones((5, 5), np.uint8)
            dilation = cv2.dilate(image, kernel, iterations=1)
            output_path = 'output_image.jpg'
            cv2.imwrite(output_path, dilation)
            update.message.reply_photo(photo=open(output_path, 'rb'))
            logger.info("Dilated image sent")
        else:
            update.message.reply_text('No image found. Please send an image first.')
    except Exception as e:
        logger.error("Error applying dilation: %s", e)
        update.message.reply_text('Failed to apply dilation.')

def equalize_histogram(update, context):
    try:
        image = context.user_data.get('image')
        if image is not None:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            equalized_image = cv2.equalizeHist(gray_image)
            output_path = 'output_image.jpg'
            cv2.imwrite(output_path, equalized_image)
            update.message.reply_photo(photo=open(output_path, 'rb'))
            logger.info("Histogram-equalized image sent")
        else:
            update.message.reply_text('No image found. Please send an image first.')
    except Exception as e:
        logger.error("Error equalizing histogram: %s", e)
        update.message.reply_text('Failed to equalize histogram.')

def sample_image(update, context):
    try:
        image = context.user_data.get('image')
        if image is not None:
            width, height = int(image.shape[1] / 2), int(image.shape[0] / 2)
            sampled_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
            output_path = 'output_image.jpg'
            cv2.imwrite(output_path, sampled_image)
            update.message.reply_photo(photo=open(output_path, 'rb'))
            logger.info("Sampled image sent")
        else:
            update.message.reply_text('No image found. Please send an image first.')
    except Exception as e:
        logger.error("Error sampling image: %s", e)
        update.message.reply_text('Failed to sample image.')

updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.photo, handle_image))
dispatcher.add_handler(telegram.ext.CommandHandler('blackwhite', convert_black_white))
dispatcher.add_handler(telegram.ext.CommandHandler('blur', apply_blur))
dispatcher.add_handler(telegram.ext.CommandHandler('edge', detect_edges))
dispatcher.add_handler(telegram.ext.CommandHandler('contour', detect_contours))
dispatcher.add_handler(telegram.ext.CommandHandler('erosion', apply_erosion))
dispatcher.add_handler(telegram.ext.CommandHandler('dilation', apply_dilation))
dispatcher.add_handler(telegram.ext.CommandHandler('histogram', equalize_histogram))
dispatcher.add_handler(telegram.ext.CommandHandler('sampling', sample_image))

updater.start_polling()
updater.idle()
