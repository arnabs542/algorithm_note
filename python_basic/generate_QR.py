from MyQR import myqr

version, level, qr_name = myqr.run(
words='https://baidu.com',
version = 1,
level = 'H',
picture = 'tenor.gif',
colorized = True,
contrast = 1.0,
brightness = 1.0,
save_name = 'gif_qr.gif',
)
print(version, level, qr_name)