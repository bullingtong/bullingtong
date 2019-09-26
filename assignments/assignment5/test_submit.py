import pytest
from submitAssign import Submission, WrongFiletype
from login import Login, FailLogin
from checkGrading import GradeCheck, FailGradeCheck
from comments import Comments, FailComments
from averages import Averages, FailAverages

def test_login():
	username = "Ricky"
	password = "Bobby"
	print("\nChecking %s and %s", username, password)
	assert (username == Login.userName) & (password == Login.password)

def test_fail_login():
	username = "Dick"
	password = "Cheney"
	print("\nChecking %s and %s", username, password)
	assert (username == Login.userName) & (password == Login.password)


def test_fileType():
	fileType=".png"
	with pytest.raises(WrongFiletype):
		Submission.acceptedFiletype(fileType)

def test_fail_fileType():
	fileType=".pdf"
	with pytest.raises(WrongFiletype):
		Submission.failFiletype(fileType)


def test_grading():
	print("\ntesting grade check function")
	assert GradeCheck.checkGradin(70) == 1

def test_fail_grading():
	print("\ntesting grade check function")
	assert GradeCheck.checkGradin(-20) == 1

def test_comments():
	print("\nTesting submission comments")
	assert Comments.commentFunction() != ""

def test_fail_comments():
	print("\nTesting submission comments")
	assert FailComments.commentFailFunction() != ""

def test_averages():
	print("\nTesting averages function")
	assert pytest.approx(83.4, .14) == Averages.getAverage()

def test_fail_averages():
	print("\nTesting averages function")
	assert pytest.approx(83.4) == FailAverages.getFailAverage()




		