class FancyTuple:
    # Implement the FancyTuple here
    def __init__(self, *args):
        
        self._args = args
        self._tuple = tuple(args)
        self._tuple_len = len(self._tuple)
        self.my_dictionary = {0:"first",1:"second",2:"third",3:"fourth",4:"fifth"}
        
        for i in range(0,self._tuple_len):
            setattr(self, self.my_dictionary[i], self._tuple[i])
             
    def __len__(self):
        return self._tuple_len


if __name__ == '__main__':
    FancyTuple()
