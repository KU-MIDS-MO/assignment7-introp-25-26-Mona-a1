def safe_call(func, a, b):
    ### Replace with your own code (begin) ###
    
    
        try:
            x = func(a,b)
            return (True, x, None)
            
        
        except ZeroDivisionError:
            return (False, None,"ZeroDivisionError")
        
        except TypeError:
            return (False, None,"TypeError")
        
        
        except ValueError:
            return (False, None,"ValueError")
        
        except IndexError:
            return (False, None,"IndexError")
        
        except KeyError:
            return (False, None,"KeyError")
    
    
    
    
    
    
        pass
    ### Replace with your own code (end)   ###
