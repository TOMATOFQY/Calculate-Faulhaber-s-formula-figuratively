from big_ol_pile_of_manim_imports import *
import copy

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

        # I have to roast the idea that the function ReplacementTransform is different from Transform is a really a bad design. When I first use Transform,I supposed there is some problem with my environment.But the fact turn out that the bug is just about designing.
        self.add(G)
        self.wait()
        self.play(ReplacementTransform(G,l1))
        self.wait()
        self.play(ReplacementTransform(l1,l2))
        self.wait()
        self.play(ReplacementTransform(l2,l3))
        self.wait()



        