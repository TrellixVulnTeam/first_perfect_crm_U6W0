

def view_my_own_customers(request):
    print("running permisionn hook check.....")
    print(request.user.id,request.GET.get('consultant'))
    if str(request.user.id) == request.GET.get('consultant'):
        print("访问自己创建的用户,允许")
        return True
    else:
        return False