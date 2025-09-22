from PIL import Image
print(dir(Image))

My_Image = Image.open(r"C:\Users\Hp\Desktop\React js\Python\Week 10/Big.jpeg")



# show image
My_Image.show()

# resize
Profile = My_Image.resize((200, 150))
Profile.show()

