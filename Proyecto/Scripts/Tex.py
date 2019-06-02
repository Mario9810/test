from Scripts.Bitmap import Bitmap

class Texturas(object):
	def __init__(self, file):
		
		self.__archivo = file
		self.__content = None
		self.cargo()

	def cargo(self):
		
		self.__content = Bitmap(0, 0)
		try:
			self.__content.load(self.__filename)
		except:
			
			self.__content = None

	def PutInto(self):
		
		self.__content.write(self.__filename[:len(self.__filename)-4]+"text.bmp")

	def retrieveC(self, tx, ty, intensity=1):
		
		x = self.__content.width -1 if ty == 1 else int(ty*self.__text.width)
		y = self.__content.height -1 if tx == 1 else int(tx*self.__text.height)
		#self.__text.color(int(intensity*self.__text.framebuffer[x][y][0]),int(intensity*self.__text.framebuffer[x][y][1]), int(intensity*self.__text.framebuffer[x][y][2]))
		return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.__text.framebuffer[y][x]))

	def HasTexture(self):
		return True if self.__content else False
		
