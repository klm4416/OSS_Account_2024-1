import hashlib #hashlib 사용

userdata = {} #아이디, 비밀번호 저장해둘 딕셔너리

def user_reg() : #회원가입
    id = input("id 입력: " ) #회원가입 시의 id 입력

    pw = input("password 입력: ") #회원가입 시의 pw 입력

    h = hashlib.sha256() #hashlib 모듈의 sha256 사용
    h.update(pw.encode()) #sha256으로 암호화
    pw_data = h.hexdigest() #16진수로 변환

    f = open('login.txt', 'wb') #login 파일 오픈

    userdata[id] = pw_data #key에 id값을, value에 비밀번호 값

    with open('login.txt', 'a', encoding='UTF-8') as fw: #utf-8 변환 후 login.txt에 작성
        for user_id, user_pw in userdata.items(): #딕셔너리 내에 있는 값을 모두 for문
            fw.write(f'{user_id} : {user_pw}\n') #key, value값을 차례로 login.txt파일에 저장

def user_login():
    """
    사용자로부터 아이디와 비밀번호를 입력받아 로그인 여부를 확인하는 함수입니다.

    매개변수:
        없음

    반환 값:
        없음. 함수는 입력받은 아이디와 비밀번호를 사용하여 파일 'login.txt'에 저장된 정보와 비교하여
        로그인이 성공했는지, 비밀번호가 틀렸는지, 또는 아이디가 존재하지 않는지를 출력합니다.
    """

    # 사용자로부터 아이디와 비밀번호 입력 받기
    id = input("id 입력: ")
    pw = input("password 입력: ")

    # 비밀번호를 SHA-256 알고리즘으로 해시화
    h = hashlib.sha256()
    h.update(pw.encode())
    pw_data = h.hexdigest()

    # 'login.txt' 파일을 읽어 로그인 정보 확인
    with open('login.txt', 'r', encoding='UTF-8') as fr:
        for line in fr:
            if line.startswith(id):
                if line.rstrip().endswith(pw_data):
                    print("로그인 성공")
                    break
                else:
                    print("비밀번호가 틀렸습니다.")
                    break
        else:
            print("존재하지 않는 아이디입니다.")


b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":

        break

    elif func == "2":

        break

    elif func == "3":

        break

    elif func == "?":
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit

