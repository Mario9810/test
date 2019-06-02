class loadOBJ(object):


	def __init__(self, Archivo):
		
		self.__Axiss = []
		self.__Surface = []
		self.__NormalA = []
		self.__Archivo = Archivo
		self.__materials = None
		self.__materialSurface = []
		self.__TextureV = []

	def cargo(self):
	
		file = open(self.__Archivo, "r")
		import os
		Surface = []
		currentMat, previousMat = "default", "default"
		faceCounter = 0
		matIndex = []
		lines = file.readlines()
		last = lines[-1]
		for line in lines:
			line = line.rstrip().split(" ")
			if line[0] == "mtllib":
				mtlFile = matterial(os.path.dirname(file.name) + "/" + line[1])
				if mtlFile.ItsOn():
					mtlFile.cargo()
					#self.__Surface = {}
					self.__materials = mtlFile.materials
				else:
					self.__Surface = []
			elif line[0] == "usemtl":
				if self.__materials:
					matIndex.append(faceCounter)
					previousMat = currentMat
					currentMat = line[1]
					if len(matIndex) == 2:
						self.__materialSurface.append((matIndex, previousMat))
						matIndex= [matIndex[1]+1]
			elif line[0] == "v":
				line.pop(0)
				i = 1 if line[0] == "" else 0
				self.__Axiss.append((float(line[i]), float(line[i+1]), float(line[i+2])))
			elif line[0] == "vn":
				line.pop(0)
				i = 1 if line[0] == "" else 0
				self.__NormalA.append((float(line[i]), float(line[i+1]), float(line[i+2])))
			elif line[0] == "f":
				line.pop(0)
				face = []
				for i in line:
					i = i.split("/")
					if i[1] == "":
						face.append((int(i[0]), int(i[-1])))
					else:
						face.append((int(i[0]), int(i[-1]), int(i[1])))
				self.__Surface.append(face)
				faceCounter += 1
				face = []
			elif line[0] == "vt":
				line.pop(0)
				self.__TextureV.append((float(line[0]), float(line[1])))
		if len(matIndex) < 2 and self.__materials:
			matIndex.append(faceCounter)
			self.__materialSurface.append((matIndex, currentMat))
			matIndex= [matIndex[1]+1]
		file.close()
		

	def Matts(self):		
		return self.__materials

	def facces(self):
	
		return self.__Surface

	def Verticess(self):
	
		return self.__Axiss

	def Normalist(self):
	
		return self.__NormalA
	def MTLF(self):
		return self.__materialSurface

	def XYTex(self):
		return self.__TextureV

class matterial(object):


	def __init__(self, Archivo):
		self.__Archivo = Archivo
		self.__file = None
		self.materials = {}
		self.dotMTL()

	def dotMTL(self):
	
		try:
			self.__file = open(self.__Archivo, "r")
			self.__mtlFile = True
		except:
			self.__mtlFile = False

	def ItsOn(self):
	
		return self.__mtlFile

	def cargo(self):
		if self.ItsOn():
			currentMat = None
			ac, dc, sc, ec, t, s, i, o = 0, 0, 0, 0, 0, 0, 0, 0
			for line in self.__file.readlines():
				line = line.strip().split(" ")
				if line[0] == "newmtl":
					currentMat = line[1].rstrip()
				elif line[0] == "Ka":
					ac = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "Kd":
					dc = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "Ks":
					sc = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "Ke":
					ec = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "d" or line[0] == "Tr":
					t = (float(line[1]), line[0])
				elif line[0] == "Ns":
					s = float(line[1])
				elif line[0] == "illum":
					i  = int(line[1])
				elif line[0] == "Ni":
					o = float(line[1])
				elif currentMat:
					self.materials[currentMat] = MTLS(currentMat, ac, dc, sc, ec, t, s, i, o)	
			if currentMat not in self.materials.keys():
				self.materials[currentMat] = MTLS(currentMat, ac, dc, sc, ec, t, s, i, o)	

class MTLS(object):

	def __init__(self, name, ac, dc, sc, ec, t, s, i, o):
		
		self.name = name.rstrip()
		self.ambientColor = ac
		self.difuseColor = dc
		self.specularColor = sc
		self.emissiveCoeficient = ec
		self.transparency = t
		self.shininess = s
		self.illumination = i
		self.opticalDensity = o		
