def add(stringintegers):
    intnumb=0
    stringnumb=''
    delimiter=''
    if stringintegers=='':
        return 0
    elif len(stringintegers)>1 and stringintegers[0]+stringintegers[1]=='//': 
        delimiter=stringintegers[2:stringintegers.index('\n')]
        for char in stringintegers[4:]:
            if char==delimiter:
                if int(stringnumb)>=1000:
                    stringnumb=0
                intnumb=intnumb+int(stringnumb)
                stringnumb=''
            elif char=='\n':
                if int(stringnumb)>=1000:
                    stringnumb=0
                intnumb=intnumb+int(stringnumb)
                stringnumb=''   
            else:
                stringnumb=stringnumb+char
        if int(stringnumb)>=1000:
                stringnumb=0
        return intnumb+int(stringnumb)

    else:
        for char in stringintegers:
            if char==',':
                if int(stringnumb)>=1000:
                    stringnumb=0
                intnumb=intnumb+int(stringnumb)
                stringnumb=''
            elif char=='\n':
                if int(stringnumb)>=1000:
                    stringnumb=0
                intnumb=intnumb+int(stringnumb)
                stringnumb=''   
            else:
                stringnumb=stringnumb+char 
        if int(stringnumb)>=1000:
            stringnumb=0
        
        return intnumb+int(stringnumb)


print(add("//***\n1***2***3"))




