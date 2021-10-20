import random
import threading
from typing import Union

from TGNRobot.modules.helper_funcs.msg_types import Types
from TGNRobot.modules.sql import BASE, SESSION
from sqlalchemy import BigInteger, Boolean, Column, Integer, String, UnicodeText

 DEFAULT_WELCOME = 'ஏய் {first}, நீங்கள் எப்படி இருக்கிறீர்கள்?'
DEFAULT_GOODBYE = 'பேச தெரிஞ்சா பேசு தேவையில்லாம பேசி அடிவாங்கி சாகதா 🤬!'

DEFAULT_WELCOME_MESSAGES = [
    "{first}  உங்களுக்காக தான் எல்லாரும் காத்துகிட்டு இருந்தோம்! Welcome 🥳!",  #Discord welcome messages copied
    "நீங்க பெரிய கைதி எல்லாம் பாத்துருப்பிங்க ஆனா இப்ப வரப்போறது Master {first}",
    "எவ்வளோ பேர் இருக்கிறாங்குறத்து முக்கியம் இல்லை! , {first} இருக்கான்றதுதான் முக்கியம்!😏.",
    "வாங்க {first} வந்து மொக்க அறுவையை போடுங்க!😂.",
    "{first} இரு இதயம் ஒரு இதயம் ஆனதே இரு இதயம் ஒரு இதயம் ஆனதே! அந்த ஒரு இதயம் அந்த ஒரு இதயம் நொருங்கிப்போனதே! 🤣🤣😂😂😂❤️❤️",
    "{first} IPL லில் அதிக கோப்பையை வென்ற ஒரு தனி நபர் யார்?🏆.",
    "{first} IPL லில் சிறந்த Captain யார்?🏏",
    "{first} Love-ன்றது ஆயா சுடுற வடை மாதிரி அந்த வடைய எப்பவேணும்னாலும் காக்க வந்து கவ்விட்டு போகும் ஆனா Friendship-ன்றது அந்த ஆயா மாதிரி அந்த ஆயாவ எவனாலும் தூக்க முடியாது 😍🥰",
    "{first} நீங்க Join பண்ணத நாங்க பார்த்துட்டோம்!🙈🙊",
    "ஒரு குழந்தை உருவாக்குறத்துக்கு பத்து மாசம்! ஒரு பட்டதாரி உருவாக்குறத்துக்கு மூனு வருஷம்! ஆனா ஒரு Best Admin உருவாக்குறதுக்கு ஒரு யுகமே தேவைபடுது, {first}. 😂🤧",
    "{first} Chat முக்கியம் பிகிலு..!🔥",
    "{first} நீங்க இங்க இருக்கீங்க! உங்க Friends-லாம் எங்க? 🤨",
    "நீங்க வேணா Group-ல Clash-அ Boss-அ சுத்தலாம் ஆனா, {first}. Mass என்னனு தெரியாதுல!😎.",
    "{first} தனிமை கொடுமையானது! 🥺 அதனால், எங்களோடு சேர்ந்து கொள்ளுங்கள்!☺️",
    "{first} தனிமை கொடுமையானது! 🥺 அதனால், எங்களோடு சேர்ந்து கொள்ளுங்கள்!☺️.",
    "{first} நீங்கள் Join பண்ணா மட்டும் போதாது உங்கள் Friends-யும் Invite பண்ணுங்க!😐",
    "{first} ❤️ உங்களுக்காக தான் எல்லாரும் காத்துகிட்டு இருந்தோம்! Welcome 🥳.",
    "{first} நான் உன்ன விரும்பல... உன் மேல ஆசப்படல... நீ அழகா இருக்கேனு நினைக்கல... ஆனா இதெல்லாம் நடந்துடுமோனு பயமா இருக்கு🙈🙈",
    "என்ன ஞாபகம் இருக்கா மச்சான் {first}.",
    "நல்லா குற்றாலத்துல இருக்கவேண்டியவன்லாம் இங்க வந்து நம்ம உயிர வாங்குறாங்கே!😒{first}!",
    "{first} 😈 இது கலவர பூமி ⚔️🗡🔪 ! இங்கு ஏன் வந்தீங்க?😳",
    "{first} என்னவளே என் மனதில் உள்ள எனது எண்ணத்தை நீ அறிந்தும் அறியாதது போல நடிக்கிறாயா இல்லை தகுந்த சந்தர்ப்பம் அமையட்டும் என எதிர்பார்த்து காத்திருக்கிறாயா பெண்ணே🥳🥰!",
    "{first} ஒரு பூ மலர பல பருவங்களை கடக்கிறது நீ உன் வாழ்க்கையை உணர பல தடைகளை கடந்து  செல்.இனிய காலை வணக்கம்..",
    "{first} உனக்கு welcome ல பண்ண முடியாது 😏",
    "{first} உங்கள் ராசி என்ன?👀.",
    "{first} நீங்கள் அதிக முறை திரைப்படம் எது👀",
    "{first} சம்பவம் செய்யும் வேலைய எல்லாம் அஞ்சாறு வாரம் ஒத்தி போடு Groupக்கு யாரும் வந்தாலும்கூட வள்ளலார் போல வணக்கம் போடு!😂🙏",
    "{first} உலக கோப்பை கிரிக்கெட் விளையாட்டில் அதிக முறை கோப்பையை வென்ற அணி எது?🏆",
    "{first} உங்களை யார் (inspires)தூண்டுகிறார்கள்? நீங்கள் யாரைப் போல இருக்க விரும்புகிறீர்கள்? 🎈",
    "சம்பவம் செய்யும் வேலைய எல்லாம் அஞ்சாறு வாரம் ஒத்தி போடு Groupக்கு யாரும் வந்தாலும்கூட வள்ளலார் போல வணக்கம் போடு!😂🙏 {first}",
    "{first}உங்களுக்கு Comedy பண்ண தெரியுமா? 😇",
    "{first} Long-ல பார்த்தத்தான்டா Comedy-யா இருப்பேன் கிட்டத்துல பார்த்த Terror-ஆ இருப்பேன்டா Terror-ஆ😤",
    "வாங்க {first} எல்லாரும் Busy நான் உங்களை வரவேற்கிறேன்🙏",
    "{first} யாருமே இல்லாத Group-ல யாருக்குடா Message பண்ற உன் கடமை உணர்ச்சிக்கு ஒரு அளவே இல்லையாடா🤦‍♀😂",
    "{first}கலப்படமான நல்லவனா இருக்குறதுக்கு சுத்தமான கெட்டவனா  இருந்துட்டு போகலாம்😍",
    "வாங்க {first} வந்து மொக்க அறுவையை போடுங்க!😂",
    "🎺 தங்கமே உன்னத்தான் தேடிவந்தேன் நானே வைரமே ஒருநாள் உன்னத் தூக்குவேனே..! 🎺",
    "{first}  எல்லாரும் பணம் இருந்தா நிம்மதியா வாழ்ந்திரலாம்னு நெனைக்குறாங்க ஆனா பணம் இல்லேன்னா நிம்மதியான சாகக்கூட முடியாதுனு யாரும் நெனைக்குறதே இல்லை!🎈",
    "{first} Oii Selfie எனக்கு எப்போ Ok சொல்லுவ! 😉",
    "நம்ம ஊருக்கு நாய் புடிக்குற வண்டி வரட்டும் கண்டிப்பா {first}, உன்னை நான் புடிச்சு குடுத்துறேன்!😂",
    "{first} Chatting Start பண்ண மாட்டான்.பண்ணிட்டான் நிறுத்த மாட்டான்🤪",
    "{first} அடிவெள்ளாவிவச்சுத் தான் வெளுத்தாய்ங்களா உன்ன வெயிலுக்கு காட்டாம வளர்த்தாய்ங்களா!🙈🥳😍.",  #Discord welcome messages end.
    "{first} எங்களுக்கு ஒரு கதை சொல்லிட்டு அப்பறம் பேசுங்க! 😍",
    "வந்திருக்கிறது சாதாரண ஆள் இல்ல பயத்துக்கே பயம் காட்டுரவன் 😎 {first}.",
    "குருநாதா! இதுக்கு மேல தாங்க முடியாது குருநாதா... 🥶🤬.",
    "🎼இளமை திரும்புதே புரியாத புதிராச்சே இதய துடிப்பிலே பனி காத்தும் சூடாச்சே🎼",  #Tekken
    "Ok!",
    "{first}  தங்களை அதிகம் துன்புறுத்தியது யார் ?",
    "{first} நீ என் நண்பேன்டா😍",
    "{first}  IPL லில் தங்களுக்கு பிடித்த அணி எது? 🏏",
    "{first}, நீ ஒரு டுபாக்கூர் 😝",  #Hunter Hunter
    "{first} உங்களுக்கு Comedy பண்ண தெரியுமா? 😇.",  #One Punch man s2
    "ஜெயிக்கிறதுக்கு முன்னாடி கொண்டாடுறதும் ஜெயிச்சதுக்கு அப்புறம் ஆடுறதும்  அகராதியிலே இல்லை {first}",
    "வா மச்சான் {first} எப்படி இருக்க? 😁",
    "ஐய்யோ ஓடுங்க ஓடுங்க அந்த கொடிய மிருகம் karun¥a நம்மள நோக்கி தான் வந்து கொண்டிருக்கிறது!😂🏃‍♂🏃‍♂",  #One Punch ma
    "இந்த குச்சி ஐஸ் வைக்கபோர்க்குள்ள ஒளிஞ்சுக்கிட்டு யார் கூட ஐஸ் பாய் விளையாடுறான்🤣😂.",  #One Punch ma 
    "{first}, எங்களுக்கு ஒரு கதை சொல்லிட்டு அப்பறம் பேசுங்க! 😍",  #One Punch ma
    "நீங்க ரொம்ப சப்ப Member-ஆ இருக்கீங்க! 😂 {first}.",
    "ஒரே அடி தான் நீ காலி 😏",
    "🎧 ஊரான ஊருக்குள்ள ஒன்னப்போல யாரும் இல்ல. ஆனா நீ என்ன மட்டும் சேரவே இல்ல. ",
    "வெளிய போங்கடா அயோக்கிய ராஸ்கல்களா!😏.",
    "இந்த Area அந்த Area அந்த இடம் இந்த இடம் எங்கையும் எனக்கு பயம் கெடையாதுடா All Area-லையும் Lucky கில்லிடா!🥳.",
    "உன்னையெல்லாம் பார்த்த எனக்கு பாவமா இருக்கு😂",
    "நல்லா குத்தாளத்துல இருக்கவேண்டியதெல்லாம் இங்கே இருக்குதுங்க🐒.",
    "🎵கரை ஏறி வந்த மீனு கருவாடா போகுமுனு, புரியாம போச்சே நண்பா .",
    "நண்பரிடம் பேசி உள்ளே செல்லுங்கள்.",
    "உங்களை வரவேற்கிறோம்",
    "புள்ள குட்டிய படிக்க வெய் போ... 😆.",
    "டேய் இந்த பச்சை தண்ணிய குடிச்சிட்டு பாயாசம் சாப்ட மாதிரி Buildup கொடுக்குறதெல்லாம் என்கிட்ட வேணாம் 🤬",
    "ஹோலா {first}, பேரழிவு நிலைகள் உள்ளவர்களிடம் ஜாக்கிரதை",
    "டேய் நாயே நீயா இந்த நேரத்துல இங்க எங்கடா வந்த😅.",
    "உடைஞ்சு போன வாஸ்து பொம்மைய ஓட்ட வச்சமாதிரி ஒரு மூஞ்சி இவன் Personality பத்தி பேசுறான் டா😂.",
    "அய்யோ ராமா! என்னை ஏன் இந்த மாதிரி கழிச்சடை பசங்க கூடெல்லாம் கூட்டு சேர வெக்குற😖",
    "pls உங்கள் தொலைபேசி எண்ணை வெளிப்படுத்துங்கள்",
    "டாக்டர். பாவிகளை வரவேற்கிறோம்.",
    "உடைஞ்சு போன வாஸ்து பொம்மைய ஓட்ட வச்சமாதிரி ஒரு மூஞ்சி இவன் Personality பத்தி பேசுறான் டா😂.",
    "{first} மனசார சொல்றேன் டா சாத்தியமா நீ எல்லாம் உருப்பட மாட்ட உருப்படவே மாட்ட🤦‍♀",  #tokyo ghoul
    " உங்களுக்கு பிடித்த Video அல்லது Gif ஐ அனுப்பவும் 🥰",  #hunter x hunter
    "வா சுல்தான் வா சுல்தான் வா சுல்தான் வா உனக்குனு தான் தரவா தரவா உசுர தரவா {first} ",  #one Piece
    "எருமைக்கு கூட Blue Cross இருக்கு {first}க்காக யோசிக்க உயிரா இருக்கு! 🥺",  #BNHA
    "அடிவாங்குறதுக்குனே அளவெடுத்து செஞ்சமாதிரி இருக்கான்👊🌷",  #Kamina Falls – Gurren Lagann
    "அய்யயோ!! *•.{first}கணக்கு Teacher-அ வச்சுருக்கான்டோ அதை நான் பாத்து போட்டேன்டோ!😂.",  #Hellsing
    "எங்களுக்கு ஒரு கதை சொல்லிட்டு அப்பறம் பேசுங்க! 😍..",  #Neon Genesis: Evangelion
    "உள்ள வந்தா Power அடி அண்ணே யாரு தளபதி😎",  #Pokemon
   
]
DEFAULT_GOODBYE_MESSAGES = [
    "ஏன் என்னை பிரிந்தாய் என் உயிரே என் உயிரே🥺💔.",
    "தனியாக தவிக்கின்றேன் துணைவேண்டாம் அன்பே போ🥺.",
    "மறந்தாயே மறந்தாயே பெண்ணே என்னை ஏன் மறந்தாய் கடந்தேதான் நடந்தாயே யாரோ என்று ஏன் கடந்தாய்!🥺💔.",
    "{first} has left the clan.",
    "{first} has left the game.",
    "பேச தெரிஞ்சா பேசு தேவையில்லாம பேசி அடிவாங்கி சாகதா 🤬.",
    "மனசார சொல்றேன் டா சாத்தியமா நீ எல்லாம் உருப்பட மாட்ட உருப்படவே மாட்ட🤦‍♀",
    "அய்யயோ! இந்த ஆளு Teacher-அ வச்சுருக்கான்டோ அதை நான் பாத்து போட்டேன்டோ😆",
    "போட எச்ச பயலே 🥶💦.",
    "We hope to see you again soon, {first}.",
    "ஏன்டா அறிவுகெட்டவனே அறிவு இருக்கா உனக்கு மடப்பயலே முட்டா பயலே சோத்தை திங்கிறியா இல்ல சோத்தை விட்டுட்டு லட்டியை திங்கிறியா டா😂😂🤣🤣.",
    "ஜிஞ்சர் ஈட்டிங்க் மங்க்கி 🐵",
    "அடேய் பொறம்போக்கு வீட்ல சொல்லிட்டு வந்தியா ?.",
    "Please don't leave me alone in this place, {first}!",
    "அடிவாங்குறதுக்குனே அளவெடுத்து செஞ்சமாதிரி இருக்கான்👊",
    "என்னப்பா உனக்கு பிரச்சன? 😣",
    "ஆணியே புடுங்க வேணாம்🙄.",
    "யார் எடத்துல வந்து  யார் Scene-அ போடுறது  செஞ்சுருவேன்😤😡.",
    "மூடிட்டு போடா வெண்ண! 😂.",
    "நீ பெரிய முட்டாள்னு எனக்கு எப்பயோ தெரியும்! 😜",
    "மனசார சொல்றேன் டா சாத்தியமா நீ எல்லாம் உருப்பட மாட்ட உருப்படவே மாட்ட🤦‍♀",
    "போ நீ போ 🚶‍♂",
    "ஏண்டா நாயா அடிக்கிற நாயே🐶",
    "டேய் நீ நல்லா இருக்க மாட்டடா நல்லாவே இருக்க மாட்டடா நாசமா போனவன்😑🤧",
    "இது எல்லாம் ஒரு பொழப்பு 🥵 போய் பிச்சை எடு போ",
    "அடிங்கு ஓடி போ நாயே! 🐕",
    "அடப்பாவி சண்டாளா நீயா டா என்னை கலாய்க்க வந்த🤧",
    "அடப்பாவி சண்டாளா நீயா டா என்னை கலாய்க்க வந்த🤧",
    "ஏன்டா அறிவுகெட்டவனே அறிவு இருக்கா உனக்கு மடப்பயலே முட்டா பயலே சோத்தை திங்கிறியா இல்ல சோத்தை விட்டுட்டு லட்டியை திங்கிறியா டா😂😂🤣🤣",
    "ஏன்டா அறிவுகெட்டவனே அறிவு இருக்கா உனக்கு மடப்பயலே முட்டா பயலே சோத்தை திங்கிறியா இல்ல சோத்தை விட்டுட்டு லட்டியை திங்கிறியா டா😂😂🤣🤣",
    "ஏண்டா நாயா அடிக்கிற நாயே🐶",
    "என்னப்பா உனக்கு பிரச்சன? 😣",
    "டேய் இந்த எகத்தாலமெல்லாம் என்கிட்டே வெச்சிக்காதா",
    "வாய்ப்பில்ல ராஜா.",
    "மூடிட்டு போடா வெண்ண! 😂",
    "போடா 🦊 நரி",
    "டேய் எனக்கு வெறி வர்றதுக்குள்ள இங்கிருந்து போய்டுடா😡",
    "ரத்தம் கக்கி சாவு 🙊",
    "என்ன Look-உ அப்படியே கண்ண புடுங்கி தின்னுபுடுவேன் மொகரைய பாரு மொகரைய என்ன என்னாடா என்னா😏.",
    "டேய் டேய் மூஞ்சியும் மொகரையும் பாரு🤯",
    "நல்லவர்களை நம்புங்கள்",
    "இறப்பதற்கு வாழ்க.",
    "இஞ்சி தின்ன கொரங்கு மாறி இருக்க 🐵",
    "பொண்ண பெக்க சொன்னா பொறுக்கிய பெத்துவிட்டுருக்காய்ங்க!😂😒",
    "அடிங்கு ஓடி போ நாயே! 🐕",
    "பிசாசுக்கு பொறந்த பிசாசே👻",
    "மூடிட்டு போடா வெண்ண! 😂",
    "அறிவு கெட்ட நாதாரி😤",
    "டேய் எனக்கு வெறி வர்றதுக்குள்ள இங்கிருந்து போய்டுடா😡",
    "பன்னிக்குட்டி எல்லாம் பஞ்சு டயலாக் பேசுதடா🤯",
    "நீ மங்குனி அமைச்சர் என்பதை மணிக்கு ஒருமுறை நிரூபித்துக் கொண்டே இருக்கிறாய்! 😂",
    "ஒரு பாவி மட்டுமே",
    "சென்று வாருங்கள்🥰",
    "நீங்கள் பார்த்த பிரச்சனைகள் யாருக்கும் தெரியாது",
    "மௌனமான மரணம் ஒன்று உயிரை கொண்டு போனதே உயரமான கனவு இன்று தரையில் வீழ்ந்து போனதே💔",
    "நீங்கள் திரும்ப வந்தால் மீண்டும் வரவேற்க காத்திருப்பேன்🥳",
    "சென்று வாருங்கள்🥰",
    "வெளிய போங்கடா அயோக்கிய ராஸ்கல்களா!😏",
    "வெளியே செல்",
    "கனவே கனவே கலைவதேனோ கணங்கள் ரணமாய் கரைவதேனோ நினைவே நினைவே அரைவதேனோ எனது உலகம் உடைவதேனோ💔",
]
# Line 111 to 152 are references from https://bindingofisaac.fandom.com/wiki/Fortune_Telling_Machine


