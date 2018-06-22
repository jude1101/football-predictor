from sys import argv
script, t1, t2 = argv

a1 = open(t1)
a2 = open(t2)

k1 = a1.read().split()
k2 = a2.read().split()


class team(object):
    def __init__(self, name, mdribble, mpasses, minterceptions, mtackles, mttackles, mtackled, mintercepted, rwinterceptions, rwtackles, rwttackles, rwcross_block, rwtot_cross, rwacc_cross, rwintercepted, rwdribble, rwtackled, rwpasses, lwinterceptions, lwtackles, lwttackles, lwcross_block, lwtot_cross, lwacc_cross, lwintercepted, lwdribble, lwtackled, lwpasses, bshot_block, saves, btackles, bttackles, binterceptions, ftot_shot, fon_shot, fdribble, fpasses, ftackled, fintercepted, goal):
        self.name = name
        self.mpasses = float(mpasses)
        self.mdribble = float(mdribble)
        self.mpassingv = float(mpasses) - float(mintercepted)/2
        self.mdribblev = float(mdribble)/2 - float(mtackled)/2
        self.mpassingx = -float(minterceptions)/2
        self.mdribblex = float(mttackles)/2 - float(mtackles)/2
        self.rwinterceptions = -float(rwinterceptions)/2
        self.rwtackles = float(rwttackles)/2 - float(rwtackles)/2
        self.rwcross_block = -float(rwcross_block)/2
        self.rwcross = float(rwtot_cross)
        self.rwpasses = float(rwpasses)
        self.rwdribble = float(rwdribble)
        self.rwcrossv = float(rwtot_cross) - (float(rwtot_cross) - float(rwacc_cross))/2
        self.rwpassingv = float(rwpasses) - float(rwintercepted)/2
        self.rwdribblev = float(rwdribble)/2 - float(rwtackled)/2
        self.lwinterceptions = -float(lwinterceptions)/2
        self.lwtackles = float(lwttackles)/2 - float(lwtackles)/2
        self.lwcross_block = -float(lwcross_block)/2
        self.lwcross = float(lwtot_cross)
        self.lwpasses = float(lwpasses)
        self.lwdribble = float(lwdribble)
        self.lwcrossv = float(lwtot_cross) - (float(lwtot_cross) - float(lwacc_cross))/2
        self.lwpassingv = float(lwpasses) - float(lwintercepted)/2
        self.lwdribblev = float(lwdribble)/2 - float(lwtackled)/2
        self.binterceptions = -float(binterceptions)/2
        self.btackles = float(bttackles)/2 - float(btackles)/2
        self.bshot_block = -(float(bshot_block) + float(saves))/4
        self.fpassing = float(fpasses)
        self.fdribble = float(fdribble)
        self.fshot = float(ftot_shot)
        self.fpassingv = float(fpasses) - float(fintercepted)/2
        self.fdribblev = float(fdribble)/2 - float(ftackled)/2
        self.fshotv = float(ftot_shot) - (float(ftot_shot) - float(fon_shot))/2
        self.goals = float(goal)



def midr(x,y):
    return ((x.mdribblev + y.mdribblex) / ( x.mdribble))


def rwing(x,y):
    return ((x.rwcrossv + y.lwcross_block)* (x.rwdribblev + y.lwtackles) * (x.rwpassingv + y.lwinterceptions) * midr(x,y) / (x.rwcross * x.rwpasses * x.rwdribble))


def lwing(x,y):
    return ((x.lwcrossv + y.rwcross_block)* (x.lwdribblev + y.rwtackles) * (x.lwpassingv + y.rwinterceptions) * midr(x,y) / (x.lwcross * x.lwpasses * x.lwdribble))


def area(x,y):
    return ((x.fpassingv + y.binterceptions) * (x.fdribblev + y.btackles) * (x.fshotv + y.bshot_block) * (midr(x,y) + rwing(x,y) + lwing(x,y)) / (x.fpassing * x.fdribble * x.fshot))


def goal(x,y):
    xg = area(x,y) * x.goals * 11
    yg = area(y,x) * y.goals * 11



    print x.name
    print xg
    print yg
    print y.name


team1 = team(*k1)
team2 = team(*k2)

goal(team1, team2)
