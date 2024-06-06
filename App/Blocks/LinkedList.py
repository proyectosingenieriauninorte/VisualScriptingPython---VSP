class LinkedList():
    def __init__(self, start, cmd):
        self.start = start
        self.cmd = cmd
        
    def run(self):
        currentNode = self.start
        while (currentNode != None):
            if currentNode.title == 'log':
                if self.cmd.toPlainText() == '':
                    self.cmd.setText(F">> {currentNode.execute()}")
                else:
                    self.cmd.setText(F"{self.cmd.toPlainText()}\n>> {currentNode.execute()}")
            else:
                currentNode.execute()
            currentNode = currentNode.outs['flow_out'][0]
        print("Sequence Terminated Succesfully")
        
class On_Start_Node():  
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs 
        self.outs['flow_out'] = [None] 
    def execute(self):
        print("Sequence Started with 'On_Start' Block")
        
class log_Node():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs 
        self.ins['value'] = [None, None, None]
        self.outs['flow_out'] = [None]
        self.ins['flow_in'] = [None]
    def execute(self):
        print("Sequence continued with log block")
        self.ins['value'][0] = self.ins['value'][1].outs[self.ins['value'][2]][0]
        try:
            str(self.ins['value'][0])
            print(f"printed from log: {self.ins['value'][0]}")
            return f"{self.ins['value'][0]}"
        except:
            print("Code Block log, could not convert value to string, no print available")
            return "Code Block log, could not convert value to string, no print available"
          
class str_literal():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs 
        self.outs['value'] = [None]
    def strHasChanged(self, text):
        self.outs['value'][0] = str(text)
        print(f"str has changed: {self.outs['value']}")
        
class int_literal():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs 
        self.outs['value'] = [None]
    def intHasChanged(self, text):
        try:
            self.outs['value'] = [int(text)]
            print(f"int has changed: {self.outs['value']}")
        except:
            pass
        
class bool_literal():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs 
        self.outs['true'] = [True]
        self.outs['false'] = [False]
        
class float_literal():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs 
        self.outs['value'] = [None]
    def floatHasChanged(self, text):
        try:
            self.outs['value'] = [float(text)]
            print(f"float has changed: {self.outs['value']}")
        except:
            pass
        
class if_Node():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs 
        self.outs['flow_out'] = [None]
        self.ins['flow_in'] = [None]
        self.outs['flow_true'] = [None]
        self.outs['flow_false'] = [None]
        self.ins['condition'] = [None, None, None]
    def execute(self):
        print("Sequence continued with if block")
        print(f"value for condition: {self.ins['condition'][0]}")
        print(f"swaping with: {self.ins['condition'][1].outs[self.ins['condition'][2]][0]}")
        print(f"in: {self.ins['condition'][1]}")
        print(f"with index: {self.ins['condition'][2]}")
        self.ins['condition'][0] = self.ins['condition'][1].outs[self.ins['condition'][2]][0]
        print(f"new value for condition: {self.ins['condition'][0]}")
        try:
            bool(self.ins['condition'][0])
            if self.ins['condition'][0] == None:
                self.outs['flow_out'][0] = None
            elif self.ins['condition'][0] == True:
                self.outs['flow_out'][0] = self.outs['flow_true'][0]
            elif self.ins['condition'][0] == False:
                self.outs['flow_out'][0] = self.outs['flow_false'][0]
            print(f"after all, next block is: {self.outs['flow_out'][0]}")
        except:
            print("Condition could not be parsed to Boolean, no flow checked.")
            
