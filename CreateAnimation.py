from big_ol_pile_of_manim_imports import *

class test(Scene):
    def construct(self):
        l11 = TextMobject("1")
        l12 = TextMobject("2    2")
        l13 = TextMobject("3    3    3")
        g1 = VGroup(l11,l12,l13)
        g2.arrange_submobjects(DOWN)
        self.play(GrowFromCenter(g1))
        self.play(GrowFromEdge(g2))
        
class First(Scene):
    def construct(self):
        l01 = TexMobject("Sn = 1^2 + 2^2 + 3^2 + ... + n^2")
        l01.scale(2)
        l02 = TextMobject("Sn = 1 + 2 + 2 + 3 + 3 + 3 + ...")
        l02.scale(1.5)

        self.play(ShowCreation(l01))
        self.wait()
        self.play(Transform(l01,l02))
        self.wait()

class Second(Scene):
    def construct(self):
        l02 = TextMobject("Sn = 1 + 2 + 2 + 3 + 3 + 3 + ...")
        l02.scale(1.5)

        l21 = TextMobject("1")
        l22 = TextMobject("2    2")
        l23 = TextMobject("3    3    3")
        l24 = TextMobject(".    .    .    .")
        l25 = TextMobject("n   n ..... n   n")
        
        g2 = VGroup(l21,l22,l23,l24,l25)
        g2.arrange_submobjects(DOWN) 
        g2.scale(2)

        self.add(l02)
        self.wait()
        self.play(Transform(l02,g2))
        self.wait()

class Third(Scene):
    def construct(self):
        #it's really embarassed that the deepcopy is broken here, providing "[Errno 32] Broken pipe".
        l11 = TextMobject("1")
        l12 = TextMobject("2    2")
        l13 = TextMobject("3    3    3")
        l14 = TextMobject(".    .    .    .")
        l15 = TextMobject("n   n ..... n   n")

        l21 = TextMobject("1")
        l22 = TextMobject("2    2")
        l23 = TextMobject("3    3    3")
        l24 = TextMobject(".    .    .    .")
        l25 = TextMobject("n   n ..... n   n")

        l31 = TextMobject("1")
        l32 = TextMobject("2    2")
        l33 = TextMobject("3    3    3")
        l34 = TextMobject(".    .    .    .")
        l35 = TextMobject("n   n ..... n   n")

        l41 = TextMobject("2n+1")
        l42 = TextMobject("2n+1  2n+1")
        l43 = TextMobject("2n+1  2n+1  2n+1")
        l44 = TextMobject(". . . . . . . . . .")
        l45 = TextMobject("2n+1 2n+1 ... 2n+1 2n+1")

        g1 = VGroup(l11,l12,l13,l14,l15)
        g1.arrange_submobjects(DOWN)
        g2 = VGroup(l21,l22,l23,l24,l25)
        g2.arrange_submobjects(DOWN)
        g3 = VGroup(l31,l32,l33,l34,l35)
        g3.arrange_submobjects(DOWN)
        g4 = VGroup(l41,l42,l43,l44,l45)
        g4.arrange_submobjects(DOWN)

        g1.move_to(3*LEFT)
        g3.move_to(3*RIGHT)

        G = VGroup(g1,g2,g3)
        
        self.play(GrowFromCenter(G))
        self.wait()
        self.play(Rotate(g1,-2*np.pi/3),Rotate(g3,2*np.pi/3))
        self.wait()
        self.play(ApplyMethod(g1.shift,3*RIGHT),ApplyMethod(g3.shift,3*LEFT))
        self.play(Transform(G,g4))
        self.wait()
    
class Forth(Scene):
    def construct(self):
        l41 = TextMobject("2n+1")
        l42 = TextMobject("2n+1  2n+1")
        l43 = TextMobject("2n+1  2n+1  2n+1")
        l44 = TextMobject(". . . . . . . . . .")
        l45 = TextMobject("2n+1 2n+1 ... 2n+1 2n+1")
        G = VGroup(l41,l42,l43,l44,l45)
        G.arrange_submobjects(DOWN)

        l1 = TexMobject('3*S_n = (2n + 1)*(1 + 2 + 3 + ... + n)')
        l2 = TexMobject('S_n = {(2n + 1)\\over 3}*(1 + 2 + 3 + ... + n)')
        l3 = TexMobject('S_n = {(2n + 1)(n + 1)n\\over 6}')

        self.add(G)
        self.wait()
        self.play(ReplacementTransform(G,l1))
        self.wait()
        self.play(ReplacementTransform(l1,l2))
        self.wait()
        self.play(ReplacementTransform(l2,l3))
        self.wait()

