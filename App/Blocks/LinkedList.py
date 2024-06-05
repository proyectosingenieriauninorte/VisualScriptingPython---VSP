class LinkedList():
    def __init__(self, start):
        self.start = start
        
    def run(self):
        currentNode = self.start
        while (currentNode != None):
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
        self.ins['value'][0] = self.ins['value'][1].outs[self.ins['value'][2]][0]
        print("Sequence continued with log block")
        print(f"printed from log: {self.ins['value'][0]}")
        
class literal_Node():
    def __init__(self, title, ins, outs):
        self.title = title
        self.ins = ins
        self.outs = outs 
        self.outs['value'] = [None]
    def textHasChanged(self, text):
        self.outs['value'] = [text]
        print(f"Text has changed: {self.outs['value']}")
        
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
        if self.ins['condition'][0] == None:
            self.outs['flow_out'][0] = None
        elif self.ins['condition'][0] == True:
            self.outs['flow_out'][0] = self.outs['flow_true'][0]
        elif self.ins['condition'][0] == False:
            self.outs['flow_out'][0] = self.outs['flow_false'][0]
        print(f"after all, next block is: {self.outs['flow_out'][0]}")
            
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
    