class compare_Node():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs 
        self.ins['A'] = [None, None, None]
        self.ins['B'] = [None, None, None]
        self.outs['flow_out'] = [None]
        self.ins['flow_in'] = [None]
        self.outs['>'] = [None]
        self.outs['<'] = [None]
        self.outs['='] = [None]
        self.outs['!='] = [None]
    def execute(self):
        print("Sequence continued with compare block")
        self.ins['A'][0] = self.ins['A'][1].outs[self.ins['A'][2]][0]
        self.ins['B'][0] = self.ins['B'][1].outs[self.ins['B'][2]][0]
        av = self.ins['A'][0]
        bv = self.ins['B'][0]
        if type(av) == type(bv):
            if av < bv:
                self.outs['<'][0] = True
                print("< true")
            else:
                self.outs['<'][0] = False
                print("< false")
            if av > bv:
                self.outs['>'][0] = True
                print("> true")
            else:
                self.outs['>'][0] = False
                print("> false")
            if av == bv:
                self.outs['='][0] = True
                print("= true")
            else:
                self.outs['='][0] = False
                print("= false")
            if av != bv:
                self.outs['!='][0] = True
                print("!= true")
            else:
                self.outs['!='][0] = False
                print("!= false")
        else:
            print("A and B must belong to the same type of value")
            
class add_Node():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs
        self.outs['flow_out'] = [None]
        self.ins['flow_in'] = [None]
        self.ins['A'] = [None, None, None]
        self.ins['B'] = [None, None, None]
        self.outs['result'] = [None]
        
    def execute(self):
        print("Sequence continued with add block")
        self.ins['A'][0] = self.ins['A'][1].outs[self.ins['A'][2]][0]
        self.ins['B'][0] = self.ins['B'][1].outs[self.ins['B'][2]][0]
        av = self.ins['A'][0]
        bv = self.ins['B'][0]
        print(f"A: {av}, B:{bv}")
        if (type(av) == type(bv)):
            if type(av) == bool:
                self.outs['result'][0] = av or bv
                print(f"result: {av or bv}")
            else:
                self.outs['result'][0] = av + bv
                print(f"result: {av + bv}")
        elif (type(av) != str and type(bv) != str) or (type(av) != bool and type(bv) != bool):
            self.outs['result'][0] = av + bv
            print(f"result: {av + bv}")
        
class sub_Node():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs
        self.outs['flow_out'] = [None]
        self.ins['flow_in'] = [None]
        self.ins['A'] = [None, None, None]
        self.ins['B'] = [None, None, None]
        self.outs['result'] = [None]
        
    def execute(self):
        self.ins['A'][0] = self.ins['A'][1].outs[self.ins['A'][2]][0]
        self.ins['B'][0] = self.ins['B'][1].outs[self.ins['B'][2]][0]
        av = self.ins['A'][0]
        bv = self.ins['B'][0]
        print(f"A: {av}, B:{bv}")
        if (type(av) == int or type(av) == float) and (type(bv) == int or type(bv) == float):
            self.outs['result'][0] = av - bv
            print(f"result: {av or bv}")
            
class mult_Node():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs
        self.outs['flow_out'] = [None]
        self.ins['flow_in'] = [None]
        self.ins['A'] = [None, None, None]
        self.ins['B'] = [None, None, None]
        self.outs['result'] = [None]
        
    def execute(self):
        self.ins['A'][0] = self.ins['A'][1].outs[self.ins['A'][2]][0]
        self.ins['B'][0] = self.ins['B'][1].outs[self.ins['B'][2]][0]
        av = self.ins['A'][0]
        bv = self.ins['B'][0]
        print(f"A: {av}, B:{bv}")
        if (type(av) == int or type(av) == float) and (type(bv) == int or type(bv) == float):
            self.outs['result'][0] = av * bv
            print(f"result: {av * bv}")
        elif type(av) == bool and type(bv) == bool:
            self.outs['result'][0] = av and bv
            print(f"result: {av and bv}")
            
class div_Node():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs
        self.outs['flow_out'] = [None]
        self.ins['flow_in'] = [None]
        self.ins['A'] = [None, None, None]
        self.ins['B'] = [None, None, None]
        self.outs['result'] = [None]
        
    def execute(self):
        self.ins['A'][0] = self.ins['A'][1].outs[self.ins['A'][2]][0]
        self.ins['B'][0] = self.ins['B'][1].outs[self.ins['B'][2]][0]
        av = self.ins['A'][0]
        bv = self.ins['B'][0]
        print(f"A: {av}, B:{bv}")
        if (type(av) == int or type(av) == float) and (type(bv) == int or type(bv) == float) and (bv != 0):
            self.outs['result'][0] = av / bv
            print(f"result: {av / bv}")
        
    
            
        
    