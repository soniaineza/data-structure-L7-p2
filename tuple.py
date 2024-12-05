tupl=()
print(tupl)

tupl=(1,2,3,4,5)
print(tupl)

tupl=(1,"sonya",False,5.6)
print(tupl)

tupl=("mouse",[1,2,3],(4,5,6))
print(tupl[0])
print(tupl[1][1])

tupl=tupl[1:2]
print(tupl)

tupl=(1,2,3,4,5)
for element in tupl:
    print("hello",element)