class Welcome(BASE):
    __tablename__ = "welcome_pref"
    chat_id = Column(String(14), primary_key=True)
    should_welcome = Column(Boolean, default=True)
    should_goodbye = Column(Boolean, default=True)
    custom_content = Column(UnicodeText, default=None)

    custom_welcome = Column(
        UnicodeText, default=random.choice(DEFAULT_WELCOME_MESSAGES)
    )
    welcome_type = Column(Integer, default=Types.TEXT.value)

    custom_leave = Column(UnicodeText, default=random.choice(DEFAULT_GOODBYE_MESSAGES))
    leave_type = Column(Integer, default=Types.TEXT.value)

    clean_welcome = Column(BigInteger)

    def __init__(self, chat_id, should_welcome=True, should_goodbye=True):
        self.chat_id = chat_id
        self.should_welcome = should_welcome
        self.should_goodbye = should_goodbye

    def __repr__(self):
        return "<Chat {} should Welcome new users: {}>".format(
            self.chat_id, self.should_welcome
        )


class WelcomeButtons(BASE):
    __tablename__ = "welcome_urls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(String(14), primary_key=True)
    name = Column(UnicodeText, nullable=False)
    url = Column(UnicodeText, nullable=False)
    same_line = Column(Boolean, default=False)

    def __init__(self, chat_id, name, url, same_line=False):
        self.chat_id = str(chat_id)
        self.name = name
        self.url = url
        self.same_line = same_line


