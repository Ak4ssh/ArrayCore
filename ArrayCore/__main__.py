import asyncio

from pyrogram import idle

from . import (Venom1, Venom2, Venom3, Venom4,
               Venom5, Venom6, Venom7, Venom8,
               Venom9, Venom10, Venom11, Venom12,
               Venom13, Venom14, Venom15, vcbot)
from . import (call_py1, call_py2, call_py3, call_py4,
               call_py5, call_py6, call_py7, call_py8,
               call_py9, call_py10, call_py11, call_py12,
               call_py13, call_py14, call_py15)


async def startup():
    # STARTING CLIENTS
    if Venom1:
        try:
            await Venom1.start()
        except Exception as e:
            print(str(e))

    if Venom2:
        try:
            await Venom2.start()
        except Exception as e:
            print(str(e))

    if Venom3:
        try:
            await Venom3.start()
        except Exception as e:
            print(str(e))

    if Venom4:
        try:
            await Venom4.start()
        except Exception as e:
            print(str(e))

    if Venom5:
        try:
            await Venom5.start()
        except Exception as e:
            print(str(e))

    if Venom6:
        try:
            await Venom6.start()
        except Exception as e:
            print(str(e))

    if Venom7:
        try:
            await Venom7.start()
        except Exception as e:
            print(str(e))

    if Venom8:
        try:
            await Venom8.start()
        except Exception as e:
            print(str(e))

    if Venom9:
        try:
            await Venom9.start()
        except Exception as e:
            print(str(e))

    if Venom10:
        try:
            await Venom10.start()
        except Exception as e:
            print(str(e))

    if Venom11:
        try:
            await Venom11.start()
        except Exception as e:
            print(str(e))

    if Venom12:
        try:
            await Venom12.start()
        except Exception as e:
            print(str(e))

    if Venom13:
        try:
            await Venom13.start()
        except Exception as e:
            print(str(e))

    if Venom14:
        try:
            await Venom14.start()
        except Exception as e:
            print(str(e))

    if Venom15:
        try:
            await Venom15.start()
        except Exception as e:
            print(str(e))

    # STARTING BOT CLIENT
    await vcbot.start()

    # STARTING ASSISTANTS
    if call_py1:
        await call_py1.start()
    if call_py2:
        await call_py2.start()
    if call_py3:
        await call_py3.start()
    if call_py4:
        await call_py4.start()
    if call_py5:
        await call_py5.start()
    if call_py6:
        await call_py6.start()
    if call_py7:
        await call_py7.start()
    if call_py8:
        await call_py8.start()
    if call_py9:
        await call_py9.start()
    if call_py10:
        await call_py10.start()
    if call_py11:
        await call_py11.start()
    if call_py12:
        await call_py12.start()
    if call_py13:
        await call_py13.start()
    if call_py14:
        await call_py14.start()
    if call_py15:
        await call_py15.start()
    
    # STARTUP COMPLETED
    await idle()


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(startup())
