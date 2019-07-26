init:
    image cool neutral = im.Scale("pink/neutral.png", 600, 600)
    image sis touchingHair = im.Scale("peach/touchingHair.png", 600, 600)
    image red tilted = im.Scale("red/tilted.png", 600, 600)
    image bg room = "backgrounds/room.jpg"

define sis = Character('핑크', color="#c8ffc8")
define cool = Character('피치', color="#c8ffc8")
define red = Character('레드', color="#c8ffc8")


label start:

    scene bg room with dissolve

    "내 이름은 코구치 쿠로우시(虎口 黑牛)"

    "대학교 2학년이다."

    "그래서 어쩌라고"

    return