class GoodbyeButtons(BASE):
    __tablename__ = "leave_urls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(String(14), primary_key=True)
    name = Column(UnicodeText, nullable=False)
    url = Column(UnicodeText, nullable=False)
    same_line = Column(Boolean, default=False)

    def __init__(self, chat_id, name, url, same_line=False):
        self.chat_id = str(chat_id)
        self.name = name
        self.url = url
        self.same_line = same_line


class WelcomeMute(BASE):
    __tablename__ = "welcome_mutes"
    chat_id = Column(String(14), primary_key=True)
    welcomemutes = Column(UnicodeText, default=False)

    def __init__(self, chat_id, welcomemutes):
        self.chat_id = str(chat_id)  # ensure string
        self.welcomemutes = welcomemutes


class WelcomeMuteUsers(BASE):
    __tablename__ = "human_checks"
    user_id = Column(Integer, primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    human_check = Column(Boolean)

    def __init__(self, user_id, chat_id, human_check):
        self.user_id = user_id  # ensure string
        self.chat_id = str(chat_id)
        self.human_check = human_check


class CleanServiceSetting(BASE):
    __tablename__ = "clean_service"
    chat_id = Column(String(14), primary_key=True)
    clean_service = Column(Boolean, default=True)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)

    def __repr__(self):
        return "<Chat used clean service ({})>".format(self.chat_id)


