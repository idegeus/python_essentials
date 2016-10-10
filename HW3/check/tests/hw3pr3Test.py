import test as t
import lib
import assertlib

@t.test(0)
def testMylen(test):
    def testMethod():
        func = lib.getFunction('mylen', _fileName)
        for (l, r) in [([], 0), ([5], 1), (['a', 'b'], 2)]:
            res = func(l)
            if not assertlib.exact(res, r):
                return False, "mylen(%r) should be %i, but got %r" % \
                    (l, r, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function mylen()" 


@t.test(1)
def testMult(test):
    def testMethod():
        func = lib.getFunction('mult', _fileName)
        for i in range(10):
            for j in range(10):
                exp = i * j
                res = func(i, j)
                if not assertlib.exact(res, exp):
                    return False, "mult(%i, %i) should be %i, but got %r" % \
                        (i, j, r, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function mult()" 

@t.test(2)
def testDot(test):
    def testMethod():
        eps = 0.00001
        func = lib.getFunction('dot', _fileName)
        for (l, k, r) in [([5, 3],[6, 4], 42.0), ([1, 2, 3, 4], [10, 100, 1000, 10000], 43210.0), ([5, 3], [6], 0.0)]:
            res = func(l, k)
            if not assertlib.between(res, r-eps, r+eps):
                return False, "dot(%r, %r) should be %f, but got %r" % \
                    (l, k, r, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function dot()" 

@t.test(3)
def testInd(test):
    def testMethod():
        func = lib.getFunction('ind', _fileName)
        for (n, l, r) in [(42, [55, 77, 42, 12, 42, 100], 2), (42, range(100),  42), ('i', 'team', 4)]:
            res = func(n, l)
            if not assertlib.exact(res, r):
                return False, "ind(%i, %r) should be %i, but got %r" % \
                    (l, r, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function ind()" 

@t.test(4)
def testLetterScore(test):
    def testMethod():
        eps = 0.00001
        func = lib.getFunction('letterScore', _fileName)
        for (letters, r) in [('aeilnorstu', 1), ('dg', 2), ('bcmp', 3), ('fhvwy', 4), ('k', 5), ('jx', 8), ('qz', 10), (' ./=+!9', 0)]:
            for l in letters:
                res = func(l)
                if not assertlib.exact(res, r):
                    return False, "letterScore(%s) should be %i, but got %r" %  (l, r, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function letterScore()" 

@t.test(5)
def testScrabbleScore(test):
    def testMethod():
        eps = 0.00001
        func = lib.getFunction('scrabbleScore', _fileName)
        for (s, r) in [('quetzal', 25), ('jonquil', 23), ('syzygy', 25)]:
            res = func(s)
            if not assertlib.exact(res, r):
                return False, "scrabbleScore(%s) should be %i, but got %r" % \
                    (s, r, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function scrabbleScore()" 

@t.test(5)
def testOneDNA(test):
    def testMethod():
        func = lib.getFunction('one_dna_to_rna', _fileName)
        for (s, r) in [('A', 'U'), ('C', 'G'), ('G', 'C'), ('T', 'A'), (' ', ''), ('.', ''), ('0', '')]:
            res = func(s)
            if not assertlib.exact(res, r):
                return False, "one_dna_to_rna(%s) should be %s, but got %r" % (s, r, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function one_dna_to_rna()" 

@t.test(6)
def testTranscribe(test):
    def testMethod():
        func = lib.getFunction('transcribe', _fileName)
        for (s, r) in [('ACGT TGCA', 'UGCAACGU'), ('GATTACA', 'CUAAUGU'), ('cs5', '')]:
            res = func(s)
            if not assertlib.exact(res, r):
                return False, "transcribe(%s) should be %s, but got %r" % \
                    (s, r, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function transcribe()" 

