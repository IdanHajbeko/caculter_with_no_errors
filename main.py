
while True:
    try:
        while True:
            try:
                n = float(input("1st number: "))
            except ValueError:
                print("use only numbers")
            else:
                while True:
                    try:
                        d = float(input("2end number: "))
                    except ValueError:
                        print("use only numbers")
                    else:
                        break
                break
    except:
        print("somthing went wrong")
        print("try again")
        print("-----------------------------")
    else:
        while True:
            error = False
            try:
                a = int(input("what do you want to do +[0], -[1], *[2], /[3]: "))
                if a > 3:
                    print("use only number between 0-3")
                    error = True
            except ValueError:
                error = True
                print("use only numbers")
            if not error:
                try:
                    if a == 0:
                        try:
                            ans = float(n) + float(d)
                            print(f"the answer is: {ans}")
                            print("-----------------------------")
                        except:
                            print("somthing went wrong")
                            print("try again")
                            print("-----------------------------")
                except:
                    print("somthing went wrong")
                    print("try again")
                    print("-----------------------------")
                else:
                    try:
                        if a == 1:
                            try:
                                ans = float(n) - float(d)
                                print(f"the answer is: {ans}")
                                print("-----------------------------")
                            except:
                                print("somthing went wrong")
                                print("try again")
                                print("-----------------------------")
                    except:
                        print("somthing went wrong")
                        print("try again")
                        print("-----------------------------")
                    else:
                        try:
                            if a == 2:
                                try:
                                    ans = float(n) * float(d)
                                    print(f"the answer is: {ans}")
                                    print("-----------------------------")
                                except:
                                    print("somthing went wrong")
                                    print("try again")
                                    print("-----------------------------")
                        except:
                            print("somthing went wrong")
                            print("try again")
                            print("-----------------------------")
                        else:
                            try:
                                if a == 3:
                                    try:
                                        ans = float(n)/float(d)
                                    except ZeroDivisionError:
                                        print("cannot divide by zero!")
                                        print("try again pleas")
                                        print("-----------------------------")
                                    except ValueError:
                                        print("can only divide by a number!")
                                        print("try again pleas")
                                        print("-----------------------------")
                                    except:
                                        print("somthing went wrong")
                                        print("try again")
                                        print("-----------------------------")
                                    else:
                                        print(f"the answer is: {ans}")
                                        print("-----------------------------")
                            except:
                                print("somthing went wrong")
                                print("try again")
                                print("-----------------------------")
                break