Welcome.__table__.create(checkfirst=True)
WelcomeButtons.__table__.create(checkfirst=True)
GoodbyeButtons.__table__.create(checkfirst=True)
WelcomeMute.__table__.create(checkfirst=True)
WelcomeMuteUsers.__table__.create(checkfirst=True)
CleanServiceSetting.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()
WELC_BTN_LOCK = threading.RLock()
LEAVE_BTN_LOCK = threading.RLock()
WM_LOCK = threading.RLock()
CS_LOCK = threading.RLock()


def welcome_mutes(chat_id):
    try:
        welcomemutes = SESSION.query(WelcomeMute).get(str(chat_id))
        if welcomemutes:
            return welcomemutes.welcomemutes
        return False
    finally:
        SESSION.close()


def set_welcome_mutes(chat_id, welcomemutes):
    with WM_LOCK:
        prev = SESSION.query(WelcomeMute).get((str(chat_id)))
        if prev:
            SESSION.delete(prev)
        welcome_m = WelcomeMute(str(chat_id), welcomemutes)
        SESSION.add(welcome_m)
        SESSION.commit()


def set_human_checks(user_id, chat_id):
    with INSERTION_LOCK:
        human_check = SESSION.query(WelcomeMuteUsers).get((user_id, str(chat_id)))
        if not human_check:
            human_check = WelcomeMuteUsers(user_id, str(chat_id), True)

        else:
            human_check.human_check = True

        SESSION.add(human_check)
        SESSION.commit()

        return human_check


