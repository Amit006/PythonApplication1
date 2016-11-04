class ADD(object):
   try:
       def Display(self, i, k):
                self.i = i
                self.k = k
                c = i + k
                print("Result of your add number is::%d " % c)
   except TypeError:
           print("look carefully u r adding sting into the position of number")
   finally:
          print("u must enter two number beside integer")

a = ADD()
a.Display(4.6, "Amo")
