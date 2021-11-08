# lmao
import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from TGNRobot import dispatcher
from TGNRobot.modules.disable import DisableAbleCommandHandler
from TGNRobot.modules.helper_funcs.chat_status import is_user_admin, user_admin
from TGNRobot.modules.helper_funcs.extraction import extract_user

#sleep how many times after each edit in 'lol' 
EDIT_SLEEP = 1
#edit how many times in 'lol' 
EDIT_TIMES = 10



lol_ani = [ 
          
     "Palla odachi kaila kuduthuruven🥱",
    "Hair ah pudungu🤭",
    "Po di dog🤣",
    "Railway station la suthuravan ella inga vandhurukane🤢",
    "Vaaya moodu da korangu🤫",
    "Nandri ketta naaye😡",
    "Manda bathiram",
    "Ennada ithu mooji🤣 Sethula mukkuna mathiri iruku🤣",
    "Vayila nalla varuthu🤬 Ean thalaivan @THE_BOSS_OF_TELEGRAM kaga tha amaithiya iruke🥱",
    "Nenga moodetu irukalam nu computer solluthu sir😑",
    "Po da 8+1 🤣 8 ah yu 1 ah yu setha 81 pa 🤣",
    "Yar da avan /abuse /abuse nu pottu uyira vanguran😒",
    "Dai unaya na kutralathula pathene🤔 ovvoru trees ka thavi thavi pova🤭 unaku inga enna vela 🤣",
    "Na unaya eppudi thitunalu unayala hair ah kooda pudunga mudiyathu🤣🤣🤣",
    "Moonja odaichi kaila koduthuruve pathuko🤫",
    "Enga team no way kitta mothi par da mudinja🤣, unayala hair ah kooda pudunga mudiyathu🤭,only for haters😒",
    "Ivan evan da mutta paiyan🤢",
    "yenaya ethavathu un grp la add panni admin podu na soldre😒",
    "Yar da ivan loosu mathiri olaruran",
    "My thambi veluma🤣, Apd illa pa 😳 my thambi football player atha coaching ku veluma nu kete 🤣",
    "Ivan yarrda pombala poruki ah irukan🥱",
    "Po di anguttu🤬",
    "Summa summa kadup hair ah eatha koodathu🤬",
    "Ena sound vidura 🥱 Vaya odachiruve😡",
    "Enaku /abuse nu command pottavar periya mannar parambora🤢 Ivar yarayachu thitta sonan na thitaluma 🤣🥱",
    "Dai ne ena avalo periya kinguh ah😡,Iru nalaki unaku sangu tha 🥱",
    "Ean area la nan than da raaja .👿",
    "Ippa ean da kadharura🤣",
    "Ithu 18+ Pa🚫 . ellaru nalla potengala🤣 ,Eppa Eppa nenga high level thinking ku ella pogathenga😳, Na vote ah sone🤣",
    "Moonjum aalum mandayayum paaru🤣",
    "Na enna unaku velakarana ne /abuse nu potta na soldrathuku😡",
    "Po da baadu🥱",
    "Thambi enna pa unaku ippa prechana🙄",
    "Enna da landha🥱",
    "Sanda na sollu sirappa senjiruvom🥱",
    "Tharai la ooduthu paambu ne apparama poi ****🤭 paaru nu solla vandhen athu kulla antha symbol came 🤣🤣",
    "Kuttralathula iruka vendiyavangala inga vandhu namma uyira vanguranga",
    "Po da kundu papa🤣🤭",
    "Yar da enaya koopitathu🙄",
    "Po da uncle ooda wife🤣",
    "I am tired , ipa na yarayu thittura nalamai la illa pa 🥱",
    "Kanna nondi eduthuruve 👀",
    "Seruppu keela iruku , innum oru sec la ne mela irupa🤣",
    "Vanga grandma👵",
    "Po da panni.... Next rhyming ah na pesuna avan odeeruvan🤣",
    "Pongada nengalu unga /tabuse um😒"
]



          
@run_async
def abuse(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('....')
    for x in range(EDIT_TIMES):
        msg.edit_text(lol_ani[x%10],parse_mode='markdown')
        time.sleep(2)
    msg.edit_text('.. THEN ADD ME TO YOUR GROUP*👻',parse_mode='markdown')
          
          


          
          

__help__ = """
➥ /abuse abuse in Tamil
"""


lel =DisableAbleCommandHandler("tabuse", tabuse)


dispatcher.add_handler(lel)



__mod_name__ = "Animation"
__command_list__ = ["tabuse"]
__handlers__ = [lel]