def get_human_checks(user_id, chat_id):
    try:
        human_check = SESSION.query(WelcomeMuteUsers).get((user_id, str(chat_id)))
        if not human_check:
            return None
        human_check = human_check.human_check
        return human_check
    finally:
        SESSION.close()


def get_welc_mutes_pref(chat_id):
    welcomemutes = SESSION.query(WelcomeMute).get(str(chat_id))
    SESSION.close()

    if welcomemutes:
        return welcomemutes.welcomemutes

    return False


def get_welc_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()
    if welc:
        return (
            welc.should_welcome,
            welc.custom_welcome,
            welc.custom_content,
            welc.welcome_type,
        )

    else:
        # Welcome by default.
        return True, DEFAULT_WELCOME, None, Types.TEXT


def get_gdbye_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()
    if welc:
        return welc.should_goodbye, welc.custom_leave, welc.leave_type
    else:
        # Welcome by default.
        return True, DEFAULT_GOODBYE, Types.TEXT


def set_clean_welcome(chat_id, clean_welcome):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id))

        curr.clean_welcome = int(clean_welcome)

        SESSION.add(curr)
        SESSION.commit()


def get_clean_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()

    if welc:
        return welc.clean_welcome

    return False


def set_welc_preference(chat_id, should_welcome):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id), should_welcome=should_welcome)
        else:
            curr.should_welcome = should_welcome

        SESSION.add(curr)
        SESSION.commit()


