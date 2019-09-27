class televisi(object):
	def __init__(self, t, a, p):
		self.type = t
		self.asal = a
		self.price = p

	def cetakData (self):
			print("type\t: ", self.type)
			print("asal\t: ", self.asal)
			print("price\t: ", self.price)

# mendefenisian kelas turunan(subclass)
class size (televisi):
	def __init__ (self, t, a, p, s):
		self.type = t
		self.asal = a
		self.price = p
		self.size = s 
	def cetakData (self):
		print("type\t: ", self.type)
		print("asal\t: ", self.asal)
		print("price\t: ", self.price)
		print("size\t: ", self.size)

def main ():

	size1 = size("LED", "china", "Rp.100.000.000", "5inci")

	size1.cetakData ()

if __name__ == "__main__":
	main()
	