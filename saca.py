class SA_IS:
	def __init__(self, S):
		# Define values for S, L and LMS type characters.
		self.S_type = ord('S')
		self.L_type = ord('L')
		self.LMS_type = ord('*')

		# Store given data for SA_IS object.
		self.S = S

		# Construct other info needed for SA-IS algorithm
		self.t = self.build_t()

	'''
		Build T as described in Linear Suffix Array Construction by Almost Pure Induced Sorting
		S is our original string.
	'''
	def build_t(self):
		# Create and initialize array to store t
		s_len = len(self.S)
		t = bytearray(s_len + 1)
		t[-1] = self.S_type # Empty suffix is S type by definition

		if s_len != 0:
			t[-2] = self.L_type # Last character is L type by definition
		
			# Iterate in reverse order through our string marking each character as S or L type.
			for i in range(s_len-2, -1, -1):
				if self.S[i] >= self.S[i+1]:
					t[i] = self.L_type
				else:
					t[i] = self.S_type
		return t

	def is_LMS_char(self, pos):
		# default to not an LMS character
		is_LMS = False

		if pos != 0 and self.t[pos] == self.S_type and self.t[pos - 1] == self.L_type:
			is_LMS = True
		return is_LMS

	# Getter functions for external users. 
	def get_t(self):
		return (self.t).decode('ascii')

	def get_s(self):
		return self.S

	def get_lms(self):
		lms_arr = []
		for i in range(0, len(self.type)):
			is_LMS = is_LMS_char(i)
			if is_LMS:
				lms_arr.append(is_LMS_char)

my_saca = SA_IS('mississippi')
print(my_saca.get_s())
print(my_saca.get_t())