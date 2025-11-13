from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = Image.open(file_path)
myHeight , myWidth = img.size

#img = img.resize((myHeight , myWidth), Image.LANCZOS) 
#img = img.resize((myHeight , myWidth), Image.BICUBIC) 
#img = img.resize((myHeight , myWidth), Image.BILINEAR) 

img = img.resize((myHeight , myWidth), Image.NEAREST) 

#Image.BILINEAR → کمی نرم‌تر
#Image.BICUBIC → کیفیت خوب‌تر #
#Image.NEAREST → ساده‌ترین، کیفیت پایین‌تر 

save_path = asksaveasfilename()
img.save(save_path+"_compressed.JPG")