class Fifth(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
    "color" : RED_B
    },
    "axes_color": RED_B,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.7)
        plane.axes.fade(.7)
        plane.add(plane.get_axis_labels())

        self.set_camera_orientation(0,-np.pi/2)
        D1 = self.createDiamond("1 2 2 2 2")
        D2 = self.createDiamond("1 2 2 2 2")
        D3 = self.createDiamond("1 2 2 2 2")
        D4 = self.createDiamond("1 2 2 2 2")
        D = [D1,D2,D3,D4]
        G = VGroup(D)
        G.arrange_submobjects(RIGHT*2)

        self.play(FadeIn(plane))
        self.play(ShowCreation(G))
        self.move_camera(np.pi/4,-np.pi/2)

        A = [np.array([0,0,1]),np.array([0,-3**0.5,-1]),np.array([1.5,0.5 * 3**0.5,-1]),np.array([-1.5,0.5 * 3**0.5,-1])]
        for i,a in zip(D,A):
            self.play(Rotate(i,2*np.pi/3,a))
        for i in D:
            self.play(ApplyMethod(i.move_to,np.array([0,0,0])))

        self.play(Transform(G,self.createDiamond("7 8 7 7 7")))
        self.wait
            

        
    def createDiamond(self,string):
        l1 = Line(np.array([0,0,0]),np.array([0,0,2]))
        l2 = Line(np.array([0,0,0]),np.array([0,-3**0.5,-1]))
        l3 = Line(np.array([0,0,0]),np.array([1.5,0.5 * 3**0.5,-1]))
        l4 = Line(np.array([0,0,0]),np.array([-1.5,0.5 * 3**0.5,-1]))
        lines = [l1,l2,l3,l4]
        for i in lines:
            i.set_color(DARK_BLUE)

        # I don't konw why i couldn't use for cycle to creat label here
        list = string.split()
        label1 = TextMobject(list[0])
        label0 = TextMobject(list[1])
        label21 = TextMobject(list[2])
        label22 = TextMobject(list[3])
        label23 = TextMobject(list[4])
        
        labels = [label1,label0,label21,label22,label23]

        label1.move_to(l1,2*OUT)
        label0.move_to(np.array([0,0,0]))
        label21.move_to(np.array([0,-3**0.5,-1]))
        label22.move_to(np.array([1.5,0.5 * 3**0.5,-1]))
        label23.move_to(np.array([-1.5,0.5 * 3**0.5,-1]))

        return VGroup(lines,labels)

class Sixth(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
    "color" : RED_B
    },
    "axes_color": RED_B,
    }
    def construct(self):
        self.set_camera_orientation(0.25*np.pi,-0.25*np.pi)
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.7)
        plane.axes.fade(.7)
        plane.add(plane.get_axis_labels())

        text = TexMobject("S_n=1+2+2+2+2+3+3+3+3+3+3+3+3+3")

        D1 = self.createDiamond(["1","2","2","2","2"]) 
        D1.move_to(np.array([0,0,2]))
        D2 = self.createDiamond(["","3","3","3","3"])
        D2.move_to(np.array([0,-3**0.5,-1]))
        D3 = self.createDiamond(["","3","3","3","3"])
        D3.move_to(np.array([1.5,0.5 * 3**0.5,-1]))
        D4 = self.createDiamond(["","3","3","3","3"])
        D4.move_to(np.array([-1.5,0.5 * 3**0.5,-1]))
        D = VGroup(D1,D2,D3,D4)

        self.set_camera_orientation(0,-0.5*np.pi)
        self.play(ShowCreation(text))
        self.wait()
        self.play(ReplacementTransform(text,D))
        # self.play(ShowCreation(D))
        self.move_camera(0.25*np.pi,-0.25*np.pi)
        self.wait()
        self.play(Rotating(D))
        self.wait()

    def createDiamond(self,list=["","","","",""]):
        l1 = Line(np.array([0,0,0]),np.array([0,0,2]))
        l2 = Line(np.array([0,0,0]),np.array([0,-3**0.5,-1]))
        l3 = Line(np.array([0,0,0]),np.array([1.5,0.5 * 3**0.5,-1]))
        l4 = Line(np.array([0,0,0]),np.array([-1.5,0.5 * 3**0.5,-1]))
        lines = [l1,l2,l3,l4]
        for i in lines:
            i.set_color(DARK_BLUE)

        # I don't konw why i couldn't use for cycle to creat label here
        label1 = TextMobject(list[0])
        label0 = TextMobject(list[1])
        label21 = TextMobject(list[2])
        label22 = TextMobject(list[3])
        label23 = TextMobject(list[4])
        
        labels = [label1,label0,label21,label22,label23]

        label1.move_to(l1,2*OUT)
        label0.move_to(np.array([0,0,0]))
        label21.move_to(np.array([0,-3**0.5,-1]))
        label22.move_to(np.array([1.5,0.5 * 3**0.5,-1]))
        label23.move_to(np.array([-1.5,0.5 * 3**0.5,-1]))

        return VGroup(lines,labels)


