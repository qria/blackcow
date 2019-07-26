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
    image red tilted = im.Scale("red/tilted.png", 600, 600)
    image bg room = "backgrounds/room.jpg"

define p = Character('핑크', color="#c8ffc8")
define sis = Character('유이', color="#c8ffc8", image="sisterImage")
define questionmark = Character('???', color="#c8ffc8")
define me = Character('나')
define red = Character('레드', color="#c8ffc8")


label start:

    scene bg room with dissolve

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

    "to be continued"

    return
