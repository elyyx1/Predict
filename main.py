from config.config import *
from database.db import DB
import handlers.inline_handler
import handlers.msg_handler
import handlers.cmd_handler
from other.utils import wrapper_auto_send
async def start_bot():
    while True:
        try:
            await dp.start_polling(bot, close_bot_session=False, handle_signals=False)
        except:
            print('Error start bot')


async def tasks():
    await asyncio.gather(
        start_bot(),           # запуск бота
        wrapper_auto_send()
    )
       
if __name__ == '__main__':
    DB.run()
    asyncio.run(tasks(), debug=False)
