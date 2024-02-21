class HR_DEP:
    def __init__(self,hres,**kwargs):
        print("HR department")
        super().__init__(**kwargs)
        self.hres=hres

class FINANCE_DEP:
    def __init__(self,fres,**kwargs):
        print("FINANCE department")
        super().__init__(**kwargs)
        self.fres=fres


class SALE_DEP:
    def __init__(self,sres,**kwargs):
        print("SALE department")
        super().__init__(**kwargs)
        self.sres=sres
    

class manager(FINANCE_DEP,SALE_DEP,HR_DEP):
    def __init__(self,f,s,h):
        print("All department are as follows")
        super().__init__(fres=f,sres=s,hres=h)
        # super(HR_DEP).__init__()
        # super(FINANCE_DEP,self).__init__()

m=manager('FINANCE','SALE','HR')
print("**********************************")
print(m.fres)
print(m.sres)
print(m.hres)

