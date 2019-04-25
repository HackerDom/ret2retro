import logging
from io import BytesIO
import tensorflow as tf

from nn.nn import ImageClassifier
from glitcher.main import glitch_bytes_io


graph = tf.get_default_graph()
classifier = ImageClassifier()


logger = logging.getLogger('ret2retro_bot')


def process_image(data):
    global graph
    with graph.as_default():
        score = classifier.score(data)
    buffer = BytesIO(data)
    transformed_data = glitch_bytes_io(buffer, score)
    return transformed_data, score


def start(bot, update):
    logger.info(f'User start {update.message.from_user} conversation')
    update.message.reply_text(f'Hi {update.message.from_user.first_name}, send your image and check your hackerness!')


def photo(bot, update):
    logger.info(f'Process photo from {update.message.from_user}')
    try:
        message_photo = update.message.photo[-1]
        file_object = bot.get_file(message_photo.file_id)
        file_bytearray = bytes(file_object.download_as_bytearray())
        transformed_data, score = process_image(file_bytearray)

        update.message.reply_photo(photo=BytesIO(transformed_data), caption=f'Your hackerness score: {score:.3f}')
    except Exception as e:
        logger.error(str(e))
    logger.info(f'Photo processed, score: {score:.3f}')
