#python imports
import qrcode
from qrcode.image.pure import PymagingImage

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
    "https://i.imgur.com/AR6T5fT.jpg",
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
    "https://www.youtube.com/watch?v=bHOVZ_Tb3ik" 

    ] 


if __name__ == "__main__" :
    i = 0
    for url in urls :
        img = qrcode.make(url, image_factory=PymagingImage)
        with open("qr.{}.png".format(i), "wb") as f:
            img.save(f)
        f.close()
        i = i + 1