def set_gdbye_preference(chat_id, should_goodbye):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id), should_goodbye=should_goodbye)
        else:
            curr.should_goodbye = should_goodbye

        SESSION.add(curr)
        SESSION.commit()


def set_custom_welcome(
    chat_id, custom_content, custom_welcome, welcome_type, buttons=None
):
    if buttons is None:
        buttons = []

    with INSERTION_LOCK:
        welcome_settings = SESSION.query(Welcome).get(str(chat_id))
        if not welcome_settings:
            welcome_settings = Welcome(str(chat_id), True)

        if custom_welcome or custom_content:
            welcome_settings.custom_content = custom_content
            welcome_settings.custom_welcome = custom_welcome
            welcome_settings.welcome_type = welcome_type.value

        else:
            welcome_settings.custom_welcome = DEFAULT_WELCOME
            welcome_settings.welcome_type = Types.TEXT.value

        SESSION.add(welcome_settings)

        with WELC_BTN_LOCK:
            prev_buttons = (
                SESSION.query(WelcomeButtons)
                .filter(WelcomeButtons.chat_id == str(chat_id))
                .all()
            )
            for btn in prev_buttons:
                SESSION.delete(btn)

            for b_name, url, same_line in buttons:
                button = WelcomeButtons(chat_id, b_name, url, same_line)
                SESSION.add(button)

        SESSION.commit()


