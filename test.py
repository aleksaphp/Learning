from PIL import Image
from sys import argv

class Img:
	def __init__(self, data, width, height):
		self.width = width
		self.height = height
		self.data = data

	def red_to_green(self):
		self.data = [(px[1], px[0], px[2]) for px in self.data]
		
	def grayscale(self):
         self.grayscale = [(px[0]*0.2989, px[1]*0.5870, px[2]*0.1140 ) for px in self.data]

def load(path):
	with Image.open(path) as pill:
		data = list(pill.convert("RGBA").getdata()) 
		width, height = pill.size
		return Img(data, width, height)

def save(img, name):
	with Image.new("RGBA", (img.width, img.height)) as pill:
		pill.putdata(img.data)
		pill.save(name)




img = load(argv[2])
img.grayscale()
save(img, "./test1.png")




def grayscale():
    from matplotlib import pyplot as plt
    import matplotlib.image as mpimg

    img = mpimg.imread(argv[2])

    R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
    imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
    return imgGray




