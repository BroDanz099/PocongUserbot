# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests
import random
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, edit_delete, poci_cmd
from telethon.tl.types import InputMessagesFilterVideo


@poci_cmd(pattern="asupan$")
async def _(event):
    xx = await edit_or_reply(event, "`Bentar.... cari video asupannya dlu`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Asupan_Pocong", filter=InputMessagesFilterVideo
            )
        ]
        sy = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"nih asupan buat  [{owner}](tg://user?id={sy.id}) biar ga lemess 🥵",
        )
        await xx.delete()
    except Exception:
        await xx.edit("Tidak bisa menemukan video asupan.")


@poci_cmd(pattern="wibu$")
async def _(event):
    xx = await edit_or_reply(event, "`Prosses.... ya wibuu`")
    try:
        wibukntl = [
            wibu
            async for wibu in event.client.iter_messages(
                "@pocongwibu", filter=InputMessagesFilterVideo
            )
        ]
        mmq = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(wibukntl),
            caption=f"nih buat lo [{owner}](tg://user?id={mmq.id}) vvibu bau bawang",
        )
        await xx.delete()
    except Exception:
        await xx.edit("Tidak bisa menemukan video anime.")


@poci_cmd(pattern="chika$")
async def _(event):
    xx = await edit_or_reply(event, "`Prosess....`")
    try:
        response = requests.get("https://api-alphabot.herokuapp.com/api/asupan/chika?apikey=Alphabot").json()
        await event.client.send_file(event.chat_id, response["url"])
        await xx.delete()
    except Exception:
        await xx.edit("**Maaf 🥺 , untuk cmd ini belum dapat digunakan untuk saat ini.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}chika`\
        \n  •  **Function : **Untuk Mengirim video chikakiku secara random.\
    "
    }
)

CMD_HELP.update(
    {
        "wibu": f"**Plugin : **`Wibu`\
        \n\n  •  **Syntax :** `{cmd}wibu`\
        \n  •  **Function : **Mengirim secara random video anime\
    "
    }
)