def get_custom_welcome(chat_id):
    welcome_settings = SESSION.query(Welcome).get(str(chat_id))
    ret = DEFAULT_WELCOME
    if welcome_settings and welcome_settings.custom_welcome:
        ret = welcome_settings.custom_welcome

    SESSION.close()
    return ret


def set_custom_gdbye(chat_id, custom_goodbye, goodbye_type, buttons=None):
    if buttons is None:
        buttons = []

    with INSERTION_LOCK:
        welcome_settings = SESSION.query(Welcome).get(str(chat_id))
        if not welcome_settings:
            welcome_settings = Welcome(str(chat_id), True)

        if custom_goodbye:
            welcome_settings.custom_leave = custom_goodbye
            welcome_settings.leave_type = goodbye_type.value

        else:
            welcome_settings.custom_leave = DEFAULT_GOODBYE
            welcome_settings.leave_type = Types.TEXT.value

        SESSION.add(welcome_settings)

        with LEAVE_BTN_LOCK:
            prev_buttons = (
                SESSION.query(GoodbyeButtons)
                .filter(GoodbyeButtons.chat_id == str(chat_id))
                .all()
            )
            for btn in prev_buttons:
                SESSION.delete(btn)

            for b_name, url, same_line in buttons:
                button = GoodbyeButtons(chat_id, b_name, url, same_line)
                SESSION.add(button)

        SESSION.commit()


