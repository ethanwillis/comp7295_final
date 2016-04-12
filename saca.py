class SA_IS:
	def __init__(self, S):
		# Define values for S and L types.
		self.S_type = ord('S')
		self.L_type = ord('L')
		self.S = S
		self.t = self.build_t(S)
		print(S)
		print(self.t.decode('ascii'))

	'''
		Build T as described in Linear Suffix Array Construction by Almost Pure Induced Sorting
		S is our original string.
	'''
	def build_t(self, S):
		# Create and initialize array to store t
		s_len = len(S)
		t = bytearray(s_len + 1)
		t[-1] = self.S_type # Empty suffix is S type by definition

		if s_len != 0:
			t[-2] = self.L_type # Last character is L type by definition
		
			# Iterate in reverse order through our string marking each character as S or L type.
			for i in range(s_len-2, -1, -1):
				if S[i] >= S[i+1]:
					t[i] = self.L_type
				else:
					t[i] = self.S_type
		return t

	def get_t(self):
		return self.t

my_saca = SA_IS('mississippi')