class Seventh(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
    "color" : RED_B
    },
    "axes_color": RED_B,
    }
    def construct(self):
        self.set_camera_orientation(0.25*np.pi,-0.25*np.pi)
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.7)
        plane.axes.fade(.7)
        plane.add(plane.get_axis_labels())

        D1 = self.create3OrderDiamond(ifDot=True)
        D2 = self.create3OrderDiamond("3n+1 3n+2 3n+1 3n+1 3n+1")

        self.play(ShowCreation(D2))
        self.wait()
        self.play(Transform(D2,D1))
        self.wait()

    def create3OrderDiamond(self,list="",ifDot=False):
        D1 = self.createDiamond(list,ifDot) 
        D1.move_to(np.array([0,0,2]))
        D2 = self.createDiamond(list,ifDot)
        D2.move_to(np.array([0,-3**0.5,-1]))
        D3 = self.createDiamond(list,ifDot)
        D3.move_to(np.array([1.5,0.5 * 3**0.5,-1]))
        D4 = self.createDiamond(list,ifDot)
        D4.move_to(np.array([-1.5,0.5 * 3**0.5,-1]))
        return VGroup(D1,D2,D3,D4)

    def createDiamond(self,string="",ifDot=False):
        l1 = Line(np.array([0,0,0]),np.array([0,0,2]))
        l2 = Line(np.array([0,0,0]),np.array([0,-3**0.5,-1]))
        l3 = Line(np.array([0,0,0]),np.array([1.5,0.5 * 3**0.5,-1]))
        l4 = Line(np.array([0,0,0]),np.array([-1.5,0.5 * 3**0.5,-1]))
        lines = [l1,l2,l3,l4]
        for i in lines:
            i.set_color(DARK_BLUE)

        if not ifDot:
            # I don't konw why i couldn't use for cycle to creat label here
            list = string.split()
            label1 = TextMobject(list[0])
            label0 = TextMobject(list[1])
            label21 = TextMobject(list[2])
            label22 = TextMobject(list[3])
            label23 = TextMobject(list[4])
            
            labels = [label1,label0,label21,label22,label23]

            label1.move_to(l1,2*OUT)
            label0.move_to(np.array([0,0,0]))
            label21.move_to(np.array([0,-3**0.5,-1]))
            label22.move_to(np.array([1.5,0.5 * 3**0.5,-1]))
            label23.move_to(np.array([-1.5,0.5 * 3**0.5,-1]))
        else:
            label1 = Dot()
            label0 = Dot()
            label0.set_color(RED)
            label21 = Dot()
            label22 = Dot()
            label23 = Dot()
                        
            labels = [label1,label0,label21,label22,label23]

            label1.move_to(l1,2*OUT)
            label0.move_to(np.array([0,0,0]))
            label21.move_to(np.array([0,-3**0.5,-1]))
            label22.move_to(np.array([1.5,0.5 * 3**0.5,-1]))
            label23.move_to(np.array([-1.5,0.5 * 3**0.5,-1]))

        return VGroup(lines,labels)

        