import qrcode
async def generate_qr(lnk='https://t.me/stackers_7_bot'):
    img = await qrcode.make(lnk)
    await img.save('путь')