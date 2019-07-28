init:
    image cool neutral = im.Scale("pink/neutral.png", 600, 600)
    image sisterImage closeup = im.Scale("peach/closeup.png", 600, 600)
    image sisterImage hmm = im.Scale("peach/hmm.png", 600, 600)
    image sisterImage leaningFront = im.Scale("peach/leaningFront.png", 600, 600)
    image sisterImage mouthOpen = im.Scale("peach/mouthOpen.png", 600, 600)
    image sisterImage neutral = im.Scale("peach/neutral.png", 600, 600)
    image sisterImage smiling = im.Scale("peach/smiling.png", 600, 600)
    image sisterImage smirk = im.Scale("peach/smirk.png", 600, 600)
    image sisterImage touchingHair = im.Scale("peach/touchingHair.png", 600, 600)

    image pinkImage annoyed = im.Scale("pink/annoyed.png", 600, 600)
    image pinkImage attentive = im.Scale("pink/attentive.png", 600, 600)
    image pinkImage curious = im.Scale("pink/curious.png", 600, 600)
    image pinkImage going = im.Scale("pink/going.png", 600, 600)
    image pinkImage neutral = im.Scale("pink/neutral.png", 600, 600)
    image pinkImage smiling = im.Scale("pink/smiling.png", 600, 600)
    image pinkImage smiling2 = im.Scale("pink/smiling2.png", 600, 600)
    image pinkImage tilted = im.Scale("pink/tilted.png", 600, 600)
    image pinkImage tilted2 = im.Scale("pink/tilted2.png", 600, 600)


    image red tilted = im.Scale("red/tilted.png", 600, 600)
    image church = im.Scale("church.png", 600, 600)

    image bg room = "backgrounds/room.jpg"
    image bg campus = "backgrounds/campus.jpeg"
    image bg school = "backgrounds/school.jpeg"

define p = Character('아야', color="#c8ffc8")
define sis = Character('유이', color="#c8ffc8", image="sisterImage")
define questionmark = Character('???', color="#c8ffc8")
define c = Character('윤리학과 신입생?', color="#c8ffc8")
define me = Character('나')
define red = Character('레드', color="#c8ffc8")


label start:

    scene bg room with dissolve

    "아침 8시, 집"

    "내 이름은 코구치 쿠로우시(虎口 黑牛)"

    "대학교 2학년이다."

    "그리고 아무래도 좋지만\n나는 곧 솔로 경력을 20년 채울 예정이다."

    questionmark "오빠..?"

    show sisterImage neutral with dissolve

    "이 녀석은 유이, 내 귀여운 여동생이다."

    "참고로 이렇게 보여도 우리는 연년생이라 대학교 1년생이다."

    sis smirk "오빠, 컴퓨터 또 고장났어"

    me "음?"

    sis smirk "소리는 나는데 화면이 까매."

    me "그래? 혹시 모니터에 전원 케이블이 연결되어 있어?"

    sis smirk "음... 되있는 것 같아?"

    me "그 모니터 뒤에 검은 케이블 있잖아"

    sis neutral "음.. 나 그런거 잘 모르는데..."

    sis neutral "그냥 와서 한 번 봐주면 안돼?"

    me "알았어 이것만 하고."

    sis leaningFront "오빠 나 좀 바쁜데..."

    me "아 그래? 그럼 잠시만,"

    "나는 여동생의 방에 들어가 모니터 뒤쪽을 확인해 보았다."

    "역시나 전선 케이블이 빠져 있었으며 꽂으니 정상적으로 작동했다."

    sis smiling "앗 된다! 고마워 오빠!"

    me "뭘 이정도 가지고! 또 고장나면 언제든지 불러!"

    sis mouthOpen "오빠 근데 있잖아 이거 좀 더 좋은거는 없었어?"

    me "응?"

    sis mouthOpen "내가 10만원이나 줬는데 좀 느린 것 같아서..."

    me "아아 미안, 다음엔 좀 더 발품을 팔아볼게."

    sis touchingHair "그래? 그럼 다음에 기대해 볼께!"

    me "응 고마워!"

    hide sis dissolve

    "보통 남매는 매일 싸운다고 하는데, 정말 신기하게 우리 남매는 싸워본 적이 한 번도 없다."

    "이렇게 귀여운 여동생과 사이가 좋다니... 정말 나는 운이 좋은 것 같다"

    scene bg campus with dissolve

    "아침 9시, 학교 캠퍼스 안"

    "1교시를 신청해버린 불쌍한 학우들의 분주한 움직임이 보인다."

    "내 수업은 시작이 아직 많이 남았으니 느긋하게 도서관에 들렀다 갈 생각이다."

    questionmark "저기요, 잠시만요"

    show church with dissolve

    me "네?"

    questionmark "저기 혹시 여기 서점이 어디있는지 아세요?"

    me "서점이요?"

    c "네 제가 윤리학과 신입생인데요, 이 쪽을 잘 몰라가지고.."

    "우리 학교에 윤리학과도 있었구나.."

    me "아 서점이라면 저쪽 건물이 교보문고가 하나 있어요"

    c "아 정말 감사합니다! 완전 헤매고 있었는데 덕분에"

    c "혹시 지금 수업가고 계시나요?"

    me "아 아뇨 도서관 가는 중이었어요"

    c "제가 신입생이고 해서 진로가 요즘 좀 고민이라서 다른분들하고 얘기를 좀 하고 싶어서요"

    me "아 그러세요? 다음수업까지 좀 시간이 남긴 하네요"

    c "아 정말요? 정말 다행이다~! 그럼 같이 커피 한잔 해요!"

    me "그럴까요?"

    questionmark "쿠로우시 군!"

    "갑자기 뒤에서 누군가 부르는 소리가 들렸다"

    show pink smiling with dissolve

    questionmark "기다리고 있었는데 여기서 뭐하고 있어?"

    me "응?"

    "이 녀석은 토우죠 아야"

    "작년부터 수업을 같이 듣는 게 많아서 친해졌다"

    pink "뭐해여기서? 5분 전부터 기다리고 있었다고!"

    me "???"

    show pink smiling2 with dissolve

    "갑자기 아야가 팔짱을 꼈다"

    pink "우리 같이 도서관에서 공부하기로 했잖아! 빨리와!"

    "팔을 끌어당기더니 갑자기 걷기 시작했다"

    me "아앗!"

    "어느 샌가 아까 그 윤리학과 학생은 안보였다"

    me "헉헉.. 갑자기 뭐하는 짓이야?"

    pink tilted "뭐하냐 너"

    me "너야말로 뭐해? 난 약속 잡은 기억 없는데?"

    pink "저 사람하고 뭐하고 있었어?"

    me "저 사람 윤리학과 학생이라고 좀 도와달라고 하던데?"

    pink annoyed "우리학교에 윤리학과는 없어 멍청아"

    me "아 그래? 그럼 저 사람은 뭐지?"

    pink ""

    me "그래?"

    return
