def build_pipeline(operation_names):
    
    
    
    def square(a):
        return a **2
    
    def cube(a):
        return a **3
    
    def double(a):
        return a + a
    
    def multiplication(a):
        return a + a
        
    def triple(a):
        return a * 3
    
    
    
    operations = {
        "square": square,
        "cube": cube,
        "double": double,
        "multiplication": multiplication,
        "triple": triple
            }
    
    for i in operation_names:
        if i not in operations:
            raise KeyError
    
    
    
    def pipeline(a):
        result = a
        for i in operation_names:
            
            operation = operations[i] 
            
            result = operation(result)
            
        return result
    
    
    return pipeline
    
    
    
    
    
    pass
