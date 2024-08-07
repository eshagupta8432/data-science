story=" "
while True:
    line=input(">>>>")
    if not line:
        print("the end")
        break
    story=story+line+'\n'
print(f"my story \n {story}")