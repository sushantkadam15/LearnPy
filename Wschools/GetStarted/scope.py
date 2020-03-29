def fun():
    x = "This variable is under fun() and acessible within only."
    def innerFun():
        print(x)
    innerFun()

fun()