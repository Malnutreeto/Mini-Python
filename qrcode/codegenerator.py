import qrcode

# Method 1
qr_image = qrcode.make() #insert your link in brackets
type(qr_image) 
qr_image.save("qr1.png")

# Method 2

# qr_image2 = qrcode.make() #insert your link in brackets
# qr_image2 = qrcode.QRCode(
#     version=1, 
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr_image2.add_data("some file")
# qr_image2.make(fit=True)

# img = qr_image2.make_image(fill_color=(), back_color=())
# img.save("name.ext")

