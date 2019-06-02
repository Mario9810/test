import struct

class Bitmap(object):
                def __char(self, c):
                    return struct.pack("c", c.encode("ascii"))
                def ___word(self, c):
                    return struct.pack("h", c)
                def ___dword(self, c):
                    return struct.pack("l", c)
                def __init__(self, Wd, Hd):
                    self.Wd = abs(int(Wd))
                    self.Hd = abs(int(Hd))
                    self.framebuffer = []
                    self.z_buff = []
                    self.glclear()

                def SetColor(self, r=0, g=0, b=0):
                    r = r%256
                    g = g%256
                    b = b%256
                    return bytes([b, g, r])
                def glclear(self, r=0, b=0, g=0):
                    self.framebuffer = [
				[
					self.SetColor(r, b, g)     
						for x in range(self.Wd)					
				]
				for y in range(self.Hd)
			]
                    self.z_buff = [ [-float('inf') for x in range(self.Wd)] for y in range(self.Hd)]
                def point(self, x, y, color):
                    if(x < self.Wd and y < self.Hd):
                        try:
                            self.framebuffer[x][y] = color
                        except Exception as e:
                            pass
                def write(self, archivoname, z_buff=False):
                    clearcolor = self.SetColor(0,0,0)
                    import os
                    os.makedirs(os.path.dirname(archivoname), exist_ok=True)
                    archivo = open(archivoname, "bw")
                    pixelW = self.Wd
                    pixelH = self.Hd
                    
                    #header
                    archivo.write(self.__char("B"))
                    archivo.write(self.__char("M"))
                    archivo.write(struct.pack("=l",(14 + 40 + pixelW * pixelH * 3)))
                    archivo.write(self.___dword(0))
                    archivo.write(self.___dword(14 + 40))

                    archivo.write(self.___dword(40))
                    archivo.write(self.___dword(self.Wd))
                    archivo.write(self.___dword(self.Hd))
                    archivo.write(self.___word(1))
                    archivo.write(self.___word(24))
                    archivo.write(self.___dword(0))
                    archivo.write(struct.pack("=l",(pixelW * pixelH * 3)))
                    archivo.write(self.___dword(0))
                    archivo.write(self.___dword(0))
                    archivo.write(self.___dword(0))
                    archivo.write(self.___dword(0))
                    for x in range(pixelW):
                        for y in range(self.Hd):
                            if(x < self.Wd and y < self.Hd):
                                if z_buff:
                                    if self.z_buff[y][x] == -float("inf"):
                                        archivo.write(clearcolor)
                                    else:
                                        z = abs(int(self.z_buff[y][x]*255))
                                        archivo.write(self.color(z,z,z))
                                else:
                                    archivo.write(self.framebuffer[y][x])
                            else:
                                archivo.write(self.__char("c"))
                    archivo.close()
                def carga(self,archivo):
                    archivo = open(archivo, "rb")
                    archivo.seek(10)
                    headerSize = struct.unpack("=l", archivo.read(4))[0]
                    archivo.seek(18)
                    self.Wd = struct.unpack("=l", archivo.read(4))[0]
                    self.Hd = struct.unpack("=l", archivo.read(4))[0]
                    self.clear()
                    for y in range(self.Hd):
                        for x in range(self.Wd):
                            if x < self.Wd and y < self.Hd:
                                b, g, r = ord(archivo.read(1)), ord(archivo.read(1)), ord(archivo.read(1))
                                self.point(x, y, self.color(r,g,b))
                    archivo.close()
                def pad(self, algr, remain):
                    if(remain %  algr == 0):
                        return remain
                    else:
                        while (remain % algr):
                            remain += 1
                        return remain
                def collectZaxis(self, x, y):
                    if x < self.Wd and y < self.Hd:
                        return self.z_buff[x][y]
                    else:   
                        return -float("inf")
                def placeZaxis(self, x, y, z):
                    if x < self.Wd and y < self.Hd:
                        self.z_buff[x][y] = z
                        return 1
                    else:
                        return 0
    
