from PIL import Image, ImageOps, ImageDraw, ImageFont
from bot.config import PICS_DIRECTORY, QUOTATION_DATABASE

import textwrap
import sqlite3
import random
import os
import io


def get_random_quote():
    conn = sqlite3.connect(QUOTATION_DATABASE)
    cursor = conn.cursor()

    count = cursor.execute('SELECT COUNT(*) FROM quotes;').fetchone()[0]
    random_id = random.randint(1, count)

    return cursor.execute('SELECT author, quote FROM quotes WHERE id = ?', (random_id, )).fetchone()[1]


def create_quote_photo():
    img_quote = Image.new(mode="RGB", size=(850, 400))
    img_quote = ImageOps.expand(img_quote, border=2, fill='white')
    img_komaru = Image.open(os.path.join(PICS_DIRECTORY, random.choice(os.listdir(PICS_DIRECTORY))))
    img_komaru = img_komaru.resize((int(img_komaru.size[0] * (350 / img_komaru.size[1])), 350))
    img_quote.paste(img_komaru, (25, 25))

    quote = get_random_quote()

    font1 = ImageFont.truetype('times.ttf', size=20)
    font2 = ImageFont.truetype('times.ttf', size=24)
    draw_text = ImageDraw.Draw(img_quote)

    margin = 420
    offset = 25

    for line in textwrap.wrap(quote, width=45):
        draw_text.text((margin, offset), line, font=font1, fill="white")
        offset += font1.getsize(line)[1]

    author = '- Комару -'
    draw_text.text((790 - font2.getsize(author)[0], 310), author, font=font2, fill="white")

    byte_arr = io.BytesIO()
    img_quote.save(byte_arr, format='PNG')
    byte_arr.seek(0)

    return byte_arr
