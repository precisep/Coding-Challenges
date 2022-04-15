def triangle(number):

    i = 1


    
    if number < 0 :
        while number <= 0:
            print('#'*((-1)*number))
            number+=1
    else:
        while i <= number:
            print('#'*i)
            i +=1
       
triangle(-4)