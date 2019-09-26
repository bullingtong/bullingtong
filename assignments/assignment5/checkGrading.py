class GradeCheck():
	def checkGradin(grade):
		if grade < 0 or grade > 100:
			print("\nGrade out of standard grade range")
			return 0
		else:
			return 1
			check = checkGradin(70)
			print(check)


class FailGradeCheck():
	def checkFailGradin(grade):
		if grade < 0 or grade > 100:
			print("\nGrade out of standard grade range")
			return 0
		else:
			return 1
			check = checkFailGradin(-70)
			print(check)
