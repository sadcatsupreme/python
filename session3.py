class GameController:
    #the _underscore denotes a private value that is bound to a class
    #Damn I did not realize before that None is null for Python
    _instance = None

    #this will be a constructor that checks to make sure there are no existing instances of self
    def init (self):
        raise RuntimeError("There is already and instance of this class. Use the get_instance() function.")
    
    #some of these reserved words declare something as class instance [bound to local class global scope]
    @classmethod
    def get_instance(cls):
        if cls._instance == None: #Will prevent multiple instances of the singleton
            cls._instance = cls.__new__(cls) #the new method bypass the class constructor
        return cls._instance #returns the newly created instance. 
    
    # We just declared a static 

    # class myclass():
    # public static Class  myclass myinstance = new myclass()

    #def destroy():
         #myinstance = None