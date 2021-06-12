import telegram

my_token = "1721016649:AAEbB2fOcmeqzZOG5pwuLSzUClWt83WP22c"

# Tạo bot
bot = telegram.Bot(token=my_token)


# Gửi thử text message
# bot.sendMessage(chat_id = "1246123900", text="Gưi từ PyCharm")
bot.sendPhoto(chat_id="1246123900", photo = open("b.jpeg","rb"), caption = "Có súng, nguy hiêm!")
