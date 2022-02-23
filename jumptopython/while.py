#열 번 찍어 안 넘어가는 나무 없다.

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1                      # 이 표현 잘 기억해두기./ (treeHit + = 1)
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")


#여러 가지 선택지 중 하나를 선택해서 입력받는 예제   ############################오류

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """

number =  0
while number != 4:                      #4가 아닌 동안 prompt 출력하고 사용자로부터 번호를 입력받는다.
    print(prompt)
    number = int(input())               # 사용자의 숫자 입력을 받아들이는 것

1. Add
2. Del
3. List
4. Quit

Enter number : 4

## While 문 강제로 빠져나가기
# 커피 자판기 -> 커피가 떨어졌을 때 판매를 중단하고 "판매 중지" 문구를 사용자에게 보여주기 (((break문)))

coffee = 10
money = 500
while money:
    print("돈을 받았습니다. 커피를 내립니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
        break

############

coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 내립니다." % (money -300))
    else:
        print("돈을 다시 돌려주고 커피를 내리지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." %d coffee)
    if coffee ==0:
        print("커피가 모두 소진되었습니다. 판매를 중지 합니다.")
        break


##while문의 맨 처음으로 돌아가기

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)