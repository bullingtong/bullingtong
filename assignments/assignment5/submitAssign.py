
class WrongFiletype(Exception):
	pass



class Submission:
	

	def acceptedFiletype(fileType):
		filetype=".pdf"
		if (fileType != ".pdf"):
			raise WrongFiletype("Incorrect filetype was submitted")

	def failFiletype(fileType):
		filetype=".doc"
		if (fileType != ".pdf"):
			raise WrongFiletype("Incorrect filetype was submitted")


