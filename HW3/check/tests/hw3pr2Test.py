import test as t
import lib
import assertlib

@t.test(0)
def testDbl(test):
    def testMethod():
        func = lib.getFunction('dbl', _fileName)
        for i in range(1, 10):
            res = func(i)
            exp = i * 2
            if not assertlib.exact(res, exp):
                return False, "%i doubled should be %i, but got %i" % (i, exp, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function dbl()" 

@t.test(1)
def testSq(test):
    def testMethod():
        func = lib.getFunction('sq', _fileName)
        for i in range(1, 10):
            res = func(i)
            exp = i ** 2
            if not assertlib.exact(res, exp):
                return False, "%i squared should be %i, but got %i" % (i, exp, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function sq()" 

@t.test(2)
def testInterp(test):
    def testMethod():
        func = lib.getFunction('interp', _fileName)
        e = 0.00001
        for (h, l, f, r) in [(1.0, 9.0, 0.25, 3.0), (1.0, 3.0, 0.25, 1.5),
            (2, 12, 0.22, 4.2)]:
            res = func(h, l, f)
            if not assertlib.between(res, r-e, r+e):
                return False, "interp(%f, %f, %f) should be %f, but got %f" % \
                    (h, l, f, r, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function interp()" 

@t.test(3)
def testCheckends(test):
    def testMethod():
        func = lib.getFunction('checkends', _fileName)
        for (s, exp) in [('no match', False), ('hah! a match', True),
            ('q', True)]:
            res = func(s)
            if not assertlib.exact(res, exp):
                return False, "checkends(%s) should be %r, but got %r" % (s, exp, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function checkends()" 

@t.test(4)
def testFlipside(test):
    def testMethod():
        func = lib.getFunction('flipside', _fileName)
        for (s, exp) in [('homework', 'workhome'), ('carpets', 'petscar')]:
            res = func(s)
            if not assertlib.exact(res, exp):
                return False, "flipside(%s) should be %s, but got %s" % (s, exp, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function flipside()" 

@t.test(5)
def testconvertFromSeconds(test):
    def testMethod():
        func = lib.getFunction('convertFromSeconds', _fileName)
        for (s, exp) in [(610, [0, 0, 10, 10]), (100000, [1, 3, 46, 40])]:
            res = func(s)
            if not assertlib.exact(res, exp):
                return False, "convertFromSeconds(%i) should be %r, but got %r" % \
                (s, exp, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function convertFromSeconds()" 

@t.test(6)
def testFront3(test):
    def testMethod():
        func = lib.getFunction('front3', _fileName)
        for s in ['Java', 'Chocolate', 'abc']:
            res = func(s)
            exp = s[:3]*3
            if not assertlib.exact(res, exp):
                return False, "front3(%s) should be %s, but got %s" % (s, exp, res)
        return True	
    
    test.test = testMethod
    test.description = lambda : "correct outputs for the function front3()" 

