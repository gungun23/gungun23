#rect.py
class rectangle:
    def_init_(self):
       print("rectangle")
    def area(self,length,width):
        self l=length
        self w=width
        print("area of rectangle is:"self.l*self.w)

        #sq.py
        class square:
            def_init_(self):
            print("square")
            def area (self,side):
                self.a=side
                print("area of square is:",self.a*self.a)

                #tri.py
                class triangle:
                    def_init_(self):
                    print("trinagle")
                    def area (self,base,height):
                        self.b=base
                        self.h=height
                        ar=(1/2)*self.b*self.h
                        print("area of triangle is:",ar)

                        #main.py
                        import rect
                        import _sq
                        import tri
                        r=rect.rectangle()
                        r.area(10,20)
                        s=sq.square()
                        s.area(10)
                        t=tri.triangle()
                        t.area(6,8)


        
