import random
import math 

random.seed(1337) 

ALL = []

class Node:

	def __init__(self, id=None, data=None, type=None):
		self.id = id 
		self.data = data
		self.type = type
		ALL.append(self)

	def setid(self, id): self.id = id
	def rand(id=None): return Node(id=id, data=random.uniform(-1, 1), type=Variable)
	def Tensor(*shape): return Node(id="Tensor", data=[Node.rand(id=str(_)) for _ in range(math.prod(shape))], type=Tensor(shape))

	def __str__(self):
		if (self.type == Variable): return f"{self.id} = {format(self.data, '.4f')}" 
		if isinstance(self.type, Tensor): return f"he" 
		return f"{self.id}: {self.data}"

	def __repr__(self):
		if (self.type == Variable): return f"{format(self.data, '.4f')}" 
		if isinstance(self.type, Tensor): return f"he" 
		return f"{self.id} = {self.data}"
	
	# def __add__(x, y):
		# out = Mono(data=(x.data + y.data))
		# out.id = f"({x.id} + {y.id})"
		# out.stck.append(out.id)
		# return out

	# def __mul__(self, other):
		# out = Mono(data=(x.data * y.data))
		# out.id = f"({x.id} x {y.id})"
		# out.stck.append(out.id)
		# return out

class Variable: 
	def rand(): return random.uniform(-1, 1)
	# def __add__(a, b): return a + b

class Tensor: 
	def __init__(self, *shape):
		 self.shape = shape
		
	# def init(*shape): return [Mono.new(str(shape), s=shape, t=Tensor)]*m]
	def matmul(a, b): return a * b

	def zeros(*s): return Mono.new(shape=s, t=Tensor)
	def ones(*s): return Mono.new(shape=s)
	def randn(*s): return Mono.new(shape=s)


x = Node.Tensor(3, 1)
print(x)
