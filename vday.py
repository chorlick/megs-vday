#python imports
import qrcode
from qrcode.image.pure import PymagingImage
import os
import PIL
from fpdf import FPDF
from wand.image import Image as wand_image_Image

#urls
urls = [
    "https://i.imgur.com/33eyKQe.jpg",
    "https://i.imgur.com/sBmBIu7.jpg",
    "https://i.imgur.com/2KKdnQE.jpg",
    "https://i.imgur.com/3sBQurp.jpg",
    "https://i.imgur.com/PQPVP5O.jpg",
    "https://i.imgur.com/irwqjbh.jpg", 
    "https://i.imgur.com/nnNfxfE.jpg", 
    "https://i.imgur.com/4riwdcR.jpg", 
    "https://i.imgur.com/VJy0REB.png",
    "https://i.imgur.com/Lct5PKm.jpg",
    "https://i.imgur.com/ULCYWww.jpg",
    "https://github.com/chorlick/megs-vday",
    "https://i.imgur.com/UpX04aG.jpg",
    "https://i.imgur.com/j2H6nia.png",
    "https://i.imgur.com/J4FTRzL.jpg",
    "https://i.imgur.com/wunRUOH.jpg",
    "https://i.imgur.com/Uw0wEve.jpg",
    "https://i.imgur.com/yyRI3jp.jpg",
    "https://i.imgur.com/hZ5S273.jpg",
    "https://i.imgur.com/yRdvMcG.jpg",
    "https://i.imgur.com/k15CdIa.jpg",
    "https://i.imgur.com/zh5tlrY.png",
    "https://www.youtube.com/watch?v=fHI8X4OXluQ" 
    "https://www.youtube.com/watch?v=wg4hV0ziH-g" , 
    "https://www.youtube.com/watch?v=bHOVZ_Tb3ik",
    "https://www.youtube.com/watch?v=ImAlx0amAIc"
    ] 

def create_qr_codes(img_dir):
    i = 0
    if not os.path.exists(img_dir) :
        print("Error : Image folder does not exist")
        return False

    try :
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10, border=4)
        for url in urls :
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="pink", back_color="white")
            file = "IMG{0:03d}.png".format(i)
            path = "{}/{}".format(img_dir, file)
            print(path)
            with open(path, "wb") as f:
                img.save(f)
            f.close()
            i = i + 1
            qr.clear()
        return True
    except Exception as e:
        print("Error in qr image creation: {}".format(e))

def render_pdf(img_dir, output_file):
    files = os.listdir(img_dir)
    print("Processing {} files".format(len(files)))
    pdf = FPDF()
    sdir = "{}/".format(img_dir)
    w,h = 0,0
    for i in range(0,len(files)):
        fname = sdir + "IMG%.3d.png" % i
        if os.path.exists(fname):
            if i == 1:
                cover = PIL.Image.open(fname)
                w,h = cover.size
                pdf = FPDF(unit = "pt", format = [w,h])
            image = fname
            pdf.add_page()
            pdf.image(image,0,0,w,h)
        else:
            print("File not found:", fname)
        print("processed %d" % i)
    pdf.output("{}.pdf".format(output_file), "F")
    print("done")

def render_png(img_dir, output_file) :
    new_image = wand_image_Image(width=600, height=600)
    k = 0
    for i in range(0,5) :
        for j in range(0,5) :
            file = "IMG{0:03d}.png".format(k)
            path = "{}/{}".format(img_dir, file)
            img = wand_image_Image(filename=path)
            new_image.composite(image=img, left=i * 60 + (50 *i) , top=j * 60 + (50*j))
            k = k + 1
    new_image.save(filename=output_file)


def scale_images(img_dir) : 
    files = os.listdir(img_dir)
    for i in range(0,len(files)):
        file = "IMG{0:03d}.png".format(i)
        path = "{}/{}".format(img_dir, file)
        img = PIL.Image.open(path)
        img = img.resize((100,100), PIL.Image.ANTIALIAS)
        img.save(path)

if __name__ == "__main__" :
    if not create_qr_codes("imgs"):
        print("Error processing files. I dunno check the output")
        exit(-1)
    scale_images("imgs")
    render_png  ("imgs", "Vday.png")