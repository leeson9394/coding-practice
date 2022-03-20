class Server(object):
    ...
    type: str
    swap_bytes: int

    def get_swap_size(self):
        """Gets swap partition size in bytes or None
        when the server has no swap partition"""
        return self.swap_bytes

    def get_swap_size_mb(self):
        """Gets swap partition size in mibibytes or None
        when the server has no swap partition"""
        length = self.get_swap_size()
        if length is not None:
            return length / (1024*1024)
        return None

       
       
if __name__ == "__main__":
    obj = Server()
    obj.type = "linux"
    obj.swap_bytes = 1 << 30
    print(obj.get_swap_size_mb.__doc__)
    print(obj.get_swap_size_mb())
    
    
    
    '''1. Fix len variable squashing
    2. Instead of returning boolean for no swap return None
    3. 
    

    in - for item in some_list: if item == value: return True
    == - "test" == "test"
    is -  "test" is "test" 
    
    None, True, False always signletons 
    -5 - 256 are singletons in cpython
    '''