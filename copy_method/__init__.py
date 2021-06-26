
def copy(c, m, chat_id: int, page_preview: bool):
    msg = await m.copy(chat_id)

    if msg.text:
        return await msg.edit(text=m.text, disable_web_page_preview=page_preview)

    else:
        return msg

