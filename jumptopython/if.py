money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어라가")


# 비교연산자

money = True
if money:
    x = 3
    y = 2
    x > y


# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라.
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else :
    print("걸어가라")

# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라 #card 빼먹지 말기
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else :
    print("걸어가라")

# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

## 조건문에서 아무 일도 하지 않게 설정하기 (pass)
# 주머니에 돈이 있으면 가만히 있고 돈이 없으면 카드를 꺼내라
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket :
    pass
else:
    print("카드를 꺼내라")

#위의 pass문 더 간략하게 코드 작성하기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

###다양한 조건을 판단하는 elif(다중 조건 판단 가능)

##주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라
#조건을 판단하는 부분은 두 군데 (돈이 있는지 / 카드가 있는지)

#if와 else로 나타내보기

pocket = ['paper', 'handphone']
card = True #card 빼먹지 말기
if 'money' in pocket :
    print("택시를 타고 가라")
else :
    if card :
        print("택시를 타고 가라")
    else:
        print("걸어가라")

#elif로 나타내기 (-> 조건문이 거짓일 때만 수행)
pocket =  ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card :
    print("택시를 타고 가라")
else :
    print("걸어가라")

#조건부 표현식
score=100
if score >= 60:
    message = "success"
else:
    message = "failure"  #라는 코드를 python의 conditional expression으로 표현해보기

score=100
message = "success" if score >= 60 else "failure"
print(message)

##################### score값 입력 안 해줘서 오류났고, print() 안 해줘서 출력이 안됐었음 ##################