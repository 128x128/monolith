class OP:
	def __init__(self, op, inputs, out):
		self.inputs = inputs
		self.out = out
		self.op = op

		[_.outputs.append(self) for _ in self.inputs]
		out.input = self

	def forward(self):
		match self.op:
			case "+":
				self.out.data = self.inputs[0].data + self.inputs[1].data
			case "-":
				self.out.data = self.inputs[0].data - self.inputs[1].data
			case "*":
				self.out.data = self.inputs[0].data * self.inputs[1].data
			case "/":
				self.out.data = self.inputs[0].data / self.inputs[1].data
			case "^":
				self.out.data = self.inputs[0].data ** self.inputs[1].data
			case "NEG":
				self.out.data = -self.inputs[0].data
			case "EXP":
				self.out.data = math.exp(self.inputs[0].data)
			case "ReLU":
				self.out.data = 0 if self.inputs[0].data < 0 else self.inputs[0].data
			case "SUM":
				self.out.data = 0
				for n in self.inputs:
					self.out.data += n.data 
			case "AVG":
				self.out.data = 0
				for n in self.inputs:
					self.out.data += n.data 
				self.out.data /= len(self.inputs)
			case "MAX":
				self.out.data = 0
				_max_ = -1.0
				for n in self.inputs:
					if (n.data > _max_):
						self.out.data = n.data 
						_max_ = n.data

	def backward(self):
		match self.op:
			case "+":
				self.inputs[0].grad += self.out.grad
				self.inputs[1].grad += self.out.grad
			case "-":
				self.inputs[0].grad += self.out.grad
				self.inputs[1].grad -= self.out.grad	
			case "*":
				self.inputs[0].grad += self.inputs[1].data * self.out.grad
				self.inputs[1].grad += self.inputs[0].data * self.out.grad
			case "/":
				self.inputs[0].grad += (1 / self.inputs[1].data) * self.out.grad
				self.inputs[1].grad += (self.inputs[1].data - self.inputs[0].data) / (self.inputs[0].data ** 2) * self.out.grad
			case "^":
				self.inputs[0].grad += (self.inputs[1].data * (self.inputs[0].data ** (self.inputs[1].data - 1))) * self.out.grad
			case "NEG":
				self.inputs[0].grad += -self.out.grad 
			case "EXP":
				self.inputs[0].grad += self.inputs[0].data * self.out.grad
			case "ReLU":
				self.inputs[0].grad += (self.out.data > 0) * self.out.grad 
			case "SUM":
				for n in self.inputs:
					n.grad += self.out.grad
			case "AVG":
				for n in self.inputs:
					n.grad += self.out.grad
			case "MAX":
				for n in self.inputs:
					n.grad += self.out.grad
			
				
	def zero(self):
		self.out.grad = 0
		for _ in self.inputs:
			_.grad = 0
		

	def __repr__(self):
		buffer = f"{hex(id(self))}"
		off = (len(buffer)-1) * " "
		buffer +=  f" ({self.op})"
		buffer += "\n"
		for i in self.inputs:
			buffer += off + f"\t{hex(id(i))}: {i.data:.4f}\n"
		buffer += off + f"\t-> {hex(id(self.out))}: {self.out.data:.4f}\n"
		return buffer 

