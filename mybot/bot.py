from telegram.ext import Updater, CommandHandler

proxy = {'proxy_url': 'socks5://t3.learn.python.ru:1080', 
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print("Вызван /start")
    print(update)
    update.message.reply_text("Здравствуй, кожанный!")
    


def main():
    mybot = Updater("1613471126:AAEFTI6wEWD3Bo_fiep98K5biiDhntxoK8U", use_context = True, request_kwargs = proxy)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    mybot.idle()

main()
