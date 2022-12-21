import random
import math 
from varname import varname 

random.seed(hash("Monolith")) 


class Mono:

	def __init__(self, data=None, _type_=None):
		self.id = varname()
		self.type = _type_
		self.data = data
		self.stck = []
		if (self.type == Variable): self.data = Variable.rand(); return
		# if (self.type == Matrix): self.data = Matrix.init(m, n)

	def new(name, d=None, t=None): n=Mono(data=d, _type_=t); n.id=name; return n
	def rand(): return Mono.new(varname(), t=Variable)
	def matrix(m, n): return Mono.new(varname(), d=Matrix.init(m, n), t=Matrix)

	def __str__(self):
		if (self.type == Variable): return f"{self.id} = {format(self.data, '.2f')}" 
		return f"{self.id} = {self.data}"

	def __repr__(self):
		if (self.type == Variable): return f"{format(self.data, '.2f')}" 
		return f"{self.id} = {self.data}"
	
	def __add__(x, y):
		out = Mono(data=(x.data + y.data))
		out.id = f"({x.id} + {y.id})"
		out.stck.append(out.id)
		return out

	def __mul__(self, other):
		out = Mono(data=(x.data * y.data))
		out.id = f"({x.id} x {y.id})"
		out.stck.append(out.id)
		return out

class Variable: 
	def rand(): return random.uniform(-1, 1)
	# def __add__(a, b): return a + b

class Matrix: 
	def init(m, n): return [*map(lambda a: [a]*n,[Mono.new("y", t=Variable)]*m)]
	def matmul(a, b): return a * b


x = Mono.matrix(3, 2)
print(x)
