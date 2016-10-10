import test as t
import lib
import assertlib

@t.test(0)
def answer0(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[0], "[2, 5, 9]")
	test.description = lambda : "correct output for answer0"

@t.test(1)
def answer1(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[1], "[7, 1]")
	test.description = lambda : "correct output for answer1"

@t.test(2)
def answer2(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[2], "[9, 1, 1]")
	test.description = lambda : "correct output for answer2"

@t.test(3)
def answer3(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[3], "[1, 4, 1, 5, 9]")
	test.description = lambda : "correct output for answer3"

@t.test(4)
def answer4(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[4], "[1, 2, 3, 4, 5]")
	test.description = lambda : "correct output for answer4"

@t.test(5)
def answer5(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[5], "heyyou")
	test.description = lambda : "correct output for answer5"

@t.test(6)
def answer6(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[6], "collude")
	test.description = lambda : "correct output for answer6"

@t.test(7)
def answer7(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[7], "arveyudd")
	test.description = lambda : "correct output for answer7"

@t.test(8)
def answer8(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[8], "hardeharharhar")
	test.description = lambda : "correct output for answer8"

@t.test(9)
def answer9(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[9], "legomyego")
	test.description = lambda : "correct output for answer9"

@t.test(10)
def answer10(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[10], "clearcall")
	test.description = lambda : "correct output for answer10"