def get_custom_gdbye(chat_id):
    welcome_settings = SESSION.query(Welcome).get(str(chat_id))
    ret = DEFAULT_GOODBYE
    if welcome_settings and welcome_settings.custom_leave:
        ret = welcome_settings.custom_leave

    SESSION.close()
    return ret


def get_welc_buttons(chat_id):
    try:
        return (
            SESSION.query(WelcomeButtons)
            .filter(WelcomeButtons.chat_id == str(chat_id))
            .order_by(WelcomeButtons.id)
            .all()
        )
    finally:
        SESSION.close()


def get_gdbye_buttons(chat_id):
    try:
        return (
            SESSION.query(GoodbyeButtons)
            .filter(GoodbyeButtons.chat_id == str(chat_id))
            .order_by(GoodbyeButtons.id)
            .all()
        )
    finally:
        SESSION.close()


def clean_service(chat_id: Union[str, int]) -> bool:
    try:
        chat_setting = SESSION.query(CleanServiceSetting).get(str(chat_id))
        if chat_setting:
            return chat_setting.clean_service
        return False
    finally:
        SESSION.close()


def set_clean_service(chat_id: Union[int, str], setting: bool):
    with CS_LOCK:
        chat_setting = SESSION.query(CleanServiceSetting).get(str(chat_id))
        if not chat_setting:
            chat_setting = CleanServiceSetting(chat_id)

        chat_setting.clean_service = setting
        SESSION.add(chat_setting)
        SESSION.commit()


def migrate_chat(old_chat_id, new_chat_id):
    with INSERTION_LOCK:
        chat = SESSION.query(Welcome).get(str(old_chat_id))
        if chat:
            chat.chat_id = str(new_chat_id)

        with WELC_BTN_LOCK:
            chat_buttons = (
                SESSION.query(WelcomeButtons)
                .filter(WelcomeButtons.chat_id == str(old_chat_id))
                .all()
            )
            for btn in chat_buttons:
                btn.chat_id = str(new_chat_id)

        with LEAVE_BTN_LOCK:
            chat_buttons = (
                SESSION.query(GoodbyeButtons)
                .filter(GoodbyeButtons.chat_id == str(old_chat_id))
                .all()
            )
            for btn in chat_buttons:
                btn.chat_id = str(new_chat_id)

        SESSION.commit()
