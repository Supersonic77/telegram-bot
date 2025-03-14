
# ALL Imports
import os  
import random
import telebot
from telebot import types
from decouple import config
import time
import re
import json
import functools
import base64


bot= telebot.TeleBot('5824801243:AAGbkxSCHcuG9yRfmrEbdSOWml8CQrwyUN8')
Sound_File_Location="C:\\Users\\Engmu\\OneDrive\\Desktop\\audio bot\\"
Pictures_File_Location = "C:\\Users\\Engmu\\OneDrive\\Desktop\\ALL PARTS\\"

Protect_Content_Switch_Fuses =None  #  الفيوزات
Protect_Content_Switch_G     =None  #  مشاكل شائعة
Protect_Content_Switch_R     =None  #  الاستدعائات
Protect_Content_Switch_H     =None  #  الاعدادات والبرمجة
Protect_Content_Switch_W     =True  #  مراجع وكتيبات
Protect_Content_Switch_A     =True  #  ارقام ومواقع محلات القطع
Protect_Content_Switch_O     =True  #  توصيات الورش
Protect_Content_Switch_K     =True  #  ارقام واسعار وصور القطع 
Protect_Content_Switch_P     =True  #  تشخيص الاعطال 
         # (متاح حتى الان)          #  بحث المواصفات B    +   الصيانات الدورية   +  الكميات والمقاسات
Protect_Content_Switch       =True  # كل بقية الاكواد العشوائية  و خيارات البوت الرئيسية  الردد الرئيسي طالما كان الجواب فيه ولم تحذف الرساله
MY_ID=5308309193
trigger_BOT={"بوت"}
Blocked=[   ]   
Main_Group_ID= -1001375465311
Test_Group_ID= -4793174484
Allowed_ID_to_use= [ Test_Group_ID ]

#_________________________________  لجعل كل شخص له خيارات خاصة لاتعمل الا له________________________________________________xxxx
# Initialize ownership dictionary
message_user_map = {}  
user_keyboard_ownership = {}  # Tracks {(chat_id, message_id): user_id}
def wrap_bot_method(original_method):
    def wrapped(chat_id, *args, **kwargs):
        # Send the message
        sent_message = original_method(chat_id, *args, **kwargs)
        # Check if it's a reply and has a keyboard
        reply_to_id = kwargs.get('reply_to_message_id')
        reply_markup = kwargs.get('reply_markup')
        if reply_to_id and reply_markup:
            # Get user_id from the message_user_map
            user_id = message_user_map.get((chat_id, reply_to_id), None)
            if user_id:
                user_keyboard_ownership[(sent_message.chat.id, sent_message.message_id)] = user_id
        return sent_message
    return wrapped 

# Override ALL bot methods you use 
bot.send_voice = wrap_bot_method(bot.send_voice)
bot.send_photo = wrap_bot_method(bot.send_photo)
bot.send_message = wrap_bot_method(bot.send_message)
bot.reply_to = wrap_bot_method(bot.reply_to)
bot.edit_message_reply_markup = wrap_bot_method(bot.edit_message_reply_markup)
#bot.edit_message_caption = wrap_bot_method(bot.edit_message_caption)
#_________________________________  لجعل كل شخص له خيارات خاصة لاتعمل الا له_______________________________________________

#All  Sound Files
#fits ALL
wait_replies   = [ "Searching_5","Searching_5","Searching_5","Searching_5", "Searching_14", "Searching_15", "Searching_16",  "Searching_23", "Searching_31" ,     "Searching_41","Searching_41","Searching_41","Searching_41","Searching_41", "Searching_50" , "Searching_54", "Searching_50" , "Searching_54" ]
#خاص ومناسب لقسم A
wait_replies_A = wait_replies  + ["wait_replies_A_1","wait_replies_A_3","wait_replies_A_4","wait_replies_A_5","wait_replies_A_6","wait_replies_A_7","wait_replies_A_8","wait_replies_A_1","wait_replies_A_3","wait_replies_A_4","wait_replies_A_5","wait_replies_A_6","wait_replies_A_7","wait_replies_A_8" ]
#خاص ومناسب لقسم B
wait_replies_B = wait_replies_C = wait_replies_D = wait_replies_E = wait_replies_F = wait_replies_G = wait_replies_H = wait_replies_J = wait_replies_K = wait_replies_L = wait_replies_N = wait_replies_O = wait_replies_R = wait_replies

# رد الإستقبال وتحديد المطلوب
Click_Start_replies=["Ring_Tone1", "Ring_Tone1"]
First_Bot_replies  =["YesSir1", "YesSir2", "YesSir3", "YesSir3_1", "YesSir4", "YesSir6", "YesSir7", "YesSir9", "YesSir9_1", "YesSir10", "YesSir11", "YesSir13", "YesSir14", "YesSir14_1", "YesSir15", "YesSir15_1", "YesSir16", "YesSir17"  , "YesSir18" , "YesSir19", "YesSir20", "YesSir21", "YesSir22", "YesSir23", "YesSir24", "YesSir25", "YesSir26", "YesSir27", "YesSir28", "YesSir3_1","YesSir2","YesSir3","YesSir4","YesSir13"]
Pick_any_Subject   =["YesSir3","YesSir6","YesSir7","YesSir9","YesSir9_1","YesSir10","YesSir11","YesSir13","YesSir14","YesSir14_1","YesSir15","YesSir15_1","YesSir16","YesSir19","YesSir25","YesSir27"]
pick_from_list     =["YesSir3_1","YesSir15_1","YesSir18" ,"YesSir21","YesSir22","YesSir23","YesSir24","YesSir26","YesSir28"]
Model_Eng          =["Model_Eng_1", "Model_Eng_2", "Model_Eng_3", "Model_Eng_4", "Model_Eng_5", "Model_Eng_6", "Model_Eng_7", "Model_Eng_8", "Model_Eng_9", "Model_Eng_10", "Model_Eng_11", "Model_Eng_12", "Model_Eng_13", "Model_Eng_9","Model_Eng_10",      "YesSir3_1","YesSir18","YesSir23","YesSir24" ]
Model_Wheel        =["Model_Wheel_1",  "Model_Wheel_2",  "Model_Wheel_3",  "Model_Wheel_4",  "Model_Wheel_5",  "Model_Wheel_6",  "Model_Wheel_7",  "Model_Wheel_8",  "Model_Wheel_6",  "Model_Wheel_7",  "Model_Wheel_8","Model_Wheel_8",                      "YesSir3_1","YesSir18","YesSir23","YesSir24" ]
pick_from_list_H   =["YesSir4","YesSir11","YesSir15_1","YesSir17","YesSir20"]
wait_replies_Z     =["Ring_Tone1"] 

# الرد الأخير بعد البحث
All_Answer_replies=["Results4" ,"Results5"  ,"Results47","Results4" ,"Results5"  ,"Results47","Results10" ,"Results11" ,"Results12" ,"Results13" ,"Results14" ,"Results17" ,"Results18","Results21" ,"Results22" ,"Results23"  ,"Results26" ,"Results27" ,"Results28" ,"Results29" ,"Results26" ,"Results27" ,"Results28" ,"Results29","Results30","Results31","Results41","Results42","Results46"]
Answer_Fits_All   =["Results12","Results17","Results23","Results21","Results27","Results46"]
# "هذا الي طلع معي"
Answer_found_This = ["Results4","Results11" ,"Results26","Results28" ,"Results29" ,"Results30"]
Answer_AS_Lnik    = ["Link_Result1" , "Link_Result2" , "Link_Result3" , "Link_Result4" , "Link_Result5" , "Link_Result6" , "Link_Result7"  , "Link_Result9" , "Link_Result10" , "Link_Result11" , "Link_Result12" , "Link_Result13" , "Link_Result14" ,  "Link_Result16" ,  "Link_Result25" , "Link_Result26" , "Link_Result27" , "Link_Result28" , "Link_Result29" , "Link_Result30" , "Link_Result31"]

Answer_replies_A  = Answer_Fits_All  + ["Answer_replies_A_2_2", "Answer_replies_A_3", "Answer_replies_A_4", "Answer_replies_A_5", "Answer_replies_A_6", "Answer_replies_A_7","Answer_replies_A_2_2", "Answer_replies_A_3", "Answer_replies_A_4", "Answer_replies_A_5", "Answer_replies_A_6", "Answer_replies_A_7","Answer_replies_A_8","Answer_replies_A_9", "Answer_replies_A_10", "Answer_replies_A_11", "Answer_replies_A_12", "Answer_replies_A_13", "Answer_replies_A_14" ]
Answer_replies_A1 = Answer_replies_A + ["store_RYD", "store_RYD","store_RYD","store_RYD","store_RYD","store_RYD","store_RYD","store_RYD" , "store_RYD","store_RYD","store_RYD","store_RYD","store_RYD","store_RYD","store_RYD" , "store_RYD","store_RYD","store_RYD","store_RYD","store_RYD","store_RYD"]
Answer_replies_A2 = Answer_replies_A + ["store_JDH", "store_JDH", "store_JDH", "store_JDH", "store_JDH", "store_JDH", "store_JDH", "store_JDH" , "store_JDH", "store_JDH", "store_JDH", "store_JDH", "store_JDH", "store_JDH" , "store_JDH", "store_JDH", "store_JDH", "store_JDH", "store_JDH", "store_JDH"]
Answer_replies_A3 = Answer_replies_A + ["store_MKH", "store_MKH", "store_MKH", "store_MKH", "store_MKH", "store_MKH", "store_MKH", "store_MKH" , "store_MKH", "store_MKH", "store_MKH", "store_MKH", "store_MKH", "store_MKH" , "store_MKH", "store_MKH", "store_MKH", "store_MKH", "store_MKH", "store_MKH"]
Answer_replies_A4 = Answer_replies_A + ["store_MDN", "store_MDN", "store_MDN", "store_MDN", "store_MDN", "store_MDN", "store_MDN", "store_MDN" , "store_MDN", "store_MDN", "store_MDN", "store_MDN", "store_MDN", "store_MDN" , "store_MDN", "store_MDN", "store_MDN", "store_MDN", "store_MDN", "store_MDN"]
Answer_replies_A5 = Answer_replies_A + ["store_DMM", "store_DMM", "store_DMM", "store_DMM", "store_DMM", "store_DMM", "store_DMM", "store_DMM" , "store_DMM", "store_DMM", "store_DMM", "store_DMM", "store_DMM", "store_DMM" , "store_DMM", "store_DMM", "store_DMM", "store_DMM", "store_DMM", "store_DMM"]
Answer_replies_A6 = Answer_replies_A + ["store_YUN", "store_YUN", "store_YUN", "store_YUN", "store_YUN", "store_YUN", "store_YUN", "store_YUN" , "store_YUN", "store_YUN", "store_YUN", "store_YUN", "store_YUN", "store_YUN" , "store_YUN", "store_YUN", "store_YUN", "store_YUN", "store_YUN", "store_YUN"]
Answer_replies_A7 = Answer_replies_A + ["store_TBK", "store_TBK", "store_TBK", "store_TBK", "store_TBK", "store_TBK", "store_TBK", "store_TBK" , "store_TBK", "store_TBK", "store_TBK", "store_TBK", "store_TBK", "store_TBK" , "store_TBK", "store_TBK", "store_TBK", "store_TBK", "store_TBK", "store_TBK"]
Answer_replies_A8 = Answer_replies_A + ["store_ABH", "store_ABH", "store_ABH", "store_ABH", "store_ABH", "store_ABH", "store_ABH", "store_ABH" , "store_ABH", "store_ABH", "store_ABH", "store_ABH", "store_ABH", "store_ABH" , "store_ABH", "store_ABH", "store_ABH", "store_ABH", "store_ABH", "store_ABH"]
Answer_replies_A9 = Answer_replies_A + ["store_TYF", "store_TYF", "store_TYF", "store_TYF", "store_TYF", "store_TYF", "store_TYF", "store_TYF" , "store_TYF", "store_TYF", "store_TYF", "store_TYF", "store_TYF", "store_TYF" , "store_TYF", "store_TYF", "store_TYF", "store_TYF", "store_TYF", "store_TYF"]
Answer_replies_A10= Answer_replies_A + ["store_NJR", "store_NJR", "store_NJR", "store_NJR", "store_NJR", "store_NJR", "store_NJR", "store_NJR" , "store_NJR", "store_NJR", "store_NJR", "store_NJR", "store_NJR", "store_NJR" , "store_NJR", "store_NJR", "store_NJR", "store_NJR", "store_NJR", "store_NJR"]
Answer_replies_A11= Answer_replies_A + ["store_QSM", "store_QSM", "store_QSM", "store_QSM", "store_QSM", "store_QSM", "store_QSM", "store_QSM" , "store_QSM", "store_QSM", "store_QSM", "store_QSM", "store_QSM", "store_QSM" , "store_QSM", "store_QSM", "store_QSM", "store_QSM", "store_QSM", "store_QSM"]

Answer_replies_B = ["VINN"]
Answer_replies_C = Answer_Fits_All      + Answer_found_This                      # + []
Answer_replies_D = All_Answer_replies   + Answer_Fits_All                                         # + [] 
Answer_replies_E = Answer_Fits_All      + Answer_found_This                      # + [] 
Answer_replies_F = All_Answer_replies   + Answer_Fits_All                                     # + []
Answer_replies_G = Answer_Fits_All      + Answer_found_This   + Answer_AS_Lnik     + ["Results_G1" ,"Results_G2" ,"Results_G3" ,"Results_G4" ,"Results_G5" ,"Results_G6" ,"Results_G8" ,"Results_G9","Results_G10"  ,"Results_G11" ,"Results_G12" ,"Results_G13" ,"Results_G14" ,"Results_G15"  ,"Results_G16" ,"Results_G17" ,"Results_G18" ,"Results_G19" ,"Results_G20"  ,"Results_G21" ,"Results_G23","Results_G25"    ]
Answer_replies_H = Answer_Fits_All      + Answer_found_This   + Answer_AS_Lnik   # + []
Answer_replies_J = All_Answer_replies   + Answer_Fits_All
Answer_replies_K = Answer_Fits_All      + Answer_AS_Lnik   + Answer_Fits_All
Answer_replies_L = All_Answer_replies   + Answer_Fits_All
Answer_replies_N = Answer_Fits_All 
Answer_replies_O = Answer_Fits_All      + Answer_found_This + ["Answer_replies_A_7" ,"Answer_replies_A_8","Answer_replies_A_9", "Answer_replies_A_10", "Answer_replies_A_11", "Answer_replies_A_12", "Answer_replies_A_13", "Answer_replies_A_14","Answer_replies_A_7" ,"Answer_replies_A_8","Answer_replies_A_9", "Answer_replies_A_10", "Answer_replies_A_11", "Answer_replies_A_12", "Answer_replies_A_13", "Answer_replies_A_14","Answer_replies_A_7","Answer_replies_A_8","Answer_replies_A_9", "Answer_replies_A_10", "Answer_replies_A_11", "Answer_replies_A_12", "Answer_replies_A_13", "Answer_replies_A_14","Answer_replies_A_7","Answer_replies_A_8","Answer_replies_A_9", "Answer_replies_A_10", "Answer_replies_A_11", "Answer_replies_A_12", "Answer_replies_A_13", "Answer_replies_A_14" ]
Answer_replies_R = Answer_Fits_All      + Answer_found_This   + Answer_AS_Lnik
Answer_replies_T = Answer_Fits_All      + Answer_found_This 
Eng_Amount_2013  = [ "2013+_eng_oil_1", "2013+_eng_oil_2","2013+_eng_oil_3","2013+_eng_oil_4","2013+_eng_oil_5","2013+_eng_oil_6","2013+_eng_oil_7", "2013+_eng_oil_2","2013+_eng_oil_3","2013+_eng_oil_4","2013+_eng_oil_5","2013+_eng_oil_6","2013+_eng_oil_2","2013+_eng_oil_3", "2013+_eng_oil_4","2013+_eng_oil_5" ,"2013+_eng_oil_6"]
Eng_Amount_2012  = [ "2012_eng_oil_1", "2012_eng_oil_2",  "2012_eng_oil_3", "2012_eng_oil_4" ]
Aft_Amount_2013  = ["Aft_1",   "Aft_2","Aft_3","Aft_4","Aft_5","Aft_3","Aft_3","Aft_4","Aft_5" ]
Aft_Amount_2012  = ["Aftt_2012_1",  "Aftt_2012_2"  ,  "Aftt_2012_2",  "Aftt_2012_2"]
Reply_Welcome    =["Wlcm1", "Wlcm2"]
parts_prices_replies=[ ]

#________________________________________________________________________________________________________

# All DEfines 
#لحل مشكله الروابط التي تحتوي على underscore 

def escape_links(link_list):
    """Return links without escaping underscores"""
    return link_list  # Remove the underscore replacement

BOT_ID=5824801243 ; last_time = 0 ; last_Click= 0 ;sleep_time1=25;   sleep_time2=20;  sleep_time3=15;  sleep_time4=10 ;  sleep_time5=5
Signature= f"\n\n @ _SuperSyn_"  ; Put_At_End_Of_Message=""
Short_Pause_BeforeAnotherReply=5 ; Long_Pause_BeforeAnotherReply=120
Main_Return="العودة للقائمة الرئيسية" ; Exit="🔚الخروج من القائمة"
K0="فيوجن 2013-2019"  ;K00="فيوجن 2009-2012" 
X ="لم يكتمل بعد..مازلت أتعلم\U0001F643"
IDK= "شاركو معلوماتكم بالقروب لأضيفها"
Q="Diagnosis"                            ;Q1="حرارة المحرك"      ; Q1A="الحرارة منخفضة"   ; Q1B="الحرارة مرتفعة"  ; Q1C="كم الحرارة الطبيعية للمحرك ؟"   ; Q1D="."    ; Q1E="."                ; Q2="مكيف السيارة"   ; Q2A="دفع الهواء ضعيف"    ; Q2B="المكيف حار عند وقوف السياره"     ; Q2C="المكيف حار من الجهتين طوال الوقت"     ; Q2D="جهه الراكب أبرد من جهه السائق"     ; Q2E="المكيف يشتغل لوحدة"     ; Q2F="الكومبروسر يفصل"     ; Q2G="."     ; Q2H="."                     ; Q3="مراوح رديتر\n2013-2019"  
U="Specs"                    ;U1="المكينة" ;   U2="القير" ;   U3="الفرامل"  ;   U4="بطارية - مولد" ;   U5="نظام التكييف" ;   U6="نظام التبرييد" ;   U7="نظام الوقود" ;   U8="نظام التشغيل" ;   U9="نظام التعليق" ;   U10="بواجي"    ;  U11="Lug nut torqe"   ; U12="Relays - testing"
V= "شراء إكسسوارات 2014-2019"              ;V1=".." ;   V2=".." ;   V3=".." ;   V4=".." ;   V5=".." ;   V6=".." ;   V7=".." ;   V8=".." ;   V9=".." ;   V10=".."                    
W=""
Z= "حول البوت\U00002753"           ;Z1="مستوى البوت الخاص بك"   ;Z2="معلومات أكثر.." 

Pick_one_1=["\n\n❗️حدد المطلوب.." , "\n\n❗️إختار المطلوب..", "\n\n❗️حدد من القائمة..", "\n\n❗️حدد إلي بتسأل عنة..", "\n\n❗️حدد من الخيارات..", "\n\n❗️ هذي الخيارات.."]
Pick_City_1=["\n\n❗️حدد المدينة المطلوبة..", "\n\n❗️حدد المدينة.." , "\n\n❗️أي مدينة ؟" , "\n\n❗️عن أي مدينة نتكلم..", "\n\n❗️ إختار المدينة المطلوبة.." ,"\n\n❗️تمام.. في أي مدينة بالضبط؟"]
Pick_Engine_1=["\n\n❗️إختار حجم المحرك..", "\n\n❗️كم حجم المحرك..", "\n\n❗️كم سعة المحرك..", "\n\n❗️ عن أي حجم محرك نتكلم..", "\n\n❗️إختار أي محرك.." ]
Pick_model_1=["\n\n❗️إختار موديل السيارة..", "\n\n❗️ حدد موديل السيارة..", "\n\n❗️أي موديل بالضبط..", "\n\n❗️عن أي موديل نتكلم.." , "\n\n❗️إختار الموديل..", "\n\n❗️حدد موديل السيارة.." ]
Pick_wheel_size_1=["\n\n❗️كم مقاس الجنط..", "\n\n❗️ايش مقاس الجنط..", "\n\n❗️أي مقاس جنط بالضبط..", "\n\n❗️كم مقاس الجنط..", "\n\n❗️كم مقاس الجنط.." ]
Searching_Text_1=["✔️\n\nجاري البحث...🔍", "✔️\n\nجاري البحث...🔍", "✔️\n\nجاري البحث...🔍", "✔️\n\n ثواني...🔍" ]

#________________________________________________________________________________________________________

#BBBB
#💠بحث برقم الهيكل عن الموديل، سعة المكينة، الفئة، بلد المنشأ: bbbb
B = "بحث مواصفات الفيوجن"
trigger_B=["بوت Vin","vin بوت","بوت vln","بوت VIN","VIN بوت","بوت vin","","","","","","","","","","","","","","","" ]
REPLY_TEXT_VIN="لمعرفة معلومات المركبة مثل حجم المحرك والفئة وبلد المنشأ:\nإكتب رقم هيكل الفيوجن متبوعة ب VIN أو PIN\n\nمثال لموديلات 2013-2019...\nVIN 3FA6P0H78ER287852\n\nمثال لموديلات 2012-2009...\nPIN 3FA6P0H78ER287852"

#_________________________________________________________________________________________________________

#RRRR
#💠الإستدعائات:  RRRR
R = "إستدعائات"                              ;R1="رابط الإستدعائات"    ;R2="موديل 2014"   ;R3="موديل 2015"   ;R4="موديل 2016"   ;R5="موديل 2017"   ;R6="موديل 2018"
trigger_R  =["استدعا","إستدعا"]
trigger_R1 =["","","","","","","","","","","","","","","","","","","","","" ]
trigger_R2 =["","","","","","","","","","","","","","","","","","","","","" ]
trigger_R3 =["","","","","","","","","","","","","","","","","","","","","" ]
#_____________________________________________#


#💠 بحث موقع الفيوز: CCCC  
intro_fuse_location="\n إختار الفيوز الي تريد تبحث عنة"
Fuse_finder_reply="تم تحديد الموديل\U00002714\n تم تحديد الفيوز\U00002714"
Internal_fuse_box ="علبة الفيوز الداخلية"
External_fuse_box1="علبة الفيوز الخارجية"
External_fuse_box2="علبة الفيوز الخارجية. من الخلف"
Fuses_Return="العودة لقائمة الموديلات"



C = "بحث عن فيوز"                           ;C1="..2010.."  ;C2="..2011.."  ;C3="..2012.."    ;C4="..2014.."   ;C5="..2015.."     ;C6="..2016.."    ;C7="..2017.."    ;C8="..2018.."    ;C9="..2019.."    ;C10="..2020.."  
ClickC=["clickC", "clickC1" ,"clickC2" ,"clickC3" ,"clickC4" ,"clickC5" ,"clickC6" ,"clickC7" ,"clickC8" ,"clickC9",         "clickX1", "clickX2_84", "clickX4_79", "clickX5", "clickX10", "clickX11", "clickX12", "clickX16", "clickX22_33_12", "clickX40_56", "clickX41_48", "clickX46", "clickX47", "clickX68", "clickX70", "clickX74", "clickX83", "clickM1", "clickM3", "clickM5", "clickM10", "clickM12", "clickM16", "clickM18", "clickM24", "clickM25", "clickM26", "clickM29", "clickM30", "clickM32", "clickM33", "clickM35", "clickX42_58", "clickX54", "clickX40_50", "clickM24_2015",                      "clickN5_55" , "clickN9" , "clickN17" , "clickN22" , "clickN25_43" , "clickN28" , "clickN29" , "clickN31" , "clickN32" , "clickN35_52" , "clickN36" , "clickN41" , "clickN48" , "clickP1" , "clickP2" , "clickP4" , "clickP6" , "clickP7" , "clickP8" , "clickP9" , "clickP10" , "clickP12" , "clickP13" , "clickP14" , "clickP15" , "clickP17" , "clickP21" , "clickP22" , "clickP23" , "clickP24" , "clickP27" , "clickP32" , "clickP39" , "clickP41" , "clickP47" ]
trigger_C  =["الفيوز","فيوز","الفيوزات","فيوزات" ]
trigger_C1 =["موديل١٠","موديلات ١٠","موديل ١٠","موديلات١٠","موديل 2010","موديل2010","موديلات 2010","موديل 10","","فيوجن١٠","فيوجن ١٠","فيوجن ١٠","فيوجن ١٠","فيوجن2010","فيوجن 2010","فيوجن 10","فيوجن10","١٠", "10", "2010", "٢٠١٠"  ]
trigger_C2 =["موديل١١","موديلات ١١","موديل ١١","موديلات١١","موديل 2011","موديل2011","موديلات 2011","موديل 11","","فيوجن١١","فيوجن ١١","فيوجن ١١","فيوجن ١١","فيوجن2011","فيوجن 2011","فيوجن 11","فيوجن11","١١", "11", "2011", "٢٠١١"  ]
trigger_C3 =["موديل١٢","موديلات ١٢","موديل ١٢","موديلات١٢","موديل 2012","موديل2012","موديلات 2012","موديل 12","","فيوجن١٢","فيوجن ١٢","فيوجن ١٢","فيوجن ١٢","فيوجن2012","فيوجن 2012","فيوجن 12","فيوجن12","١٢", "12", "2012", "٢٠١٢"  ]
trigger_C4 =["موديل١٤","موديلات ١٤","موديل ١٤","موديلات١٤","موديل 2014","موديل2014","موديلات 2014","موديل 14","","فيوجن١٤","فيوجن ١٤","فيوجن ١٤","فيوجن ١٤","فيوجن2014","فيوجن 2014","فيوجن 14","فيوجن14","١٤", "14", "2014", "٢٠١٤"  ]
trigger_C5 =["موديل١٥","موديلات ١٥","موديل ١٥","موديلات١٥","موديل 2015","موديل2015","موديلات 2015","موديل 15","","فيوجن١٥","فيوجن ١٥","فيوجن ١٥","فيوجن ١٥","فيوجن2015","فيوجن 2015","فيوجن 15","فيوجن15","١٥", "15", "2015", "٢٠١٥"  ]
trigger_C6 =["موديل١٦","موديلات ١٦","موديل ١٦","موديلات١٦","موديل 2016","موديل2016","موديلات 2016","موديل 16","","فيوجن١٦","فيوجن ١٦","فيوجن ١٦","فيوجن ١٦","فيوجن2016","فيوجن 2016","فيوجن 16","فيوجن16","١٦", "16", "2016", "٢٠١٦"  ]
trigger_C7 =["موديل١٧","موديلات ١٧","موديل ١٧","موديلات١٧","موديل 2017","موديل2017","موديلات 2017","موديل 17","","فيوجن١٧","فيوجن ١٧","فيوجن ١٧","فيوجن ١٧","فيوجن2017","فيوجن 2017","فيوجن 17","فيوجن17","١٧", "17", "2017", "٢٠١٧"  ]
trigger_C8 =["موديل١٨","موديلات ١٨","موديل ١٨","موديلات١٨","موديل 2018","موديل2018","موديلات 2018","موديل 18","","فيوجن١٨","فيوجن ١٨","فيوجن ١٨","فيوجن ١٨","فيوجن2018","فيوجن 2018","فيوجن 18","فيوجن18","١٨", "18", "2018", "٢٠١٨"  ]
trigger_C9 =["موديل١٩","موديلات ١٩","موديل ١٩","موديلات١٩","موديل 2019","موديل2019","موديلات 2019","موديل 19","","فيوجن١٩","فيوجن ١٩","فيوجن ١٩","فيوجن ١٩","فيوجن2019","فيوجن 2019","فيوجن 19","فيوجن19","١٩", "19", "2019", "٢٠١٩"  ]
ALL_models= trigger_C1 + trigger_C2 + trigger_C3 + trigger_C4 + trigger_C5 + trigger_C6 + trigger_C7 +trigger_C8 + trigger_C9
#_________________________________________________________________________________________________________

#💠المقاسات والكميات: jjjj  and  dddd
Amounts_and_Sizes="كميات - مقاسات"
ClickD=["clickD","clickD2","clickD[01]" ,"clickD[1]"  ,"click31" ,"click32"  ,"click33"  ,"click35" ,"click36" , "click37" ,"click38" ,"clickD[0]","clickD[2]", "clickD[3]","clickD[03]" ,"clickD[4]","clickD[02]"]
ClickJ=["clickJ","Amounts_Return","clickJ2","clickJ[2]","clickJ[3]","clickJ[4]","clickJ[1]","clickJ[01]", "clickJ[04]", "clickJ[02]"  ,"clickE2", "clickJ[00]", "clickJ[0]", "click1", "click3", "click4", "click5", "clickJ[03]"]
J = "كميات"                                 ;J1="كمية زيت المكينة"  ;J2="كمية زيت القير"  ;J3="كمية زيت الفرامل"  ;J4="كمية ماء الرديتر"  ;J5="كمية زيت و فريون المكيف"
trigger_J =["كمية","كميه","كميات","كم علب","كم لتر"]
trigger_J1=["مكين" ] # زيت المكينه
trigger_J2=["قير"  ] # زيت القير
trigger_J3=["فرامل"] # زيت فرامل
trigger_J4=["رديتر","راديتر","مبرد"]
trigger_J5=["فريون"]
trigger_J6=["","" ]
D = "مقاسات"                                ;D1="مقاس البطارية" ;D2="مقاس الكفرات"  ;D3="مقاس اللمبات"  ;D4="مقاس المساحات"  ;D5="مقاس صواميل الكفر"
trigger_D =["مقاس","حجم"]
trigger_D1=["بطاري"]
trigger_D2=["كفر"]
trigger_D3=["لمب","ليد"]
trigger_D4=["مساح"]
trigger_D5=["صامول","صواميل"]
trigger_D6=["","" ]

# DDDD SIZES
tire_size1="\nموديل 2009-2012\nتم تحديد (جنط 16)\U00002714\n.................\n\nالمقاس المناسب (205/60/16)"
tire_size2="\nموديل 2009-2012\nتم تحديد (جنط 17)\U00002714\n.................\n\nالمقاس المناسب (225/50/17)"
tire_size3="\nموديل 2009-2012\nتم تحديد (جنط 18)\U00002714\n.................\n\nالمقاس المناسب (225/45/18)"
tire_size4="\nموديل 2013-2019\nتم تحديد (جنط 16)\U00002714\n.................\n\nالمقاس المناسب (215/60/16)"
tire_size5="\nموديل 2013-2019\nتم تحديد (جنط 17)\U00002714\n.................\n\nالمقاس المناسب (235/50/17)"
tire_size6="\nموديل 2013-2019\nتم تحديد (جنط 18)\U00002714\n.................\n\nالمقاس المناسب (235/45/18)"
Wheel_Size1="جنط 16"
Wheel_Size2="جنط 17"
Wheel_Size3="جنط 18"
intro_battery="\nحدد نوع المحرك وموديل السيارة"
 
REPLY_TEXT_Engine_Oil_AMOUNT1          ="موديلات (2013-2019) \n.................\n\nتوجد تصنيفات مختلفة للزيت:\n واحد من أفضل الزيوت هو *شل الترا بيور*\n [إضغط هنا لعرض العلبة](https://t.me/fusion1/127509)\n\nرقم الفلتر [FL-910]  أو [FL-2131]\n*الكمية المطلوبة للتغيير مع الفلتر:*\nلمكينة 2.5 : ( *5.4 لتر* )\nلمكينة 2.0 : ( *5.4 لتر* )\nلمكينة 1.5 : ( *4.1 لتر* )\n [إضغط هنا إذا لاتعلم حجم محرك سيارتك](https://t.me/fusion1/61180)"
REPLY_TEXT_Engine_Oil_AMOUNT2          ="موديلات (2009-2019) \n.................\n\nتوجد تصنيفات مختلفة للزيت:\n واحد من أفضل الزيوت هو *شل الترا بيور*\n [إضغط هنا لعرض العلبة](https://t.me/fusion1/127509)\n\nرقم الفلتر [FL-910]  أو [FL-2131]\n*الكمية المطلوبة للتغيير مع الفلتر:*\nلمكينة 2.5 : ( *5 لتر* )"

REPLY_TEXT_ATF_AMOUNT_1                ="موديلات (2013-2019) \n.................\n\nنوع لزيت المناسب :\n[MERCON LV](https://t.me/fusion1/83090)\n\nالكمية المطلوبة للتغير:\n- بالطريقة العادية (4.3 لتر)\n- شفط النظام كامل (8.5 لتر تقريبا)\n\n ⛔️بعدها لابد أنك تعاير المستوى والقير حامي\n[إضغط هنا لمزيد من المعلومات](https://t.me/fusion1/72316)"
REPLY_TEXT_ATF_AMOUNT_2                ="موديلات (2009-2012) \n.................\n\nنوع لزيت المناسب :\n[MERCON LV](https://t.me/fusion1/83090)\n\nالكمية المطلوبة للتغير:\n- بالطريقة العادية (4.5 لتر)\n- شفط النظام كامل (8.5 لتر تقريبا)\n\n ⛔️بعدها لابد أنك تعاير المستوى والقير حامي\n[إضغط هنا لمزيد من المعلومات](https://t.me/fusion1/116726)"
REPLY_TEXT_FERON_AMOUNT                ="موديلات (2013-2019) \n.................\n\nكمية زيت الكومبروسر (155 ملي)\n\nكمية الفريون :\nلمكينة 2.5 : (680 جرام)\nلمكينة 2.0 : (??? جرام)\nلمكينة 1.5 : (??? جرام)\n\nنوع الفريون المناسب ( R-134a )"
REPLY_TEXT_BrakeFluid_AMOUNT           ="موديلات (2009-2019) \n.................\n\nتوجد تصنيفات مختلفة للزيت:\n مثل (DOT3  و  DOT4)\nلابد تختار DOT4  *هذا الموصى به*\n\n[زيت موتوركرافت](https://t.me/fusion1/197002)\n\nالكمية المطلوبة للتغير:\n- بالطريقة العادية (تقريبا 300 ملي)\n- شفط النظام كامل (بين  300-900 ملي)"
REPLY_TEXT_COOLANT_AMOUNT              ="موديلات (2013-2019) \n.................\n\nماء الرديتر تجي نوعين: مركز او مخفف\n- المخفف جاهز للإستخدام\nالمركز تحتاج تخففة 50% بماء مقطر\n\nكمية سائل التبريد في كامل النظام :\nلمكينة 2.5 : (6.8 لتر)\nلمكينة 2.0 : (4.4 لتر)\nلمكينة 1.5 : (10.5 لتر)\n\nتحتاج نصف هذه الكميات إذا بتغير بالطريقة العادية"

LIGHTS_REPLY_TEXT                      ="\nموديلات (2009-2016) \n.................\n\n فيش العالي H7 \n فيش الواطي والضباب H11 \n\n الواط (لكل لمبة) لايزيد عن 55-60 واط\n\nتنوية: بعض الفيوجنات مثل الواردة من اوروبا تختلف مقاساتها"
REPLY_TEXT_BATTERY                     ="\nموديلات (2009-2019) \n.................\n\n1- لاتقل قيمة CCA عن 500\nكل مازاد كل ماكان أفضل\n............................\n2-السعة Ampere-Hour\nلايقل عن 50 امبير.ساعة\nوالزيادة أفضل بين 60-70"
REPLY_TEXT_WIPERS                      ="\nموديلات (2009-2012) \nجهه السواق 24 بوصة\nجهه الراكب 19 بوصة\n\nموديلات (2013-2019) \nجهه السواق 26 بوصة\nجهه الراكب 26 بوصة\n\nلابأس بالزيادة البسيطة"
REPLY_TEXT_LugNut                      ="\nموديلات (2013-2019) \n.................\n\nمقاس صامولة الكفرات:\n1.5 x M12"


#_________________________________________________________________________________________________________


#💠محلات قطع الغيار   AAAA
Parts_Related_Klick=["Parts_Related", "Parts_Related_Sub", "None3"]
Parts_Related="رقم وسعر وصور القطع  وطريقة تغييرها"
Show_Location= "الخريطة توضح المناطق بالألوان: تم ترتيب المحلات بالأسفل بناء عليها.\n مثال: اذا كانت المنطقة الخضراء هي الأقرب لك... إنزل تحت بالرسالة الى اللون الأخضر\n\n- إضغط عالمحل لعرض الموقع ورقم التواصل"
A="محلات قطع الغيار"
trigger_A  =["محلات قطع","محلات القطع","محل قطع","ارقام محلات","بوت أرقام محلات","ارقام المحلات","أرقام المحلات","محل القطع","رقم محل","رقم محلات","رقم المحل","محلات الغيار","محلات غيار","محلات بيع قطع","محلات بيع القطع","محلات تبيع قطع","محل بيع قطع", "محلات قطع", "محل قطع","محل القطع","شراء قطع","مواقع تبيع","محل يبيع","موقع يبيع","شتري قطع"]
trigger_A1 =["الرياض","رياض"]
trigger_A2 =["جدة","جده"]
trigger_A3 =["مكة","مكه"]
trigger_A4 =["المدينه","المدينة"]
trigger_A5 =["الدمام","دمام","خبر","ظهران","شرقية","شرقيه" ]
trigger_A6 =["ينبع"]
trigger_A7 =["تبوك"]
trigger_A8 =["أبها","ابها"]
trigger_A9 =["الطايف","الطائف"]
trigger_A10=["نجران"]
trigger_A11=["القصيم"]
trigger_A12=["الجبيل","جبيل"]
trigger_A13=["",""]
trigger_A14=["",""]
trigger_A15=["",""]

###########################  كل مدخلات ومخرجات قطع الغيار والأسعر والمحلات  ومواقع القطع  بالسيارة###########################
ClickA=["clickA", "City[0]", "City[1]", "City[2]", "City[3]", "City[4]", "City[5]", "City[6]", "City[7]", "City[8]", "City[9]", "City[10]", "City[11]", "City[12]", "City[13]","City[14]" ,"City[15]"  , "City[X]"]
City=["الرياض", "جدة", "مكة", "المدينة", "الشرقية", "ينبع", "تبوك", "أبها", "الطائف", "نجران", "القصيم", "الجبيل",   "",   "",  "",  "" ]
#        0        1       2         3          4         5      6        7        8          9        10           11       12    13   14  15

max_Caption_length = 2500 
read_full_parts = "\n\nأرسلت رسالتين...إطلع فوق شيك من البداية"
def read_city_data(file_path):
    emojis = ["🟡", "🔴", "🟢", "🟣", "🟤", "🟠", "🔵"]
    groups = []  # List of tuples: (header, [(store1, location1), (store2, location2), ...])
    current_header = None
    current_stores = []
    current_locations = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            for line in lines:
                line = line.strip()
                if line in emojis:  # Line is an emoji/header
                    if current_header:  # Save the previous group
                        groups.append((current_header, list(zip(current_stores, current_locations))))
                        current_stores = []
                        current_locations = []
                    current_header = line  # Set new header
                elif line.startswith("http"):  # Line is a location
                    current_locations.append(line)
                elif line:  # Line is a store name
                    current_stores.append(line)
            
            # Add the last group after loop ends
            if current_header:
                groups.append((current_header, list(zip(current_stores, current_locations))))
                
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    return groups


# محلات قطع الغيار الرياض                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
#Parts_Store_Group0       =[         "شركة محمد نهار القحطاني"                                        ,           "شركة محمد نهار لقحطاني (صناعية العاصمة مخرج 28)"            ,       "شركة يوسف إبراهيم العوض"                                         ,                                  "المغلوث"                               ,                                   "الملحم للسيارات"                      ,                               "العبدالله"                                ,          "شركة المهد"                                                    ,       "احمد مسفر الشمراني للتجارة"                                      ,          "قطع غيار بالصناعية"                                            ,        "توكيلات الجزيره"                                                  ,       "أرقام تشاليح"                                                                                                                                                                                        ]
#Store_Number_Group0      =[              "059 199 8352"                                                ,                     "050 525 4949"                                        ,                  "011 447 7034"                                           ,                               "011 447 7101"                              ,                                           "055 840 0233"                  ,                                "011 448 2428"                             ,         "053 275 1720"                                                    ,             "059 995 9081"                                                ,               "056 678 7562"                                              ,           "011 252 7660"                                                  ,        "059 589 0672\n054 153 7851\n055 189 3110\n050 285 3695\n055 155 9729\n045 736 1278\n056 700 1817\n059 095 6631\n055 196 2755\n050 511 5261\n050 815 4622\n055 007 2744\n050 259 0749\n011 214 2555"  ]     
#Store_Number2_Group0     =[              "054 636 3564"                                                ,                     ""                                                    ,                  "053 333 9066"                                           ,                               "011 448 8512"                              ,                                               ""                          ,                                  ""                                       ,          "050 665 6426"                                                   ,                "055 545 4122"                                             ,                    ""                                                     ,             "011 252 7807"                                                ,           ""                                                                                                                                                                                                 ]  
#Store_Location_Group0    =[ "https://maps.app.goo.gl/vFXA4bBNo9LkwvbP8?g_st=atm"                       ,                           ""                                              ,                           ""                                              ,                           ""                                              ,                           ""                                              ,                           ""                                              ,                           ""                                              ,                           ""                                              ,                           ""                                              ,                           ""                                              ,                          ""                                              ] 


Parts_Store_Group0    = ["\n🟡",        "العبدالله لقطع غيار فورد الاصليه"         ,          "العوض لقطع غيار سيارات فورد"           , "شركة المهد لقطع غيار فورد"                       ,              "مرحبا المتحدة"                       ,           "قطع غيار الملحم للسيارات"              , "تقنية القطع السيارات الأمريكية"                   ,     "مشاعل الكثيري لقطع الامريكية"                 ,    "الكثيري لقطع غيارالسيارات الأمريكية"          ,                   "مؤسسة غياركم"                   ,      "ناصر مطلق السيف لقطع غيار سيارات"           ,        "السبيعي لقطع الغيار الامريكي"              ,    "أضواء الشرقية لقطع الامريكية"                 ,"\n🔴",        "الحربي لقطع غيار السيارات الامريكية"       ,   "محمد بن نهار القحطاني لقطع السيارات"          ,   "شركة التقوى لقطع غيار السيارات"                , "المغلوث لقطع غيار السيارات الامريكية"            , "شركة صالح عبدالله الحمد - قطع غيار"              , "شركة الجواد الادهم - قطع غيار"                    , "المغلوث لقطع غيار السيارات الامريكية"            ,     "مؤسسة محمد علي العطاس لقطع غيار"            , "شركة أبناء عبود أحمد باعاصم المحدودة"            ,"\n🟢",              "أخوان فورد أمريكي"                  ,            "لملحم لقطع غيار فورد"                  ,         "شركة التقوى لقطع غيار السيارات"         ,        "العتيبي لقطع غيار السيارات الامريكية"      ,           "شركة النسيم الذهبي لقطع غيار"         ,              "القحطاني امريكي"                     ,               "شركة قطع غيار الريان"               ,              "قطع غيار السيارات الامريكيه"         ,           "مؤسسة سعد سعيد سعد أل دعجم"           ,"\n🟣",             "المطلق لقطع غيار السيارات الامريكية"  , "التحالف لقطع غيار السيارات الامريكيه"            ,"\n🟤",      "مؤسسة البريك لقطع غيار السيارات"           ,      "مؤسسة صالح مرعي الصيعري للتجارة"            ,            "الدوائر الأهلية لقطع غيار"             ,"\n🟠",         "شركة التقوى لقطع غيار السيارات"          ,           "شركة التقوى لقطع غيار السيارات"       ,          "محلات خالد الحربي لقطع الغيار"           ,        "آفاق العليا لقطع السيارات الامريكي"       ,"\n🔵", "يوسف ابراهيم العوض للتجارة"                      , "شركة بالبيد قطع غيار أمريكية"                   ,           "محل عبدالله الحبس لقطع الغيار"         ,       "شركة راشد محمد الحمد لقطع غيار"           ,         "مؤسسة نجم الشمال لقطع غيار"               ,           "العثيم لقطع غيار فورد"                 ]
Store_Location_Group0 = ["\n🟡","https://maps.app.goo.gl/BkF8JqEvaVb7sncy6?g_st=atm", "https://maps.app.goo.gl/xEyfbNVoPQNDJM3T9?g_st=atm", "https://maps.app.goo.gl/ByJ3tcSZ57PFwQEv9?g_st=atm", "https://maps.app.goo.gl/LAUtcmU7WiLvQhzAA?g_st=atm", "https://maps.app.goo.gl/19fCzkNKxv3omF6d6?g_st=atm", "https://maps.app.goo.gl/5gndJBcHf7WstkL17?g_st=atm", "https://maps.app.goo.gl/7B7vFEJR5jKiXr8g9?g_st=atm", "https://maps.app.goo.gl/37bUjxeitkPcyHsi6?g_st=atm", "https://maps.app.goo.gl/XizzFE4h8jPReoAe9?g_st=atm", "https://maps.app.goo.gl/T6m4BhvQwcnLP4Nu8?g_st=atm", "https://maps.app.goo.gl/by3PLD7YywHSLRZE7?g_st=atm", "https://maps.app.goo.gl/jaoTPby6XAyCyqYy6?g_st=atm","\n🔴", "https://maps.app.goo.gl/CU5NHF9YbfeBD5Ht9?g_st=atm", "https://maps.app.goo.gl/vfv9Wj8Gx9vAi3La9?g_st=atm", "https://maps.app.goo.gl/7aE15uW8fBcfn5Z17?g_st=atm", "https://maps.app.goo.gl/LsMdusQwirQUQkue7?g_st=atm", "https://maps.app.goo.gl/pwANNRA2PuXKUVDw6?g_st=atm", "https://maps.app.goo.gl/5vBTDDvDxmQvV6f96?g_st=atm", "https://maps.app.goo.gl/snH1MWYHxC2TThgE6?g_st=atm", "https://maps.app.goo.gl/Y5T7AMaLQGw9dEiCA?g_st=atm", "https://maps.app.goo.gl/imT8eNmwcvKjRQ1fA?g_st=atm","\n🟢", "https://maps.app.goo.gl/TMqnMoRx23ybaxo5A?g_st=atm", "https://maps.app.goo.gl/JUrSYgYnBwaHDyUf7?g_st=atm", "https://maps.app.goo.gl/36pzVc77L2vZ4YCy5?g_st=atm", "https://maps.app.goo.gl/cSpDomnD1S6Eb1EAA?g_st=atm", "https://maps.app.goo.gl/25VpXYSvhtVMEeLb8?g_st=atm", "https://maps.app.goo.gl/mZAzDSi43QEuvcWJ9?g_st=atm", "https://maps.app.goo.gl/UuxcrbjdkCKNvX2R7?g_st=atm", "https://maps.app.goo.gl/NHXL3tk6vZHtdR278?g_st=atm", "https://maps.app.goo.gl/4J2vUJy5f76eVt6TA?g_st=atm","\n🟣", "https://maps.app.goo.gl/xsPLohGJdLJ2eZBMA?g_st=atm", "https://maps.app.goo.gl/eTiWa78WTV27MCvE8?g_st=atm","\n🟤", "https://maps.app.goo.gl/xBGju2WGKFkDoejMA?g_st=atm", "https://maps.app.goo.gl/8xQQbcZd18KZ6B5s6?g_st=atm", "https://maps.app.goo.gl/XaySwHLxAqPFbnAo9?g_st=atm","\n🟠", "https://maps.app.goo.gl/JwaZK9z8dC4iQp5p7?g_st=atm", "https://maps.app.goo.gl/GHsYKFoodxjPWoKq6?g_st=atm", "https://maps.app.goo.gl/TaGtQhiV8Q9FFaqt5?g_st=atm", "https://maps.app.goo.gl/1RyLCkJqFDYgvAq27?g_st=atm","\n🔵", "https://maps.app.goo.gl/Pb1ZqUJHBWrj4YmF7?g_st=atm", "https://maps.app.goo.gl/9FvZbjJinRq7F8mm6?g_st=atm", "https://maps.app.goo.gl/zmzR8HmRtVzrWHnq5?g_st=atm", "https://maps.app.goo.gl/TMjnmvgjByzvtmKV7?g_st=atm", "https://maps.app.goo.gl/WkUJKqgB1aqSAG526?g_st=atm", "https://maps.app.goo.gl/o2Q6kb4prfvzWgUh6?g_st=atm"]
#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# محلات قطع الغيار جدة                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
#Parts_Store_Group1       =[      "بن إسحاق (شارع سلطان بن سلمان)"                                    ,             "بن إسحاق (شارع بني مالك)"                                   ,     "جيان فورد ( شارع سلطان بن سلمان)"                                 ,       "صقر الجزيرة (شارع بني مالك)"                                     ,      "صقر الجزيرة (حي النزهة)"                                          ,     "باعقيل (شارع سلطان بن سلمان)"                                      ,             "ياسين قطع فيوجن"                                            ,     "موارد القطع (قطع غيار فورد وبودي) "                                ,       "الإعتلاء الدولي لقطع غيار الأمريكي "                               ,     "بابلغوم لقطع الغيار الامريكية"                                      ,        "شمس الصباح لقطع غيار الامريكي"                                  ,                       ""                                                 ]
#Store_Number_Group1      =[                 "050 438 1840"                                             ,                   "058 219 9631"                                           ,               "053 353 3555"                                             ,               "053 535 0678"                                              ,                   "012 654 4626"                                          ,               "054 956 3689"                                              ,               "055 060 2831"                                              ,                "054 603 6451"                                             ,                 "012 612 6137"                                            ,                 "012 655 1768"                                            ,                "012 605 5357"                                            ,                       ""                                                 ]     
#Store_Number2_Group1     =[                 "055 468 5568"                                             ,                         ""                                                 ,                   ""                                                     ,                   ""                                                      ,                   "050 136 8012"                                          ,                     ""                                                    ,                    ""                                                     ,                       ""                                                  ,                       ""                                                  ,                       ""                                                  ,                     ""                                                   ,                       ""                                                 ] 
#Store_Location_Group1    =[                    ""                                                      ,                        ""                                                  ,                   ""                                                     ,                                        ""                                 ,                           ""                                              ,                                    ""                                     ,                         ""                                                ,                    ""                                                     ,               ""                                                          ,              ""                                                           ,                     ""                                                   ,                       ""                                                 ] 

Parts_Store_Group1    = ["\n🔴",                      "بن اسحاق"                   ,     "صقر الجزيرة لقطع الامريكية"                   ,       "صقر الجزيرة لقطع الامريكية"                 ,                    "جيان فورد"                     ,             "الللي لقطع السيارات الامريكيه"        ,           "بقشان"                                  ,             "العبدان قطع غيار فورد"                ,            "مكرم لقطع غيار فورد الأصلية"           , "الحازمي لقطع غيار السيارات"                      ,                "شركة موارد القطع"                  , "الانوار المتقدمة السيارات الأمريكة"               , "مقيبل قطع غيار سيارات امريكية"                   ,     "اسطورة الشرق لقطع  السيارات الأمريكية"        ,       "خوجه لقطع غيار السيارات الأمريكيه"          ,         "رواحل لقطع غيار السيارات الأمريكية"      ,                  "مؤسسة شمس للتجارة"               ,"\n🟢",            "بن اسحاق لقطع الغيار الأمريكية"       ,            "صقر الجزيره لقطع الامريكية"            ,       "صقر الجزيره لقطع غيار الامريكية"            ,                 "بابلغوم لقطع غيار أمريكي"        , "بالبيد لقطع غيار الامريكية"                       ,   "لؤلؤة الياقوت لقطع غيار الامريكية"             , "الوكالة لقطع غيار الأمريكية"                      , "انوار الشرق لقطع غيار الامريكية"                  , "شركة موارد القطع بني مالك"                       ,           "الشعلة لقطع غيار امريكي"                ,            "شمس قطع غيار امريكي"                  ,   "مرسى الغربية لقطع غيار الامريكية"              ,   "دار الكواسب لقطع غيار الامريكية"]
Store_Location_Group1 = ["\n🔴","https://maps.app.goo.gl/nHCHGPNDfk9gtTja9?g_st=atm", "https://maps.app.goo.gl/UKeEQRShhy4KsTi69?g_st=atm", "https://maps.app.goo.gl/J9vv1NoYBMCJ3csR9?g_st=atm", "https://maps.app.goo.gl/kfwpgchME3kLbMvm6?g_st=atm", "https://maps.app.goo.gl/RugVAtZ4sbndg9zv5?g_st=atm", "https://maps.app.goo.gl/ushd5BweeQK9hawk8?g_st=atm", "https://maps.app.goo.gl/SYEjB8FB2vyJNidw5?g_st=atm", "https://maps.app.goo.gl/aBJdHX6nHKCNLKLB8?g_st=atm", "https://maps.app.goo.gl/S1ojUCekwJjBqbhP9?g_st=atm", "https://maps.app.goo.gl/U3Ysdjm6EW48sNck7?g_st=atm", "https://maps.app.goo.gl/zSnSzXUPmsUbJ6F26?g_st=atm", "https://maps.app.goo.gl/UMVHxBFSAPknZ5U29?g_st=atm", "https://maps.app.goo.gl/KdbDueWPmPdmDr9s9?g_st=atm" , "https://maps.app.goo.gl/44zJkwdFZiarUDoa9?g_st=atm", "https://maps.app.goo.gl/5En7ebGpbdFg5WJK7?g_st=atm", "https://maps.app.goo.gl/iwcmGmKyENbRQZeTA?g_st=atm","\n🟢", "https://maps.app.goo.gl/UD8Xf6P4KZSdQrir8?g_st=atm", "https://maps.app.goo.gl/qxFU8Q8F5uq8zmit8?g_st=atm", "https://maps.app.goo.gl/9WNGptVkaKmpQnUG7?g_st=atm", "https://maps.app.goo.gl/qoBzYEtkY7jT344E7?g_st=atm", "https://maps.app.goo.gl/pDpYPQ4Zd7dzQCSR7?g_st=atm", "https://maps.app.goo.gl/HmEkvKPCQpjAiAKp9?g_st=atm", "https://maps.app.goo.gl/EPc1z8aryjnMXokbA?g_st=atm", "https://maps.app.goo.gl/Hier5i4QqCypTBvbA?g_st=atm", "https://maps.app.goo.gl/BF5ssYtuW4EJ1SZQ9?g_st=atm", "https://maps.app.goo.gl/79JZYJiFaFXyuooq7?g_st=atm", "https://maps.app.goo.gl/ECqtbBBpgXCiMF2W8?g_st=atm", "https://maps.app.goo.gl/sWLNZUjiJKhLMgCq5?g_st=atm", "https://maps.app.goo.gl/G4DEHrcRBMc2o3UW7?g_st=atm"]
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# محلات قطع الغيار مكة                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
Parts_Store_Group2       =[                  "بن إسحاق"                                               ,                      "العكبري (شارع الحج)"                                ,                 "باجبران"                                               ,              "طيبة فورد"                                                 ,                "بن عمار"                                                  ,             "العطاف"                                                     ,              "المحمادي"                                                   ,               ""                                                          ]
Store_Number_Group2      =[                 "057 162 0814"                                             ,                     "050 554 3490"                                         ,                "012 542 1699"                                            ,              "054 424 4885"                                               ,              "055 427 9375"                                               ,                       "059 479 2010"                                      ,              "056 562 4367"                                               ,               ""                                                          ]     
Store_Number2_Group2     =[                      ""                                                    ,                         "055 314 1819"                                     ,                   ""                                                     ,                   ""                                                      ,                   ""                                                      ,                     "054 644 9900"                                        ,                    ""                                                     ,                       ""                                                  ] 
Store_Location_Group2    =[                      ""                                                    ,                        ""                                                  ,                   ""                                                     ,                   ""                                                      ,                           ""                                              ,                                    ""                                     ,                         ""                                                ,                    ""                                                     ] 
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# محلات قطع الغيار المدينة                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
Parts_Store_Group3       =[          "صادق محمد حمزة خليفة"                                          ,                              "تكساس"                                       ,                 "الحماد"                                                ,                "الجوده"                                                   ,                "الوكيل لقطع الأمريكي"                                    ,      "مؤسسة التقوى"                                                      ,          "قطع غيار"                                                       ,               ""                                                          ]
Store_Number_Group3      =[              "014 834 2309"                                                ,                           "014 822 2782"                                   ,             "057 024 1455"                                               ,              "014 838 9212"                                               ,                    "056 009 9022"                                         ,       "014 837 3197"                                                      ,         "056 148 2122"                                                    ,               ""                                                          ]     
Store_Number2_Group3     =[               "014 824 4962"                                               ,                         ""                                                 ,            "014 838 5637"                                                ,                   ""                                                      ,                   ""                                                      ,                     ""                                                    ,                    ""                                                     ,                       ""                                                  ] 
Store_Location_Group3    =[        "https://maps.app.goo.gl/vFXA4bBNo9LkwvbP8?g_st=atmnk1"             ,         "https://maps.app.goo.gl/vFXA4bBNo9LkwvbP8?g_st=atm"               ,                   ""                                                     ,                   ""                                                      ,                           ""                                              ,                                    ""                                     ,                         ""                                                ,                    ""                                                     ] 

#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# محلات قطع الغيار الشرقية                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
#Parts_Store_Group4       =[                  "عالم فورد"                                              ,                              "الوفى الذهبي"                               ,                 "الملحم"                                                 ,                "المغلوث"                                                  ,                    "ركن القطع"                                          ,         "العثيم"                                                          ,          "المسلم"                                                        ,          "الخليفة"                                                       ,          "توكيلات الجزيرة كويك بارتس"                                       ]
#Store_Number_Group4      =[                "050 684 5727"                                              ,                           "055 686 8112"                                   ,              "050 460 2341"                                              ,              "013 837 3654"                                                ,                    "050 307 2835"                                        ,       "013 837 3532"                                                      ,         "n013 837 3511"                                                   , "053 914 1216\n013 839 0066"                                              ,          "013 829 6191 \n013 859 5151"                                      ]     
#Store_Number2_Group4     =[                "059 717 0551"                                              ,                                ""                                          ,               "013 837 4238"                                             ,                   ""                                                       ,                         ""                                               ,          ""                                                               ,              ""                                                           ,              ""                                                           ,                       ""                                                    ] 
#Store_Location_Group4    =[                      ""                                                    ,                        ""                                                  ,                   ""                                                     ,                   ""                                                       ,                           ""                                             ,                                    ""                                     ,                         ""                                                ,                    ""                                                     ,               ""                                                            ] 

Parts_Store_Group2       =["\n🟢" ,       "العثيم لقطع غيار فورد الأصلية"               ,        "الملحم لقطع الغيار"                       ,        "محلات المغلوث"                              ,                     "المعجل"                        ,            "الملحم للسيارات"                      ,            "مركز الظهران لقطع غيار السيارات"      ,             "مؤسسة أرض المودّه التجارية"           ,              "مؤسسة سلمان سعود"                    ,          "مؤسسة عبدالله محمد آل محائي"            , "\n🔴" ,                   "الوفى الذهبي"                     ,               "الملحم للسيارات"                   ,             "عالم فورد لقطع السيارات"             ,                "العثيم لقطع غيار فورد"              ,                   "ركن القطع"                        ,              "محل النجم الساطع لقطع غيار"         ,               "المعجل لقطع غيار"                  ,              "الهاجري لقطع الغيار"                 ,                 "مؤسسة المعجل للتجارة"            ,               "مشعل لقطع غيار جمس و فورد"          ,             "الجواد الادهم - قطع غيار"            ,              "المواسم الاولى التجارية"              ]
Store_Location_Group2    =["\n🟢" ,  "https://maps.app.goo.gl/cUMmjF2AKmVQ3krXA?g_st=atm", "https://maps.app.goo.gl/5ejjovMzSsM4o3WH8?g_st=atm", "https://maps.app.goo.gl/4eCRD6zGtp8Z84ZZ8?g_st=atm", "https://maps.app.goo.gl/CyK7HH9rZrsTDoFr8?g_st=atm", "https://maps.app.goo.gl/tZ2wQFyyx3ZjYEJF8?g_st=atm", "https://maps.app.goo.gl/hnTn929rYfXD5DyJ6?g_st=atm", "https://maps.app.goo.gl/ZbqbATDi4A4N4BLo6?g_st=atm", "https://maps.app.goo.gl/kRkFS8HF9biEX6a18?g_st=atm", "https://maps.app.goo.gl/nSoz9m6fDQc7gqzY6?g_st=atm", "\n🔴" ,  "https://maps.app.goo.gl/en7qP7gALFgkDWtw9?g_st=atm" , "https://maps.app.goo.gl/9jih2QE4jZj6djsi6?g_st=atm", "https://maps.app.goo.gl/ee8A4BHxcuFL8hjW7?g_st=atm", "https://maps.app.goo.gl/x3ykTThmwJ3YEWPD7?g_st=atm" ,  "https://maps.app.goo.gl/KQ9RjgbTWAjYX8w27?g_st=atm" , "https://maps.app.goo.gl/cKHzT9uCbLtz6AtN7?g_st=atm", "https://maps.app.goo.gl/zyzjaT24qMGAhaP16?g_st=atm", "https://maps.app.goo.gl/XYis6CuY7jn1s1Lt8?g_st=atm", "https://maps.app.goo.gl/ys7B9vyhB1qRCjnr9?g_st=atm", "https://maps.app.goo.gl/uV3gp8cG1xZJNgmk6?g_st=atm", "https://maps.app.goo.gl/qoYbG5YLjTaVEKHo6?g_st=atm", "https://maps.app.goo.gl/zFLdRfyizYpCTd6N9?g_st=atm"]













#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# محلات قطع الغيار ينبع                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
Parts_Store_Group5       =[                "نخبه التعاون"                                             ,                         "مركز الجزيرة"                                    ,            "بن صالح للمريكيه"                                           ,              ""                                                            ,                    ""                                                    ,           ""                                                              ]
Store_Number_Group5      =[                 "014 391 8024"                                             ,                          "057 227 0304"                                    ,               "014 357 9997"                                             ,              ""                                                            ,                    ""                                                    ,           ""                                                              ]     
Store_Number2_Group5     =[                       ""                                                   ,                               ""                                           ,                    ""                                                    ,              ""                                                            ,                    ""                                                    ,           ""                                                              ] 
Store_Location_Group5    =[                      ""                                                    ,                       ""                                                   ,                   ""                                                     ,                   ""                                                       ,                           ""                                             ,                                    ""                                     ] 
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# محلات قطع الغيار تبوك                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
Parts_Store_Group6       =[           "العمرى لقطع غيار السيارات"                                    ,              "مؤسسة محمد مردح الشهري"                                    ,    "الركن لقطع الغيار"                                                  ,       "درة خالد لقطع الغيار السيارات"                                    ,             "بن بشر"                                                    ,        "العمري لقطع الغيار"                                              ]
Store_Number_Group6      =[                "014 425 2290"                                              ,                  "014 423 2204"                                            ,       "014 424 5725"                                                     ,                "014 421 2532"                                              ,           "014 427 5949"                                                 ,          "014 424 6086"                                                   ]     
Store_Number2_Group6     =[                "014 422 7521"                                              ,                       ""                                                   ,            ""                                                            ,                       ""                                                   ,               ""                                                         ,                ""                                                         ] 
Store_Location_Group6    =[                   ""                                                       ,                     ""                                                     ,                   ""                                                     ,                   ""                                                       ,                           ""                                             ,                                    ""                                     ] 
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# محلات قطع الغيار أبها                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
Parts_Store_Group7       =[                  "جيان فورد"                                              ,             "نور الفتح"                                                   ,    "التوكيلات المعتمدة"                                                  ,      "عوض سالم القحطاني قطع غيار امريكي"                                 ,               ""                                                        ,        ""                                                                  ]
Store_Number_Group7      =[                  "055 475 4444"                                            ,             "017 227 3734"                                                 ,       "017 226 4789"                                                     ,                "017 227 4455"                                              ,             ""                                                           ,         ""                                                                ]     
Store_Number2_Group7     =[                       ""                                                   ,                  ""                                                        ,            ""                                                            ,                      ""                                                    ,             ""                                                           ,         ""                                                                ] 
Store_Location_Group7    =[                   ""                                                       ,                    ""                                                      ,                   ""                                                     ,                    ""                                                      ,                           ""                                             ,                                    ""                                     ] 
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# محلات قطع الغيار الطائف                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
Parts_Store_Group8       =[               "بالبيد"                                                    ,             "الدوليه لقطع الامريكي"                                        ,    "المجمع الأمريكي لقطع الغيار"                                        ,      "محلات بن سعد الامريكي"                                               ,             ""                                                           ,         ""                                                                ]
Store_Number_Group8      =[               "012 742 0159"                                               ,             "012 743 5333"                                                 ,          "012 748 3001"                                                  ,           "012 727 3391"                                                   ,             ""                                                           ,         ""                                                                ]     
Store_Number2_Group8     =[                    ""                                                      ,                  ""                                                        ,               ""                                                         ,                 ""                                                         ,             ""                                                           ,         ""                                                                ] 
Store_Location_Group8    =[                   ""                                                       ,                    ""                                                      ,                   ""                                                     ,                    ""                                                      ,                           ""                                             ,                                    ""                                     ] 
#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# محلات قطع الغيار نجران                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
Parts_Store_Group9       =[          "زاوية الاسطورة للامريكي"                                         ,             "عالم الفورد"                                                 ,                ""                                                        ,                    ""                                                      ,                ""                                                        ,           ""                                                              ]
Store_Number_Group9      =[              "017 544 0049"                                                ,             "050 801 4166"                                                 ,                ""                                                        ,                    ""                                                      ,                ""                                                        ,           ""                                                              ]     
Store_Number2_Group9     =[                   ""                                                       ,                  ""                                                        ,                ""                                                        ,                    ""                                                      ,                ""                                                        ,           ""                                                              ] 
Store_Location_Group9    =[                   ""                                                       ,                    ""                                                      ,                   ""                                                     ,                    ""                                                      ,                           ""                                             ,                                    ""                                     ] 
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# محلات قطع الغيار القصيم                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
Parts_Store_Group10      =[          "لتويجري لقطع فورد"                                              ,            "العبيدان"                                                     ,               "الحنطي"                                                  ,      "العبيدان"                                                            ,                "nالمحيمدي"                                              ,        "مؤسسة الطريف لقطع غيار  الأمريكي"                                ,                  "الجنيدلي"                                              ,         "الجناح"                                                         ,      "الشعار لقطع غيار السيارات"                                         ,    "عالم المصادر لقطع الغيار"                                             ,  "مؤسسة الحصان التجارية"                                                                   ,                                               "تشاليح"                                                           ]
Store_Number_Group10     =[              "016 324 1272"                                                ,            "050 801 4166"                                                  ,           "055 849 1777"                                                 ,     "016 325 1928"                                                         ,                "016 364 0008"                                            ,                  "016 362 1405"                                            ,                       ""                                                 ,       "053 692 0730"                                                      ,             "016 325 0078"                                                 ,           "050 427 7234"                                                    ,      "016 327 1223"                                                                          ,   "050 517 5424\n055 545 5467\n055 313 1000\n059 329 1888\n016 329 0111\n055 202 5868"                           ]     
Store_Number2_Group10    =[                   ""                                                       ,                 ""                                                         ,            "053 620 0777"                                                ,          ""                                                                ,                      ""                                                  ,                        ""                                                  ,                        ""                                                ,            ""                                                             ,                    ""                                                      ,                  ""                                                         ,            ""                                                                                ,                                                ""                                                                ] 
Store_Location_Group10   =[                   ""                                                       ,                   ""                                                       ,                   ""                                                     ,                    ""                                                      ,                           ""                                             ,                                    ""                                      ,                         ""                                               ,                    ""                                                     ,               ""                                                           ,              ""                                                             ,      ""                                                                                      ,                                                                                                                  ] 
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# O OOOO توصيات الورش 
O = "توصيات الورش"    
X_O="إكتب تجربتك مع ورشة تنصح فيها حتى اضيفها للقائمة:\n- موديل السياره\n- المدينه\n- الإصلاح الي تم\n- معلومات اضافيه مثل التكلفة او سبب ترشيحك للورشة\n\nمازال تحت التجميع أحتاج تكتبو لي تجاربكم حتى أضيفها"
trigger_O  =["افضل ورش","أفضل ورش","افضل الورش","أفضل الورش","توصيات","توصيه","توصية","","","","","","","","","","","","" ]
trigger_O1=trigger_A1
trigger_O2=trigger_A2
trigger_O3=trigger_A3
trigger_O4=trigger_A4
trigger_O5=trigger_A5
trigger_O6=trigger_A6
trigger_O7=trigger_A7
trigger_O8=trigger_A8
trigger_O9=trigger_A9
trigger_O10=trigger_A10
trigger_O11=trigger_A11
trigger_O12=trigger_A12
trigger_O13=trigger_A13
trigger_O14=trigger_A14
trigger_O15=trigger_A15

ClickO=["clickO", "FixShop[0]", "FixShop[1]", "FixShop[2]", "FixShop[3]", "FixShop[4]", "FixShop[5]", "FixShop[6]", "FixShop[7]", "FixShop[8]", "FixShop[9]", "FixShop[10]", "FixShop[11]", "FixShop[12]", "FixShop[13]"   ]
City=["الرياض", "جدة", "مكة", "المدينة", "الشرقية", "ينبع", "تبوك", "أبها", "الطائف", "نجران", "القصيم",  "",   "",   "",  "",  "" ]

#         اسم الورشة وتحتها الرقم والموقع والي متخصصين فية                     Fist Shop                                                                                                            Shop2                                                                                                              Shop3 ....
#   ورش صيانة بالرياض                
Shop_Store____Group0 =[                                                           "ورشة"                                                ,                                                              ""                                               ,                                                              ""                                              ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group0 =[                                                        "0552985551"                                              ,                                                              ""                                               ,                                                              ""                                              ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group0 =[                            "صناعية الخليج\nhttps://maps.app.goo.gl/vMWomaStAojUfc2m6?g_st=it"                   ,                                                              ""                                               ,                                                              ""                                              ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group0 =[                                      "ميكانيكي (صابر)  ممتاز لتوظيب قير \n"                                    ,                                                              ""                                               ,                                                              ""                                              ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#  صيانة في جدة  
Shop_Store____Group1 =[                                                              {X}                                                 ,                                                              ""                                               ,                                                                ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group1 =[                                                              {X}                                                 ,                                                              ""                                               ,                                                                ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group1 =[                                                              {X}                                                 ,                                                              ""                                               ,                                                                ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group1 =[                                                              {X}                                                 ,                                                              ""                                               ,                                                                ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#  صيانة في مكة 
Shop_Store____Group2 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group2 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group2 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group2 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#  صيانة في المدينة 
Shop_Store____Group3 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group3 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group3 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group3 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#  صيانة في الشرقية  
Shop_Store____Group4 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group4 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group4 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group4 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#  صيانة في ينبع  
Shop_Store____Group5 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group5 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group5 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group5 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#  صيانة في تبوك  
Shop_Store____Group6 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group6 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group6 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group6 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#  صيانة في أبها  
Shop_Store____Group7 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group7 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group7 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group7 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#  صيانة في الطائف  
Shop_Store____Group8 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group8 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group8 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group8 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#  صيانة في نجران  
Shop_Store____Group9 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group9 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group9 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group9 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#  صيانة في القصيم  
Shop_Store____Group10 =[                                                              {X}                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]
Shop_Number___Group10 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ]     
Shop_Location_Group10 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
Speciality____Group10 =[                                                              ""                                                 ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ,                                                              ""                                                  ] 
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#💠إعدادات - ضبط - برمجة:  HHHH
ClickH=["clickH", "botton_Return_H","Settings_2013+", "Settings_2012" , "H[0]", "H[1]", "H[2]", "H[3]", "H[4]", "H[5]", "H[6]", "H[7]", "H[8]","H[9]","H[10]","H[11]", "H[12]", "H[13]", "H[14]", "H[15]", "H[16]", "H[17]", "H[18]", "H[19]", "H[20]",   "H_[0]", "H_[1]", "H_[2]", "H_[3]", "H_[4]", "H_[5]", "H_[6]", "H_[7]", "H_[8]","H_[9]","H_[10]","H_[11]", "H_[12]", "H_[13]", "H_[14]", "H_[15]", "H_[16]", "H_[17]", "H_[18]", "H_[19]", "H_[20]"]
Reset_oil="⭐️ تصفيير عداد عمر الزيت بعد تغييرة:"   
Relearn="⭐️ إعادة ضبط وتعليم الثروتل (البوابة) وقيم ال Idle.. بعد تغييرها او تنظيفها" 
H = "إعدادات وضبط"                     ;H1="مود صيانة الفرامل"  ;H2="TPMS"  ;H3="BMS"  ;H4="شاشة البيانات"  ;H5="تصفير عمر الزيت"    ;H6="إعدادات سينك" ; H7="الدخول بالرمز"  ; H8="اعاده ضبط النوافذ"  ; H9="اعاده تعليم الثروتل"   
trigger_H  =["عدادات","برمجة","برمجه","اعاده ضبط","إعاده ضبط","اعادة ضبط","إعادة ضبط","تحديث","تصفير","تفعيل","دخول"]
trigger_H1 =["وضع صيان","صيانه الفرامل","وضع الصيان","صيانة فرامل","صيانه فرامل","","صيانة الفرامل","صيانه الفرامل","لوضع الصيان","لوضع صيان","لوضع الصيان","مود صيان","مود الصيان","لمود الصان","لمود صيان","","","" ]
trigger_H2 =["TPMS","tpms","Tpms","حساس الكفر","حساس كفر","","","","","","","","","","","","","","","","" ]
trigger_H3 =["BMS","Bms","bms","البطار","","","","","","","","","","","","","","","","","" ]
trigger_H4 =["شاشه البيانات","شاشة البيانات","ETM","etm","ET","et","Et","","","","","","","","","","","","","","" ]
trigger_H5 =["عمر الزيت","عداد الزيت","عمر زيت","عداد زيت","","","","","","","","","","","","","","","","","" ]
trigger_H6 =["البلوتوث","","","","","","","","","","","","","","","","","","","","" ]
trigger_H7 =["رقم","رمز","سري","","","","","" ]
trigger_H8 =["النوافذ","القزاز","قزاز","نوافذ","","","","","","","","","","","","","","","" ]
trigger_H9 =["الثروتل","البوابة","البوابه","ثروتل","بوابه","بوابة","","","","","","","","","","","","","","","" ]
trigger_H10=["سينك","تحديث سينك","تحديث سنك","","","","","","","","","","","","","","","","","" ]
trigger_H11=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_H12=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_H13=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_H14=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_H15=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_H16=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_H17=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_H18=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_H19=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_H20=["","","","","","","","","","","","","","","","","","","","","" ]

Sections_G=["2013-2020"]
Settings                 =[       "وضع صيانة الفرامل"                   ,               "TPMS"                          ,                "BMS"                             ,           "شاشة البيانات"                ,           "تصفير عمر الزيت"                ,           "إعدادات سينك"                   ,             "رمز الدخول"                 ,          "ضبط النوافذ"                  ,           "ضبط الثروتل"                 ,       "تحديث سينك 1"                ,"","","","","","","","","","","","","","","","","","","","",""  ]#   ,    "                            "         ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                 ]
Sections_H0              =[       "وضع صيانة الفرامل"                   ,               "TPMS"                          ,                "BMS"                             ,           "شاشة البيانات"                ,           "تصفير عمر الزيت"                ,           "إعدادات سينك"                   ,             "رمز الدخول"                 ,          "ضبط النوافذ"                  ,           "ضبط الثروتل"                 ,       "تحديث سينك 1"                ,"","","","","","","","","","","","","","","","","","","","",""  ]#   ,    "                            "         ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                   ,             "         "                 ]                    
Answer_By_Link1_H0       =[     "https://t.me/fusion1/100015"            ,     "https://t.me/fusion1/48521"              , "https://www.youtube.com/watch?v=I4sG3ufFiXs"     ,   "https://t.me/fusion1/76920"            ,   "https://t.me/fusion1/41282"              ,     "https://t.me/fusion1/56157"            ,    "https://t.me/fusion1/47115"          ,    "https://youtu.be/cU03gVgj0Ms"        ,     "https://t.me/fusion1/87647"         ,"https://t.me/fusion1/88943"          ,"","","","","","","","","","","","","","","","","","","","",""  ]#   ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "       ]
Answer_By_Link2_H0       =[                 ""                           ,                 ""                            ,                 ""                                ,                 ""                        ,                 ""                          ,                  ""                         ,                 ""                       ,                 ""                       ,                 ""                       ,              ""                      ,"","","","","","","","","","","","","","","","","","","","",""  ]#   ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "       ] 
Answer_Editable_H0       =[                 ""                           ,                 ""                            ,                 ""                                ,                 ""                        ,                 ""                          ,                  ""                         ,                 ""                       ,                 ""                       ,                 ""                       ,              ""                      ,"","","","","","","","","","","","","","","","","","","","",""  ]#   ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "       ] 

#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#💠مشاكل شائعة وحلول:   GGGG                      
G = "مشاكل شائعة"                        ; G1="حساس ABS" ;   G2="صواميل الكفرات" ; G3="نتعة القير" ;  G4="جلبة عصا القير" ;G5="سقوط الشماسة" ;  G6="حساس دعسة الفرامل" ;G7="مشكلة سينك" ;  G8="لمبة الايرباق" ; G9="تهريب زيت غطا البلوف"  ; G10="لمبة البريك"   ; G11="قفل الباب 2014-2015"   ;G12=""    ;G13="المكيف يشتغل لحاله"    ;G14="حساس حرارة الجو"    ;G15="تهريب رديتر"    ;G16="إرتفاع حرارة"   
trigger_G  =["مشاكل","مشكلة","مشكله"]
trigger_G1 =["حساس ABS","حساس اي بي اس","حساس abs","حساس Abs","حساس السرع" ]
trigger_G2 =["صواميل الكفر","صامولة الكفر","صاموله الكفر","صامولة كفر","صواميل كفر"]
trigger_G3 =["قيرنتعات القير","نتعه قير","نتعة قير","نتعه في القير","نتعة في القير","نتعات القير","نتعات في القير","نتعه بالقير","نتعة بالقير","نتعات بالقير","نتعه بالقير","نتعة قير","نتعه في بالقير","نتعة في بالقير","نتعات بالقير","نتعات في بالقير","النتع","نتعه","نتعة","","","","","" ]
trigger_G4 =["جلبة عصا القير","جلبه عصا القير","ربله عصا القير","ربلة عصا القير","جلدة عصا القير","جلده عصا القير","","جلبة عصى القير","جلبه عصى القير","ربله عصى القير","ربلة عصى القير","جلدة عصى القير","جلده عصى القير","","","","","","","","","","","","","" ]
trigger_G5 =["سقوط الشماسة","سقوط الشماس","كلبس الشماس","","","","","","","","","","","","","","","","","","" ]
trigger_G6 =["حساس دعسة الفرامل","حساس دعسه الفرامل","حساس الفرامل","حساس فرامل","حساس دعسه فرامل","حساس فرامل","","","","","","","","","","","","","","","","","" ]
trigger_G7 =["سينك","سينك","البلوتوث","البلوتوث","بلوتوث يعلق","البلوتوث يعلق","","","","","","","","","","","","","","","" ]
trigger_G8 =["لمبه الايرباق","لمبة الإيرباق","لمبه الإيرباق","لمبة ايرباق","","لمبه ايرباق","لمبة ايرباق","لمبه إيرباق","لمبة إيرباق","","","","","","","","","","","","","","","" ]
trigger_G9 =["تهريب غطا البلوف","تهريب غطى البلوف","تهريب وجه","","تهريب وجة","","","","","","","","","","","","","","","","" ]
trigger_G10=["لمبة البريك","لمبه البريك","","","","","","","","","","","","","","","","","","","" ]
trigger_G11=["قفل الباب","قفل الأبواب","قبل الأبو","قفل الابو","","","","","","","","","","","","","","","","","" ]
trigger_G12=["صرفي","استهلاك","إستهلاك","","","","","","","","","","","","","","" ]
trigger_G13=["المكيف يشتغل لحال","المكيف يشتغل لوحد","مكيف يشتغل لوحد","مكيف يشتغل لحال","","","","","","","","","","","","","","","","","" ]
trigger_G14=["حساس حرارة الجو","حساس الحرارة الخارجي","حساس حراره الجو","حساس الحراره الخارجي","حساس حرار","","","","","","","","","","","","","","","","" ]
trigger_G15=["تهريب رديتر","تهريب ماء رديتر","تهريب ماء الرديتر","تهريب موية رديتر","تهريب مويه رديتر","","","","","","","","","","","","","","","","" ]
trigger_G16=["إرتفاع الحرار","ارتفاع الحرار","حرارة المكين","حراره المكين","","","","","","","","","","","","","","","","","" ]
trigger_G17=["مشكلة الكاميرا الخلفي","مشكله الكاميرا الخلفي","الكاميرا الخلفي","","","","","","","","","","","","","","","","","","" ]
trigger_G18=["صوت مويه بالطبلون","صوت موية بالطبلون","صوت جريان ماء","صوت جريان موي","","","","","","","","","","","","","","","","","" ]
trigger_G19=["ريحة كربون بالسيارة","","","","","","","","","","","","","","","","","","","","" ]
trigger_G20=["تهريب جلدة العكس","","","","","","","","","","","","","","","","","","","","" ]
trigger_G21=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_G22=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_G23=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_G24=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_G25=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_G26=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_G27=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_G28=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_G29=["","","","","","","","","","","","","","","","","","","","","" ]
trigger_G30=["","","","","","","","","","","","","","","","","","","","","" ]

ClickG=["clickG","botton_Return_G" ,"Problems_2013+", "Problems_2012", "G[0]",  "G[1]", "G[2]", "G[3]", "G[4]", "G[5]", "G[6]", "G[7]", "G[8]", "G[9]", "G[10]", "G[11]","G[12]","G[13]","G[14]","G[15]","G[16]","G[17]","G[18]","G[19]","G[20]"]
Sections_G=["2013-2020"]                 
#                                               [0]                                             [1]                                         [2]                                         [3]                                      [4]                                     [5]                                             [6]                                   [7]                                        [8]                                              [9]                                           [10]                                         [11]                                     [12]                                          [13]                                            [14]                                    [15]                                         [16]                               [17]                                                    [18]                                       [19]                                     [20]                                       [21]                                        [22]                                       [23]                                        [24]                                   [25]                                
Sections_G0              =[                 "حساس ABS"                    ,             "صواميل الكفرات"              ,           "مشاكل القير"                 ,          "جلبة عصا القير"                ,         "سقوط الشماسة"               ,          "حساس دعسة الفرامل"            ,             "مشكلة سينك"                  ,        "لمبة الإيرباق"             ,        "تهريب زيت غطا المحرك"                   ,      "لمبة البريك الالكتروني"             ,              "قفل الباب "                        ,       "صرفية البنزين"              ,           "مكيف يشتغل لحالة"               ,         "حساس حرارة الجو"              ,                   "تهريب رديتر"           ,            "إرتفاع الحرارة"              ,           "الكاميرا الخلفية"             ,"صوت جريان ماء"                              ,                  ""                      ,                  ""                      ,                  ""                      ,                  ""                      ,                 ""                       ,                  ""                      ,                  ""                      ,                  ""                       ]                       
Answer_By_Link1_G0       =[        "https://t.me/fusion1/72510"           ,    "https://t.me/fusion1/78024"             ,    "https://t.me/fusion1/65555"          ,    "https://t.me/fusion1/101644"          ,    "https://t.me/fusion1/117310"     ,     "https://t.me/fusion1/51627"          ,    "https://t.me/fusion1/46065"            ,    "https://t.me/fusion1/65713"    ,                {X}                               ,    "https://t.me/fusion1/101553"           ,      "https://t.me/fusion1/49787"                ,  "https://t.me/fusion1/67385"       ,     "https://t.me/fusion1/62032"            ,    "https://t.me/fusion1/93820"         ,                         {X}                 ,                 {X}                      ,    "https://t.me/fusion1/104929"           ,"https://t.me/fusion1/119233"                 ,                 {X}                      ,                 {X}                      ,                 {X}                      ,                 {X}                      ,                 {X}                      ,                 {X}                      ,                 {X}                      ,                 {X}                       ]   
Answer_By_Link2_G0       =[                    ""                         ,                    ""                       ,                    ""                    ,                    ""                     ,                    ""                ,                 ""                        ,                    ""                      ,                    ""              ,                 ""                               ,                    ""                      ,                ""                                 ,              ""                     ,                    ""                       ,                    ""                   ,                          ""                 ,                 ""                       ,                    ""                      ,            ""                                ,                 ""                       ,                 ""                       ,                 ""                       ,                 ""                       ,                 ""                       ,                 ""                       ,                 ""                       ,                 ""                        ]      
Answer_Editable_G0       =[                    ""                         ,                    ""                       ,                    ""                    ,                    ""                     ,                    ""                ,                 ""                        ,                    ""                      ,                    ""              ,                 ""                               ,                    ""                      ,                ""                                 ,              ""                     ,                    ""                       ,                    ""                   ,                          ""                 ,                 ""                       ,                    ""                      ,            ""                                ,                 ""                       ,                 ""                       ,                 ""                       ,                 ""                       ,                 ""                       ,                 ""                       ,                 ""                       ,                 ""                        ]

#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# KKKK   PARTS RELATED  
L = "سعر ورقم القطعة" 
P = "سعر القطعة"
N = "رقم القطعة"
K = "طريقة التغيير"  
T= "مواقع القطع"
car_header = "🚗 فيوجن 2013-2016 (2.5L)\n.....................\n"

# these are the four General triggers
trigger_Price   =["سعر", "أسعار","اسعار"]
trigger_number  =["رقم", "أرقام","ارقام"]
trigger_Location=["مكان", "مواقع","موقع","صور"]
trigger_Tutorial=["تغيير","فك","تركيب","أغير","يتغير","يتفك","ينفك","افك","أفك","اغير"]
ClickK=["clickK","mode_pn","mode_pp","mode_pl","mode_ct", "botton_Return_K", "How_to_2013", "How_to_2012"  ,   "part_cp_L9_10","part_cp_L9_8", 'part_conflict_', "part_cp_L9_9"  ]      
INTAKE_MANI_GASKETS="4 جلد:\n8E5Z-9439-A\n\nالخامسة:\n1S7Z-9J469-AA" 
Bushing_STABILIZER="أمامي DG9Z-5484-C\nخلفي DG9Z-5493-F"
AIRBAGS_NUMBERS= {X}
# similar names of parts Re-Direct : yyyyy 
similar_groups = [
    ['Group_A2' , 'Group_A3','Group_A4'],                                                            
    ['Group_A9' , 'Group_A5', 'Group_A6', 'Group_A7', 'Group_A8'],              
    ['Group_A11', 'Group_A12'],                                                  
    ['Group_A13', 'Group_A14'],                                                  
    ['Group_A15', 'Group_A16', 'Group_A17', 'Group_A18', 'Group_A19'],          
    ['Group_A21', 'Group_A22'],                                                 
    ['Group_B11', 'Group_B12'],                                                 #"حساس الاكسجين"
    ['Group_B25', 'Group_B26'],                                                 #"حساس التيار"
    ['Group_B39', 'Group_B40'],                                                 # بلف بخار  بلف تبخير
    ['Group_B8' , 'Group_B15' , 'Group_B27' , 'Group_B28' , 'Group_B30'],       # حساس ضغط
    ['Group_B16', 'Group_B17','Group_B18'],                                     # حساس حرارة
    ['Group_B19', 'Group_B20','Group_B22', 'Group_B23'],                        # حساس سرعه
    ['Group_B31', 'Group_B32', 'Group_B33'],                                    # حساس دعسة  حساس فرامل 
    ['Group_B50', 'Group_B51' ],                                                # مضخه او دينو  مساحات
    ['Group_E8',   'Group_E9',  'Group_E10'],                                    # قسامات وموزعات المكيف
    ['Group_D6',  'Group_E5',  'Group_E6' ],                                     #  المراوح ومنظم المروحه
    ['Group_F1', 'Group_F2'], 
    ['Group_F3', 'Group_F4'],
    ['Group_F7', 'Group_F8'],
    ['Group_F9', 'Group_F10'],                                                  # المجموعات هذي تخص قطع الفرامل  امامي وخلفي
    ['Group_F11', 'Group_F12'],
    ['Group_F17', 'Group_F18'],
    ['Group_G2', 'Group_G3'],                                                   # سير مكيف ومكينه
    ['Group_J3', 'Group_J4']                                                    # فلتر مكيف ومكينه
    ]       


#"🔴 عضلات السيارة"  vvvv
L1= "🔴 عضلات السيارة"
Group_A1  = ["كرسي المكين", "كرسي مكين", "كراسي المكين", "كراسي مكين"]
Group_A2  = ["قواعد كراسي القير", "كرسي قير", "كرسي القير", "قاعده الكرسي", "قاعده الكرسي", "قاعده كراسي", "قاعده كراسي"]
Group_A3  = ["كرسي القير العلوي", "كرسي قير", "كرسي القير", "كراسي قير", "كراسي القير" ]
Group_A4  = ["كرسي القير السفلي", "كرسي قير", "كرسي القير", "كراسي قير", "كراسي القير"]
Group_A5  = ["المساعد الأمام", "مساعد"]
Group_A6  = ["المساعد الخلفي", "مساعد"]
Group_A7  = ["كرسي المساعد الأمامي", "مساعد"]
Group_A8  = ["كرسي المساعد الخلفي", "مساعد"]
Group_A9  = ["رمان كرسي المساعد", "مساعد"]
Group_A10 = ["عامود توازن"]
Group_A11 = ["مسمار توازن أمامي", "مسمار توازن", "مسامير توازن", "مسمار التوازن", "مسامير التوازن"]
Group_A12 = ["مسمار توازن خلفي", "مسمار توازن", "مسامير توازن", "مسمار التوازن", "مسامير التوازن"]
Group_A13 = ["العكس اليسار", "عكس", "عكوس"]
Group_A14 = ["العكس اليمين", "عكس", "عكوس"]
Group_A15 = ["المقص الأمامي", "مقص"]
Group_A16 = ["لينك أفقي", "مقص"]
Group_A17 = ["مقص خلفي علوي", "مقص"]
Group_A18 = ["المقص الخلفي السفلي", "مقص"]
Group_A19 = ["لينك عمودي", "مقص"]
Group_A20 = ["صاجة المكين", "صاجه المكين", "صاجه مكين", "صاجة مكين"]
Group_A21 = ["ذراع دركسون داخلي", "ذراع الدركسون", "ذراع دركسون", "ذراع الداخلي"]
Group_A22 = ["ذراع دركسون خارجي", "ذراع الدركسون", "ذراع دركسون", "ذراع الخارجي"]
Group_A23 = ["دودة الدركسون", "دوده", "دودة", "علبة الدركسون", "علبه الدركسون", "علبة دركسون", "علبه دركسون"]
Group_A24 = ["", ""]
Group_A25 = ["", ""]

#_________________________________________________________________


#"🔵 قطع مكينة-قير-حساسات-بلوف"          
L2= "🔵 قطع مكينة-قير-حساسات-بلوف"
Group_B1  = ["الكويل", "كويل"]
Group_B2  = ["البواجي", "بواجي", "بوجي"]
Group_B3  = ["بوابه", "بوابة", "ثروتل"]
Group_B4  = ["البخاخات", ""]
Group_B5  = ["empty...", ""]
Group_B6  = ["empty...", ""]
Group_B7  = ["حساس MAF", "حساس الماف", "حساس كميه الهوا", "حساس كمية الهوا", "حساس maf", "حساس Maf"]
Group_B8  = ["حساس MAP", "حساس ضغط ثلاجة المكينة", "حساس الماب", "حساس map", "حساس Map" , "حساس ضغط"  , "حساس الضغط"]
Group_B9  = ["حساس الكرنك", "حساس كرنك"]
Group_B10 = ["حساس الكام", "حساس كام"]
Group_B11 = ["حساس الأكسجين فوق", "حساس الاكسجين", "حساس أكسجين", "حساس اكسجين",  "حساس الشكمان",  "حساس الأكسجين", "حساس شكمان", "حساس دبة",  "حساس دبه",  "حساس الدبه", "حساس الدبة" ]
Group_B12 = ["حساس الأكسجين تحت", "حساس الاكسجين", "حساس أكسجين", "حساس اكسجين",  "حساس الشكمان",  "حساس الأكسجين", "حساس شكمان", "حساس دبة",  "حساس دبه",  "حساس الدبه", "حساس الدبة" ]
Group_B13 = ["حساس الطرق", "حساس طرق"]
Group_B14 = ["حساسات الايرباق", "حساس ايرباق" , "حساس الايرباق"  , "حساس الإيرباق"  ,  "حساس إيرباق"]
Group_B15 = ["حساس ضغط زيت", "حساس ضغط"  , "حساس الضغط"]
Group_B16 = ["حساس حرارة المكينة", "حساس حرار",  "حساس الحرار"]
Group_B17 = ["حساس حرارة الجو"   , "حساس حرار",  "حساس الحرار"]
Group_B18 = ["حساس حرارة المكيف" , "حساس حرار",  "حساس الحرار"]
Group_B19 = ["حساس Abs أمامي", "حساس ABS", "حساس Abs", "حساس abs", "حساس سرع", "حساس السرع", "حساس ال أي", "حساس ال اي", "حساس أي بي" , "حساس اي بي"]
Group_B20 = ["حساس Abs خلفي" , "حساس ABS", "حساس Abs", "حساس abs", "حساس سرع", "حساس السرع", "حساس ال أي", "حساس ال اي", "حساس أي بي" , "حساس اي بي"]
Group_B21 = ["حساس موضع القير", ""]
Group_B22 = ["حساس سرعة القير",                             "حساس سرع", "حساس السرع"]
Group_B23 = ["حساس TSS", "حساس سرعة التوربين", "حساس tss", "حساس سرع", "حساس السرع"]
Group_B24 = ["حساس الاصطفاف", ""]
Group_B25 = ["حساس تيار البطارية", "حساس التيار" ,"حساس تيار" ]
Group_B26 = ["حساس تيار الدينمو" , "حساس التيار" ,"حساس تيار" ]
Group_B27 = ["حساس ضغط التانكي",  "حساس ضغط"  , "حساس الضغط"]
Group_B28 = ["حساس ضغط البنزين المنخفض", "حساس ضغط"  , "حساس الضغط"]
Group_B29 = ["حساس كمية البنزين", ""]   ################################ need fix
Group_B30 = ["حساس ضغط الكفر", "حساس ضغط"  , "حساس الضغط"]
Group_B31 = ["حساس الدعسة",                                                      "حساس الدعس", "حساس دعس","حساس الفرامل", "حساس فرامل","حساس البريك", "حساس بريك"]
Group_B32 = ["حساس سحب معزز الفرامل", "حساس الباكم", "حساس باكم",              "حساس الدعس", "حساس دعس","حساس الفرامل", "حساس فرامل","حساس البريك", "حساس بريك"]
Group_B33 = ["حساس دعسة الفرامل",                                                "حساس الدعس", "حساس دعس","حساس الفرامل", "حساس فرامل","حساس البريك", "حساس بريك"]
Group_B34 = ["حساس موية المساحات", "حساس المساح", "حساس مساح", "حساس موية المساح", "حساس مويه المساح", "حساس موية مساح", "حساس مويه مساح"]
Group_B35 = ["حساس ضوء", "حساس النور", "حساس نور", "حساس الضوء"]
Group_B36 = ["empty...", ""]
Group_B37 = ["بلف EGR", "بلف egr", "اي جي ار"]
Group_B38 = ["بلف VVT", "بلف vvt"]
Group_B39 = ["بلف بخار المكين", "PCV", "Pcv", "pcv",                   "بلف تبخير", "بلف بخار", "بلف التبخير", "بلف البخار"]
Group_B40 = ["بلف بخار البنزين",                                       "بلف تبخير", "بلف بخار", "بلف التبخير", "بلف البخار"]
Group_B41 = ["طرمبة البنزين"   , "طرمبه البنزين", "طرمبة بنزين", "طرمبه بنزين", "مضخة البنزين", "مضخه البنزين", "مضخة بنزين", "مضخه بنزين"]
Group_B42 = ["مضخة زيت المكينة", "طرمبه الزيت", "طرمبة زيت", "طرمبه زيت", "مضخة الزيت", "مضخه الزيت", "مضخة زيت", "مضخه زيت"] 
Group_B43 = ["طنجرة القير","طنجر"]
Group_B44 = ["مقبض القير", "مسكة القير", "مسكة قير" , "مسكه القير" , "مسكه قير" , "مقبض قير"]
Group_B45 = ["مبرد القير", "مبرد قير"]
Group_B46 = ["بدي فالف", "صمامات القير"]
Group_B47 = ["معيار زيت", "معيار", "المعيار"]
Group_B48 = ["حساس ضغط الفريون العالي"] ################################ need fix
Group_B49 = ["بلف expansion المكيف", ""]
Group_B50 = ["مضخة موية المساحات", "مضخه مساح","مضخة مساح","طرمب مساح","طرنب مساح","دينمو مساح",   "مضخه المساح","مضخة المساح","طرمب المساح","طرنب المساح","دينمو المساح"  , "دنمو المساح" , "دنمو مساح" ]
Group_B51 = ["دينمو محرك المساحات", "مضخه مساح","مضخة مساح","طرمب مساح","طرنب مساح","دينمو مساح",   "مضخه المساح","مضخة المساح","طرمب المساح","طرنب المساح","دينمو المساح"  , "دنمو المساح" , "دنمو مساح"]
Group_B52 = ["", ""]
#_________________________________________________________________


#"🟤 ربلات - جلد - صوف   
Group_C1  = ["جلد غطا البلوف","جلده غطا البلوف","جلدة غطا البلوف","جلد غطى البلوف","جلده غطى البلوف","ربلة غطى البلوف", "ربلات غطا البلوف","ربله غطا البلوف","ربلة غطا البلوف","ربلات غطى البلوف","ربله غطى البلوف","ربلة غطى البلوف","جلدة غطى البلوف","جلدة غطا البلوف","جلبة غطا البلوف","جلبه غطا البلوف","جلبة غطى البلوف","جلبه غطى البلوف","","",""]
Group_C2  = ["جلدة بلف التيمن","جلده بلف التيمن","ربلة بلف التيمن","ربله بلف التيمن","","","","","","","","","","","","","","","","",""]
Group_C3  = ["صوف المكينة","","",""]
Group_C4  = ["صوف القير","","",""] 
Group_C5  = ["جلبة عصا القير","جلبه عصا القير","جلبة عصى القير","ربله عصى القير","جلدة عصا القير","ربله عصا القير","جلدة عصى القير","ربله عصى القير","جلدة عصى القير","جلدة عصا القير","جلدة عصا القير","جلدة عصى القير","جلدة عصى القير","","","","","","","",""]
Group_C6  = ["صوفة فلتر الزيت","","",""]
Group_C7  = ["جلد ثلاجة المكينة"]
Group_C8  = ["صوفة EGR", "","", "", ""]
Group_C9  = ["ربلة البوابة", "ربله البواب", "ربلة البواب",  "جلد البواب", "جلدة البواب",  "جلده البواب",      "ربله بواب", "ربلة بواب",  "جلد بواب", "جلدة بواب",  "جلده بواب",     "ربله الثروتل", "ربلة الثروتل",  "جلد الثروتل", "جلدة الثروتل",  "جلده الثروتل",        "ربله ثروتل", "ربلة ثروتل",  "جلد ثروتل", "جلدة ثروتل",  "جلده ثروتل"  ]
Group_C10 = ["انبوب سحب البوابة", "خرطوش الثروتل", "انبوب الثروتل",  "أنبوب الثروتل", "هوز الثروتل",  "خرطوش البواب", "انبوب البواب",  "أنبوب البواب", "هوز البواب",         "خرطوش ثروتل", "انبوب ثروتل",  "أنبوب ثروتل", "هوز ثروتل",       "خرطوش بواب", "انبوب بواب",  "أنبوب بواب", "هوز بواب", ]
Group_C11 = ["جلدة طرمبة البنزين","ربله طرمبه البنزين","ربلة طرمبه البنزين","ربله طرمبة البنزين","ربلة طرمبة البنزين"]
Group_C12 = ["جلدة طرمبة الماء","ربله طرمبه المو","ربلة طرمبه المو","ربله طرمبة المو","ربلة طرمبة المو"]
Group_C13 = ["جلدة قسام الرديتر"]
Group_C14 = ["جلدة عمود توازن","جلده عمود توازن","جلدة عمود التوازن","جلده عمود الوازن", "جلد عمود توازن","جلد عمود توازن","","","","","","","","","","","","","","",""]
Group_C15 = ["ربلات الدودة","ربله دود","ربلة دود"]
Group_C16 = ["صوفة العكس اليسار","صوفه العكس اليسار"]
Group_C17 = ["مساحات الزجاج","مساح"] 
Group_C18 = ["فتحه تهويه الشنطه",""]
Group_C19 = ["صوفة الباكم",""]
Group_C20 = ["","","",""]
Group_C21 = ["","","",""]
Group_C22 = ["","","",""]


#"🟡 نظام تبريد الرديتر"
Group_D1  = ["طرمبة الموي", "طرمبه الموي", "طرمبة الماء", "طرمبه الماء", "مضخة الموي", "مضخه الموي", "مضخة الماء", "مضخه الماء", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D2  = ["غطاء القرب", "غطا القرب", "غطى القرب", "غطاء قرب", "غطا قرب", "غطى قرب"]
Group_D3  = ["قربه مويه", "قربة موية", "قربه موية", "قربة مويه", "قربه مويه", "قربة الموية", "قربه الموية", "قربة المويه", "خزان رديتر", "قربة رديتر", "قربه الرديتر", "قربة الرديتر", "", "", "", "", "", "", "", "", "", ""]
Group_D4  = ["بلف الحرار", "بلف حرار"]
Group_D5  = ["قسام رديتر", "قسام الرديتر", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D6  = ["مروحه الرديتر", "مروح", "مراوح", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D7  = ["غطا التصريف", "غطا تصريف", "غطى التصريف", "غطى تصريف", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D8  = ["مبرد القير", "مبرد قير", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D9  = ["ماء رديتر", "موية رديتر", "مويه رديتر", "ماء الرديتر", "موية الرديتر", "مويه الرديتر", "سائل التبريد", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D10 = ["رديتر", "الرديتر", "رادييتر", "الرادييتر", "راديتر", "الراديتر", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D11 = ["لي السخان", "لي سخان"]
Group_D12 = ["لي راجع طويل", "اللي الراجع الطويل", "لي راجع الطويل"]
Group_D13 = ["لي راجع قصير", "اللي الراجع القصير", "لي راجع القصير"]
Group_D14 = ["Upper Hose", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D15 = ["Lower Hose", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D16 = ["radiator coolant hose", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D17 = ["radiator coolant hose connection water - outlet", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D18 = ["لي مزدوج يشبك بالقسام", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D19 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_D20 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


#"🟢 نظام التكييف"
Group_E1  = ["كلتش الكومبروسر", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E2  = ["كومبروسر", "الكومبروسر", "كمبرس", "كومبرس", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E3  = ["ثلاجة المكيف", "ثلاجه المكيف", "ثلاجة مكيف", "ثلاجه مكيف", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E4  = ["المكثف", "المكثف", "مكثف", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E5  = ["مروحه المكيف","مروح", "مراوح", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E6  = ["منظم مروحة المكيف", "مروح", "مراوح", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E7  = ["السخان", "سخان", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E8  = ["قسام حرار", "منظم حرار", "قسام الحرار", "منظم الحرار",     "قسام مكيف", "قسام المكيف", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E9  = ["قسام توزيع", "منظم توزيع", "قسام التوزيع", "منظم التوزيع", "قسام مكيف", "قسام المكيف", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E10 = ["قسام تدوير", "منظم تدوير", "قسام التدوير", "منظم التدوير", "قسام مكيف", "قسام المكيف", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E11 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E12 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E13 = ["انبوب الثلاجة", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E14 = ["لي الحار", "اللي الحار", "لي المكيف الحار", "لي فريون حار", "لي الفريون الحار", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E15 = ["refrigerant liquid Tube", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E16 = ["refrigerant suction Hose Inlet", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Group_E17 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


#"⚪️ الفرامل وملحقاتها"
Group_F1  = ["أقمشة أمامي",  "أقمش","اقمش","فحم"  ]
Group_F2  = ["أقمشة خلفي",   "أقمش","اقمش","فحم"  ]
Group_F3  = ["هوب امامي",    "الهوب","هوب","","","","","","","","","","","","","","","","","","" ]
Group_F4  = ["هوب خلفي" ,    "الهوب","هوب","","","","","","","","","","","","","","","","","","" ]
Group_F5  = ["دينمو الكليبرات","دينمو كليب","دنمو الكليب","دنمو كليب","دينمو كليب","","","","","","","","","","","","","","","","" ]
Group_F6  = ["مضخة ABS","طرمبه الabs","مضخه abs","مضخة abs","","","","","","","","","","","","","","","","","" ]
Group_F7  = ["حديدة الكليبر الامامي",    "حديدة الكليبر","","","","","","","","","","","","","","","","","","","" ]
Group_F8  = ["حديدة الكليبر الخلفي",    "حديدة الكليبر","","","","","","","","","","","","","","","","","","","" ]
Group_F9  = ["كليبر امامي",  "الكليبر","كليبر","","","","","","","","","","","","","","","","","","" ]
Group_F10 = ["كليبر خلفي",   "الكليبر","كليبر","","","","","","","","","","","","","","","","","","" ]
Group_F11 = ["فلنجة امامي",  "الفلنجات","فلنج","","","","","","","","","","","","","","","","","","" ]
Group_F12 = ["فلنجة خلفي",   "الفلنجات","فلنج","","","","","","","","","","","","","","","","","","" ]
Group_F13 = ["قربة زيت الفرامل","قربة زيت فرامل","قربه زيت فرامل","قربة زيت الفرامل","قربه زيت الفرامل","","","","","","","","","","","","","","","","" ]
Group_F14 = ["غطا زيت الفرامل","","","","","","","","","","","","","","","","","","","","" ]
Group_F15 = ["معزز الفرامل" ,"باكم","","","","","","","","","","","","","","","","","","","" ]
Group_F16 = ["brake vacum hose supply hose","","","","","","","","","","","","","","","","","","","","" ]
Group_F17 = ["لي فرامل امامي","لي الفرامل","لي فرامل","","","","","","","","","","","","","","","","","","" ]
Group_F18 = ["لي فرامل خلفي","لي الفرامل","لي فرامل","","","","","","","","","","","","","","","","","","" ]
Group_F19 = ["سويتش البريك","","","","","","","","","","","","","","","","","","","","" ]
Group_F20 = ["","","","","","","","","","","","","","","","","","","","","" ]


#"🟣 سيور- بكرات - شداد"
Group_G1  = ["شداد","الشداد","شداد سير","شداد السير","","","","","","","","","","","","","","","" ]
Group_G2  = ["سير المحرك الخارجي",   "سير",   "سيور","","","","","","","","","","","","","","","" ]
Group_G3  = ["سير المكيف",            "سير",  "سيور","","","","","","","","","","","","","","","","","","" ]
Group_G4  = ["بكرة الايدل","","","","","","","","","","","","","","","","","","","","" ]
Group_G5  = ["بكرة الدينمو","بكره الدينمو","بكرة دينمو","بكره دينمو","بكره دنمو","","","","","","","","","","","","","","","","" ]
Group_G6  = ["بكرة طرمبه الموية","بكره طرمب","بكره الطرمب","بكرة طرمب","بكرة الطرمب","","","","","","","","","","","","","","","","","" ]
Group_G7  = ["بكرة الكرنك","بكره الكرنك","بكرة حساس الكرنك","بكره حساس الكرنك","","","","","","","","","","","","","","","","","" ]
Group_G8  = ["جنزير التيمن","جنزير تيمن","","","","","","","","","","","","","","","","","","","" ]
Group_G9  = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_G10 = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_G11 = ["","","","","","","","","","","","","","","","","","","","","" ]


#"⚫️ نظام الشحن + نظام التشغيل"  
Group_H1  = ["اصباع بطارية سالب","","","","","","","","","","","","","","","","","","","","" ]
Group_H2  = ["ظفيرة بطارية موجب","","","","","","","","","","","","","","","","","","","","" ]
Group_H3  = ["البطارية","","","","","","","","","","","","","","","","","","","","" ]
Group_H4  = ["الدينمو","دينمو","","","","","","","","","","","","","","","","","","","" ]
Group_H5  = ["السلف","سلف","","","","","","","","","","","","","","","","","","","" ]
Group_H6  = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_H7  = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_H8  = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_H9  = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_H10 = ["","","","","","","","","","","","","","","","","","","","","" ]


#"🟠 زيوت-فلاتر-منظفات"
Group_J1  = ["فلتر الزيت","فلتر زيت مكين","فلتر زيت المكين","سيفون المكين","سيفون مكين","","","","","","","","","","","","","","","","" ]
Group_J2  = ["فلتر القير","فلتر زيت قير","فلتر زيت القير","فلتر قير","سيفون القير","سيفون قير","","","","","","","","","","","","","","","" ]
Group_J3  = ["فلتر المكيف",        "فلتر هوا", "فلتر الهوا" ,  ""  , "" ]
Group_J4  = ["فلتر هوا المكينة",  "فلتر هوا", "فلتر الهوا" ,  ""  , "" ]
Group_J5  = ["فلتر بنزين","فلتر البنزين","سيفون البنزين","سيفون بنزين","","","","","","","","","","","","","","","","","" ]
Group_J6  = ["فلتر الفريون","فلتر الرديتر","فلتر رديتر","","","","","","","","","","","","","","","","","","" ]
Group_J7  = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_J8  = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_J9  = ["زيت المكين","الزيت حق المكين","زيت مكين","","","","","","","","","","","","","" ]
Group_J10 = ["زيت القير","الزيت حق القير","زيت قير","","","","","","","","","","","","","","","","","" ]
Group_J11 = ["زيت الفرامل","زيت فرامل","سائل الفرامل","سائل فرامل","الزيت حق الفرامل","","","","","","","","","","","","","","","","" ]
Group_J12 = ["","","","","","","","","","","","","","","","","","","","","" ]


#"✳️ نظام التوجية"
Group_K1  = ["شريحة البوري","","","","","","","","","","","","","","","","","","","","" ]
Group_K2  = ["بوري","هرن","البوري","الهرن","","","","","","","","","","","","","","","","","" ]
Group_K3  = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_K4  = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_K5  = ["Transceiver - Immobilizer Module","","","","","","","","","","","","","","","","","","","","" ]
Group_K6  = ["Ignition Switch" ,"","","","","","","","","","","","","","","","","","","","" ]
Group_K7  = ["Ignition Lock Cylinder" ,"","","","","","","","","","","","","","","","","","","","" ]
Group_K8  = ["الطارة","","","","","","","","","","","","","","","","","","","","" ]
Group_K9  = ["أزارير يسار","","","","","","","","","","","","","","","","","","","","" ]
Group_K10 = ["أزارير يمين","","","","","","","","","","","","","","","","","","","","" ]
Group_K11 = ["سويتش المساحات","","","","","","","","","","","","","","","","","","","","" ]
Group_K12 = ["سويتش الغمازات","","","","","","","","","","","","","","","","","","","","" ]
Group_K13 = ["","","","","","","","","","","","","","","","","","","","","" ]
Group_K14 = ["","","","","","","","","","","","","","","","","","","","","" ]


#"💠 بودي-اقفال-نظام الترفية وغيرها"
Group_L1 =[f"{X}","","","","","","","","","","","","","","","","","","","","" ]
Group_L2 =["","","","","","","","","","","","","","","","","","","","","" ]
Group_L3 =["","","","","","","","","","","","","","","","","","","","","" ]
Group_L4 =["","","","","","","","","","","","","","","","","","","","","" ]
Group_L5 =["","","","","","","","","","","","","","","","","","","","","" ]
Group_L6 =["","","","","","","","","","","","","","","","","","","","","" ]
Group_L7 =["","","","","","","","","","","","","","","","","","","","","" ]
Group_L8 =["","","","","","","","","","","","","","","","","","","","","" ]
Group_L9 =["","","","","","","","","","","","","","","","","","","","","" ]
Group_L10=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L11=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L12=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L13=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L14=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L15=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L16=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L17=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L18=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L19=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L20=["","","","","","","","","","","","","","","","","","","","","" ]
Group_L21=["","","","","","","","","","","","","","","","","","","","","" ]


#أسعار وأرقام وصور ومواقع القطع الإستهلاكية 
L1= "🔴 عضلات السيارة"
L2= "🔵 قطع مكينة وقير - حساسات وبلوف"
L3= "🟤 جلد - ربلات - صوف" 
L4= "🟡 تبريد الرديتر"
L5= "🟢 تبريد المكيف"
L6= "⚪️ البريك وملحقاتة"
L7= "🟣 سيور - بكرات"
L8= "⚫️ الشحن والتشغيل"
L9= "🟠 زيوت - فلاتر"
L10="✳️ مجموعة الدركسون"
L11="💠 البودي والداخلية والإضائة"


# 🛠️ أسعار وأرقام وصور ومواقع القطع الإستهلاكية ا
group_headers = {
    "L1":  "🔴 عضلات السيارة",
    "L2":  "🔵 قطع مكينة وقير - حساسات وبلوف",
    "L3":  "🟤 جلد - ربلات - صوف",
    "L4":  "🟡 تبريد الرديتر",
    "L5":  "🟢 تبريد المكيف",
    "L6":  "⚪️ البريك وملحقاتة",
    "L7":  "🟣 سيور - بكرات",
    "L8":  "⚫️ الشحن والتشغيل",
    "L9":  "🟠 زيوت - فلاتر",
    "L10": "✳️ مجموعة الدركسون",
    "L11": "💠 البودي والداخلية والإضائة"}
# 🛠️ ربط الحروف القديمة (A-L) بالمجموعات الجديدة (L1-L11)
group_mapping = {
    "A": "L1", "B": "L2", "C": "L3", "D": "L4",
    "E": "L5", "F": "L6", "G": "L7", "H": "L8",
    "J": "L9", "K": "L10", "L": "L11"}


# ويكونو بنفس تسلسل ترتيب القطع   مهم جداا  اذا ضفت شي هنا لازم تضيفه فوق ايضا  
# Part_Location_group  الجدول الي تحت ايضا متعلق بايجاد مواقع القطع كل الي عليك تكمل البيانات وتحط صوره بالملف ب اسم القطعه مثل هنا بالضبط في خانه

# kkkk                                                    
#🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴 نظام التعليق (عضلات وكل شي اسفل السيارة)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
Parts_Group_A        =               [           "كرسي المكينة"                 ,       "قاعدة كرسي قير السلفية"   ,       "كرسي قير علوي"                      ,          "كرسي قير سفلي"                              ,          "المساعد الأمامي"                       ,       "المساعد الخلفي"                                        ,       "كرسي مساعد أمامي"                   ,        "كرسي مساعد خلفي"             ,         "رمان كرسي مساعد"                     ,              "عمود التوازن"                 ,       "مسمار توازن أمامي"          ,      "مسمار توازن خلفي"           ,           "عكس يسار"               ,           "عكس يمين"              ,           "مقص أمامي"              ,          "لينك أفقي"              ,     "مقص خلفي علوي"                ,              "مقص خلفي كبير سفلي"                                                                   ,         "لينك عمودي"                             ,        "بطانة المكينة"            ,       "ذراع دركسون داخلي"            ,      "ذراع دركسون خارجي"                       ,          "دودة الدركسون"              ,              ""                 ,              ""                     ] 
Parts_numbers_group_A=               [           "DG9Z-6038-H"                   ,          "JG9Z-6E042-C"            ,       "GG9Z-6068-A"                         ,           "DP5Z-6068-A"                               ,"\n(يمين) HG9Z-18124-A\n(يسار) HG9Z-18124-F"      ,           "DG9Z-18125-U"                                       ,          "DG9Z-3A197-AB"                    ,          "DG9Z-18A161-C"              ,          "DG9Z-18198-A"                        ,               "DG9Z-5482-D"                   ,        "DG9Z-5K484-A"               ,        "DG9Z-5C486-A"              ,         "HG9Z-3B437-B"              ,          "HG9Z-3B436-E"           ,    "GS7Z-3078-B\nGS7Z-3079-B"       ,          "DG9Z-5K898-B"            ,        "DG9Z-5500-Q"                ,    "يسار GS7Z-5500-C\nيمين GS7Z-5500-J"                                                             ,          "DG9Z-5A972-A"                           ,        "DG9Z-6P013-E"              ,         "DG9Z-3280-A"                  ,"L: DG9Z-3A130-B\nR: DG9Z-3A130-A"               ,          "KG9z-3504-G"                 ,               ""                ,               ""                    ]
Parts_prices_group_A =               [  [ 440,460,420,430,370,550 ]              ,   [ "?","?","?","?","?","?" ]      ,   [240,220,270,240,210,200]                 ,   [ 160,170,180,140,145,180 ]                         ,   [ 260,290,350,310,280,"?" ]                     ,   [ 210,190,290,180,"?","?" ]                                  ,   [ 80,110,100,130,"?","?" ]                ,   [ "?","?","?","?","?","?" ]         ,   [ 75,80,100,60,"?","?" ]                     ,   [ "?","?","?","?","?","?" ]                 ,   [ 45,70,70,120,"?","?" ]          ,   [ 57,"?","?","?","?","?" ]       ,   [ 700,780,720,800,"?","?" ]       ,   [ 700,850,"?","?","?","?" ]     ,   [ 430,360,480,440,440,750 ]       ,   [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]       ,   [ "جهه اليسار\n(بالعادة اغلى)\n",1100,1060,"\n\nجهه اليمين\n", 730,750 ]                        ,   [ "?","?","?","?","?","?" ]                     ,   [ 630,620,570,600,1000,"?" ]     ,   [ 195,"?","?","?","?","?" ]          ,   [ 100,100,"?","?","?","?" ]                   ,   [ 4000,"?","?","?","?","?" ]         ,   [ "?","?","?","?","?","?" ]   ,   [ "?","?","?","?","?","?" ]       ] 
Part_Location_group_A=               [          "Engine Mount"                   ,     "Lower Trans mount support"    ,   "Transmission Mounts"                     ,    "Transmission Mounts"                              ,     "Front Struts System"                         ,      "rear Struts System"                                      ,       "Front Struts System"                 ,    "rear Struts System"               ,   "Front Struts System"                        ,            ""                                 ,         "front susp"                ,       "Rear Stabilizer"            ,    "Front Axle Drive"               ,        "Front Axle Drive"         ,     "front susp"                    ,           "Rear susp"              ,      "Rear susp"                    ,                "Rear susp"                                                                           ,      "Rear susp"                                  ,  "Splash shield air deflector"     ,             "Steering Gear"            ,               "Steering Gear"                   ,    "Steering Gear"                     ,             ""                  ,             ""                      ]
How_2_Change_A_Link1 =escape_links(  [  "                            "           ,  "                            "    , "                            "              , "                            "                        ,  "https://youtu.be/37mUTF18b2M"                   ,  "https://youtu.be/lZgS2F3dlYo"                                , "                            "              ,  "https://youtu.be/ViFZ8uEXcFE"       ,  "                            "                ,  "                            "               ,  "https://youtu.be/gkaXn1M-hjs"     ,  "https://youtu.be/OV4jy1Umk4c"    ,  "https://youtu.be/_oRljRzZWJY"     ,  "                            "   ,  "https://youtu.be/Rq7MOwM4PRg"     ,  "                            "    ,  "                            "     ,  "                            "                                                                      ,  "                            "                   ,  "                            "    ,  "https://youtu.be/AbL9HUqPSws"        ,  "https://youtu.be/BiV51VF74mg"                 ,  "https://youtu.be/F8ssaEYSHhw"        , "                            "  ,  "                            "     ])
How_2_Change_A_Link2 =escape_links(  [  "                            "           ,  "                            "    , "                            "              , "                            "                        ,  "https://youtu.be/At8qnEjFD0M"                   ,  "https://youtu.be/VgmkbOiDJQY"                                , "                            "              ,  "                            "       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "https://youtu.be/TJtQUshlFK8"     ,  "                            "   ,  "https://youtu.be/zPhMhNGfG_4"     ,  "                            "    ,  "                            "     ,  "                            "                                                                      ,  "                            "                   ,  "                            "    ,  "                            "        ,  "                            "                 ,  "                            "        , "                            "  ,  "                            "     ])
How_2_Change_A_Link3 =escape_links(  [  "                            "           ,  "                            "    , "                            "              , "                            "                        ,  "https://youtu.be/RYkUeQjVTg0"                   ,  "                            "                                , "                            "              ,  "                            "       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "https://youtu.be/RukdxCnsCuU"     ,  "                            "   ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "                                                                      ,  "                            "                   ,  "                            "    ,  "                            "        ,  "                            "                 ,  "                            "        , "                            "  ,  "                            "     ])
How_2_Change_A_Link4 =escape_links(  [  "                            "           ,  "                            "    , "                            "              , "                            "                        ,  "https://youtu.be/Yt3C-v-7SHA"                   ,  "                            "                                , "                            "              ,  "                            "       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "   ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "                                                                      ,  "                            "                   ,  "                            "    ,  "                            "        ,  "                            "                 ,  "                            "        , "                            "  ,  "                            "     ])

#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________-
#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________-
#🔵 قطع المكينة والقير + حساسات  +  بلوف  + مضخات                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
Parts_Group_B        =               [           "الكويل"                        ,           "بواجي"                 ,           "البوابة"                        ,        "البخاخات"                                     ,                ""                                 ,             ""                                                 ,              "حساس MAF"                    ,   "حساس MAP"                          ,              "حساس الكرنك"                    ,         "حساس الكام"                         ,        "حساس أكسجين فوق"           ,        "حساس أكسجين تحت"          ,             "حساس الطرق"           ,          "حساسات الايرباق"        ,   "حساس ضغط زيت المكينة"          ,     "حساس حرارة المكينة"          ,    "حساس حرارة الجو"               ,          "حساس حرارة المكيف"                                                                        ,            "حساس ABS أمامي"                     ,     "حساس ABS خلفي"                ,     "حساس موضع القير"                 ,         "حساس سرعة القير"                     ,      "حساس سرعة التوربين"             ,            "حساس الاصطفاف"       ,       "حساس تيار البطارية"           ,   "حساس تيار الدينمو"                 ,        "حساس ضغط التانكي"       ,       "حساس ضغط بنزين low"                      ,     "حساس كمية البنزين"             ,      "حساس ضغط الكفر"           ,    "حساس الدعسة"                  ,   "حساس الباكم"                             ,        "حساس دعسة الفرامل"       ,         "حساس ماء المساحات"       ,        "حساس ضوء الشمس"            ,           "..."                          ,           "بلف EGR"                         ,          "بلف VVT"                   ,       "بلف بخار المكينة"                              ,       "بلف بخار البنزين"             ,      "طرمبه بنزين"                   ,    "مضخة زيت المكينة"           ,     "طنجرة القير"                 ,        "مقبض القير"                      ,      "مبرد القير"                           ,    "بدي فالف والصمامات"            ,      "معيار زيت المكينة"            , "حساس ضغط الفريون المرتفع"               , "بلف expansion المكيف"              ,       "مضخة موية المساحات"                         ,       "دينمو محرك المساحات"                      ,             ""                           ]   
Parts_numbers_group_B=               [         "9E5Z-12029-A"                    ,       "SP530X"                     ,         "DS7Z-9E926-D"                      ,         "9E5Z-9F593-A"                                ,              ""                                   ,              ""                                                ,               "BR3Z-12B579-A"               ,   "1S7Z-9F479-AD"                     ,               "5M6Z-6C315-A"                   ,         "6M8Z-6B288-D"                        ,           "EJ5Z-9F472-B"            ,          "CJ5Z-9G444-B"            ,       "1S7Z-12A699-BB"              ,           "AIRBAGS_NUMBERS"       ,        "G1CZ-9278-B"                ,        "8S4Z-6G004-A"              ,      "AU5Z-12A647-B"                ,          "CV6Z-19C734-A"                                                                             ,  "(يمين) JG9Z-2C204-A\n(يسار) JG9Z-2C205-A"      ,      "JG9Z-2C190-P"                ,        "GN1Z-7H557-B"                  ,            "CC3Z-7H103-B"                       ,        "DL8Z-7M101-A"                  ,          " DA5Z-15K859-AAPTM"    ,            "BT4Z-14B357-C"             ,    "BT4Z-14B357-B"                     ,              ""                  ,   "DG9Z-9J279-QH\nالحساس مدمج مع اللي"          ,         "DG9Z-9A299-H"               ,       "9L3Z-1A189-A"             ,      "DG9Z-9F836-D"                ,       "DE9Z-2C444-B"                         ,           "GL3Z-13480-A"          ,          "EM2Z-17B649-A"            ,         "DG9Z-13A018-B"             ,         ""                               ,         "1S7Z-9D475-A"                      ,       "CJ5Z-6M280-A"                  ,"البلف\n8S4Z-6A666-A\nالمجموعة كاملة\n9E5Z-6A785-B"    ,       "9U5Z-9C915-J"                  ,       "DG9Z-9H307-Z"                  ,        "8E5Z-6600-A"              ,     "9L8Z-7902-BRM"               ,        "DG9Z-7213-EA"                     ,      "DG9Z-7A095-A"                          ,            ""                        ,       "CV6Z-6750-A"                  ,         "HG1Z-19D594-A"                     ,   "DG9Z-19849-B"                    ,               "JL3Z-17664-A"                         ,              ""                                   ,              ""                          ]
Parts_prices_group_B =               [   [130,140,175,140,150,220 ]              ,   [105,110,115,120,90,"?"]         ,   [ 450,345,230,280,290,550 ]               ,   [ "?","?","?","?","?","?" ]                         ,   [ "?","?","?","?","?","?" ]                     ,   [ "?","?","?","?","?","?" ]                                  ,   [ "?","?","?","?","?","?" ]               ,   [ "?","?","?","?","?","?" ]         ,   [ "?","?","?","?","?","?"]                   ,        [ "?","?","?","?","?","?"]             ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]       ,      [ "?","?","?","?","?","?" ]  ,   [ 70,50,50,60,30,"?" ]            ,   [ "?","?","?","?","?","?" ]      ,   [ 70,55,"?","?","?","?" ]         ,      [ "?","?","?","?","?","?" ]                                                                     ,     [ 80,100,105,120,90,140 ]                     ,   [ "?","?","?","?","?","?" ]      ,    [ "?","?","?","?","?","?" ]         ,       [ "?","?","?","?","?","?" ]               ,   [ "?","?","?","?","?","?" ]          ,   [ "?","?","?","?","?","?" ]    ,      [ "?","?","?","?","?","?" ]       ,     [ "?","?","?","?","?","?" ]        ,     [ "?","?","?","?","?","?" ]  ,      [ "?","?","?","?","?","?" ]                 ,     [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]    ,  [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]                ,  [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]            ,   [ 660,"?","?","?","?","?" ]               ,   [ 220,135,"?","?","?","?" ]         ,   [ 125,100,"?","?","?",185 ]                           ,   [ 140,140,130,"?","?","?" ]         ,   [ 620,"?","?","?","?","?" ]         ,  [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]     ,  [ "?","?","?","?","?","?" ]              ,   [ "?","?","?","?","?","?" ]                ,   [ "?","?","?","?","?","?" ]        ,  [ "?","?","?","?","?","?" ]         ,    [ "?","?","?","?","?","?" ]              ,   [ 180,200,"?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]                        ,   [ "?","?","?","?","?","?" ]                     ,   [ "?","?","?","?","?","?" ]            ] 
Part_Location_group_B=               [             "Ignition"                    ,             "Ignition"             ,      "Intake Manifold"                      ,    "Fuel Injectors and Pipes"                         ,              ""                                   ,               ""                                               , "Air_Cleaner_filter_MAF_sensor"             ,     "Intake Manifold"                 ,             ""                                 ,     "CAM SENSOR location"                     ,          "O2_Sensors"               ,        "O2_Sensors"                ,    "Engine Knock Sensor_KS"         ,          "Airb_Sensors"           ,             ""                      ,     "Cylinder Head"                , "Ambient Air Temperature Sensor"    ,    "Air Conditioning Controls"                                                                       ,        "Wheel speed sensors"                      ,     "Wheel speed sensors"          , "Transmission Modules and Sensors"     ,    "Transmission Modules and Sensors"           ,  "Transmission Modules and Sensors"    ,       "Parking Aid Sensor"       ,       "Battery sensors"                ,    "Battery sensors"                   ,  "FTP_fuel tank pressure sensor" ,       "low_Fuel_pressure_sensor"                 ,   "Fuel tank assemply_fuel pump"     ,             ""                   ,             ""                     ,             ""                               ,             ""                    , "Windshield Washer_pump sensor"     ,     "Air Conditioning Controls"     ,               ""                         , "EGR_Exhaust Gas Recirculation"             ,             ""                        ,      "PCV valve"                                        ,    "Intake Manifold"                  , "Fuel tank assemply_fuel pump"        ,   "Oil Pump_timing chain"         ,     "Converter"                   ,          "Gear Change"                    , "Transmission Cooling System"                , "Transmission Control Assembly"      ,             ""                       ,        "ac clutch switch"                   ,             ""                      , "Windshield Washer_pump sensor"                      ,       "Wiper_Blade_motors"                        ,               ""                         ]
How_2_Change_B_Link1 =escape_links(  [  "https://youtu.be/5OBZnGoGdyQ"           , "https://youtu.be/5OBZnGoGdyQ"     , "https://youtu.be/K6G75GwBBjg"              ,  "                            "                       ,  "                            "                   ,  "                            "                                ,  "                            "             ,  "                            "       ,  "                            "                , "                            "                ,  "                            "     ,  "                            "    ,  "                            "     ,                ""                 , "                            "      ,  "                            "    ,  "                            "     ,                ""                                                                                    ,    "https://youtu.be/haoW4kv6UXM"                 ,  "https://youtu.be/r3uCYB1yd4U"    ,                ""                      ,                ""                               ,  "                            "        ,  "https://youtu.be/RTf9ebYC5u0"  ,                ""                      ,                ""                      ,                ""                ,                ""                                ,                ""                    ,  "                            "  ,  "                            "    ,  "                            "              ,  "                            "   ,  "                            "     ,  "                            "     ,  "                            "          ,  "https://youtu.be/Nt5-jCIi7Rc"             ,  "https://youtu.be/rAoqsf0u2EM"       ,  "https://youtu.be/b_Qs1EiYYvg"                         , "https://youtu.be/bNJ6MOoW4cI"        ,  "https://youtu.be/ljWQHz8jYTE"       ,  "                            "   ,  "                            "   , "                            "            ,              ""                              ,            ""                        ,  "                            "      ,  "                            "             ,  "                            "     ,  "                            "                      ,  "                            "                   ,  "                            "          ])
How_2_Change_B_Link2 =escape_links(  [  "                            "           , "                            "     , "https://youtu.be/ygr9OARe1TU"              ,  "                            "                       ,  "                            "                   ,  "                            "                                ,  "                            "             ,  "                            "       ,  "                            "                , "                            "                ,  "                            "     ,  "                            "    ,  "                            "     ,                ""                 , "                            "      ,  "                            "    ,  "                            "     ,                ""                                                                                    ,    "https://youtu.be/1SX6o4IUZvs"                 ,  "                            "    ,                ""                      ,                ""                               ,  "                            "        ,                ""                ,                ""                      ,                ""                      ,                ""                ,                ""                                ,                ""                    ,  "                            "  ,  "                            "    ,  "                            "              ,  "                            "   ,  "                            "     ,  "                            "     ,  "                            "          ,  "                            "             ,  "https://youtu.be/KRTfYEnqTfY"       ,  "https://youtu.be/diQ_dw38KF0"                         , "                            "        ,  "https://youtu.be/CvEraphc4Wg"       ,  "                            "   ,  "                            "   , "                            "            ,              ""                              ,            ""                        ,  "                            "      ,  "                            "             ,  "                            "     ,  "                            "                      ,  "                            "                   ,  "                            "          ])
How_2_Change_B_Link3 =escape_links(  [  "                            "           , "                            "     , "https://youtu.be/nTOl9Sif4KQ"              ,  "                            "                       ,  "                            "                   ,  "                            "                                ,  "                            "             ,  "                            "       ,  "                            "                , "                            "                ,  "                            "     ,  "                            "    ,  "                            "     ,                ""                 , "                            "      ,  "                            "    ,  "                            "     ,                ""                                                                                    ,    "https://youtu.be/mw2lMAM6y78"                 ,  "                            "    ,                ""                      ,                ""                               ,  "                            "        ,                ""                ,                ""                      ,                ""                      ,                ""                ,                ""                                ,                ""                    ,  "                            "  ,  "                            "    ,  "                            "              ,  "                            "   ,  "                            "     ,  "                            "     ,  "                            "          ,  "                            "             ,  "                            "       ,  "                            "                         , "                            "        ,  "                            "       ,  "                            "   ,  "                            "   , "                            "            ,              ""                              ,            ""                        ,  "                            "      ,  "                            "             ,  "                            "     ,  "                            "                      ,  "                            "                   ,  "                            "          ])
How_2_Change_B_Link4 =escape_links(  [  "                            "           , "                            "     ,  "https://t.me/fusion1/87647"               ,  "Resetting The Keep Alive Memory (KAM)."             ,  "                            "                   ,  "                            "                                ,"طريقة التنظيف:\nhttps://t.me/fusion1/52211",  "https://youtu.be/PipJqr_KVs0"       ,  "                            "                , "                            "                ,  "                            "     ,  "                            "    ,  "                            "     ,                ""                 , "                            "      ,  "                            "    ,  "                            "     ,                ""                                                                                    ,    "https://youtu.be/PAHkkCAwbpo"                 ,  "                            "    ,                ""                      ,                ""                               ,  "                            "        ,                ""                ,                ""                      ,                ""                      ,                ""                ,                ""                                ,                ""                    ,  "                            "  ,  "                            "    ,  "                            "              ,  "                            "   ,  "                            "     ,  "                            "     ,  "                            "          ,  "https://youtu.be/Nt5-jCIi7Rc"             ,  "                            "       ,  "                            "                         , "                            "        ,  "                            "       ,  "                            "   ,  "                            "   , "                            "            ,              ""                                           ""                        ,  "                            "      ,  "                            "             ,  "                            "     ,  "                            "                      ,  "                            "                   ,  "                            "          ])                                                      
#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________-
# ______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________-
#🟤ربلات جلد وصوف  + وهوزات وليات                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
Parts_Group_C        =               [      "جلد غطى البلوف"                    ,        "جلدة بلف التيمن"          ,         "صوف المكينة"                      ,          "صوف القير"                                 ,          "جلبة عصا القير"                        ,     "صوفة فلتر الزيت"                                         ,         "جلد ثلاجة المكينة"                ,     "صوفة بلف EGR"                    ,        "ربلة الثروتل"                         ,        "انبوب سحب البوابة"                   ,        "جلدة طرمبة البنزين"       ,       "جلدة طرمبة الماء"         ,    "جلدة قسام الرديتر"             ,         "جلده عمود توازن"        ,          "ربلات الدودة"             ,        "صوف العكس"                ,       "مساحات الزجاج"              ,                    "فتحه تهويه الشنطه"                                                              ,      "صوفة الباكم"                               ,              ""                     ,              ""                        ,              ""                                 ,              ""                        ,              ""                 ,              ""                         ,              ""                    ]  
Parts_numbers_group_C=               [        "CV6Z-6584-A"                      ,           "BR3Z-6C535-B"           ,               ""                            ,               ""                                      ,            "KV6Z-7k340-A"                         ,        "1S7Z-6840-AA"                                          ,       {INTAKE_MANI_GASKETS}                 ,        "1S7Z-9D476-AA"                ,       "8E5Z-9E936-A"                           ,       "DS7Z-9B659-B"                          ,          "4L3Z-9276-AA"             ,          "1S7Z-8507-AE"            ,       "6G9Z-8255-BA"                ,       {Bushing_STABILIZER}        ,  "DG9Z-3K661-A\nDG9Z-3332-A"        ,         ""                         ,  "يسار WW-2601\nيمين WW-2700"      ,                      "AG1Z61-280B62-A"                                                               ,       "DG9Z-2B022-A"                              ,               ""                    ,               ""                       ,               ""                                ,               ""                       ,               ""                ,               ""                        ,               ""                    ]
Parts_prices_group_C =               [   [90,80,130,120,"?","?"]                 ,   [ 40,25,40,35,"?","?" ]          ,   [ "?","?","?","?","?","?" ]               ,   [ "?","?","?","?","?","?"]                          ,   [ 8,10,10,10,12,"?" ]                           ,  [ "?","?","?","?","?","?" ]                                   ,      [ "?","?","?","?","?","?" ]            ,  [ "?","?","?","?","?","?" ]          ,   [ 40,"?","?","?","?","?" ]                   ,   [ "?","?","?","?","?","?" ]                 ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]       ,    [25,40,50,75,35,"?" ]          ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]      ,       [ 95,80,60,65,85,"?" ]        ,                  [ "?","?","?","?","?","?" ]                                                         ,   [ "?","?","?","?","?","?" ]                     ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]          ,   [ "?","?","?","?","?","?" ]                   ,   [ "?","?","?","?","?","?" ]          ,   [ "?","?","?","?","?","?" ]   ,   [ "?","?","?","?","?","?" ]           ,   [ "?","?","?","?","?","?" ]      ] 
Part_Location_group_C=               [     "Valve cover Gasket"                  ,        "Valve cover Gasket"        ,             ""                              ,             ""                                        ,             ""                                    ,            ""                                                  ,        "Intake Manifold"                    ,            ""                         ,             "Intake Manifold"                  ,             ""                                ,             ""                      ,             ""                     ,             ""                      ,           "front susp"            ,             ""                      ,             ""                     ,             ""                      ,                            ""                                                                        ,             ""                                    ,             ""                      ,             ""                         ,             ""                                  ,             ""                         ,             ""                  ,             ""                          ,             ""                     ]
How_2_Change_C_Link1 =escape_links(  [ "https://youtu.be/Y-aScxyk7pM"            , "                            "     ,  "                            "             ,  "                            "                       ,  "                            "                   , "                            "                                 , "                            "              , "                            "        ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "                            "     ,   "                            "  ,  "                            "     ,  "                            "    ,  "https://youtu.be/RHOxNYxViiA"     ,                 "                            "                                                       ,  "                            "                   ,  "                            "     ,  "                            "        ,  "                            "                 ,  "                            "        ,  "                            " ,  "                            "         ,  "                            "    ])
How_2_Change_C_Link2 =escape_links(  [ "https://youtu.be/WxO8wyWDEy8"            , "                            "     ,  "                            "             ,  "                            "                       ,  "                            "                   , "                            "                                 , "                            "              , "                            "        ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "                            "     ,   "                            "  ,  "                            "     ,  "                            "    ,  "https://youtu.be/5VQgVdZV--M"     ,                 "                            "                                                       ,  "                            "                   ,  "                            "     ,  "                            "        ,  "                            "                 ,  "                            "        ,  "                            " ,  "                            "         ,  "                            "    ])
How_2_Change_C_Link3 =escape_links(  [ "                            "            , "                            "     ,  "                            "             ,  "                            "                       ,  "                            "                   , "                            "                                 , "                            "              , "                            "        ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "                            "     ,   "                            "  ,  "                            "     ,  "                            "    ,  "https://youtu.be/lE-PBSZIayg"     ,                 "                            "                                                       ,  "                            "                   ,  "                            "     ,  "                            "        ,  "                            "                 ,  "                            "        ,  "                            " ,  "                            "         ,  "                            "    ])
How_2_Change_C_Link4 =escape_links(  [ "                            "            , "                            "     ,  "                            "             ,  "                            "                       ,  "                            "                   , "                            "                                 , "                            "              , "                            "        ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "                            "     ,   "                            "  ,  "                            "     ,  "                            "    ,"⚙️ لضبط الوزنية\nhttps://youtu.be/xzFGon2kN9Y",      "                            "                                                       ,  "                            "                   ,  "                            "     ,  "                            "        ,  "                            "                 ,  "                            "        ,  "                            " ,  "                            "         ,  "                            "    ])   
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#🟡 كل شي يخص نظام تبريد الرديتر                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
Parts_Group_D        =               [             "طرمبه المويه"               ,         "غطا القربة"              ,     "قربه مويه الرديتر"                   ,          "بلف الحرارة"                                ,         "قسام الرديتر"                           ,      "مراوح رديتر"                                            ,          "غطا تصريف رديتر"                 ,            "مبرد القير"              ,         "موية الرديتر"                        ,                "الرديتر"                     ,            "لي السخان"             ,       "لي راجع الطويل"            ,       "لي راجع القصير"             ,      "Upper Hose"                 ,              "Lower Hose"           ,      "radiator coolant hose"       ,         "water outlet hose"         ,      "لي مزدوج خاص بالقسام"                                                                        ,              ""                                   ,                ""                   ,             ""                      ]  
Parts_numbers_group_D=               [               "4S4Z-8501-E"               ,        "DG9Z-8100-A"               ,        "HG9Z-8A080-B"                       ,          "3M4Z-8575-B"                                ,          "6S4Z-8K556-A"                           ,       "DG9Z-8C607-J"                                           ,             "DG9Z-8115-A"                   ,            "DG9Z-7A095-A"             ,             "VC13G1"                           ,               "DG9Z-8005-K"                   ,           "DG9Z-18472-AA"           ,         "DG9Z-8063-D"              ,         "DG9Z-8075-C"               ,          "DG9Z-8260-DB"           ,               "DG9Z-8286-D"         ,           "G9Z8597A"               ,          "3M4Z8597AA"               ,            "18472A"                                                                                 ,               ""                                  ,              ""                     ,              ""                     ]
Parts_prices_group_D =               [       [ 200,230,"?","?","?","?" ]         ,   [ 15,25,20,35,30,"?" ]           ,   [ 250,300,300,300,320,320 ]               ,     [ 80,70,90,60,90,80 ]                             ,   [ 130,180,"?","?","?","?" ]                     ,   [ 620,670,720,880,"?","?" ]                                  ,   [ "?","?","?","?","?","?" ]               ,   [ "?","?","?","?","?","?" ]         ,    [100,80,80,85,"?","?" ]                     ,   [ "?","?","?","?","?","?" ]                 ,   [ 370,230,195,"?","?","?" ]       ,   [ 160,125,115,"?","?","?" ]      ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]     ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]                                                                       ,   [ "?","?","?","?","?","?"]                      ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]       ] 
Part_Location_group_D=               [                "Cooling System"           ,             "Cooling System"       ,             "Cooling System"                ,         "Thermostat"                                  ,             ""                                    ,             "Cooling System"                                   ,             ""                              ,             ""                        ,           ""                                   ,             ""                                ,           "Heater Hoses"            ,       "overflow hose 1"            ,             "overflow hose 2"       ,             ""                    ,             ""                      ,             ""                     ,             ""                      ,             ""                                                                                      ,             ""                                    ,              ""                     ,               ""                    ]
How_2_Change_D_Link1 =escape_links(  [     "https://youtu.be/IWG5WV07tRQ"        ,  "                            "    ,  "                            "             , "https://youtu.be/dB2VykWuBxw"                        ,  "                            "                   ,  "https://youtu.be/sYY5cwrgC2s"                                ,  "                            "             ,  "                            "       ,"https://youtu.be/BUy-4zQvqTg"                  ,  "https://youtu.be/sYY5cwrgC2s"               ,  "                            "     , "                            "     ,  "                            "     ,  "                            "   ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "                                                                     ,  "                            "                   ,  "                            "     ,  "                            "     ])
How_2_Change_D_Link2 =escape_links(  [     "https://youtu.be/ljWQHz8jYTE"        ,  "                            "    ,  "                            "             , "https://youtu.be/EC4kXtSvtG4"                        ,  "                            "                   ,  "                            "                                ,  "                            "             ,  "                            "       ,"https://t.me/fusion1/118022"                   ,  "                            "               ,  "                            "     , "                            "     ,  "                            "     ,  "                            "   ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "                                                                     ,  "                            "                   ,  "                            "     ,  "                            "     ])
How_2_Change_D_Link3 =escape_links(  [     "https://youtu.be/G2RZIRPVRr4"        ,  "                            "    ,  "                            "             , "                            "                        ,  "                            "                   ,  "                            "                                ,  "                            "             ,  "                            "       ,"                            "                  ,  "                            "               ,  "                            "     , "                            "     ,  "                            "     ,  "                            "   ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "                                                                     ,  "                            "                   ,  "                            "     ,  "                            "     ])
How_2_Change_D_Link4 =escape_links(  [     "https://t.me/fusion1/119233"         ,  "                            "    ,  "                            "             , "                            "                        ,  "                            "                   ,  "                            "                                ,  "                            "             ,  "                            "       ,"                            "                  ,  "                            "               ,  "                            "     , "                            "     ,  "                            "     ,  "                            "   ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "                                                                     ,  "                            "                   ,  "                            "     ,  "                            "     ])
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#🟢 كل شي يخص المكيف                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
Parts_Group_E        =               [         "كلتش الكومبروسر"               ,           "كومبروسر"               ,        "ثلاجه مكيف"                         ,           "مكثف"                                     ,         "مروحة مكيف"                              ,         "منظم مروحة المكيف"                                  ,              "Heater Core"                   ,     "منظم حرارة الهوا"              ,        "منظم توزيع الهوا "                    ,       "منظم دخول الهواء"                     ,              ""                     ,              ""                    ,          "انبوب الثلاجة"          ,          "لي مكيف الحار"           ,      "refrigerant liquid Tube"     ,    "refrigerant suction Hose Inlet" ,                ""                   ,             ""                                                                                       ]  
Parts_numbers_group_E=               [           "DG9Z-19D786-CA"               ,         "FB5Z-19703-B"              ,       "GG9Z-19850-A"                        ,           "HG9Z-19712-D"                             ,         "DG9Z-19805-B"                             ,          "G3GZ19E624A"                                        ,               "DG9Z-18476-A"                 ,     "GS7Z-19E616-B"                   ,            "GS7Z-19E616-A"                     ,            "GS7Z-19E616-C"                    ,               ""                    ,               ""                   ,          "DG9Z-19A834-M"          ,           "DG9Z-19972-B"             ,           "HG9Z-19835-B"          ,           "DG9Z-19D742-K"           ,              ""                     ,              ""                                                                                      ]
Parts_prices_group_E =               [      [ "?","?","?","?","?","?" ]         , [ 1200,"?","?","?","?","?" ]        ,   [400,420,430,460,510,570]                 ,   [ 580,"?","?","?","?","?" ]                        ,   [ "?","?","?","?","?","?" ]                      ,   [ "?","?","?","?","?","?"]                                  ,   [ "?","?","?","?","?","?" ]                ,   [ "?","?","?","?","?","?" ]         ,    [ 80,"?","?","?","?","?" ]                  ,   [ "?","?","?","?","?","?" ]                 ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]     ,   [270,"?","?","?","?","?"  ]        ,   [ "?","?","?","?","?","?" ]     ,   [ "?","?","?","?","?","?"]        ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]                                                                        ] 
Part_Location_group_E=               [            "AC_Clutch"                   ,           ""                        ,              ""                             ,             ""                                       ,         "AC components"                            ,             "AC components"                                   ,         "AC components"                      ,         "AC components"               ,         "AC components"                        ,         "AC components"                       ,             ""                      ,             ""                     ,    "Air Conditioning System"      ,     "Air Conditioning System"        ,      "Air Conditioning System"    ,      "Air Conditioning System"      ,              ""                     ,               ""                                                                                     ]
How_2_Change_E_Link1 =escape_links(  [     "                            "       ,"                            "       , "                            "              ,  "                            "                      ,  "https://youtu.be/TfPNxEwX1-o"                    ,  "https://youtu.be/golSQ85aBVY"                               ,  "                            "              ,  "https://youtu.be/TSLbiEl-AQI"       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "                            "   ,  "                            "      ,  "                            "   ,  "                            "     ,  "                            "     ,  "                            "                                                                      ])
How_2_Change_E_Link2 =escape_links(  [     "                            "       ,"                            "       , "                            "              ,  "                            "                      ,  "                            "                    ,  "                            "                               ,  "                            "              ,  "                            "       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "                            "   ,  "                            "      ,  "                            "   ,  "                            "     ,  "                            "     ,  "                            "                                                                      ])
How_2_Change_E_Link3 =escape_links(  [     "                            "       ,"                            "       , "                            "              ,  "                            "                      ,  "                            "                    ,  "                            "                               ,  "                            "              ,  "                            "       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "                            "   ,  "                            "      ,  "                            "   ,  "                            "     ,  "                            "     ,  "                            "                                                                      ])
How_2_Change_E_Link4 =escape_links(  [     "                            "       ,"                            "       , "                            "              ,  "                            "                      ,  "                            "                    ,  "                            "                               ,  "                            "              ,  "                            "       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "    ,  "                            "   ,  "                            "      ,  "                            "   ,  "                            "     ,  "                            "     ,  "                            "                                                                      ])
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#⚪️فرامل وكفرات وملحقاتها                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
Parts_Group_F        =               [           "اقمشة أمامية"                ,        "اقمشة خلفيه"               ,         "هوب امامي"                        ,             "هوب خلفي"                              ,               "دينمو الكليبر"                     ,            "مضخة ABS"                                         ,       "حديدة الكليبر الأمامي"                ,       "حديدة الكليبر الخلفي"       ,          "كليبر امامي"                        ,          "كليبر خلفي"                         ,      "فلنجه الأمامية"               ,       "فلنجة خلفية"               ,        "قربة زيت الفرامل"         ,        "غطا زيت الفرامل"          ,             "الباكم"              ,  "brake vacum hose supply hose"     ,        "لي فرامل أمامي"           ,        "لي فرامل خلفي"                                                                             ,           "سويتش البريك"                         ,             ""                          ]  
Parts_numbers_group_F=               [              "DG9Z-2001-F"               ,        "FU2Z-2V200-H"               ,      "KS7Z-1125-A"                          ,        "KS7Z-2C026-B"                               ,  "يسار DG9Z-2B713-A\nيمين DG9Z-2B712-A"            ,           "EG9Z-2C215-A"                                      ,        "DG9Z-2B486-B"                         ,         "DG9Z-2B486-B"              ,"يسار DG9Z-2B121-A\nيمين DG9Z-2B120-A"          ,"يسار DG9Z-2553-C\nيمين DG9Z-2552-C"           ,             "DG9Z-1104-T"           ,         "DG9Z-1109-C"              ,         "DG9Z-2K478-B"             ,             "BV6Z-2162-A"          ,              "EG9Z-2005-D"         ,          "DS7Z-9C490-AC"            ,"يسار DG9Z-2078-E\nيمين DG9Z-2078-F",    "يسار DG9Z-2282-M\nيمين DG9Z-2282-Q"                                                        ,         "FG9Z-2B623A-A"                           ,              ""                         ]
Parts_prices_group_F =               [      [260,200,"?","?","?","?"]           ,    [220,230,"?","?","?","?" ]       ,     [ "?","?","?","?","?","?"]              ,   [ "?","?","?","?","?","?"]                        ,   [ 600,"?","?","?","?","?" ]                       ,   [ "?","?","?","?","?","?" ]                                 ,   [ "?","?","?","?","?","?" ]                 ,    [ "?","?","?","?","?","?"]       ,   [ "?","?","?","?","?","?" ]                   ,   [ 870,"?","?","?","?","?" ]                 ,   [ 270,260,380,300,"?","?" ]       ,   [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?"]       ,  [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]                                                                        ,   [ "?","?","?","?","?","?" ]                     ,   [ "?","?","?","?","?","?" ]           ] 
Part_Location_group_F=               [    "Front Brake Discs and Calipers"      ,    "Rear Brake Discs and Calipers"  ,   "Front Brake Discs and Calipers"          ,  "Rear Brake Discs and Calipers"                    ,    "Rear Brake Discs and Calipers"                  ,         "Parking Brake"                                       ,   "Front Brake Discs and Calipers"            ,  "Rear Brake Discs and Calipers"    ,    "Front Brake Discs and Calipers"             ,    "Rear Brake Discs and Calipers"            ,             ""                      ,             ""                     ,         " Master Cylinder"         ,       " Master Cylinder"           ,       "Brake Booster Assy"         ,         "Brake Booster Assy"        ,             ""                     ,             ""                                                                                       ,              ""                                   ,               ""                        ]
How_2_Change_F_Link1 =escape_links(  [    "https://youtu.be/exVpIJdtQHE"        ,   "https://youtu.be/vb_lmM8dRgc"    ,   "                            "            ,  "                            "                     ,  "                            "                     ,  "                            "                               ,  "                            "               ,  "                            "     ,  "                            "                 ,  "https://youtu.be/KCRBvCT8d9A"               , "https://youtu.be/Fn6IDRmyjPw"      , "https://youtu.be/Jt77RZL2sw0"     ,  "                            "    ,  "                            "    , "                            "     ,  "                            "     ,  "https://youtu.be/vYDq1MawWcM"    ,  "https://youtu.be/8QXZHKAVggI"                                                                      ,  "                            "                   ,  "                            "         ])
How_2_Change_F_Link2 =escape_links(  [    "https://youtu.be/xGuG8puig7U"        ,   "https://youtu.be/h1MigjXDy4E"    ,   "                            "            ,  "                            "                     ,  "                            "                     ,  "                            "                               ,  "                            "               ,  "                            "     ,  "                            "                 ,  "                            "               , "https://youtu.be/8juVqkf2AFk"      , "                            "     ,  "                            "    ,  "                            "    , "                            "     ,  "                            "     ,  "https://youtu.be/4eQlPUV7bCc"    ,  "                            "                                                                      ,  "                            "                   ,  "                            "         ])
How_2_Change_F_Link3 =escape_links(  [    "https://youtu.be/68fdhkY0TCc"        ,   "                            "    ,   "                            "            ,  "                            "                     ,  "                            "                     ,  "                            "                               ,  "                            "               ,  "                            "     ,  "                            "                 ,  "                            "               , "https://youtu.be/ma8v_CgXsG0"      , "                            "     ,  "                            "    ,  "                            "    , "                            "     ,  "                            "     ,  "                            "    ,  "                            "                                                                      ,  "                            "                   ,  "                            "         ])
How_2_Change_F_Link4 =escape_links(  [    "https://youtu.be/Wmu9n_RA2sM"        ,   "                            "    ,   "                            "            ,  "                            "                     ,  "                            "                     ,  "                            "                               ,  "                            "               ,  "                            "     ,  "                            "                 ,  "                            "               , "https://youtu.be/hP0nM2xUgHU"      , "                            "     ,  "                            "    ,  "                            "    , "                            "     ,  "                            "     ,  "                            "    ,  "                            "                                                                      ,  "                            "                   ,  "                            "         ]) 
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#🟣 سيور وملحقاتها                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
Parts_Group_G        =               [          "شداد السير"                   ,           "سير المحرك الخارجي"     ,          "سير المكيف"                     ,     "بكرة الايدل"                                    ,     "بكرة  دنمو البطارية"                          ,       "بكرة طرمية الماء"                                    ,          "بكرة الكرنك"                        ,         "جنزير التيمن"             ,              ""                                 ,              ""                               ,             ""                    ]  
Parts_numbers_group_G=               [           "DS7Z-6A228-A"                 ,             "JK4542B-8620"          ,          "JK4365-8620"                     ,       "DS7Z-8678-A"                                  ,          "FJ7Z-10344-A"                             ,          "HJ5Z-8509-A"                                       ,          "CV6Z-6312-D"                         ,           "1L5Z-6268-AA"            ,               ""                                ,               ""                              ,             ""                     ]
Parts_prices_group_G =               [      [ 250,160,190,140,170,"?" ]         ,      [40,70,50,"?","?","?" ]        ,   [40,70,"?","?","?","?"]                  ,   [ "?","?","?","?","?","?" ]                        ,   [ "?","?","?","?","?","?" ]                       ,   [ "?","?","?","?","?","?" ]                                ,   [ "?","?","?","?","?","?" ]                  ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]                   ,   [ "?","?","?","?","?","?" ]                 ,  [ "?","?","?","?","?","?" ]       ] 
Part_Location_group_G=               [      "Pulleys and Drive Belts"           ,    "Pulleys and Drive Belts"        ,   "Pulleys and Drive Belts"                ,             ""                                       ,             ""                                      ,       "Water pump puelly"                                    ,             ""                                 ,          "Timing chain"             ,              ""                                 ,             ""                                ,             ""                     ]
How_2_Change_G_Link1 =escape_links(  [    "                            "        ,     "https://youtu.be/Lp-mjP20p8g"  , "                            "             ,  "                            "                      ,  "                            "                     ,  "                            "                              , "                            "                 ,  "                            "     ,  "                            "                 ,  "                            "               ,  "                            "    ])
How_2_Change_G_Link2 =escape_links(  [    "                            "        ,     "                            "  , "                            "             ,  "                            "                      ,  "                            "                     ,  "                            "                              , "                            "                 ,  "                            "     ,  "                            "                 ,  "                            "               ,  "                            "    ])
How_2_Change_G_Link3 =escape_links(  [    "                            "        ,     "                            "  , "                            "             ,  "                            "                      ,  "                            "                     ,  "                            "                              , "                            "                 ,  "                            "     ,  "                            "                 ,  "                            "               ,  "                            "    ])
How_2_Change_G_Link4 =escape_links(  [    "                            "        ,     "                            "  , "                            "             ,  "                            "                      ,  "                            "                     ,  "                            "                              , "                            "                 ,  "                            "     ,  "                            "                 ,  "                            "               ,  "                            "    ])
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#⚫️نظام الشحن ونظام التشغيل  +  ظفاير                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
Parts_Group_H        =               [           "اصباع بطارية سالب"           ,   "ظفيرة بطارية موجب"             ,         "البطارية"                        ,         "الدينمو"                                    ,            "السلف"                                 ,               ""                                             ,             ""                                 ,             ""                        ,              ""                               ,              ""                               ,              ""                     ]  
Parts_numbers_group_H=               [           "BT4Z-14450-BA"                ,               "DG9Z-14300-D"        ,        "BXT-90T5-590"                      ,             "DS7Z-10346-T"                           ,"HD9Z-11002-B\nor\nFJ5Z-11002-A"                     ,               ""                                             ,               ""                               ,               ""                      ,               ""                              ,               ""                              ,               ""                   ]
Parts_prices_group_H =               [      [ "?","?","?","?","?","?" ]         ,   [ "?","?","?","?","?","?" ]       ,  ["?","?","?","?","?","?"]                 ,    ["?","?","?","?","?","?"]                         ,  [600,580,"?","?","?","?" ]                         ,   [ "?","?","?","?","?","?" ]                                ,   [ "?","?","?","?","?","?" ]                  ,   [ "?","?","?","?","?","?" ]         ,   [ "?","?","?","?","?","?" ]                 ,   [ "?","?","?","?","?","?" ]                 ,   [ "?","?","?","?","?","?" ]      ] 
Part_Location_group_H=               [                ""                        ,             ""                      ,             ""                             ,             ""                                       ,            ""                                       ,             ""                                               ,             ""                                 ,              ""                       ,             ""                                ,             ""                                ,             ""                     ]
How_2_Change_H_Link1 =escape_links(  [     "                            "       , "                            "      ,"https://youtu.be/Si7-aizWuU4"              , "https://youtu.be/xFJTdplcjQM"                       , "https://youtu.be/NBs1j8KtH4o"                      ,  "                            "                              ,  "                            "                ,  "                            "       ,  "                            "               ,  "                            "               ,  "                            "    ])
How_2_Change_H_Link2 =escape_links(  [     "                            "       , "                            "      ,"                            "              , "                            "                       , "https://youtu.be/aKDUhhDUEq8"                      ,  "                            "                              ,  "                            "                ,  "                            "       ,  "                            "               ,  "                            "               ,  "                            "    ])
How_2_Change_H_Link3 =escape_links(  [     "                            "       , "                            "      ,"                            "              , "                            "                       , "                            "                      ,  "                            "                              ,  "                            "                ,  "                            "       ,  "                            "               ,  "                            "               ,  "                            "    ])
How_2_Change_H_Link4 =escape_links(  [     "                            "       , "                            "      ,"                            "              , "                            "                       , "                            "                      ,  "                            "                              ,  "                            "                ,  "                            "       ,  "                            "               ,  "                            "               ,  "                            "    ])
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#🟠زيوت وفلاتر + وبخاخات ومنظفات                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
Parts_Group_J        =               [        "فلتر زيت المكينة"                ,           "فلتر القير"            ,        "فلتر المكيف"                       ,        "فلتر هوا المكينة"                          ,          "فلتر البنزين"                            ,        "فلتر الفريون"                                         ,               ""                             ,              ""                       ,        "زيت المكينة"                          ,         "زيت القير"                         ,          "زيت الفرامل"              ,             ""                     ]  
Parts_numbers_group_J=               [           "FL-2131"                       ,          "7T4Z-7A098-B"            ,       "DG9Z-19N619-AA"                      ,         "DS7Z-9601-D"                               ,             "FG-1114"                               ,         "DG9Z-19C836-B"                                        ,               ""                             ,               ""                      ,               ""                               ,          ""                                  ,               ""                     ,             ""                     ]
Parts_prices_group_J =               [    [ 20,25,"?","?","?","?" ]              ,   [ "?","?","?","?","?","?" ]      ,  [50,50,45,"?","?","?" ]                    ,   [70,65,85,"?","?","?"]                            ,    [60,55,75,70,65,"?"]                             ,   [ 160,"?","?","?","?","?" ]                                  ,   [ "?","?","?","?","?","?" ]                ,   [ "?","?","?","?","?","?" ]         ,   [ "?","?","?","?","?","?" ]                  ,   [ 25,30,22,"?","?","?" ]                   ,   [ 40,"?","?","?","?","?" ]         ,   [ "?","?","?","?","?","?" ]      ] 
Part_Location_group_J=               [     "engine oil filter"                   ,             ""                     ,            ""                               ,       "Air_Filter_Location"                         ,    "Fuel_Filter_location"                           ,             ""                                                 ,             ""                               ,             ""                        ,             ""                                 ,             ""                               ,             ""                       ,             ""                     ]
How_2_Change_J_Link1 =escape_links(  [   "                            "          ,  "                            "    , "https://youtu.be/Xp_SzFJRqTg"              , "https://youtu.be/rVu2YAIHhbA"                      , "                            "                      , "                            "                                 ,  "                            "              ,  "                            "       ,  "https://youtu.be/fCkka-6TI_g"                ,  "https://youtu.be/vYXW0sOpbtQ"              , "https://youtu.be/2YuevQFv4Hs"       ,  "                            "    ]  )
How_2_Change_J_Link2 =escape_links(  [   "                            "          ,  "                            "    , "https://youtu.be/DvLdZj0jHPk"              , "                            "                      , "                            "                      , "                            "                                 ,  "                            "              ,  "                            "       ,  "https://youtu.be/J9J6yIz2Mp4"                ,  "https://t.me/fusion1/72316"                , "https://youtu.be/or4DEtXN\_eY"      ,  "                            "    ]  )
How_2_Change_J_Link3 =escape_links(  [   "                            "          ,  "                            "    , "https://youtu.be/qg8bK4Bh65E"              , "                            "                      , "                            "                      , "                            "                                 ,  "                            "              ,  "                            "       ,  "https://youtu.be/oNf9-6RgcrI"                ,  ""                                          , ""                                   ,  "                            "    ]  )
How_2_Change_J_Link4 =escape_links(  [   "                            "          ,  "                            "    , "                            "              , "                            "                      , "                            "                      , "                            "                                 ,  "                            "              ,  "                            "       ,  "https://t.me/fusion1/41282"                  ,  ""                                          , ""                                   ,  "                            "    ]  )
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#✳️ نظام التوجية والطارة وملحقاتة                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
Parts_Group_K        =               [         "شريحة البوري"                   ,          "البوري"                 ,              ""                              ,              ""                                     ,  "Transceiver - Immobilizer Module"                 ,         "Ignition Switch"                                      ,    "Ignition Lock Cylinder"                 ,             "الطارة"                  ,         "أزارير يسار"                         ,        "أزارير يمين"                         ,         "سويتش المساحات"           ,        "سويتش الغمازات"              ,              ""                    ,              ""                   ]  
Parts_numbers_group_K=               [         "EG9Z-14A664-H"                   ,        "DG9Z-13832-A"              ,               ""                             ,               ""                                    ,           "DS7Z-15607-A"                            ,         "DG9Z-11572-A"                                         ,       "CP9Z-11582-A"                        ,         "DS7Z-3600-AF"                ,       "DG9Z-9C888-AD"                          ,       "DG9Z-9C888-DC"                         ,          "DG9Z-17A553-AA"           ,         "EG9Z-13341-AA"               ,               ""                   ,               ""                  ]
Parts_prices_group_K =               [    ["?","?","?","?","?","?"]              , [120,"?","?","?","?","?" ]         ,    ["?","?","?","?","?","?"]                 ,    ["?","?","?","?","?","?"]                        ,   [ "?","?","?","?","?","?" ]                       ,   [ "?","?","?","?","?","?" ]                                  ,   [ "?","?","?","?","?","?" ]               ,   [ "?","?","?","?","?","?" ]         ,   [ "?","?","?","?","?","?" ]                  ,   [ "?","?","?","?","?","?" ]                 ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?" ]         ,   [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]     ] 
Part_Location_group_K=               [          "Clock Spring"                   ,           "Horn"                   ,             ""                               ,             ""                                      ,           "Transceiver"                             ,             ""                                                 ,             ""                              ,             ""                        ,               ""                               ,              ""                               ,             ""                      ,             ""                        ,             ""                     ,             ""                    ]
How_2_Change_K_Link1 =escape_links(  [  "https://youtu.be/SYwBC8CVafw"           ,"                            "      , "                            "               , "                            "                      ,  "                            "                     ,  "                            "                                , "                            "              ,  "                            "       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "       ,  "                            "    ,  "                            "   ])
How_2_Change_K_Link2 =escape_links(  [  "                            "           ,"                            "      , "                            "               , "                            "                      ,  "                            "                     ,  "                            "                                , "                            "              ,  "                            "       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "       ,  "                            "    ,  "                            "   ])
How_2_Change_K_Link3 =escape_links(  [  "                            "           ,"                            "      , "                            "               , "                            "                      ,  "                            "                     ,  "                            "                                , "                            "              ,  "                            "       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "       ,  "                            "    ,  "                            "   ])
How_2_Change_K_Link4 =escape_links(  [  "                            "           ,"                            "      , "                            "               , "                            "                      ,  "                            "                     ,  "                            "                                , "                            "              ,  "                            "       ,  "                            "                ,  "                            "               ,  "                            "     ,  "                            "       ,  "                            "    ,  "                            "   ])
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#💠قطع بودي واقفال ونظام الترفية وغيرها                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
Parts_Group_L        =               [               ""                          ,             ""                     ,              ""                             ,               ""                                      ,               ""                                  ,              ""                                                ,             ""                               ,             ""                        ,              ""                               ,              ""                              ,              ""                      ,              ""                    ,              ""                     ,             ""                   ,             ""                      ,             ""                     ,"","","","","","","","","","","","","","","","","","","",""]  
Parts_numbers_group_L=               [               ""                          ,             ""                     ,               ""                            ,               ""                                      ,               ""                                  ,               ""                                               ,               ""                             ,               ""                      ,               ""                              ,               ""                             ,               ""                     ,               ""                   ,               ""                    ,               ""                 ,             ""                      ,             ""                     ,"","","","","","","","","","","","","","","","","","","",""]
Parts_prices_group_L =               [   ["؟","?","?","?","?","?" ]              ,   ["?","?","?","?","?","?"]        ,    ["?","?","?","?","?","?"]                ,   [ "?","?","?","?","?","?" ]                         ,   [ "?","?","?","?","?","?" ]                     ,   [ "?","?","?","?","?","?" ]                                  ,   [ "?","?","?","?","?","?" ]                ,   [ "?","?","?","?","?","?" ]         ,   [ "?","?","?","?","?","?" ]                 ,   [ "?","?","?","?","?","?" ]                ,   [ "?","?","?","?","?","?" ]        ,   [ "?","?","?","?","?","?" ]      ,   [ "?","?","?","?","?","?" ]       ,   [ "?","?","?","?","?","?"]     ,   [ "?","?","?","?","?","?"]        ,             ""                     ,"","","","","","","","","","","","","","","","","","","",""] 
Part_Location_group_L=               [             ""                            ,              ""                    ,             ""                              ,             ""                                        ,             ""                                    ,             ""                                                 ,             ""                               ,              ""                       ,             ""                                ,             ""                               ,             ""                       ,             ""                     ,             ""                      ,             ""                   ,             ""                      ,             ""                     ,             ""                   ,             ""                  ,             ""                  ,             ""                  ,             ""                     ,             ""                  ,             ""                  ,             ""                  ,             ""                  ,             ""                  ,             ""                  ,             ""                  ,             ""                  ,             ""                  ,             ""                ]
How_2_Change_L_Link1 =escape_links(  [  "                            "           , "                            "     , "                            "              ,  "                            "                       ,  "                            "                   , "                            "                                 ,  "                            "              ,  "                            "       ,  "                            "               ,  "                            "              ,  "                            "      ,  "                            "    ,  "                            "     ,  "                            "  ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "   ,  "                            "    ,  "                            "    ,  "                            "        ,  "                            "    ,  "                            "     ,  "                            "   , "                            "  ,  "                            "   ,  "                            "   ,  "                            "   ,  "                            "   ,  "                            "   , "                            "])
How_2_Change_L_Link2 =escape_links(  [  "                            "           , "                            "     , "                            "              ,  "                            "                       ,  "                            "                   , "                            "                                 ,  "                            "              ,  "                            "       ,  "                            "               ,  "                            "              ,  "                            "      ,  "                            "    ,  "                            "     ,  "                            "  ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "   ,  "                            "    ,  "                            "    ,  "                            "        ,  "                            "    ,  "                            "     ,  "                            "   , "                            "  ,  "                            "   ,  "                            "   ,  "                            "   ,  "                            "   ,  "                            "   , "                            "])
How_2_Change_L_Link3 =escape_links(  [  "                            "           , "                            "     , "                            "              ,  "                            "                       ,  "                            "                   , "                            "                                 ,  "                            "              ,  "                            "       ,  "                            "               ,  "                            "              ,  "                            "      ,  "                            "    ,  "                            "     ,  "                            "  ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "   ,  "                            "    ,  "                            "    ,  "                            "        ,  "                            "    ,  "                            "     ,  "                            "   , "                            "  ,  "                            "   ,  "                            "   ,  "                            "   ,  "                            "   ,  "                            "   , "                            "])
How_2_Change_L_Link4 =escape_links(  [  "                            "           , "                            "     , "                            "              ,  "                            "                       ,  "                            "                   , "                            "                                 ,  "                            "              ,  "                            "       ,  "                            "               ,  "                            "              ,  "                            "      ,  "                            "    ,  "                            "     ,  "                            "  ,  "                            "     ,  "                            "    ,  "                            "     ,  "                            "   ,  "                            "    ,  "                            "    ,  "                            "        ,  "                            "    ,  "                            "     ,  "                            "   , "                            "  ,  "                            "   ,  "                            "   ,  "                            "   ,  "                            "   ,  "                            "   , "                            "])

#💡 قسم الإضائات والكشافات  
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________



#💠MAINTENANCE الصيانات الدورية    
MAINTENANCE="الصيانة الدورية"
N = "جدول صيانة"  
trigger_Schedual = ["جدول","دوري","طريق"]
trigger_MAINTENANCE =["صيان","تنظيف","تنسيم","تزييت"]
Click_Maintenance = ["Maintenance"]  

# ================== ENHANCED CONFIGURATION ==================  
MAINTENANCE_CONFIG = {
    "الصيانة الدورية": {
        "header": "🔧 <b>الصيانة الدورية</b>\nفيوجن 2013-2016 🔧\n\nاختر الجزء المطلوب:",
        "items": {
            "زيت فرامل": {
                "part_number": "",
                "video": [How_2_Change_J_Link1[10]],
                "emoji": "",
                "interval_km": "كل سنتين الى ثلاث سنوات",
                "important_tips": "توجد تصنيفات مختلفة للزيت:\nلابد تختار DOT4"
            },
            "زيت المكينة": {
                "part_number": "",
                "video": [How_2_Change_J_Link2[8]],
                "emoji": "",
                "interval_km": "النصف تخليقي كل 5,000\nالتخليقي الكامل كل 8,000",
                "important_tips": f"[{Reset_oil} *إضغط هنا*](https://t.me/fusion1/41282)"
            },
            "زيت القير": {
                "part_number": "",
                "video": [How_2_Change_J_Link1[9]],
                "emoji": "",
                "interval_km": "كل 40 الف  كيلومتر",
                "important_tips": "[*إضبط وزنية القير بعد تغييرة*](https://t.me/fusion1/72317)"
            },
            "فلتر البنزين": {
                "part_number": f"{Parts_numbers_group_J[4]}",
                "video": [How_2_Change_J_Link1[4]],
                "emoji": "",
                "interval_km": "كل 40 الف  كيلومتر",
                "important_tips": "إطلب الفلتر برقم القطعة\nالفلتر يوجد فقط في محرك 2.5"
            },
            "فلتر الهوا": {
                "part_number": f"{Parts_numbers_group_J[3]}",
                "video": [How_2_Change_J_Link1[3]],
                "emoji": "",
                "interval_km": "كل 20 الف  كيلومتر",
                "important_tips": ""
            },
            "فلتر المكيف": {
                "part_number": f"{Parts_numbers_group_J[2]}",
                "video": [How_2_Change_J_Link1[2]],
                "emoji": "",
                "interval_km": "كل 20 الف  كيلومتر",
                "important_tips": "عند تركيب الفلتر تأكد ان السهم المرسوم على الفلتر متجة للأعلى"
            },
            "بلف الحراره": {
                "part_number": f"{Parts_numbers_group_D[3]}",  
                "video": [How_2_Change_D_Link1[3]],            
                "emoji": "",
                "interval_km": "كل 100 الف  كيلومتر",
                "important_tips": "قم بتغيير غطاء القربة أيضا"
            },
            "مويه الرديتر": {
                "part_number": f"{Parts_numbers_group_D[8]}",  
                "video": [How_2_Change_D_Link1[8]],            
                "emoji": "",
                "interval_km": "كل 100 الف  كيلومتر",
                "important_tips": "بعد تغيير الماء إعمل تنسيم للنظام\n"
            },
            "تغيير بواجي": {
                "part_number": f"{Parts_numbers_group_B[1]}",  
                "video": [How_2_Change_B_Link1[1]],            
                "emoji": "",
                "interval_km": "كل 100 الف  كيلومتر",
                "important_tips": "وقت تركيب الكويلات لاتشد مساميرها بزيادة.. حتى مايخرب مكان المسمار ويصير مايثبت"
            },
            "تنظيف بخاخات": {
                "part_number":   "",  
                "video":   "",            
                "emoji": "",
                "interval_km": "كل 100 الف  كيلومتر",
                "important_tips": "تأكد من تنظيف البخاخات بشكل دوري لتحسين أداء المحرك وتقليل انبعاثات العادم."
            },
            "تنظيف ثروتل": {  
                "part_number":   "",  
                "video":   [How_2_Change_B_Link3[2]],           
                "emoji": "",
                "interval_km": "كل 100 الف  كيلومتر",
                "important_tips": f'[*اعمل إعادة ضبط للبوابة بعد تغييرها*]({How_2_Change_B_Link4[2]})'
            },
            "تنظيف ثلاجة المكينة": {
                "part_number": "",  
                "video": "",            
                "emoji": "",
                "interval_km": "بعد 160 الف  كيلومتر",
                "important_tips": "قم بتغيير بلف PCV أيضا وموقعة خلف ثلاجة المكينة\nبلف PCV  هو بلف تبخير المكينة"
            },
            "تنظيف MAF": {
                "part_number":   "",  
                "video":   [How_2_Change_B_Link4[6]],            
                "emoji": "",
                "interval_km": "كل 100 الف  كيلومتر",
                "important_tips": "مستشعر الهواء MAF يجب تنظيفه بانتظام لتجنب تأثيره السلبي على أداء المحرك."
            },
            "تنظيف EGR": {
                "part_number": "",  
                "video":  [How_2_Change_B_Link4[36]],              
                "emoji": "",
                "interval_km": "بعد 160 الف  كيلومتر",
                "important_tips": "تابع من الدقيقة  12:50"
            },
            "تنظيف MAP": {
                "part_number": "",  
                "video": [How_2_Change_B_Link4[7]],                
                "emoji": "",
                "interval_km": "بعد 160 الف  كيلومتر",
                "important_tips": "تابع من الدقيقة  2:00"
            },
            "جلبة عصا القير": {
                "part_number": f"{Parts_numbers_group_C[4]}",  
                "video": [How_2_Change_C_Link1[4]],            
                "emoji": "",
                "interval_km": "كل 100 الف  كيلومتر",
                "important_tips": "عاملها مثل معاملة القطع الاستهلاكية\n"
            },
            "سير المكينة": {
                "part_number": f"{Parts_numbers_group_G[1]}",  
                "video": [How_2_Change_G_Link1[1]],            
                "emoji": "",
                "interval_km": "بعد 160 الف  كيلومتر",
                "important_tips": "غير الشداد مع السير حتى تتجنب مشاكل الشداد القديم"
            },
            "تدوير كفرات": {
                "part_number": f"",  
                "video": "",            
                "emoji": "",
                "interval_km": "كل 20 الف  كيلومتر",
                "important_tips": "تدوير الكفرات بشكل دوري يساهم في تمديد عمر الكفرات ويعزز أداء القيادة."
            },
            " تنسيم هوا الرديتر": {
                "part_number": "",  
                "video": [How_2_Change_D_Link4[0]],            
                "emoji": "",
                "interval_km": "بعد كل تغيير لماء الرديتر.\n او بعد فك أي جزء من النظام",
                "important_tips": ""
            },

        },
        "button_layout": [3, 3, 3, 3, 3],
    }
    }



# ENGINE                  
E = "صيانة المكينة"                               
trigger_E =["مكين","محرك","مكاين"]     
trigger_E1=["نوع","أفضل","افضل"]  
trigger_E2=["لزوج"]
trigger_E3=["تصفية","تصفية"]
# TRANSMISSION    
F = "صيانة القير"                                   
trigger_F =["قير"] 
trigger_F1=["نوع","أفضل", "افضل"]  
trigger_F2=["فلتر" ]

E1="أفضل زيت مكينة"   ;E2="كمية زيت المكينة"   ;E3="أنواع محركات الفيوجن"   ;E4="صور محركات الفيوجن"   ;E5="تصفية شاملة" ; E6="اللزوجة المناسبة" 
F1="نوع زيت القير"   ;F2="كمية زيت القير"  ;F3="خطوات تغيير زيت القير"  ;F4= "التعامل مع الزيت القديم" ;F5="حلول ل نتعة القير"    ;F6="فلتر القير" ; F7="متى يتغير ؟" ; F11= "النوع - الكمية - متى أغير"; F22="خطوات التغيير - أهملت الزيت ماذا افعل؟"

AFT_HOW_TO=f"{F3}\n\nلموديلات 2009-2012\nhttps://t.me/fusion1/116726\n\n لموديلات 2013-2019\nhttps://t.me/fusion1/72316"
AFT_OIL_TYPE=f"{F1}:\nMERCON LV (MOTORCRAFT)"
AFT_WHEN_CHANGE=f"({F7})\n\n\U000026D4 كل 40-50 الف\nأو بعد مرور سنتين بغض النظر عن الممشى"
AFT_DEAL_WITH_OLD=f"{F4}\nهذا فيديو يشرح كيف تتصرف اذا طولت على الزيت وما غيرته\nhttps://www.youtube.com/watch?v=pYvsgM1uALo"
REPLY_TEXT_MAINTENANCE_PROGRAM="⭐️تغيير زيت المحرك مع الفلتر\nكل ٥٠٠٠ اذا الزيت نصف تخليقي\nكل ٨٠٠٠ اذا الزيت تخليقي كامل\nاو بعد مرور ٨ شهور\n\n⭐️كل ٢٠  الف\n-تدوير الإطارات\n-تغيير فلتر هواء المحرك\n-تغيير فلتر هواء الكبينة\n\n⭐️ كل ٤٠ الف\n-تغيير فلتر البنزين\n-تغيير زيت القير (او بعد مرور سنتين)\n\n⭐️كل  ١٠٠ - ١٢٠  الف\n-تغيير مويه الرديتر وبلف الحراره وغطاء القربه\n-تغيير بواجي\n-تنظيف بخاخات \n-تنظيف البوابة ثروتل\n-تنظيف حساس الهواء\n- تغيير جلبة عصا القير 2013-2019\n\n⭐️كل ١٦٠ - ٢٠٠ الف \nفحص وتغيير السيور مع الشداد\n\n⭐️كل سنتين الى ثلاث سنوات\n- تغيير سائل الفرامل"  
Oil_Cjoose="أي زيت تقصد؟\n إضغط للتأكيد..."
intro_engine="\n حدد موديل سيارتك ونوع المحرك وبعطيك الكمية المطلوبة لتغيير زيت المكينة"
oil_level="ثم عاير المستوى والمحرك مقفل\n *المعيار الصحيح موضح بالصورة*"
Viscosity="محرك 2.5 لتر\n5w20\U00002714\n5w30\U00002714\n10w30\U00002714\n\nمحرك 2.0 لتر\n5w30\U00002714\n10w30\U00002714\n\nمحرك 1.5 لتر\n5w20\U00002714\n5w30\U00002714\n10w30\U00002714"  
REPLY_TEXT_ENGINE_OIL="ثلاث نقاط لازم تكون مكتوبة على علبة الزيت : \n\n 1-اللزوجة المناسبة\n5w20 - 5w30\n\n2- (تركيبة الزيت (تخليقي كامل \nfull synthetic\n\n3-تصنيف الزيت API SP\n (أعلى تصنيف)\n\n....................\n\nوإحرص تكون الشركة موثوقة وتاريخ الإنتاج جديد"
REPLY_TEXT_ENGINE_TYPES="2013-2020:\n1.5 ايكوبووست\n2.0 ايكوبووست\n2.5 تنفس طبيعي\n\nلمعرفة النوع الي بسيارتك برقم الهيكل \n\nإكتب(بوت VIN)"
REPLY_TEXT_ENGINE_CLEAN="تصفية شاملة وصيانة دورية:\n\nتنظيف:\nالبخاخات (مثال: كل ١٠٠ الف)\n البوابة(مثال: كل ١٠٠ الف)\n حساس الهواء(مثال: كل ١٠٠ الف)\n ثلاجة المحرك ودبه الرصاص و حساسات الأكسجين حسب الحاجة\n\nتغيير:\n فلتر الهواء (مثال: كل٢٠ الف)\n البواجي(ينصح بحدود ١٠٠ الف)\n فلتر البنزين (كل ٤٠ - ٨٠ الف)"
trigger_E_F_1=["بوت أفضل زيت","بوت افضل زيت","بوت إيش أفضل زيت","بوت إيش افضل زيت","بوت إيش نوع الزيت","بوت وش نوع الزيت","بوت نوع الزيت","","بوت ايش أفضل زيت","بوت ايش افضل زيت","بوت ايش نوع الزيت","","بوت وش أفضل زيت","بوت وش افضل زيت","بوت شنو نوع الزيت","بوت اي زيت استخدم","بوت اي زيت احط","","","","","" ]

#_________________________________________________________________________________________________________
# WWWW W W W
W="المراجع والكتيبات"
W1= "دليل المالك PDF"   
W2="المواصفا الفنية"      
ClickW=["clickW", "clickW1" ,"clickW2" ,"clickW3" ,"clickW4" ,"clickW5" ,"clickW6" ,"clickW7" ,"clickW8" ,"clickW9"]

trigger_W=["مراجع","مرجع"]
trigger_Wm=["كتيب","دليل"]
Model_Year = ["2010", "2011", "2012", "2014", "2015", "2016", "2017", "2018", "2019"]
trigger_W1 = trigger_C1
trigger_W2 = trigger_C2
trigger_W3 = trigger_C3
trigger_W4 = trigger_C4
trigger_W5 = trigger_C5
trigger_W6 = trigger_C6
trigger_W7 = trigger_C7
trigger_W8 = trigger_C8
trigger_W9 = trigger_C9






import os
import base64
import hashlib
from telebot import types

# القاموس اللي بيخزن المسارات
path_dict = {}

# Define the starting folder path
START_FOLDER_PATH = r"C:\Users\Engmu\OneDrive\Desktop\ALL PARTS\W - References"

# Function to encode paths for callback_data
def encode_path(path):
    return base64.urlsafe_b64encode(path.encode()).decode()

# Function to decode callback_data back to paths
def decode_path(encoded_path):
    return base64.urlsafe_b64decode(encoded_path.encode()).decode()

# دالة توليد مفتاح قصير باستخدام الهاش
def generate_key(path):
    hash_object = hashlib.md5(path.encode())
    return hash_object.hexdigest()[:10]  # نستخدم أول 10 حروف من الهاش لتقليل الحجم

# دالة إضافة المسار للقاموس
def store_path(key, path):
    path_dict[key] = path

# دالة استرجاع المسار من القاموس
def get_path(key):
    return path_dict.get(key)

# دالة لعرض المجلدات في المسار المعطى
def list_folders(path):
    return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

# دالة لعرض ملفات الـ PDF والمجلدات
def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.pdf')]

# دالة إنشاء لوحة أزرار ديناميكية
def create_keyboard(items, path):
    keyboard = types.InlineKeyboardMarkup()
    for item in items:
        full_path = os.path.join(path, item)
        key = generate_key(full_path)
        store_path(key, full_path)
        keyboard.add(types.InlineKeyboardButton(text=item, callback_data=key))
    return keyboard









#______________________________________________________________________________________________
# qqqq  قسم تشخيص الأعطال
#Q تشخيص مشاكل
Q="تشخيص الأعطال"
clickQ = [ "clickQ", "Q[0]", "Q[1]", "Q[2]", "Q[3]", "Q[4]", "Q[5]", "Q[6]", "Q[7]", "Q[8]", "Q[9]", "Q[10]", "Q[11]", "Q[12]", "Q[13]", "Q[14]", "Q[15]", "Q[16]", "Q[17]", "Q[18]", "Q[19]", "Q[20]", "Q[21]", "Q[22]", "Q[23]", "Q[24]", "Q[25]", "Q[26]", "Q[27]", "Q[28]", "Q[29]", "Q[30]", "Q[31]", "Q[32]", "Q[33]", "Q[34]", "Q[35]", "Q[36]", "Q[37]", "Q[38]", "Q[39]", "Q[40]", "Q[41]", "Q[42]", "Q[43]", "Q[44]", "Q[45]", "Q[46]", "Q[47]", "Q[48]", "Q[49]", "Q[50]"]

#    PIN POINT TESTS     
#                                 
trigger_Q=["تشخيص","شخص","فحص"]
trigger_Q1=["عطل","كود","مشكل","","","","","","","","","","","","","","","","","","" ]
trigger_Q2=["","","","","","","","","","","","","","","","","","","","","" ]


PinPoint_Test_Name    =[          "HC-Fuel delivery"               ,                 "test"                            ,                 ""                                ,                 ""                        ,                 ""                          ,                  ""                         ,                 ""                       ,                 ""                       ,                 ""                       ,              ""                      ,"","","","","","","","","","","","","","","","","","","","",""  ]#   ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "       ] 
Text_File1_Name       =[          "HC - Fuel delivery Check1"      ,                 "test1"                           ,                 ""                                ,                 ""                        ,                 ""                          ,                  ""                         ,                 ""                       ,                 ""                       ,                 ""                       ,              ""                      ,"","","","","","","","","","","","","","","","","","","","",""  ]#   ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "       ] 
Text_File2_Name       =[          "HC - Fuel delivery Check2"      ,                 "test2"                           ,                 ""                                ,                 ""                        ,                 ""                          ,                  ""                         ,                 ""                       ,                 ""                       ,                 ""                       ,              ""                      ,"","","","","","","","","","","","","","","","","","","","",""  ]#   ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "         ,    "                            "       ] 




Thrmostat_Stuck_open="بناء على معطياتك\n\nتحتاج الى تغيير بلف الحرارة\n\nتكلفة البلف حول 70 ريال"
NORMAL_ENGINE_TEMP1="الحرارة الطبيعية لهذا المحرك تقريبا بين 85 -106"
NORMAL_ENGINE_TEMP2="الحرارة الطبيعية لهذا المحرك تقريبا بين 80 -97"
COOLING_FAN_DIAG="تتبع التعليمات وتكون دقيق حتى يطلع التشخيص اقرب مايمكن للصواب\n\n إفتح كبوت السيارة وإدخل على شاشة البيانات  الشاشة, شغل السيارة وراقب درجه الحرارة...وطوال الوقت المكيف يكون مطفي\n\n إذا وصلت الحرارة ل 99 راقب مروحه جهه الراكب وراقب مروحه جهه السواق وإكتب  الملاحظات كالتالي:\n\n الملاحظة الأولى: مروحه جهه السواق\nإذا كانت تعمل اكتب رقم 1. اذا ماتعمل اكتب 0\n\n الملاحظة الثانية: مروحه جهه الراكب\nإذا كانت تعمل اكتب رقم 1. اذا ماتعمل اكتب 0\n\n\n الآن شعل مكيف السيارة وتاكد زر ال AC مضغوط وراقب المراوح من جديد وإكتب الملاحظات كالتالي:\n\n  الملاحظة الثالثة: عن مروحه جهه السواق\nإذا كانت تعمل اكتب رقم 1. اذا ماتعمل اكتب 0\n\n الملاحظة الرابعة: مروحه جهه الراكب\nإذا كانت تعمل اكتب رقم 1. اذا ماتعمل اكتب 0\n\n\n لابد تكتب الارقام من اليسار لليمين...  مثال إذا مروحة جهه السواق لاتعمل اثناء تشغيل المكيف. وكل الملاحظات الأخرى طبيعية بيطلع الرقم هذا  \n\n 1 1 0 1"
COOLING_FAN_NOTE1="1 1 1 1"  ; COOLING_FAN_NOTE2="1 1 1 0" ; COOLING_FAN_NOTE3="0 0 0 1"  ;COOLING_FAN_NOTE4="1 1 0 1"  ; COOLING_FAN_NOTE5="0 0 1 1"    ;COOLING_FAN_NOTE6="0 0 1 0"
COOLING_FAN_RESULT1=" All working "
COOLING_FAN_RESULT2="check Fuse 59 and Relay HFC"
COOLING_FAN_RESULT3="Bad Fuse 60 or Relay LFC  or bad/unstable driver motor connector or bad diver motor verify first by chaking connector and tapping motor\n and can be bad FC Relay's pin won't conduct current (Rare)"
COOLING_FAN_RESULT4="if Relay FC won't switch: driver fan move slow (AC on) or maymbe won't move in high speed"
COOLING_FAN_RESULT5="Bad Fuse 63 - ask why (bad passenger motor?)"
COOLING_FAN_RESULT6="bad or unstable passenger motor connector or bad passenger motor which might got fuse 63 blown"


# عدد الاكواد الي حفظها   
# اسم الملف
filename = "dtc_data.json"
# قراءة البيانات من الملف مع تحديد الترميز
with open(filename, "r", encoding="utf-8") as file:
    data = json.load(file)
# استخراج جميع المفاتيح (الأكواد)
codes = list(data.keys())
json_file_path = "dtc_data.json"  # Fixed JSON file path
def check_code_prefixes():
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:  # Set encoding to UTF-8
            data = json.load(file)
        valid_prefixes = {'P', 'C', 'B', 'U'}  # Valid starting characters
        prefix_counts = {'P': 0, 'C': 0, 'B': 0, 'U': 0}
        invalid_codes = []

        for code in data.keys():
            if not code or code[0].upper() not in valid_prefixes:
                invalid_codes.append(code)
            else:
                prefix = code[0].upper()
                prefix_counts[prefix] += 1
        total_codes = len(data)
        return total_codes, prefix_counts, invalid_codes
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found")
        return 0, {}, []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file_path}'")
        return 0, {}, []
    

#"المساعد الذكي للمساعدة في تشخيص مشاكل الفيوجن"
# ================= Data Structures =================
DIAG = "المساعد الذكي للمساعدة في تشخيص مشاكل الفيوجن"
user_states = {}

# Systems and their subsections
systems = {
    "cooling": {
        "title": "مشاكل نظام تبريد المكينة",
        "text": "اختر القسم الذي تريد تشخيصه:",
        "subsections": {
            "overheat": {
                "text": "ارتفاع حرارة المحرك", 
                "flow": "overheat",
                "header": "تشخيص ارتفاع حرارة المحرك"
            },
            "fans": {
                "text": "عطل مروحة الرديتر", 
                "flow": "fans",
                "header": "تشخيص مروحة الرديتر"
            },
            "leak": {
                "text": "تهريب رديتر", 
                "flow": "leak",
                "header": "تشخيص تهريب الرديتر"
            }
        }
    },
    #_______________________________________________________
    "ac_problem1": {
        "title": "مشاكل التكييف",
        "text": "اختر نوع المشكلة في نظام التكييف:",
        "subsections": {
            "problem1": {
                "text": "مشكلة 1", 
                "flow": "ac_problem1",
                "header": "تشخيص مشكلة التكييف 1"
            }
        }
    },
    #_______________________________________________________
    "charging_system": {
        "title": "مشاكل نظام الشخن",
        "text": "اختر نوع المشكلة في نظام الشحن:",
        "subsections": {
            "problem1": {
                "text": "مشكلة 1", 
                "flow": "charging_system_problem1",
                "header": "تشخيص مشكلة التكييف 1"
            }
        }
    },    
    #_______________________________________________________
    "starting_system": {
      "title": "مشاكل تشفيل السيارة",
      "text": "اختر نوع المشكلة في نظام التشغيل:",
      "subsections": {
         "no_crank": {  # ✅ Unique key
               "text": "المحرك لايدور أثناء محاولة التشغيل",  # Button
               "flow": "starting_system_no_crank",
               "header": "تشخيص مشكلة المحرك لايدور"
         },
         "crank_no_start": {  # ✅ Unique key
               "text": "المحرك يدور ولاكن لاتشتغل السيارة",    # Button
               "flow": "starting_system_crank_no_start",
               "header": "تشخيص مشكلة المحرك يدور ولكن السيارة لاتشتغل"
         }    
      }
   }
}

# Centralized flows dictionary
flows = {
    "overheat": {
        "start": {
            "text": "",
            "options": ["📋 الأسباب المحتملة", "🔧 بدء التشخيص"],
            "tip": "💡 نصيحة: تأكد دائمًا من مستوى سائل التبريد قبل البدء!",
            "possible_causes": (
                "1. انخفاض مستوي ماء الرديتر (تهريب داخلي او خارجي)\n",
                "2. ماء الرديتر غير مناسب (قديم، صدأ، غير اصلي، نسبة الخليط)\n",
                "3. غطاء القربة تالف او لم يتم تركيبة بالشكل الصحيح\n",
                "4. انسداد أو تقييد تدفق الهواء (المكثف شبك الرديتر الشتر)\n",
                "5. عطل في مروحة الرديتر\n",
                "6. هواء محبوس داخل النظام\n",
                "7. مشاكل داخل الرديتر (انسداد - صدأ - تلف)\n",
                "8. عطل او ضعف في مضخة مويه الرديتر\n",
                "9. انحشار الثرموستات على وضع الاقفال\n",
                "10. خلط الماء مع الزيت (القير او المكينة)\n",
                "11. خلل في حساس حرارة المحرك\n",
                "12. خلل في مؤشر الحرارة\n"
            )
        },
        "B1": {
            "text": "🔍 B1: إجراء الفحص والتحقق\n\nقم بإجراء الفحص والتحقق في هذا القسم.\nهل توجد أي مشاكل؟",
            "yes": {"action": "🛠️ قم بالإصلاح حسب الحاجة", "next": None},
            "no": {"next": "B2"},
            "tip": "💡 تأكد من فحص جميع الأجزاء المرئية للنظام."
        },
        "B2": {
            "text": "🌬️ B2: التحقق من انسداد تدفق الهواء\n\nتحقق من المبرد أو مكثف التكييف لوجود عوائق خارجية (أوراق شجر، كرتون).\nهل يوجد انسداد؟",
            "yes": {"action": "🧹 قم بإزالة العائق", "next": None},
            "no": {"next": "B3"},
            "tip": "💡 تحقق من وجود أوراق الشجر أو الأتربة في المبرد."
        },
        "B3": {
            "text": "💧 B3: التحقق من مستوى سائل التبريد واختبار الضغط\n\n1. تحقق من مستوى سائل التبريد في خزان التمدد\n2. اختبر ضغط نظام التبريد\nهل يوجد تسريب خارجي؟",
            "yes": {"action": "🔧 قم بإصلاح/استبدال المكونات", "next": None},
            "no": {"next": "B4"},
            "tip": "💡 استخدم جهاز اختبار الضغط للتحقق من التسريبات."
        },
        "B4": {
            "text": "🛠️ B4: التحقق من تسريب سائل التبريد الداخلي\n\nافحص سائل التبريد لوجود علامات زيت المحرك.\nهل يوجد زيت محرك في سائل التبريد؟",
            "yes": {"action": "⚙️ راجع تشخيص نظام المحرك", "next": None},
            "no": {"next": "B5"},
            "tip": "💡 تحقق من وجود زيت محرك في سائل التبريد."
        },
        "B5": {
            "text": "🛢️ B5: التحقق من وجود سائل التبريد في الزيت\n\nافحص زيت المحرك لوجود علامات سائل التبريد.\nهل يوجد سائل تبريد في الزيت؟",
            "yes": {"action": "⚙️ راجع تشخيص نظام المحرك", "next": None},
            "no": {"next": "B6"},
            "tip": "💡 تحقق من وجود سائل تبريد في زيت المحرك."
        },
        "B6": {
            "text": "🔄 B6: التحقق من وجود سائل ناقل الحركة في سائل التبريد\n\nافحص خزان التمدد لوجود علامات سائل ناقل الحركة.\nهل يوجد سائل ناقل حركة في سائل التبريد؟",
            "yes": {"action": "🔄 قم بتركيب مبرد سائل ناقل حركة جديد\nراجع نظام تبريد ناقل الحركة", "next": None},
            "no": {"next": "B7"},
            "tip": "💡 تحقق من وجود سائل ناقل الحركة في سائل التبريد."
        },
        "B7": {
            "text": "🔄 B7: التحقق من وجود سائل التبريد في سائل ناقل الحركة\n\nافحص سائل ناقل الحركة لوجود علامات سائل التبريد.\nهل يوجد سائل تبريد في سائل ناقل الحركة؟",
            "yes": {"action": "🔄 قم بتركيب مبرد سائل ناقل حركة جديد\nراجع نظام تبريد ناقل الحركة", "next": None},
            "no": {"next": "B8"},
            "tip": "💡 تحقق من وجود سائل تبريد في سائل ناقل الحركة."
        },
        "B8": {
            "text": "🔥 B8: التحقق من وجود غازات الاحتراق\n\nاستخدم جهاز اختبار تسريب غازات الاحتراق في سائل التبريد.\nهل توجد غازات احتراق؟",
            "yes": {"action": "⚙️ راجع تشخيص نظام المحرك", "next": None},
            "no": {"next": "B9"},
            "tip": "💡 استخدم جهاز اختبار غازات الاحتراق للتحقق."
        },
        "B9": {
            "text": "🧼 B9: التحقق من حالة سائل التبريد\n\nافحص سائل التبريد لوجود أوساخ أو صدأ أو تلوث.\nهل حالة سائل التبريد جيدة؟",
            "yes": {"next": "B10"},
            "no": {"action": "🚿 قم بتنظيف نظام التبريد", "next": None},
            "tip": "💡 تأكد من نظافة سائل التبريد."
        },
        "B10": {
            "text": "🌀 B10: التحقق من مروحة التبريد الكهربائية\n\nقم بتشغيل المحرك، اضبط التكييف على الوضع الأقصى.\nهل تعمل المروحة بشكل طبيعي؟",
            "yes": {"next": "B11"},
            "no": {"action": "🔌 قم بتشخيص نظام المروحة\nراجع دليل PC/ED", "next": None},
            "tip": "💡 تحقق من عمل المروحة الكهربائية."
        },
        "B11": {
            "text": "💦 B11: التحقق من مضخة سائل التبريد\n\nقم بتشغيل المحرك لمدة 30 دقيقة، تحقق من حرارة خرطوم السخان.\nهل خرطوم السخان ساخن؟",
            "yes": {"next": "B12"},
            "no": {"action": "🔧 قم بتركيب مضخة تبريد جديدة", "next": None},
            "tip": "💡 تحقق من حرارة خرطوم السخان."
        },
        "B12": {
            "text": "🌡️ B12: التحقق من عمل الثرموستات\n\nقم بتشغيل المحرك لمدة 30 دقيقة، تحقق من حرارة خرطوم المبرد السفلي.\nهل خرطوم المبرد السفلي ساخن؟",
            "yes": {"action": "📈 تحقق من عمل مقياس الحرارة", "next": None},
            "no": {"next": "B13"},
            "tip": "💡 تحقق من حرارة خرطوم المبرد السفلي."
        },
        "B13": {
            "text": "🔍 B13: الفحص البصري للثرموستات\n\nقم بفحص الثرموستات بصريًا.\nهل الثرموستات تالف؟",
            "yes": {"action": "🔧 قم بتركيب ثرموستات جديد", "next": None},
            "no": {"action": "🔧 قم بتركيب ثرموستات جديد", "next": None},
            "tip": "💡 تأكد من سلامة الثرموستات."
        }
    },
    "fans": {
        "start": {
            "text": "🌀 تشخيص مروحة الرديتر\n\nتحقق من عمل المروحة الكهربائية.",
            "options": ["📋 الأسباب المحتملة", "🔧 بدء التشخيص"],
            "tip": "💡 نصيحة: تحقق من الفيوزات والأسلاك الكهربائية.",
            "possible_causes": (
                "1. فيوزات تالفة.\n"
                "2. أسلاك كهربائية مقطوعة.\n"
                "3. عطل في المحرك الكهربائي.\n"
                "4. مشكلة في وحدة التحكم."
            )
        },
        "B1": {
            "text": "🔌 B1: تحقق من الفيوزات\n\nافحص الفيوزات الخاصة بالمروحة.\nهل الفيوزات سليمة؟",
            "yes": {"next": "B2"},
            "no": {"action": "🔌 استبدل الفيوزات التالفة", "next": None},
            "tip": "💡 تحقق من الفيوزات الخاصة بالمروحة."
        },
        "B2": {
            "text": "🔧 B2: تحقق من الأسلاك الكهربائية\n\nافحص الأسلاك الكهربائية للمروحة.\nهل الأسلاك سليمة؟",
            "yes": {"next": "B3"},
            "no": {"action": "🔧 قم بإصلاح الأسلاك التالفة", "next": None},
            "tip": "💡 تحقق من سلامة الأسلاك الكهربائية."
        },
        "B3": {
            "text": "⚙️ B3: تحقق من المحرك الكهربائي للمروحة\n\nافحص المحرك الكهربائي للمروحة.\nهل المحرك يعمل بشكل صحيح؟",
            "yes": {"next": "B4"},
            "no": {"action": "🔧 قم باستبدال المحرك الكهربائي", "next": None},
            "tip": "💡 تحقق من عمل المحرك الكهربائي."
        },
        "B4": {
            "text": "🎛️ B4: تحقق من وحدة التحكم في المروحة\n\nافحص وحدة التحكم في المروحة.\nهل الوحدة تعمل بشكل صحيح؟",
            "yes": {"action": "✅ المروحة تعمل بشكل طبيعي", "next": None},
            "no": {"action": "🔧 قم باستبدال وحدة التحكم", "next": None},
            "tip": "💡 تحقق من عمل وحدة التحكم."
        }
    },
    "leak": {
        "start": {
            "text": "💧 تشخيص تهريب الرديتر\n\nتحقق من وجود تسريب في نظام التبريد.",
            "options": ["📋 الأسباب المحتملة", "🔧 بدء التشخيص"],
            "tip": "💡 نصيحة: افحص الخراطيم والتوصيلات.",
            "possible_causes": (
                "1. خراطيم تالفة أو متشققة.\n"
                "2. توصيلات غير محكمة.\n"
                "3. تشققات في الرديتر.\n"
                "4. تلف في خزان التمدد."
            )
        },
        "B1": {
            "text": "🔍 B1: تحقق من الخراطيم\n\nافحص خراطيم التبريد لوجود تشققات أو تلف.\nهل الخراطيم سليمة؟",
            "yes": {"next": "B2"},
            "no": {"action": "🔧 استبدل الخراطيم التالفة", "next": None},
            "tip": "💡 تحقق من سلامة الخراطيم."
        },
        "B2": {
            "text": "🔧 B2: تحقق من التوصيلات\n\nافحص التوصيلات بين الخراطيم والرديتر.\nهل التوصيلات سليمة؟",
            "yes": {"next": "B3"},
            "no": {"action": "🔧 قم بإصلاح التوصيلات التالفة", "next": None},
            "tip": "💡 تحقق من سلامة التوصيلات."
        },
        "B3": {
            "text": "🔍 B3: تحقق من الرديتر\n\nافحص الرديتر لوجود تشققات أو تلف.\nهل الرديتر سليم؟",
            "yes": {"action": "✅ نظام التبريد يعمل بشكل طبيعي", "next": None},
            "no": {"action": "🔧 قم باستبدال الرديتر", "next": None},
            "tip": "💡 تحقق من سلامة الرديتر."
        }
    },


    "no_crank": {
        "start": {
            "text": "🚗 **تشخيص مشكلة المحرك لا يدور** 🚗\n\nالخطوات التالية مبنية على دليل فورد الرسمي.",
            "options": ["📋 الأسباب المحتملة", "🔧 بدء التشخيص"],
            "possible_causes": [
                "1. مشكلة في البطارية أو كابلاتها",
                "2. عطل في محرك البدء (Starter Motor)",
                "3. تلف ريلاي البداية في صندوق التوزيع (BJB Starter Relay)",
                "4. مشاكل في وحدة التحكم بالمحرك (PCM)",
                "5. دارات كهربائية مقطوعة أو قصيرة"
            ],
            "tip": "💡 تأكد من شحن البطارية (فولتية أعلى من 12.2 فولت)"
        },
        "A1": {
            "text": "🔍 A1: الفحص البصري الأولي\n\n• تفقد الفيوزات (Fuse 84 في BJB و Fuse 18 في BCM)\n• تأكد من سلامة الوصلات الكهربائية الرئيسية",
            "yes": {"action": "إصلاح السبب الظاهر", "next": None},
            "no": {"next": "A2"},
            "tip": "💡 ابحث عن أسلاك مقطوعة أو وصلات مترهلة"
        },
        "A2": {
            "text": "📡 A2: فحص اتصال وحدات التحكم\n\n• شغّل الإشعال (Ignition ON)\n• استخدم أداة التشخيص لإجراء Network Test للـ BCM و PCM",
            "yes": {"next": "A3"},
            "no": {"action": "راجع قسم الاتصالات في الدليل", "next": None},
            "tip": "💡 الأخطاء هنا تشير لمشكلة في شبكة CAN"
        },
        "A3": {
            "text": "⚠️ A3: قراءة رموز الأعطال (DTCs)\n\n• استخدم أداة التشخيص لفحص رموز الأعطاب في BCM و PCM",
            "yes": {"action": "اتبع جدول رموز الأعطال للـ BCM/PCM", "next": None},
            "no": {"next": "A4"},
            "tip": "💡 رمز PD6E9 يشير لمشكلة في أداء محرك البدء"
        },
        "A4": {
            "text": "🔌 A4: فحص إشارة التشغيل من المفتاح\n\n• راقب PID IGN_SW_STRT أثناء تحويل المفتاح إلى وضع START",
            "yes": {"next": "A5"},
            "no": {"action": "تفقد دائرة تشغيل المفتاح", "next": None},
            "tip": "💡 عدم التغيير يشير لمشكلة في دائرة التشغيل"
        },
        "A5": {
            "text": "🚦 A5: فحص وضع ناقل الحركة\n\n• تأكد أن القير في وضع P أو N\n• راقب PID IN_GEAR",
            "yes": {"next": "A6"},
            "no": {"action": "راجع قسم ناقل الحركة", "next": None},
            "tip": "💡 القير يجب أن يكون في وضع محايد"
        },
        "A6": {
            "text": "⚡ A6: فحص إشارة التدوير من PCM\n\n• راقب PID ENG_CRANK أثناء تشغيل المفتاح",
            "yes": {"next": "A7"},
            "no": {"next": "A17"},
            "tip": "💡 الإشارة يجب أن تتغير إلى Active"
        },
        "A7": {
            "text": "🔋 A7: فحص دائرة ريلاي البداية\n\n• أزل ريلاي البداية\n• استخدم لمبة اختبار بين PIN 1 و PIN 2",
            "yes": {"next": "A8"},
            "no": {"next": "A15"},
            "tip": "💡 الإضاءة تشير لوصول التيار"
        },
        "A8": {
            "text": "🔧 A8: قياس فولتية ريلاي البداية\n\n• قس الفولتية على PIN 3 للريلاي (مقارنة ب الأرض)",
            "yes": {"next": "A9"},
            "no": {"action": "تفقد فيوز 30A أو إصلاح الدائرة", "next": None},
            "tip": "💡 يجب أن تكون الفولتية فوق 11 فولت"
        },
        "A9": {
            "text": "⚙️ A9: اختبار تشغيل محرك البدء يدويًا\n\n• وصّل جسر كهربائي بين PIN 3 و PIN 5 في الريلاي",
            "yes": {"action": "استبدل ريلاي البداية", "next": None},
            "no": {"next": "A10"},
            "tip": "💡 إذا لم يعمل المحرك، المشكلة في الدائرة الرئيسية"
        },
        "A10": {
            "text": "🔩 A10: فحص كابلات الأرضية للبطارية\n\n• قس الفولتية بين كابلات الأرضية و نقاط التوصيل",
            "yes": {"next": "A11"},
            "no": {"action": "نظف أو استبدل الكابلات", "next": None},
            "tip": "💡 التآكل هو السبب الشائع"
        },
        "A11": {
            "text": "🔌 A11: فحص تأريض محرك البدء\n\n• قس الفولتية بين جسم المحرك و الأرض",
            "yes": {"next": "A12"},
            "no": {"action": "نظف نقاط التوصيل", "next": None},
            "tip": "💡 تأكد من تثبيت المحرك بشكل صحيح"
        },
        "A12": {
            "text": "🔋 A12: قياس فولتية محرك البدء\n\n• قس الفولتية على طرف B لمحرك البدء",
            "yes": {"next": "A13"},
            "no": {"action": "استبدل كابلات البطارية", "next": None},
            "tip": "💡 الفولتية المنخفضة تشير لكابلات تالفة"
        },
        "A13": {
            "text": "🛠️ A13: اختبار أداء محرك البدء\n\n• نفّذ اختبار الدائرة الإيجابية لمحرك البدء",
            "yes": {"action": "أصلح السبب المحدد", "next": None},
            "no": {"next": "A14"},
            "tip": "💡 ابحث عن تلف في التروس الداخلية"
        },
        "A14": {
            "text": "🔌 A14: فحص إشارة البدء عند المحرك\n\n• قس الفولتية على طرف S لمحرك البدء",
            "yes": {"action": "نظف نقاط التوصيل", "next": None},
            "no": {"action": "أصلح الدائرة الكهربائية", "next": None},
            "tip": "💡 عدم وجود فولتية يشير لقطع في السلك"
        },
        "A15": {
            "text": "⚠️ A15: فحص دارات PCM للقصر مع الأرض\n\n• قس المقاومة بين دارات التحكم و الأرض",
            "yes": {"next": "A16"},
            "no": {"action": "أصلح الدائرة المعيبة", "next": None},
            "tip": "💡 المقاومة يجب أن تكون فوق 10,000 أوم"
        },
        "A16": {
            "text": "🔍 A16: فحص اتصال دارات PCM\n\n• تأكد من عدم وجود قطع في الأسلاك بين PCM والريلاي",
            "yes": {"next": "A17"},
            "no": {"action": "أصلح الدائرة", "next": None},
            "tip": "💡 المقاومة يجب أن تكون أقل من 3 أوم"
        },
        "A17": {
            "text": "💻 A17: فحص وحدة PCM\n\n• تفقد توصيلات PCM\n• نظف الطرفيات إذا لزم الأمر",
            "yes": {"action": "استبدل PCM أو اتبع TSBs", "next": None},
            "no": {"action": "المشكلة مؤقتة - أعد الفحص", "next": None},
            "tip": "💡 ابحث عن تحديثات برمجية إن وجدت"
        }
    }
}

# ================= Core Functions =================
def start_diagnosis(message):
    """Starts the diagnosis process by showing main system options."""
    keyboard = types.InlineKeyboardMarkup()
    for system_key, system_data in systems.items():
        keyboard.add(types.InlineKeyboardButton(
            text=system_data["title"],
            callback_data=f"Diag_System_{system_key}"  # Updated prefix
        ))
    bot.send_message(
        message.chat.id,
        f"({DIAG})\n\nاختر النظام الذي تريد تشخيصه:",
        reply_markup=keyboard
    )
def show_subsystem(call, system_key):
    """Shows the subsections for the selected system."""
    print(f"Debug: show_subsystem called with system_key = {system_key}")  # Debugging
    if system_key not in systems:
        print(f"Error: System key '{system_key}' not found in systems dictionary.")
        return
    system = systems[system_key]
    keyboard = types.InlineKeyboardMarkup()
    for sub_key, sub_data in system["subsections"].items():
        keyboard.add(types.InlineKeyboardButton(
            text=sub_data["text"],
            callback_data=f"Diag_Sub_{system_key}_{sub_key}"  # Updated prefix
        ))
    update_message(call, system["text"], keyboard)
def start_flow(call, system_key, sub_key):
    """Starts the diagnosis flow for the selected subsection."""
    sub_data = systems[system_key]["subsections"][sub_key]
    flow_name = sub_data["flow"]
    user_states[call.from_user.id] = {
        "current_flow": flow_name,  # تخزين اسم التدفق الحالي
        "current_step": "start",
        "header": sub_data["header"],
        "tip": sub_data.get("tip", ""),
        "started": False  # إضافة علامة بدء التشخيص
    }
    show_flow_step(call)
def show_flow_step(call):
    """Displays the current step in the diagnosis flow."""
    user_id = call.from_user.id
    state = user_states.get(user_id)
    
    flow = flows.get(state["current_flow"])
    step = flow.get(state["current_step"])
    
    # بناء النص الأساسي
    text = f"**{state['header']}**\n\n{step['text']}"
    
    # إضافة الأسباب المحتملة إذا كانت موجودة
    if state["current_step"] == "start" and "possible_causes" in step:
        causes = "\n".join(step["possible_causes"])
        text += f"📋 **الأسباب المحتملة:**\n{causes}"
    # إضافة النصيحة إذا كانت موجودة
    if "tip" in step:
        text += f"\n{step['tip']}"
    markup = types.InlineKeyboardMarkup()
    if "options" in step:
        for option in step["options"]:
            markup.add(types.InlineKeyboardButton(
                text=option,
                callback_data=f"flowopt_{state['current_flow']}_{option}"
            ))
    else:
        if "yes" in step:
            markup.add(types.InlineKeyboardButton("✅ نعم", callback_data=f"flowans_{state['current_step']}_yes"))
        if "no" in step:
            markup.add(types.InlineKeyboardButton("❌ لا", callback_data=f"flowans_{state['current_step']}_no"))
    update_message(call, text, markup)
def handle_flow_option(call, flow_name, option):
    """Handles user selection of options in the flow."""
    user_id = call.from_user.id
    state = user_states.get(user_id)
    if not state:
        return
    # الحصول على التدفق الحالي من القاموس العام flows
    current_flow = flows.get(flow_name)
    if not current_flow:
        print(f"Error: Flow '{flow_name}' not found.")
        return
    current_step = current_flow.get(state["current_step"])
    if not current_step:
        print(f"Error: Step '{state['current_step']}' not found.")
        return
    if option == "📋 الأسباب المحتملة":
        text = f"**{state['header']}**\n\nالأسباب المحتملة:\n"
        if "possible_causes" in current_step:
            text += current_step["possible_causes"]
        else:
            text += "لا توجد أسباب محددة متاحة." 
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=text
        )
    elif option == "🔧 بدء التشخيص":
        state["started"] = True
        state["current_step"] = "B1"  # بدء من الخطوة الأولى
        show_flow_step(call)
def handle_flow_answer(call, step, answer):
    """Handles Yes/No answers in diagnosis flows."""
    user_id = call.from_user.id
    state = user_states.get(user_id)
    if not state:
        return
    
    flow = flows.get(state["current_flow"])
    current_step = flow.get(step)
    response = current_step.get(answer.lower())
    # استخراج نص السؤال الأساسي (بدون تفاصيل إضافية)
    question_text = current_step['text'].split('\n')[0]  # السطر الأول فقط
    state["history"] = state.get("history", [])  # تهيئة القائمة إذا لم تكن موجودة
    state["history"].append(f"{question_text} ({'✅ نعم' if answer == 'yes' else '❌ لا'})")
    if response.get("action"):
        # بناء نص الملخص مع الأسئلة الأصلية
        summary = "\n".join(state["history"])  # سطر واحد بين كل إجابة
        text = (
            f"📜 **ملخص الإجابات:**\n"  # لا يوجد سطر فارغ بعد العنوان
            f"{summary}\n"
            f"............................\n\n"  # خط فاصل بعد الأسئلة
            f"⚡ **الإجراء المطلوب:**\n"
            f"{response['action']}"
        )
        # إضافة النصيحة إذا كانت متوفرة (بدون سطر فارغ بعدها)
        if "tip" in current_step:
            text += f"\n\n💡 **نصيحة:**\n{current_step['tip']}"
        # تحديث الرسالة مع الملخص المنظم
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=text,
            parse_mode="Markdown"  # تفعيل Markdown للتنسيق
        )
    elif response.get("next"):
        state["current_step"] = response["next"]
        show_flow_step(call)
    else:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="✅ اكتمل التشخيص. يمكنك البدء من جديد إذا لزم الأمر."
        )
        user_states.pop(user_id, None)
# ================= Callback Handler =================
def handle_query(call):
    """Main callback handler."""
    print(f"Debug: Received callback data: {call.data}")
    if call.data.startswith("Diag_System"):
        _, _, system_key = call.data.split('_', 2)
        show_subsystem(call, system_key)
    elif call.data.startswith("Diag_Sub"):
        _, _, system_sub = call.data.split('_', 2)
        system_key, sub_key = system_sub.split('_', 1)
        start_flow(call, system_key, sub_key)
    elif call.data.startswith("flowans"):
        _, step, answer = call.data.split('_', 2)
        handle_flow_answer(call, step, answer)
    elif call.data.startswith("flowopt"):
        _, flow_name, option = call.data.split('_', 2)
        handle_flow_option(call, flow_name, option)
# ================= Helper Functions =================
def update_message(call, text, markup):
    """Updates the message text only"""
    try:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=text,
            reply_markup=markup,
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Error updating message: {str(e)}")
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# احذف هذول اذا تبين ان مالهم داعي

# اللمبات صورة لها
#headlights All bulbs lamps      zzzzz

# https://youtu.be/0-PAoCj_G0c  قفل الباب الامامي

# الصدام الامامي https://youtu.be/KbZCJsuJ9qY?

# مقبض فتح كبوت https://youtu.be/iaUMf2UPPeI
# https://youtu.be/8KQlliBipIo
#https://youtu.be/rZNx-peGwfA

# كيبل الكبوت  https://youtu.be/bCLiae3YR5A

# قفل الكبوت جهه السواق  https://youtu.be/S4jHuZM6IDM

#  اللمبه الخلفيه https://youtu.be/V7ANerhYMjI

#"بوت ضبط وزنية اللمب"
#"https://t.me/fusion1/114493"

# سماعه اماميه 102 ريال
# رقم القطعه DS7Z-18808-F
# fuel line  https://youtu.be/J78PNqEGlzA




# قربه مويه المساحات https://youtu.be/mNClYe32gOk


# تزييت شنطه  https://youtu.be/6qBxw79sU6o

# فلنجه امامي احتياط 
#https://youtu.be/uwKStL3kaB4

# فريون 
#https://youtu.be/IjLfyXCBw1k




#   "طريقة صيانة\تغيير\تنظيف"  
# مقبض فتح الكبوت       
# فك الكبوت من الخارج   https://youtu.be/DFiOohr8vnA   
 #  فك الظهر الخلفي للكرسي الخلفي  https://youtu.be/h7SilGaUCbE
# مقبض الباب https://youtu.be/rEuCBD-zdT8
#  المفتاح   https://youtu.be/qS9TE75fgoE
#بطاريية المفتاح  https://youtu.be/HksQGk-mEac
# زجاج السواق https://youtu.be/SEHR_2PQj4A   

# لازم قسم لنظام العادم 


#Click_Start_time=3 ; sleep_time_A=20;  sleep_time_B=5;  sleep_time_C=7;  sleep_time_D=20;  sleep_time_E=20;  sleep_time_F=20;  sleep_time_G=20;  sleep_time_H=20;  sleep_time_J=20;  sleep_time_K=20;  sleep_time_L=20;  sleep_time_M=20;  sleep_time_N=20;  sleep_time_O=20;   sleep_time_Q=20;   sleep_time_R=20;  sleep_time_T=20; sleep_time_U=20;  sleep_time_V=20
#Reply_Welcome_Text=[ "العفو" ,   "عفوا" ,   "حياك" ,   "👍." ,   "العفو", "😇"  ]
#Selected_Icon="🔍"
#Founded__Icon="تم البحث..✔️"
#outro_stores=""#فضلاً..بعد شراء القطع صور الفاتورة بالقروب حتى أجمع قائمة لأسعار وأرقام القطع الإستهلاكية"
#All_cities_stores="................\nيوفر قطع وممكن يشحن لك:\nبن إسحاق (جدة)\n050 438 1840\n058 219 9631\n055 468 5568\n\nجيان فورد (جدة)\n053 353 3555\nجيان فورد (أبها)\n055 475 4444\n\nاو طلب من مواقع مثل موقع RockAuto"
#Shop_locations="\nلتحديد موقع المحل..إكتب في قوقل ماب (قطع غيار فورد + اسم المحل)"
#intro_Parts ="\nحدد المنطقة لأتمكن من مساعدتك"
#inro_parts_numbers = "\nإختار الفرع الي تنتمي لة القطعة الإستهلاكية ...قد لاتجد ماتريدة هنا.  مازالت أتعلم"
#Intro_Locations="تم العثور على صورة وموقع القطعة بنجاح\U00002714\n\n"
#Intro_prices= "\nفيوجن 2013-2016\nمحرك 2.5"
# (الرد الثاني (جاري البحث
#💠بحث موقع: TTTT
#ClickT=["clickT" , "Parts_Related","botton_Return_T" ,"T_2013+" ,"Return_T_2013+" ,"T_2012" ,"Return_T_2012" ,"clickT1" ,"clickT2" ,"clickT3" ,"clickT4" ,"clickT5" ,"clickT6" ,"clickT7" ,"clickT8" ,"clickT9" ,"clickT10" ,"clickT11" ,"T_A[0]" ,"T_A[1]" ,"T_A[2]",  "Location_A[0]","Location_A[1]","Location_A[2]","Location_A[3]","Location_A[4]","Location_A[5]","Location_A[6]","Location_A[7]","Location_A[8]","Location_A[9]","Location_A[10]","Location_A[11]","Location_A[12]","Location_A[13]","Location_A[14]","Location_A[15]","Location_A[16]","Location_A[17]","Location_A[18]","Location_A[19]","Location_A[20]","Location_A[21]","Location_A[22]","Location_A[23]","Location_A[24]","Location_A[25]","Location_A[26]","Location_A[27]","Location_A[28]","Location_A[29]","Location_A[30]","Location_B[0]","Location_B[1]","Location_B[2]","Location_B[3]","Location_B[4]","Location_B[5]","Location_B[6]","Location_B[7]","Location_B[8]","Location_B[9]","Location_B[10]","Location_B[11]","Location_B[12]","Location_B[13]","Location_B[14]","Location_B[15]","Location_B[16]","Location_B[17]","Location_B[18]","Location_B[19]","Location_B[20]","Location_B[21]","Location_B[22]","Location_B[23]","Location_B[24]","Location_B[25]","Location_B[26]","Location_B[27]","Location_B[28]","Location_B[29]","Location_B[30]",        "Location_C[0]","Location_C[1]","Location_C[2]","Location_C[3]","Location_C[4]","Location_C[5]","Location_C[6]","Location_C[7]","Location_C[8]","Location_C[9]","Location_C[10]","Location_C[11]","Location_C[12]","Location_C[13]","Location_C[14]","Location_C[15]","Location_C[16]","Location_C[17]","Location_C[18]","Location_C[19]","Location_C[20]","Location_C[21]","Location_C[22]","Location_C[23]","Location_C[24]","Location_C[25]","Location_C[26]","Location_C[27]","Location_C[28]","Location_C[29]","Location_C[30]","Location_D[0]","Location_D[1]","Location_D[2]","Location_D[3]","Location_D[4]","Location_D[5]","Location_D[6]","Location_D[7]","Location_D[8]","Location_D[9]","Location_D[10]","Location_D[11]","Location_D[12]","Location_D[13]","Location_D[14]","Location_D[15]","Location_D[16]","Location_D[17]","Location_D[18]","Location_D[19]","Location_D[20]","Location_D[21]","Location_D[22]","Location_D[23]","Location_D[24]","Location_D[25]","Location_D[26]","Location_D[27]","Location_D[28]","Location_D[29]","Location_D[30]","Location_E[0]","Location_E[1]","Location_E[2]","Location_E[3]","Location_E[4]","Location_E[5]","Location_E[6]","Location_E[7]","Location_E[8]","Location_E[9]","Location_E[10]","Location_E[11]","Location_E[12]","Location_E[13]","Location_E[14]","Location_E[15]","Location_E[16]","Location_E[17]","Location_E[18]","Location_E[19]","Location_E[20]","Location_E[21]","Location_E[22]","Location_E[23]","Location_E[24]","Location_E[25]","Location_E[26]","Location_E[27]","Location_E[28]","Location_E[29]","Location_E[30]","Location_F[0]","Location_F[1]","Location_F[2]","Location_F[3]","Location_F[4]","Location_F[5]","Location_F[6]","Location_F[7]","Location_F[8]","Location_F[9]","Location_F[10]","Location_F[11]","Location_F[12]","Location_F[13]","Location_F[14]","Location_F[15]","Location_F[16]","Location_F[17]","Location_F[18]","Location_F[19]","Location_F[20]","Location_F[21]","Location_F[22]","Location_F[23]","Location_F[24]","Location_F[25]","Location_F[26]","Location_F[27]","Location_F[28]","Location_F[29]","Location_F[30]","Location_G[0]","Location_G[1]","Location_G[2]","Location_G[3]","Location_G[4]","Location_G[5]","Location_G[6]","Location_G[7]","Location_G[8]","Location_G[9]","Location_G[10]","Location_G[11]","Location_G[12]","Location_G[13]","Location_G[14]","Location_G[15]","Location_G[16]","Location_G[17]","Location_G[18]","Location_G[19]","Location_G[20]","Location_G[21]","Location_G[22]","Location_G[23]","Location_G[24]","Location_G[25]","Location_G[26]","Location_G[27]","Location_G[28]","Location_G[29]","Location_G[30]","Location_H[0]","Location_H[1]","Location_H[2]","Location_H[3]","Location_H[4]","Location_H[5]","Location_H[6]","Location_H[7]","Location_H[8]","Location_H[9]","Location_H[10]","Location_H[11]","Location_H[12]","Location_H[13]","Location_H[14]","Location_H[15]","Location_H[16]","Location_H[17]","Location_H[18]","Location_H[19]","Location_H[20]","Location_H[21]","Location_H[22]","Location_H[23]","Location_H[24]","Location_H[25]","Location_H[26]","Location_H[27]","Location_H[28]","Location_H[29]","Location_H[30]","Location_J[0]","Location_J[1]","Location_J[2]","Location_J[3]","Location_J[4]","Location_J[5]","Location_J[6]","Location_J[7]","Location_J[8]","Location_J[9]","Location_J[10]","Location_J[11]","Location_J[12]","Location_J[13]","Location_J[14]","Location_J[15]","Location_J[16]","Location_J[17]","Location_J[18]","Location_J[19]","Location_J[20]","Location_J[21]","Location_J[22]","Location_J[23]","Location_J[24]","Location_J[25]","Location_J[26]","Location_J[27]","Location_J[28]","Location_J[29]","Location_J[30]","Location_K[0]","Location_K[1]","Location_K[2]","Location_K[3]","Location_K[4]","Location_K[5]","Location_K[6]","Location_K[7]","Location_K[8]","Location_K[9]","Location_K[10]","Location_K[11]","Location_K[12]","Location_K[13]","Location_K[14]","Location_K[15]","Location_K[16]","Location_K[17]","Location_K[18]","Location_K[19]","Location_K[20]","Location_K[21]","Location_K[22]","Location_K[23]","Location_K[24]","Location_K[25]","Location_K[26]","Location_K[27]","Location_K[28]","Location_K[29]","Location_K[30]","Location_L[0]","Location_L[1]","Location_L[2]","Location_L[3]","Location_L[4]","Location_L[5]","Location_L[6]","Location_L[7]","Location_L[8]","Location_L[9]","Location_L[10]","Location_L[11]","Location_L[12]","Location_L[13]","Location_L[14]","Location_L[15]","Location_L[16]","Location_L[17]","Location_L[18]","Location_L[19]","Location_L[20]","Location_L[21]","Location_L[22]","Location_L[23]","Location_L[24]","Location_L[25]","Location_L[26]","Location_L[27]","Location_L[28]","Location_L[29]","Location_L[30]"]                  
#T="مواقع وصور القطع"            ;T1="ENGINE CONTROLS"    ;T2="AC SYSTEM" ;    T3="DRIVE BELT" ;   T4="AIRBAG SYSTEM" ;   T5="Emission Controls" ;   T6="Fuel SYSTEM" ;   T7="HORN SYSTEM" ;   T8="MODULES" ;   T9="Parking Brake" ;   T10="Rear Suspension" ;   T11="TPMS" ;     T12="ENGINE Cooling" ;     T13="Trans Cooling" ;     T14="ALL Views" ;          
#  BOT LEVELS
#داخل الاقواس حط رمز المستخدم لكل عضوا بما يتناسب مع مستواه

#______________________________________________________________________________________________________________________________


# قسم الصيانات الدورية
def generate_maintenance_keyboard(category):
    config = MAINTENANCE_CONFIG[category]
    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(
            text=f"{config['items'][part]['emoji']} {part}",
            callback_data=f"maintenance_{category}_{part}"
        ) for part in config['items']
    ]
    # Arrange buttons in rows of 3
    idx = 0
    while idx < len(buttons):
        keyboard.row(*buttons[idx:idx + 3])  # Add 3 buttons in each row
        idx += 3  # Move to the next set of 3 buttons
    return keyboard
#________________________

def normalize_input(text):
    # Remove leading/trailing spaces
    text = text.strip()
    # Remove zero-width spaces and other invisible characters
    text = re.sub(r'[\u200B\u200C\u200D\uFEFF]', '', text)
    return text

def is_valid_info(text):
    #""" تتحقق مما إذا كانت البيانات تحتوي على أحرف أو أرقام """
    return bool(re.search(r'[a-zA-Z0-9ء-ي]', text))

def isMSG(message):
    return True
@bot.message_handler(func=isMSG)
def reply(message):
 global last_time ; now = time.time() ;  error_in_vin=0 ; stop_the_bot=0   # MAKE IT (1) IF YOU WANT TO DISABLE THE RESPONSES    # to allow keep it  =0
 words = message.text ; keyboard=types.InlineKeyboardMarkup()
 emoji              =['\U0001F60E ',' \U0001F642 ',' \U0001F601 ',' \U0001F604 ',' \U0001F609 ',' \U0001F60C ',' \U0001F31d ',' \U0001F31a ' ,"\U0001F60E","\U0001F60E","\U0001F60E", "\U0001F60C", '\U0001F60C', '\U0001F60C']  #\U0001F603', upside down emojii


#_______________________________________________________________________xxxx
 global message_user_map
 # Track the user's message ID and chat ID immediately
 message_user_map[(message.chat.id, message.message_id)] = message.from_user.id
#_______________________________________________________________________


#use this   bot.answer_callback_query(call.id, f"({Z})\n\n https://t.me/fusion1/77876" , show_alert=True)
################################################# (SPAM CHECK + USER ID )  ok ONLY IN MY GROUPs OR ME ########################################################
 ## CHECK SPAM MESSAGES  in  MAIN GROUP                        AND MY PRIVATE CHAT      
 if (message.chat.id == -1001375465311  )   and   ("اجازه مرضيه" in words    or"إنجاز فوري" in words  or"إلغاء مخالفات" in words   or"الغاء مخالفات" in words     or"انجاز فوري" in words   or"سكليف معتمد" in words   or"تنزل في صحتي" in words    or "اجازه مرضية" in words   or "إجازه مرضيه" in words    or "إجازه مرضية" in words     or "اجازة مرضيه"in words    or"إجازة مرضية" in words    or "اجازة مرضية" in words     or "إجازة مرضيه" in words     or "إسقاط مركبات" in words    or "اسقاط مركبات" in words    or "إسقاط مركبة" in words   or "إسقاط مركبه" in words   or "اسقاط مركبة" in words     or "اسقاط مركبة" in words   or "تسجيل جرعات" in words     or "بدون حضور" in words     or "قروبات التوظيف" in words   or "قروبات التوظيف" in words   or "قرض الزواج" in words    or "قرض ترميم" in words   or "قرض العمل الحر" in words    or "جرعات" in words    or "أسقاط مركبات" in words     or "أسقاط مركبة" in words    or "بعد النجاز" in words  or "إجازاه مرضيه" in words  or "إجازاة مرضيه"in words   or "إجازاه مرضية" in words   or "إجازاة مرضية" in words   or "أسقاط مركبة" in words   or "أسقاط مركبات" in words     or "لقاح كورونا" in words     or "تمويل الراجحي" in words    or "أسقاط مركبة" in words     or "وثيقة العمل الحر" in words     or "بدون حضور" in words    or "أسقاط مركبه" in words     or "تمويل الراجحي" in words     or "قرض امكان" in words   or "وظائف تناسبك" in words     or "وظائف نسائية" in words     or "وظائف عن بعد" in words    or "تمويل الراجحي" in words     or "تمويل الراجحي" in words     or "تمويل الراجحي" in words       or "لقاح كرونا" in words    or "لقاح كوفيد" in words      or "قرض  كنف" in words  or "سكليف ثلاث" in words   or"قروبات التوظيف"in words    or"قروبات التوظيف"in words    or"قرض الزواج"in words    or"قرض ترميم"in words    or"قرض العمل الحر"in words    or"كوفيد"in words    or"أسقاط مركبات"in words    or"أسقاط مركبة"in words    or"أسقاط مركبة"in words    or"أسقاط مركبات"in words    or"لقاح كورونا"in words    or"تمويل الراجحي"in words    or"أسقاط مركبة"in words    or"وثيقة العمل الحر"in words    or"بدون حضور"in words    or"أسقاط مركبه"in words    or"تمويل الراجحي"in words    or"قرض امكان"in words    or"وظائف تناسبك"in words    or"وظائف نسائية"in words    or"وظائف عن بعد"in words    or"تمويل الراجحي"in words    or"تمويل الراجحي"in words    or"تمويل الراجحي"in words        or"الآن شقال"in words    or"لقاح كرونا دون حضور"in words       or"الان شقال"in words    or"قرض  كنف"in words    or"معتمد صحتي"in words    or"فتح ملف"in words    or"تمديد زيارة"in words    or"تقيير مهنه عامل"in words    or"الغاء بلاغ هروب"in words    or"بعد الإنجاز"in words    or"بعد الانجاز"in words    or"لقاح كويتي"in words    or"لقاح أماراتي"in words    or"أسقاط مركبات"in words      or"تأشيرات مساند"in words      or"تفعيل ملفات"in words    or"تصفير الضريبة"in words    or"تخفيض زكاة"in words    or"تشيرات مساند"in words    or"شطب سجلات تجاري"in words    or"الغاء مخلفات"in words    or"إلغاء مخالفات"in words    or"إلغاء مخلفات"in words    or"مكتب العمل"in words    or"نقل من فردي"in words    or"فتح ملف"in words    or"تفعيل ملفات"in words    or"جميع الكشوف الطبيه"in words    or"فتح شاشه اصدار"in words    or"تصفير الضريبه"in words    or"تصفير الضريبة"in words    or"تصفير غرامات"in words    or"فك نسبه"in words    or"الغاء حمايه الاجور"in words    or"إلفاء قروض"in words    or"الغاء قروض"in words    or"الغاء قرض"in words    or"إلغاء قرض"in words    or"الدفع بعد الانجاز"in words   or"الدفع بعد الإنجاز"in words     or"إصدار رخص"in words   or"تصفير ضريبة"in words   or"تـصـفـيـر"in words   or"الدفع بعد النجاز"in words    or"الضـريبـه"in words    or"تخفيض المخالفات"in words    or"لقاح بدون حضور"in words    or"إصدار رخص قياده"in words  or"تطعيم محصن"in words   or"قرض عقاري"in words   or"قرض بنكي"in words    or"دخل اسبوعي"in words or"مجال التداول"in words   or"شُقُآلَ"in words   or"مًرکْبًهّ"in words     or"آجّآزٍهّ"in words   or"سِکْلَيَفُ"in words   or"تجّدٍيَدٍ"in words   or"إنِجّآزٍ"in words                  or"تـ"in words  or"مـ"in words  or"حـ"in words   or"صـ"in words   or"اســ"in words   or"ســـ"in words    or"نـ"in words    or"cryptocurrency"in words    or"cryptocurrency"in words or"digital currencies"in words or"digital currency"in words or"bitcoin"in words  or"Bitcoin"in words or"Cryptos"in words or"currency"in words  or"فرص وظيف"in words or"فرص وظيف"in words or"فرصه وظيف"in words or"فرصه وظيف"in words  or"فرصة وظيف"in words or"فرصة وظيف"in words         or "🖕" in words    or "ليف⢤ ك⣄س" in words   or "اـ" in words or "بـ" in words or "تـ" in words or "ثـ" in words or "جـ" in words or "حـ" in words or "خـ" in words or "دـ" in words or "ذـ" in words or "رـ" in words or "زـ" in words or "سـ" in words or "شـ" in words or "صـ" in words or "ضـ" in words or "طـ" in words or "ظـ" in words or "عـ" in words or "غـ" in words or "فـ" in words or "قـ" in words or "كـ" in words or "لـ" in words or "مـ" in words or "نـ" in words or "هـ" in words or "وـ" in words or "يـ" in words or "ـا" in words or "ـب" in words or "ـت" in words or "ـث" in words or "ـج" in words or "ـح" in words or "ـخ" in words or "ـد" in words or "ـذ" in words or "ـر" in words or "ـز" in words or "ـس" in words or "ـش" in words or "ـص" in words or "ـض" in words or "ـط" in words or "ـظ" in words or "ـع" in words or "ـغ" in words or "ـف" in words or "ـق" in words or "ـك" in words or "ـل" in words or "ـم" in words or "ـن" in words or "ـه" in words or "ـو" in words or "ـي" in words): 
    name1=message.from_user.first_name; name2=message.from_user.last_name; Spammer_ID=message.from_user.id
    # Send the alert to the user
    bot.delete_message(message.chat.id, message.message_id); t = time.localtime(); current_time = time.strftime("%H:%M:%S", t); print(f'..................\n..................\n{current_time}\n🔕 SPAM Deleted:({message.from_user.first_name})\n   ID:({message.from_user.id})')
    bot.send_message( MY_ID, f"🔕 تم رصد وحذف سبام / أو كلمات محظورة من:\n[{name1} {name2}](tg://user?id={Spammer_ID})", parse_mode="Markdown",disable_notification=True )

 # Who Can Use The Bot: (allow me always)              and allow (these group chats list)
 if ( (message.from_user.id != MY_ID)   and  (message.chat.id not in  Allowed_ID_to_use) )  :
     time.sleep(0.3)  
 else :
    ## Reply to Blocked Users 🚫🚫🚫🚫🚫🚫🚫🚫
    if  ("بوت"== words   or  words.split()[0]=="بوت") and (stop_the_bot==0)  and   (  message.from_user.id  in  Blocked   ) : 
        name1=message.from_user.first_name; name2=message.from_user.last_name; Spammer_ID=message.from_user.id
        bot.delete_message(message.chat.id, message.message_id)
        t = time.localtime(); current_time = time.strftime("%H:%M:%S", t); print(f'..................\n..................\n{current_time}\n🚫 Deleted Blocked User Message :({message.from_user.first_name})\n   ID:({message.from_user.id})')
        bot.send_message( MY_ID , f"🚫 تم رصد محاولة من محظور:\n[{name1} {name2}](tg://user?id={Spammer_ID})", parse_mode="Markdown",disable_notification=True )

     ## pause before amother reply  
    if ( (now - last_time) > (Short_Pause_BeforeAnotherReply) )  and  (  f"{Signature}" not in words  )  and  (message.from_user.id  not in  Blocked ): 
       #emoji=['\U0001F60E ',' \U0001F642 ',' \U0001F601 ',' \U0001F604 ',' \U0001F609 ',' \U0001F60C ',' \U0001F31d ',' \U0001F31a ' ,"\U0001F60E","\U0001F60E","\U0001F60E", "\U0001F60C", '\U0001F60C', '\U0001F60C']  #\U0001F603', upside down emojii   
       words_list =[" هلا ", " مرحبا ", " حياك ", " ولا يهمك  "," هلا "," أهلين "," ياهلا "," أهلا ","أبشر"]
       random_word = random.choice(words_list)#;  random_emoji = random.choice(emoji)
       Start="\n🟢 إضغط للتأكيد"; Start_Caption = random_word
       Pick_one=random.choice(Pick_one_1)
       Pick_City=random.choice(Pick_City_1)
       Pick_Engine=random.choice(Pick_Engine_1)
       Pick_model=random.choice(Pick_model_1)
       Pick_wheel_size=random.choice(Pick_wheel_size_1)
       Searching_Text=random.choice(Searching_Text_1)
       # Getting (  ID    and   Level of Sender)
       if (message.from_user.id !=5308309193)  :
          Current_Level=""
       if message.from_user.id == 5308309193 :
          Current_Level=" 🎖🎖🎖🎖🎖"

       ################################################# DIRECT SEND TO (ME OR  GROUP)  ########################################################
      #Tseto SOUND FILES TEST 
      # لاستعراض كل ملفات الصوت حسب الموجودة داخكل المجموعات
       if (  (message.from_user.id == 5308309193)  and ("testo" == words or "Testo" == words) ) : 
          wz=0
          while wz <= 100:
                Array_name=   Answer_AS_Lnik  #<<<  اختبر اي مجموعه ملفات صوتيه عن طريق اسم المجموعة فقط
                bot.send_voice(chat_id=message.chat.id, voice=open(f'{Sound_File_Location}{Array_name[wz]}.ogg','rb'),     caption=Array_name[wz],    disable_notification=True, reply_to_message_id=message.message_id) ;time.sleep(1)
                wz += 1; time.sleep(2.5)
      # لاستعراض كل ملفات الصوت حسب أسماء الملفات 
       if (  (message.from_user.id == 5308309193)  and ("testo2" == words or "Testo2" == words   or "testo 2" == words or "Testo 2" == words) ) : 
          wz=1
          while wz <= 100:          
                File_name= "Results_G"            # <<< اختبر اي ملفات صوتيه عن طريق تغيير الاسم فقط ماقبل الرقم
                bot.send_voice(chat_id=message.chat.id, voice=open(f'{Sound_File_Location}{File_name}{wz}.ogg','rb'),     caption=f'{File_name}{wz}',    disable_notification=True, reply_to_message_id=message.message_id) ;time.sleep(1)
                wz += 1; time.sleep(2.5)

       if ("\U0001F7E2..SuperSyn.." in words and message.chat.id == 5308309193):
         cleaned_message = words.replace("\U0001F7E2..SuperSyn..", "").strip()
         # Send the cleaned message to the group
         bot.send_message(Test_Group_ID, cleaned_message, disable_notification=True, protect_content=Protect_Content_Switch)
         
        ## ALL BOT Options
       if ("بوت"== words   or"بووت"== words  or"Bot"== words   or"bot"== words ) and (stop_the_bot==0)  and   (  message.from_user.id  not in  Blocked   ) : 
          refrence_IDrelpy_value=0 ;  name=message.from_user.first_name
          words_list =[" "," "," "," "," "," "," "] #" هلا "   ,   " مرحبا "   , " حياك"  ,   " "  ,   " صلي على محمد "   ,  " "  ,  " "   ,   "هل تعلم؟..يمكنك وضعي على الصامت حتى لا أزعجك بالتنبيهات\n\nإضغط على بروفايلي وثم الغي الإشعارات",   " "     ,  " "  , " "   ,   " "   , " " , " "   ,  " مرحبا"   , " حياك",
          random_word = random.choice(words_list) 
          random_emoji = random.choice(emoji)
          Message_ID=message.message_id
          t = time.localtime(); current_time = time.strftime("%H:%M:%S", t); print(f'..................\n..................\n{current_time}\n🟢 Activated By:({message.from_user.first_name})\n   ID:({message.from_user.id}) Level:{Current_Level}')
          Random_Bot_reply = random.choice(First_Bot_replies)
       #########################################  خيارات البوت  ###################################
          if  (message.from_user.id  == MY_ID  ):
               # هذا رد صوتي خاص فيني انا
               Random_Bot_reply = random.choice(First_Bot_replies)
          botton0 =types.InlineKeyboardButton(text= B                  ,callback_data='clickB')             #بحث معلومات المركبة برقم الهيكل
          botton1 =types.InlineKeyboardButton(text= MAINTENANCE        ,callback_data='MAINTENANCE')        #الصيانات الدورية
          botton2 =types.InlineKeyboardButton(text= Amounts_and_Sizes  ,callback_data='Amounts_and_Sizes')  #كميات  ومقاسات
          botton3 =types.InlineKeyboardButton(text= G                  ,callback_data='clickG')             # مشاكل متكررة
          botton4 =types.InlineKeyboardButton(text= R                  ,callback_data='clickR')             #الإستدعائات KSA
          botton5 =types.InlineKeyboardButton(text= H                  ,callback_data='clickH')             #ضبط إعدادات - مود
          botton6 =types.InlineKeyboardButton(text= O                  ,callback_data='clickO')             #أفضل الورش حسب المدينة
          botton7 =types.InlineKeyboardButton(text= Parts_Related      ,callback_data='Parts_Related')      #كل مايخص قطع الغيار 
          botton9 =types.InlineKeyboardButton(text= C                  ,callback_data='clickC')             #بحث عن فيوز
          botton11=types.InlineKeyboardButton(text= A                  ,callback_data='clickA')             # أرقام محلات قطع الغيار
          botton12=types.InlineKeyboardButton(text= Q                  ,callback_data='clickQ')             # Pin point check  تشخيص
          botton13=types.InlineKeyboardButton(text= W                  ,callback_data='clickW')             # المراجع والكتيبات

          botton00=types.InlineKeyboardButton(text= Z                  ,callback_data='clickZ')             # حول البوت
          keyboard.add(botton0).add(botton7).add(botton1,botton2).add(botton3,botton9).add(botton6,botton11).add(botton4,botton5).add(botton12,botton13).add(botton00)
          emoji   =[' \U0001F643 ',' \U0001F643','\U0001F643',' \U0001F607 ',' \U0001F60C ',"\U0001F60E","\U0001F60E","\U0001F60E","\U0001F60E","\U0001F60E"]
          random_emoji = random.choice(emoji)
          Random_Bot_reply = random.choice(First_Bot_replies)
          bot.send_voice(chat_id=message.chat.id, voice=open(f'{Sound_File_Location}{Random_Bot_reply}.ogg','rb'), caption=f'{Current_Level}\n{random_emoji}', disable_notification=True,reply_markup=keyboard, reply_to_message_id=message.message_id)                          
          last_time = now 
          stop_the_bot=1 # to stop any further checks on the rest of code

       #  DIRECT ANSWERS  
       if  (  ( "بوت الأوامر المباشر" in words   or  "بوت الاوامر المباشر" in words )  and  (stop_the_bot==0)  ) :
         last_time = now   
         bot.send_message(message.chat.id,f"{Signature}\n\U0001F607\n [الاوامر المباشره](https://t.me/fusion1/77873)", parse_mode="MarkdownV2", disable_notification=True, reply_to_message_id=message.message_id)
         stop_the_bot=1 # to stop any further checks on the rest of code
     
     
       if ("بوت كم مسمار" in words) and (stop_the_bot == 0):
         last_time = now
         file_types = {"TT1": "png", "TT2": "png", "TT3": "png", "TT4": "png", "TT5": "png"}
         all_codes = ["TT1", "TT2", "TT3", "TT4", "TT5"]
         max_retries = 3

         for attempt in range(max_retries):
            try:
                  media_group = []
                  missing_files = []  # Track missing files for debugging
                  for code in all_codes:
                     file_path = f'{Pictures_File_Location}{code}.{file_types[code]}'
                     # Check if file exists
                     if os.path.exists(file_path):
                        media_group.append(types.InputMediaPhoto(open(file_path, 'rb')))
                  # Only send if media_group is not empty
                  if media_group:
                     bot.send_media_group(
                        chat_id=message.chat.id,
                        media=media_group,
                        disable_notification=True,
                        protect_content=Protect_Content_Switch_R,
                        reply_to_message_id=message.message_id
                     )
                     break  # Exit retry loop on success
                  else:
                     break  # Exit if no files are available
            except Exception as e:
                  if attempt == max_retries - 1:  # Last attempt
                     time.sleep(1)
                     
     
       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
       #__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
           
       #B BBBBB   VIN DECODER 
       for element in trigger_B :
           if  (element in words)  and  (element !="")  and (stop_the_bot==0)  : 
                bot.send_photo(message.chat.id, photo=open(f'{Pictures_File_Location}VIN lovations.png', 'rb'), caption=f"{Signature}\n\n{REPLY_TEXT_VIN}\n\n{Put_At_End_Of_Message}", disable_notification=True, reply_to_message_id=message.message_id)
                stop_the_bot=1 # to stop any further checks on the rest of code
                break

       if (len((''.join(message.text.split()).lower())))!=20 and ( (''.join(message.text.split()).lower())[0:3]=="vin" or (''.join(message.text.split()).lower())[0:3]=="vln" ) and (len((''.join(message.text.split()).lower())))>=11  and (stop_the_bot==0) :
            bot.send_message(message.chat.id, "تأكد من رقم الهيكل. الرقم مكون من 17 خانة")
            time.sleep(20)
            bot.delete_message(message.chat.id, ((message.message_id) + 1) )
            bot.delete_message(message.chat.id, (message.message_id) )

       #check if number is correct and if model is 2013-2020  or not
       if (len((''.join(message.text.split()).lower())))==20 and ( (''.join(message.text.split()).lower())[0:3]=="vin" or  (''.join(message.text.split()).lower())[0:3]=="vln"   ) and ((''.join(message.text.split()).lower())[12]=="d"  or  (''.join(message.text.split()).lower())[12]=="e"  or  (''.join(message.text.split()).lower())[12]=="f"  or  (''.join(message.text.split()).lower())[12]=="g"  or  (''.join(message.text.split()).lower())[12]=="h" or  (''.join(message.text.split()).lower())[12]=="j"  or  (''.join(message.text.split()).lower())[12]=="k"  or  (''.join(message.text.split()).lower())[12]=="l" )  and(stop_the_bot==0) :  
            VIN_intro="\n\U0001F50D"
            random_emoji ="\U0001FAE1"
            vin_number=(''.join(message.text.split()).lower())[3:21]
            Manufacturer_Identifier = vin_number[0:3]   
            Trim_info = vin_number[4:7]
            Engine_type = vin_number[7]
            Model_year  = vin_number[9]
            Assembly_plant = vin_number[10]
            sequence_number = vin_number[11:17]
            vin_error=""
            print(vin_number)
            print("Finding VIN INFO...")

            if (Manufacturer_Identifier=="3fa") :
               Manufacturer_text ="تصنيع مكسيكي\n"
            if (Manufacturer_Identifier=="1fa") :
               Manufacturer_text ="تصنيع أمريكي\n"    
            if (Manufacturer_Identifier=="sfa") :
               Manufacturer_text ="تصنيع بريطاني\n"    
            if (Manufacturer_Identifier=="tw2") :
               Manufacturer_text ="تصنيع برتغالي\n"    
            if (Manufacturer_Identifier=="uni") :
               Manufacturer_text ="تصنيع ايرلندي\n"    
            if (Manufacturer_Identifier=="vs6") :
               Manufacturer_text ="تصنيع اسباني\n"    
            if (Manufacturer_Identifier=="wf0" or Manufacturer_Identifier=="wf1") :
               Manufacturer_text ="تصنيع الماني\n"    
            if (Manufacturer_Identifier=="xlc") :
               Manufacturer_text ="تصنيع هولندي\n"   
            if (Manufacturer_Identifier=="9bf") :
               Manufacturer_text ="تصنيع برازيلي\n" 
            if (Manufacturer_Identifier=="lvs") :
               Manufacturer_text ="تصنيع صيني\n"                
            if ( Manufacturer_Identifier != "3fa" and Manufacturer_Identifier !="1fa"  and Manufacturer_Identifier  !="sfa"  and Manufacturer_Identifier !="tw2"  and Manufacturer_Identifier !="uni"  and Manufacturer_Identifier  !="vs6"  and Manufacturer_Identifier  !="wf0"  and Manufacturer_Identifier !="wf1"  and Manufacturer_Identifier !="lvs"  and Manufacturer_Identifier !="xlc"  and Manufacturer_Identifier !="9bf") :
               Manufacturer_text="---\n" 
               error_in_vin=1
               vin_error="\nتأكد من رقم الهيكل\n(اول ثلاث أرقام)"

            if (Trim_info=="p0g") :
               Trim_text ="فئة الستاندرد - دفع أمامي\n"
            if (Trim_info=="p0h") :
               Trim_text ="فئة نص فل - دفع أمامي\n" 
            if (Trim_info=="p0k") :
               Trim_text ="فئة التيتانيوم - دفع أمامي\n" 
            if (Trim_info=="p0d") :
               Trim_text ="فئة التيتانيوم - دفع كلي\n"             
            if (Trim_info=="p0u") :
               Trim_text ="فئة الستاندرد - هايبرد - دفع أمامي\n" 
            if (Trim_info=="p0l"  or Trim_info=="p0p") :
               Trim_text ="فئة نص فل - هايبرد - دفع أمامي\n"
            if (Trim_info=="p0t") :
               Trim_text ="فئة نص فل - دفع كلي\n"
            if (Trim_info=="p0r"  or Trim_info=="p0s") :
               Trim_text ="فئة التيتانيوم - هايبرد - دفع أمامي\n" 
            if (Trim_info=="p0v") :  #for 2017+ models
               Trim_text ="فئة رياضية (سبورت) \n"
            if (Trim_info=="p0c") :  #for 2017+ models
               Trim_text ="فئة SEL  - دفع أمامي\n"
            if (Trim_info=="p0m") :   #for 2017+ models
               Trim_text ="فئة SEL  - هايبرد\n"
            if (Trim_info=="p0w") :   #for 2017+ models
               Trim_text ="فئة رياضية ترفيهية \n"
            if (Trim_info=="p0e") :   #for 2017+ models
               Trim_text ="فئة SEL  - دفع كلي\n"
            if (Trim_info=="p0f") :   #for 2017+ models
               Trim_text ="فئة بلاتينيوم - دفع أمامي\n"
            if (Trim_info=="p0j") :   #for 2017+ models
               Trim_text ="فئة بلاتينيوم - دفع كلي\n"
            if (Trim_info=="p0y") :   #for 2017+ models
               Trim_text ="فئة بلاتينيوم - هايبرد \n"
            if (Trim_info=="p0n") :   #for 2017+ models
               Trim_text ="فئة بلاتينيوم - هايبرد \n"

            if (Trim_info=="cbd") :   #for europe Mondeo
               Trim_text ="فئة (Series 10) - دفع أمامي \n"

            if ( Trim_info !="p0g"  and Trim_info !="p0h"  and Trim_info !="p0k"  and Trim_info  !="p0d"  and Trim_info  !="p0u"  and Trim_info  !="p0l"  and Trim_info  !="p0p"  and Trim_info  !="p0t"  and Trim_info  !="p0r"  and Trim_info  !="p0s"  and Trim_info  !="p0v"  and Trim_info !="p0c"  and Trim_info !="p0m"  and Trim_info  !="p0w"  and Trim_info  !="p0e"  and Trim_info  !="p0f"  and Trim_info  !="p0j"  and Trim_info !="p0y"    and Trim_info !="p0n"    and Trim_info !="cbd") :
               Trim_text="---\n" 
               vin_error="\nتأكد من رقم الهيكل\n(الرقم الخامس والسادس والسابع من اليسار)"
               error_in_vin=1
               VIN_intro="\U0001F50D\n"

            if (Engine_type=="7") :
               Engine_type_text ="محرك سعة 2.5 لتر\nتنفس طبيعي 4 سلندر\n" 
            if (Engine_type=="c" and Assembly_plant=="v"): # this is plant in germany confirmed
               Engine_type_text ="محرك سعة 2.5 لتر\nتنفس طبيعي 4 سلندر\n"
            if (Engine_type=="9") :
               Engine_type_text ="محرك سعة 2.0 لتر\nايكوبووست\n"
            if (Engine_type=="d") :
               Engine_type_text ="محرك سعة 1.5 لتر\nايكوبووست\n"
            if (Engine_type=="r") :
               Engine_type_text ="محرك سعة 1.6 لتر\n"
            if (Engine_type=="t") :
               Engine_type_text ="محرك سعة 2.5 لتر\n"
            if (Engine_type=="u") :
               Engine_type_text ="محرك سعة 2.0 لتر\n"
            if (Engine_type=="k") :
               Engine_type_text ="محرك سعة 3.7 لتر\n"
            if (Engine_type=="p") :
               Engine_type_text ="محرك سعة 2.7 لتر\n 6 سلندر \n"
               

               #if error apear this is is why >>last of the line
            if ( Engine_type!="7"  and Engine_type  !="9"  and Engine_type  !="d"  and Engine_type  !="r"  and Engine_type  !="t"  and Engine_type  !="u"   and Engine_type  !="k"   and Engine_type  !="p"   and (Engine_type!="c" and Assembly_plant!="v")  ) :
               Engine_type_text="---\n" 
               error_in_vin=1
               vin_error="\nتأكد من رقم الهيكل\n(الرقم الثامن من اليسار)"
               VIN_intro="\U0001F50D\n"

            if (Assembly_plant=="r") :
               Assembly_plant_text ="مصنع Hermosillo\n"
            if (Assembly_plant=="5") :
               Assembly_plant_text ="مصنع Flatrock\n"
            if (Assembly_plant=="1") :
               Assembly_plant_text ="مصنع Valencia\n"
            if (Assembly_plant=="4") :
               Assembly_plant_text ="مصنع Saarlouis\n"  
            if (Assembly_plant=="v") :   
               Assembly_plant_text ="مصنع Ford Werke AG\n"
            if ( Assembly_plant!="r" and Assembly_plant  !="5"   and Assembly_plant  !="1"   and Assembly_plant  !="4"  and Assembly_plant  !="v") :
               Assembly_plant_text="---\n" 
               error_in_vin=1
               vin_error="\nتأكد من رقم الهيكل\n(الرقم السابع من اليمين)"

            if (Model_year=="9") :
               Model_year_text ="\n\nموديل 2009\n"
               Engine_type_text=" "
               Trim_text=" "
               Manufacturer_text=" "
               Assembly_plant_text=" "
               vin_error="لموديلات 2009-2012\nإكتب PIN متبوعة برقم الهيكل"

            if (Model_year=="a") :
               Model_year_text ="\n\nموديل 2010\n"
               Engine_type_text=" "
               Trim_text=" "
               Manufacturer_text=" "
               Assembly_plant_text=" "
               vin_error="لموديلات 2009-2012\nإكتب PIN متبوعة برقم الهيكل"

            if (Model_year=="b") :
               Model_year_text ="\n\nموديل 2011\n"
               Engine_type_text=" "
               Trim_text=" "
               Manufacturer_text=" "
               Assembly_plant_text=" "
               vin_error="لموديلات 2009-2012\nإكتب PIN متبوعة برقم الهيكل"

            if (Model_year=="c") :
               Model_year_text ="\n\nموديل 2012\n"
               Engine_type_text=" "
               Trim_text=" "
               Manufacturer_text=" "
               Assembly_plant_text=" "
               vin_error="لموديلات 2009-2012\nإكتب PIN متبوعة برقم الهيكل"

            if (Model_year=="d") :
               Model_year_text ="\n\nموديل 2013\n"
            if (Model_year=="e") :
               Model_year_text ="\n\nموديل 2014\n"
            if (Model_year=="f") :
               Model_year_text ="\n\nموديل 2015\n"
            if (Model_year=="g") :
               Model_year_text ="\n\nموديل 2016\n"
            if (Model_year=="h") :
               Model_year_text ="\n\nموديل 2017\n"
            if (Model_year=="j") :
               Model_year_text ="\n\nموديل 2018\n"
            if (Model_year=="k") :
               Model_year_text ="\n\nموديل 2019\n"
            if (Model_year=="l") :
               Model_year_text ="\n\nموديل 2020\n"
            if (Model_year !="d"  and Model_year !="e"  and Model_year  !="f"  and Model_year  !="g"  and Model_year !="h"  and Model_year  !="j"  and Model_year !="k"  and Model_year !="l" and Model_year !="a"  and Model_year !="b"  and Model_year !="c" ) :
               Model_year_text="---\n" 
               error_in_vin=1
               vin_error="\nتأكد من رقم الهيكل\n(الرقم الثامن من اليمين)"

            VIN_Decoder_Text = [vin_number + VIN_intro + random_emoji +  Model_year_text + Engine_type_text + Trim_text + Manufacturer_text  +  Assembly_plant_text + vin_error]
            bot.reply_to(message, f" جاري البحث برقم الهيكل...\n {vin_number}")
            time.sleep(7)
            #just to show off you can random the sleep time to make it more realistic
            if error_in_vin==0 :  
               bot.edit_message_text("\U0001FAE1 إنتهى البحث",message.chat.id, ((message.message_id)+1))
               time.sleep(2)  
               bot.edit_message_text(VIN_Decoder_Text,message.chat.id, ((message.message_id)+1))
               stop_the_bot=1 # to stop any further checks on the rest of code
            else :
               bot.edit_message_text(f"عذرا لم أجد أي نتائج\n {vin_error}",message.chat.id, ((message.message_id)+1))
               time.sleep(20)
               bot.delete_message(message.chat.id, ((message.message_id) + 2))
               bot.delete_message(message.chat.id, (message.message_id)  + 1 )
               bot.delete_message(message.chat.id, (message.message_id)      )
               stop_the_bot=1 # to stop any further checks on the rest of code


       # check if the model is 2008-2012 then send corrective message     
       else :
        vin_number=(''.join(message.text.split()).lower())[3:21]

        if (len((''.join(message.text.split()).lower())))==20 and ( (''.join(message.text.split()).lower())[0:3]=="vin" or  (''.join(message.text.split()).lower())[0:3]=="vln"   ) and ((''.join(message.text.split()).lower())[12]=="8"  or  (''.join(message.text.split()).lower())[12]=="9"  or  (''.join(message.text.split()).lower())[12]=="a"  or  (''.join(message.text.split()).lower())[12]=="b"  or  (''.join(message.text.split()).lower())[12]=="c" )  and(stop_the_bot==0)  :
            bot.reply_to(message, f"جاري التحقق...\n {vin_number}")
            time.sleep(2)  
            bot.edit_message_text("لموديلات 2009-2012\nإكتب PIN\nوليس VIN\nأو تأكد من رقم الهيكل",message.chat.id, ((message.message_id)+1))
            time.sleep(20)
            bot.delete_message(message.chat.id, ((message.message_id) + 1) )
            bot.delete_message(message.chat.id, (message.message_id) )

       # when the model is not 2008-2020 then send corrective message 
        else :
         if (len((''.join(message.text.split()).lower())))==20 and (''.join(message.text.split()).lower())[0:3]=="vin" and ((''.join(message.text.split()).lower())[12]!="8"  or  (''.join(message.text.split()).lower())[12]!="9"  or  (''.join(message.text.split()).lower())[12]!="a"  or  (''.join(message.text.split()).lower())[12]!="b"  or  (''.join(message.text.split()).lower())[12]!="c" or  (''.join(message.text.split()).lower())[12]!="d"  or  (''.join(message.text.split()).lower())[12]!="e"  or  (''.join(message.text.split()).lower())[12]!="f" or  (''.join(message.text.split()).lower())[12]!="g"  or  (''.join(message.text.split()).lower())[12]!="h"  or  (''.join(message.text.split()).lower())[12]!="j"  or  (''.join(message.text.split()).lower())[12]!="k"  or  (''.join(message.text.split()).lower())[12]!="l")  and(stop_the_bot==0) :
             bot.reply_to(message, f"جاري التحقق...\n {vin_number}")
             time.sleep(3)                 
             bot.edit_message_text("تأكد من رقم الهيكل",message.chat.id, ((message.message_id)+2))
             time.sleep(20)
             bot.delete_message(message.chat.id, ((message.message_id) + 2) )
             bot.delete_message(message.chat.id, ((message.message_id) + 1) )                
             bot.delete_message(message.chat.id, (message.message_id) )                   
      #VIN DECODER  2009-2012
       if (len((''.join(message.text.split()).lower())))!=20 and ( (''.join(message.text.split()).lower())[0:3]=="pin" or  (''.join(message.text.split()).lower())[0:3]=="pln"   ) and (len((''.join(message.text.split()).lower())))>=11  and (stop_the_bot==0) :
            bot.send_message(message.chat.id, "تأكد من رقم الهيكل. الرقم مكون من 17 خانة")
            time.sleep(20)
            bot.delete_message(message.chat.id, ((message.message_id) + 2) )
            bot.delete_message(message.chat.id, ((message.message_id) + 1) )
            bot.delete_message(message.chat.id, (message.message_id) )

       if (len((''.join(message.text.split()).lower())))==20 and ( (''.join(message.text.split()).lower())[0:3]=="pin" or  (''.join(message.text.split()).lower())[0:3]=="pln"   ) and (stop_the_bot==0)  :
            VIN_intro="\n\U0001F50D"
            random_emoji ="\U0001FAE1"
            vin_number=(''.join(message.text.split()).lower())[3:21]
            Manufacturer_Identifier = vin_number[0:3]
            Trim_info = vin_number[4:7]
            Engine_type = vin_number[7]
            Model_year  = vin_number[9]
            Assembly_plant = vin_number[10]
            sequence_number = vin_number[11:17]
            vin_error=""
            print(vin_number)
            print("Finding VIN INFO...")
            
            if (Manufacturer_Identifier=="3fa") :
               Manufacturer_text ="تصنيع مكسيكي\n"  
            if (Manufacturer_Identifier=="1fa") :
               Manufacturer_text ="تصنيع أمريكي\n"  
            if (Manufacturer_Identifier=="2fa") :
               Manufacturer_text ="تصنيع كندي\n"            
            if (Manufacturer_Identifier=="1zv") :
               Manufacturer_text ="تصنيع أمريكي\n"               
            if ( Manufacturer_Identifier != "3fa" and Manufacturer_Identifier !="1fa"  and Manufacturer_Identifier  !="2fa"  and Manufacturer_Identifier !="1zf" ) :
               Manufacturer_text="---\n" 
               error_in_vin=1

            if (Trim_info=="p0g") :
               Trim_text ="فئة الستاندرد - دفع أمامي\n"
            if (Trim_info=="p0h") :
               Trim_text ="فئة نص فل - دفع أمامي\n" 
            if (Trim_info=="p0k") :
               Trim_text ="فئة سبورت - دفع أمامي\n" 
            if (Trim_info=="p0d") :
               Trim_text ="فئة سبورت - دفع كلي\n"                
            if (Trim_info=="p0l") :
               Trim_text ="هايبرد\n" 
            if (Trim_info=="p0c") : 
               Trim_text ="فئة SEL  - دفع أمامي\n"
            if (Trim_info=="p0j") :
               Trim_text ="فئة SEL - دفع أمامي\n"           
            if ( Trim_info !="p0g"  and Trim_info !="p0h"  and Trim_info !="p0k"  and Trim_info  !="p0d"   and Trim_info  !="p0l"  and Trim_info  !="p0c"  and Trim_info  !="p0j" ) :
               Trim_text="---\n" 
               VIN_intro="\U0001F50D\n"
               error_in_vin=1

            if (Engine_type=="3" or Engine_type=="a" ) :
               Engine_type_text ="محرك سعة 2.5 لتر\nتنفس طبيعي 4 سلندر\n" 
            if (Engine_type=="1" or Engine_type=="g" ) :
               Engine_type_text ="محرك سعة 3.0 لتر\n"
            if (Engine_type=="c" or Engine_type=="t" or Engine_type=="w") :
               Engine_type_text ="محرك سعة 3.5 لتر\n"
            if (Engine_type=="m" or Engine_type=="r") :
               Engine_type_text ="محرك سعة 3.7 لتر\n"
            if ( Engine_type!="3"  and Engine_type  !="a"  and Engine_type  !="1"  and Engine_type  !="g"  and Engine_type  !="c"  and Engine_type  !="t"  and Engine_type  !="w"  and Engine_type  !="m" ) :
               Engine_type_text="---\n" 
               VIN_intro="\U0001F50D\n"
               error_in_vin=1

            if (Model_year=="9") :
               Model_year_text ="\n\nموديل 2009\n"
            if (Model_year=="a") :
               Model_year_text ="\n\nموديل 2010\n"
            if (Model_year=="b") :
               Model_year_text ="\n\nموديل 2011\n"
            if (Model_year=="c") :
               Model_year_text ="\n\nموديل 2012\n"
            if (Model_year !="9"  and Model_year !="a"  and Model_year  !="b"  and Model_year  !="c" ) :
               Model_year_text="---\n" 
               error_in_vin=1

            Random_wait_reply = random.choice(wait_replies_B) # هذي ردود العشوائية الي يقول فيها حسنا انتظر او داري البحث تم كتابتها فوق كل مازادت الردود ضيفها فوق و اوتوماتيك يختار واحد عشوائي 
            bot.send_voice(chat_id=message.chat.id, voice=open(f'{Sound_File_Location}{Random_wait_reply}.ogg','rb'),   caption=None,   disable_notification=True, reply_to_message_id=message.message_id)
            time.sleep(3)
           
            VIN_Decoder_Text = [vin_number + VIN_intro + random_emoji +  Model_year_text + Engine_type_text + Trim_text + Manufacturer_text]
            bot.reply_to(message, f" جاري البحث برقم الهيكل...\n {vin_number}")
            time.sleep(7)
            #just to show off you can random the sleep time to make it more realistic
            if error_in_vin==0 :
               numbers_list1 =[2.5,2.75,3,3.25,3.5];  numbers_list2 =[2.75,3,3.25,3.5,3.75];  numbers_list3 =[2.5,2.75,3,3.25,2.5];  numbers_list4 =[0.5,0.75,1,1.25];  numbers_list5 =[0.5,0.75,1,1.25]
               random_number1= random.choice(numbers_list1);  random_number2= random.choice(numbers_list2);  random_number3= random.choice(numbers_list3);  random_number4= random.choice(numbers_list4);  random_number5= random.choice(numbers_list5)   
               time.sleep(2)  
               bot.edit_message_text(VIN_Decoder_Text,message.chat.id, ((message.message_id)+2))
               stop_the_bot=1 # to stop any further checks on the rest of code
            else :
               if (Model_year=="d" or   Model_year=="e" or   Model_year=="f" or   Model_year=="g" or   Model_year=="h" or   Model_year=="j" or   Model_year=="k" or   Model_year=="l"):
                   bot.edit_message_text(".. إكتب VIN في البداية  ان كان موديل السياره 2013-2020",message.chat.id, ((message.message_id)+2))
                   time.sleep(20)
                   bot.delete_message(message.chat.id, ((message.message_id) + 2) )
                   bot.delete_message(message.chat.id, ((message.message_id) + 1) )
                   bot.delete_message(message.chat.id, (message.message_id) )
                   stop_the_bot=1 # to stop any further checks on the rest of code
               else :
                   bot.edit_message_text("رقم الهيكل غير صحيح أو البيانات غير كافية لدي..عذراً\n\nأبحث للفيوجن فقط",message.chat.id, ((message.message_id)+2))
                   time.sleep(20)
                   bot.delete_message(message.chat.id, ((message.message_id) + 2) )
                   bot.delete_message(message.chat.id, ((message.message_id) + 1) )
                   bot.delete_message(message.chat.id, (message.message_id) )
                   stop_the_bot=1 # to stop any further checks on the rest of code
       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


       # MAINTENANCE الصيانات الدورية    
       # فحص اذا الرسالة تبدأ بكلمة "بوت"          
       for element in trigger_BOT:
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
               
                if any(trigger in words for trigger in trigger_Schedual if trigger):
                    # قراءة المصفوفات كلها والتأكد هل تحتوي الرسالة على أي كلمة مرتبطة بالمصفوفات. وتحديد الكلمة في أي مصفوفة بالضبط لتحديد الطلب الخاص
                    for i, trigger_list in enumerate([trigger_MAINTENANCE], start=1):
                        if any(trigger in words for trigger in trigger_list if trigger):
                           try:
                                 category = MAINTENANCE
                                 config = MAINTENANCE_CONFIG[category]
                                 header = config['header']
                                 
                                 # إنشاء قائمة الأزرار
                                 buttons = []
                                 for part in config['items']:
                                    sanitized_part = part.replace(" ", "_").replace("-", "").replace("(", "").replace(")", "")
                                    btn = types.InlineKeyboardButton(
                                       text=f"{config['items'][part]['emoji']} {part}",
                                       callback_data=f"maint_{sanitized_part[:30]}"  # قص السلسلة لـ 30 حرف
                                    )
                                    buttons.append(btn)
                                 # إنشاء لوحة مفاتيح مع تحديد عرض الصف 3 أزرار
                                 keyboard = types.InlineKeyboardMarkup(row_width=3)
                                 keyboard.add(*buttons)
                                 # إرسال الصورة مع الأزرار
                                
                                 with open('C:\\Users\\Engmu\\OneDrive\\Desktop\\ALL PARTS\\Maintenance.png', 'rb') as photo:                                     
                                       bot.send_photo(
                                             chat_id=message.chat.id,
                                             photo=photo,  # الكائن الذي تم فتحه
                                             reply_to_message_id=message.message_id,
                                             caption=header,
                                             parse_mode='HTML',
                                             reply_markup=keyboard  # تم إضافة القوس الناقص هنا
                                       )
                                 stop_the_bot = 1
                           except Exception as e:
                                 print(f"Error in maintenance handler: {e}")
                                 bot.reply_to(message, "⚠️ حدث خطأ في تحميل بيانات الصيانة، يرجى المحاولة لاحقًا")
                           break



                # Engine triggers
                if any(trigger in words for trigger in trigger_E):
                    Random_answer_reply = random.choice(Answer_Fits_All)
                    last_time=now
                    # Check sub-triggers
                    if any(trigger in words for trigger in trigger_E1):
                        Search_text=f"({E1})"; Send_Voice_1="No"; Voice_file_1="Intro_Engine_oil_choose2"; Voice_caption_1=f"({E1})"; Send_Voice_2="Yes"; Voice_file_2="Intro_Engine_oil_choose1"; Voice_caption_2="[إضغط هنا](https://t.me/fusion1/114525)"; Send_Photo="No"; Photo_name=""; Photo_caption=""
                    elif any(trigger in words for trigger in trigger_E2):
                        Search_text=f"({E6})"; Send_Voice_1="Yes"; Voice_file_1=Random_answer_reply; Voice_caption_1=f"({E6})\n\n{Viscosity}"; Send_Voice_2="No"; Voice_file_2="";   Voice_caption_2=""; Send_Photo="No"; Photo_name=""; Photo_caption=""
                    elif any(trigger in words for trigger in trigger_E3):
                        Search_text=f"({E5})"; Send_Voice_1="Yes"; Voice_file_1=random.choice(Answer_AS_Lnik); Voice_caption_1=f"({E5})\n\n[إضغط هنا](https://t.me/fusion1/67385)";  Send_Voice_2="No"; Voice_file_2=""; Voice_caption_2=""; Send_Photo="No"; Photo_name=""; Photo_caption=""

                # Transmission triggers
                elif any(trigger in words for trigger in trigger_F):
                    Random_answer_reply = random.choice(Answer_Fits_All)
                    last_time=now
                    if any(trigger in words for trigger in trigger_F1):
                        Search_text=f"({F1})"; Send_Voice_1="No"; Voice_file_1=Random_answer_reply; Voice_caption_1=""; Send_Voice_2="No"; Voice_file_2=""; Voice_caption_2=""; Send_Photo="Yes"; Photo_name="Mercon LV.jpg"; Photo_caption="[Motorcraft (MERCON LV)](https://t.me/fusion1/83090)"
                    elif any(trigger in words for trigger in trigger_F2):
                        Search_text=f"({F6})"; Send_Voice_1="Yes"; Voice_file_1=Random_answer_reply; Voice_caption_1=f"({F6})\n\n\U000026D4 الفلتر داخلي لكل الموديلات\nما يتغير الا مع التوظيب\n"; Send_Voice_2="No"; Voice_file_2=""; Voice_caption_2=""; Send_Photo="Yes"; Photo_name="ransmission Filter  , Transmission Pump Assy.png"; Photo_caption=""

                # Send responses
                if 'Send_Voice_1' in locals():
                    if Send_Photo == "Yes":
                        bot.send_photo(message.chat.id, photo=open(f"{Pictures_File_Location}{Photo_name}", 'rb'), caption=f"{Photo_caption}\n\n{Put_At_End_Of_Message}",parse_mode="Markdown",  disable_notification=True, protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)
                        stop_the_bot = 1
                    if Send_Voice_1 == "Yes":
                        bot.send_voice(chat_id=message.chat.id, voice=open(f'{Sound_File_Location}{Voice_file_1}.ogg','rb'), caption=f"{Voice_caption_1}\n\n{Put_At_End_Of_Message}",parse_mode="Markdown", disable_notification=True, protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)
                        stop_the_bot = 1
                    if Send_Voice_2 == "Yes":
                        bot.send_voice(chat_id=message.chat.id, voice=open(f'{Sound_File_Location}{Voice_file_2}.ogg','rb'), caption=f"{Voice_caption_2}\n\n{Put_At_End_Of_Message}",parse_mode="Markdown", disable_notification=True, protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)
                        stop_the_bot = 1

       if  ("بوت دليل الضمان" in words     or "بوت دليل الشرق" in words) and (stop_the_bot==0): 
          bot.send_photo(message.chat.id, photo=open(f'{Pictures_File_Location}qwer2.jpg', 'rb') ,caption=None, disable_notification=True, reply_to_message_id=message.message_id)
          bot.send_photo(message.chat.id, photo=open(f'{Pictures_File_Location}qwer1.jpg', 'rb') ,caption=None, disable_notification=True, reply_to_message_id=message.message_id) ;  last_time = now    
          stop_the_bot=1 # to stop any further checks on the rest of code
#________________________________________________________________________________________________________________________________________


      # HHHH  Mods - Setting  RELATED   
       # فحص اذا الرسالة تبدأ بكلمة "بوت"
       for element in trigger_BOT:
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
                # فحص اذا تحتوي الرسالة على كلمة من المصفوفة المححده للطلب العام
                if any(trigger in words for trigger in trigger_H if trigger):

                    # قراءة المصفوفات كلها والتأكد هل تحتوي الرسالة على أي كلمة مرتبطة بالمصفوفات. وتحديد الكلمة في أي مصفوفة بالضبط لتحديد الطلب الخاص
                    for i, trigger_list in enumerate([trigger_H1, trigger_H2, trigger_H3, trigger_H4, trigger_H5,
                                                    trigger_H6, trigger_H7, trigger_H8, trigger_H9, trigger_H10,
                                                    trigger_H11, trigger_H12, trigger_H13, trigger_H14, trigger_H15], start=1):
                        if any(trigger in words for trigger in trigger_list if trigger):
                            index = max(i - 1, 0)
                            refference1 = globals().get(f'Sections_H0', [])
                            refference2 = globals().get(f'Answer_By_Link1_H0', [])
                            refference3 = globals().get(f'Answer_By_Link2_H0', [])

                            response_text = f"⚙️ *{H}\n({Sections_H0[index]}):*\n\n"
                            response_text += f"📎 [*إضغط هنا*]({refference2[index]})\n\n"
                            if refference3[index]:
                                response_text += f"📎 [*الرابط الثاني*]({refference3[index]})\n\n"
                            response_text += "\n\n"  # Add space between each setting info
                            last_time = now
                            bot.send_voice(message.chat.id,
                                        voice=open(f'{Sound_File_Location}{random.choice(Answer_replies_H)}.ogg', 'rb'),
                                        caption=response_text,protect_content=Protect_Content_Switch_H,
                                        parse_mode='Markdown',
                                        disable_notification=True)  # Disable notifications
                            stop_the_bot=1 # to stop any further checks on the rest of code
                            break
                    else: # في حال ما حدد المطلوب
                        keyboard = types.InlineKeyboardMarkup()
                        buttons = [types.InlineKeyboardButton(text=Sections_H0[i], callback_data=f"H[{i}]") for i in range(len(Sections_H0))]
                        keyboard.add(buttons[0], buttons[4])
                        keyboard.add(buttons[7], buttons[8])
                        keyboard.add(buttons[9], buttons[5])
                        keyboard.add(buttons[3], buttons[6])
                        keyboard.add(buttons[1], buttons[2])
                        last_time = now
                        bot.send_voice(message.chat.id, voice=open(f'{Sound_File_Location}{random.choice(First_Bot_replies)}.ogg', 'rb'), caption=f"({H}) {Pick_one}", disable_notification=True,protect_content=Protect_Content_Switch_H,    reply_markup=keyboard,  reply_to_message_id=message.message_id)
                        stop_the_bot=1 # to stop any further checks on the rest of code
                        break

#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


       #CCCC فيوزات  
       # فحص اذا الرسالة تبدأ بكلمة "بوت"
       for element in trigger_BOT:  
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
              # فحص اذا تحتوي الرسالة على كلمة من المصفوفة المححده للطلب العام الي هو الفيوز
                if any(trigger in words for trigger in trigger_C if trigger):
                    if stop_the_bot == 0:
                        trigger_numbers = {"10", "11", "12", "14", "15", "16", "17", "18", "19", 
                                        "2010", "2011", "2012", "2014", "2015", "2016", "2017", 
                                        "2018", "2019", "١٠", "١١", "١٢", "١٤", "١٥", "١٦", 
                                        "١٧", "١٨", "١٩", "٢٠١٠", "٢٠١١", "٢٠١٢", "٢٠١٤", 
                                        "٢٠١٥", "٢٠١٦", "٢٠١٧", "٢٠١٨", "٢٠١٩"}
                        # فحص اذا تحتوي الرسالة على كلمة من المصفوفة المححده للطلب الخاص الي هو الموديلات
                        if any(num in words for num in trigger_numbers):
                            trigger_groups = [trigger_C1, trigger_C2, trigger_C3, trigger_C4, 
                                            trigger_C5, trigger_C6, trigger_C7, trigger_C8, trigger_C9]
                            cref_groups = [C1, C2, C3, C4, C5, C6, C7, C8, C9]
                            for idx, (trigger_group, cref) in enumerate(zip(trigger_groups, cref_groups), start=2):
                                if any(word in words and word != "" for word in trigger_group):
                                    reff = idx
                                    Xref = reff - 1
                                    Creff = cref
                                    break
        
                            ref_sec = "clickC"
                            Parts_ref1  =  f"{ref_sec}{Xref}"   #<<< for the specified model   
                            Parts_ref2  =  f"{ref_sec}"         #<<< for all models
                            name=message.from_user.first_name;  t = time.localtime(); current_time = time.strftime("%H:%M:%S", t); print(f'..................\n..................\n{current_time}\n🟢 Activated By:({message.from_user.first_name})\n   ID:({message.from_user.id}) Level:{Current_Level}')   
                            Random_wait_reply  = random.choice(pick_from_list) # هذي ردود العشوائية الي يقول فيها حسنا انتظر او داري البحث تم كتابتها فوق كل مازادت الردود ضيفها فوق و اوتوماتيك يختار واحد عشوائي              
                            keyboard = types.InlineKeyboardMarkup()
                            bottonK0 =types.InlineKeyboardButton(text= f"موديل {Creff}"   ,callback_data=f'{Parts_ref1}')  #موديل 2013-2016
                            bottonK00 =types.InlineKeyboardButton(text= "لعرض جميع الموديلات" ,callback_data=f'{Parts_ref2}')  #موديل 2009-2012
                            keyboard.add(bottonK0,bottonK00)
                            last_time = now
                            stop_the_bot=1 # to stop any further checks on the rest of code
                            bot.send_voice(message.chat.id, voice=open(f'{Sound_File_Location}{Random_wait_reply}.ogg','rb'), caption=f"({C})\n{Creff}\n\nإضغط للتأكيد..", disable_notification=True,protect_content=Protect_Content_Switch_Fuses, reply_markup=keyboard, reply_to_message_id=message.message_id)
                    
                        # اذا ماتحدد الموديل اظهر خيارات الموديلات
                        else:
                            last_time = now;  name=message.from_user.first_name;  t = time.localtime(); current_time = time.strftime("%H:%M:%S", t); print(f'..................\n..................\n{current_time}\n🟢 Activated By:({message.from_user.first_name})\n   ID:({message.from_user.id}) Level:{Current_Level}')   
                            words_list =[" هلا ", " مرحبا ", " حياك ", " ولا يهمك  "," هلا "," أهلين "," ياهلا "," أهلا ","أبشر"]
                            random_word = random.choice(words_list);  random_emoji = random.choice(emoji)
                            Random_wait_reply=random.choice(pick_from_list)
                            bottonC1 =types.InlineKeyboardButton(text= C1 ,callback_data='clickC1')
                            bottonC2 =types.InlineKeyboardButton(text= C2 ,callback_data='clickC2')
                            bottonC3 =types.InlineKeyboardButton(text= C3 ,callback_data='clickC3')
                            bottonC4 =types.InlineKeyboardButton(text= C4 ,callback_data='clickC4')
                            bottonC5 =types.InlineKeyboardButton(text= C5 ,callback_data='clickC5')
                            bottonC6 =types.InlineKeyboardButton(text= C6 ,callback_data='clickC6')
                            bottonC7 =types.InlineKeyboardButton(text= C7 ,callback_data='clickC7')
                            bottonC8 =types.InlineKeyboardButton(text= C8 ,callback_data='clickC8')
                            bottonC9 =types.InlineKeyboardButton(text= C9 ,callback_data='clickC9')
                            keyboard.add(bottonC1,bottonC2,bottonC3).add(bottonC4,bottonC5,bottonC6).add(bottonC7,bottonC8,bottonC9)
                            stop_the_bot=1 # to stop any further checks on the rest of code
                            bot.send_voice(chat_id=message.chat.id, voice=open(f'{Sound_File_Location}{Random_wait_reply}.ogg','rb'), caption=f"({C}){Pick_model}", disable_notification=True,protect_content=Protect_Content_Switch_Fuses,reply_markup=keyboard, reply_to_message_id=message.message_id)
                            break  

       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
       # ذا اول كلمه بوت
       # Direct Amounts   JJJJ
       # ALL Common problems
       for element in trigger_BOT:
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
                # فحص اذا تحتوي الرسالة على كلمة من المصفوفة المححده للطلب العام والي هو كمية
                if   any(trigger in words for trigger in trigger_J if trigger):
                     last_time = now
                     Random_wait_reply  = random.choice(pick_from_list) # هذي ردود العشوائية الي يقول فيها حسنا انتظر او داري البحث تم كتابتها فوق كل مازادت الردود ضيفها فوق و اوتوماتيك يختار واحد عشوائي              
                     ref_sec = "clickJ"
                     # Initialize Xref as None
                     Xref = None
                   
                     # Check all trigger groups (J1-J6) concisely
                     for group_num, trigger in enumerate([trigger_J1, trigger_J2, trigger_J3, 
                                                         trigger_J4, trigger_J5, trigger_J6], 1):
                        if any(element and element in words for element in trigger):
                           # Special handling for J1 (set random reply)
                           if group_num == 1:
                                 Random_wait_reply = random.choice(Model_Eng)
                           # Always update ref values for matched group
                           reff, Xref = group_num, group_num - 1
                        
                     # Show main options if Xref is not assigned
                     if Xref is not None:
                        Parts_ref1  =   f"{ref_sec}[{Xref}]"  #<<< for 2013+    
                        Parts_ref2  =  f"{ref_sec}[0{Xref}]"  #<<< for 2012- 
                        last_time = now; name=message.from_user.first_name;  t = time.localtime(); current_time = time.strftime("%H:%M:%S", t); print(f'..................\n..................\n{current_time}\n🟢 Activated By:({message.from_user.first_name})\n   ID:({message.from_user.id}) Level:{Current_Level}')   
                        keyboard = types.InlineKeyboardMarkup()
                        bottonK0 =types.InlineKeyboardButton(text= K0   ,callback_data=f'{Parts_ref1}')  #موديل 2013-2016
                        bottonK00 =types.InlineKeyboardButton(text= K00 ,callback_data=f'{Parts_ref2}')  #موديل 2009-2012
                        keyboard.add(bottonK0,bottonK00)
                        stop_the_bot=1 # to stop any further checks on the rest of code
                        bot.send_voice(message.chat.id, voice=open(f'{Sound_File_Location}{Random_wait_reply}.ogg','rb'), caption="الرجاء تأكيد الموديل... :", disable_notification=True,reply_markup=keyboard, reply_to_message_id=message.message_id)
                     else:
                        if Xref is None:
                           #  خيارات كميات الزيوت اذا ماحدد 
                           if "زيت" in words:
                              # Create inline keyboard
                              keyboard = types.InlineKeyboardMarkup()
                              bottonJ1 = types.InlineKeyboardButton(text=J1, callback_data='clickE2')
                              bottonJ2 = types.InlineKeyboardButton(text=J2, callback_data='clickJ2')
                              bottonJ3 = types.InlineKeyboardButton(text=J3, callback_data='clickJ[2]')
                              keyboard.add(bottonJ1,bottonJ2).add(bottonJ3)  # Or use .row() for separate rows
                              stop_the_bot=1 # to stop any further checks on the rest of code
                              bot.send_voice(message.chat.id, voice=open(f'{Sound_File_Location}{Random_wait_reply}.ogg','rb'), caption=f"(كمية الزيت..)\n{Pick_one}", disable_notification=True,reply_markup=keyboard, reply_to_message_id=message.message_id)
                              break
                           else :
                              # J جميع الكميات
                              keyboard = types.InlineKeyboardMarkup()
                              bottonJ1 =types.InlineKeyboardButton(text= J1 ,callback_data='clickE2')  # كمية زيت المكينة  المدخلات فوق جاهزه مايحتاج اضافه
                              bottonJ2 =types.InlineKeyboardButton(text= J2 ,callback_data='clickJ2')  
                              bottonJ3 =types.InlineKeyboardButton(text= J3 ,callback_data='clickJ[2]')  
                              bottonJ4 =types.InlineKeyboardButton(text= J4 ,callback_data='clickJ[3]')  
                              bottonJ5 =types.InlineKeyboardButton(text= J5 ,callback_data='clickJ[4]')  
                              keyboard.add(bottonJ1,bottonJ2).add(bottonJ3,bottonJ4).add(bottonJ5)
                              stop_the_bot=1 # to stop any further checks on the rest of code
                              bot.send_voice(message.chat.id, voice=open(f'{Sound_File_Location}{Random_wait_reply}.ogg','rb'), caption=f"({J}){Pick_one}", disable_notification=True,reply_markup=keyboard, reply_to_message_id=message.message_id)
                              break

       # ذا اول كلمه بوت
       # DDDD Sizes
       for element in trigger_BOT:
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
                # فحص اذا تحتوي الرسالة على كلمة من المصفوفة المححده للطلب العام والي هو المقاسات
                if   any(trigger in words for trigger in trigger_D if trigger): 
                     last_time = now        
                     Random_wait_reply  = random.choice(pick_from_list) # هذي ردود العشوائية الي يقول فيها حسنا انتظر او داري البحث تم كتابتها فوق كل مازادت الردود ضيفها فوق و اوتوماتيك يختار واحد عشوائي              
                     ref_sec = "clickD"
                     # Initialize Xref as None
                     Xref = None
                  
                     for element in                trigger_D1   : #<< Devide List  into elements and scan everyone until condition below it is met           
                        if (element in words)  and  (element !="")   :                                                                                      
                              reff=1  ; Xref= reff -1 ; break     
                     for element in                trigger_D2   :            
                        if (element in words)  and  (element !="")   :    
                              Random_wait_reply  = random.choice(Model_Wheel) 
                              reff=2  ; Xref= reff -1 ; break     
                     for element in                trigger_D3   :            
                        if (element in words)  and  (element !="")   :    
                              reff=3  ; Xref= reff -1 ; break     
                     for element in                trigger_D4   :       
                        if (element in words)  and  (element !="")   :    
                              reff=4  ; Xref= reff -1 ; break     
                     for element in                trigger_D5   :       
                        if (element in words)  and  (element !="")   :    
                              reff=5  ; Xref= reff -1;  break      
                     for element in                trigger_D6   :       
                        if (element in words)  and  (element !="")   :    
                              reff=6  ; Xref= reff -1 ; break     
                     
                     
                     if Xref is not None:
                        Parts_ref1  =   f"{ref_sec}[{Xref}]"  #<<< for 2013+    
                        Parts_ref2  =  f"{ref_sec}[0{Xref}]"  #<<< for 2012-
                        last_time = now;   name=message.from_user.first_name;  t = time.localtime(); current_time = time.strftime("%H:%M:%S", t); print(f'..................\n..................\n{current_time}\n🟢 Activated By:({message.from_user.first_name})\n   ID:({message.from_user.id}) Level:{Current_Level}')   
                        keyboard = types.InlineKeyboardMarkup()
                        bottonK0 =types.InlineKeyboardButton(text= K0   ,callback_data=f'{Parts_ref1}')  #موديل 2013-2016
                        bottonK00 =types.InlineKeyboardButton(text= K00 ,callback_data=f'{Parts_ref2}')  #موديل 2009-2012
                        keyboard.add(bottonK0,bottonK00)
                        stop_the_bot=1 # to stop any further checks on the rest of code
                        bot.send_voice(message.chat.id, voice=open(f'{Sound_File_Location}{Random_wait_reply}.ogg','rb'), caption="الرجاء تأكيد الموديل... :", disable_notification=True,reply_markup=keyboard, reply_to_message_id=message.message_id)
                     else:
                        # Show main options if Xref is not assigned
                        if Xref is None:
                           keyboard = types.InlineKeyboardMarkup()
                           bottonD1 =types.InlineKeyboardButton(text= D1 ,callback_data='clickD[0]') #(مقاس البطاريه)
                           bottonD2 =types.InlineKeyboardButton(text= D2 ,callback_data='clickD2') #(مقاس الكفرات)
                           bottonD3=types.InlineKeyboardButton(text= D3 ,callback_data='clickD[2]') #(مقاس المبات)
                           bottonD4 =types.InlineKeyboardButton(text= D4 ,callback_data='clickD[3]') #(مقاس المساحات)
                           bottonD5 =types.InlineKeyboardButton(text= D5 ,callback_data='clickD[4]') #"مقاس صواميل الكفر"
                           botton_Return=types.InlineKeyboardButton(text= "رجوع" ,callback_data='Amounts_and_Sizes_return')
                           keyboard.add(bottonD1,bottonD2).add(bottonD3,bottonD4).add(bottonD5)#.add(botton_Return)
                           stop_the_bot=1 # to stop any further checks on the rest of code
                           bot.send_voice(message.chat.id, voice=open(f'{Sound_File_Location}{Random_wait_reply}.ogg','rb'), caption=f"({D}){Pick_one}", disable_notification=True,reply_markup=keyboard, reply_to_message_id=message.message_id)
                           break

       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

       # GGGG ############# Common Problems ##########  
       # ALL Common problems
       for element in trigger_BOT:
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
                # فحص اذا تحتوي الرسالة على كلمة من المصفوفة المححده للطلب العام
                if any(trigger in words for trigger in trigger_G if trigger):

                    # قراءة المصفوفات كلها والتأكد هل تحتوي الرسالة على أي كلمة مرتبطة بالمصفوفات. وتحديد الكلمة في أي مصفوفة بالضبط لتحديد الطلب الخاص
                    for i, trigger_list in enumerate([trigger_G1, trigger_G2, trigger_G3, trigger_G4, trigger_G5,
                                                    trigger_G6, trigger_G7, trigger_G8, trigger_G9, trigger_G10,
                                                    trigger_G11, trigger_G12, trigger_G13, trigger_G14, trigger_G15,
                                                    trigger_G16, trigger_G17, trigger_G18, trigger_G19, trigger_G20], start=1):
                        if any(trigger in words for trigger in trigger_list if trigger):
                            index = max(i - 1, 0)
                            refference1 = globals().get(f'Sections_G0', [])
                            refference2 = globals().get(f'Answer_By_Link1_G0', [])
                            refference3 = globals().get(f'Answer_By_Link2_G0', [])

                            response_text = f"🔧 *{G}\n  ({Sections_G0[index]}) *\n\n"
                            response_text += f"📎 [*إضغط هنا*]({refference2[index]})\n"
                            if refference3[index]:
                                response_text += f"📎 [*الرابط الثاني*]({refference3[index]})\n"
                            response_text += "\n\n"  # Add space between each other info
                            last_time = now
                            stop_the_bot=1 # to stop any further checks on the rest of code
                            bot.send_voice(message.chat.id,
                                        voice=open(f'{Sound_File_Location}{random.choice(Answer_replies_G)}.ogg', 'rb'),
                                        caption=response_text,
                                        parse_mode='Markdown',
                                        disable_notification=True,protect_content=Protect_Content_Switch_G)  # Disable notifications
                            break

                    else:
                        keyboard = types.InlineKeyboardMarkup()
                        buttons = [types.InlineKeyboardButton(text=Sections_G0[i], callback_data=f"G[{i}]") for i in range(len(Sections_G0))]
                        keyboard.add(*buttons[:3])
                        keyboard.add(*buttons[3:6])
                        keyboard.add(*buttons[6:9])
                        keyboard.add(*buttons[9:])
                        last_time = now
                        stop_the_bot=1 # to stop any further checks on the rest of code
                        bot.send_voice(message.chat.id,
                                    voice=open(f'{Sound_File_Location}{random.choice(pick_from_list)}.ogg', 'rb'),
                                    caption=f"({G}) {Pick_one}",
                                    disable_notification=True,protect_content=Protect_Content_Switch_G,
                                    reply_markup=keyboard,
                                    reply_to_message_id=message.message_id)
                        break
                
       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


       # R RRRR Recalls    
       for element in trigger_BOT:
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
                # فحص اذا تحتوي الرسالة على كلمة من المصفوفة المححده للطلب العام
                if any(trigger in words for trigger in trigger_R if trigger):
                   if  (element in words)  and  (element !="")  and (stop_the_bot==0)  : 
                        name=message.from_user.first_name;  t = time.localtime(); current_time = time.strftime("%H:%M:%S", t); print(f'..................\n..................\n{current_time}\n🟢 Activated By:({message.from_user.first_name})\n   ID:({message.from_user.id}) Level:{Current_Level}')   
                        words_list =[" هلا ", " مرحبا ", " حياك ", " ولا يهمك  "," هلا "," أهلين "," ياهلا "," أهلا ","أبشر"]
                        random_word = random.choice(words_list);  random_emoji = random.choice(emoji)
                        last_time = now
                        bot.send_voice(chat_id=message.chat.id, voice=open(f'{Sound_File_Location}Recalls_1.ogg','rb'), caption=f"تم البحث\U00002714\n\n[إضغط هنا لعرض إستدعائات فيوجن 2013-2016](https://t.me/fusion1/117878)\n......................\n\nفورد الناغي (للمنطقة الغربية والجنوبية)\n8001240218\n\nفورد توكيلات الجزيرة(المنطقة الشرقية والشمالية والرياض)\n920002999", disable_notification=True,protect_content=Protect_Content_Switch_R,reply_markup=keyboard,parse_mode="Markdown", reply_to_message_id=message.message_id)
                        file_types = {
                           "18062": "jpg",
                           "21087": "png", "19204": "png", "17225": "png",
                           "20103": "png", "19059": "png", "22196": "png", "22126": "png" }
                        
                        # List of all picture codes to send
                        all_codes = ["21087", "19204", "18062", "17225", 
                                    "20103", "19059", "22196", "22126"]
                        last_time = now
                        max_retries = 2
                        for attempt in range(max_retries):
                           try:
                              media_group = []
                              for code in all_codes:
                                    media_group.append(types.InputMediaPhoto(
                                       open(f'{Pictures_File_Location}{code}.{file_types[code]}', 'rb')
                                    ))
                              bot.send_media_group(
                                    chat_id=message.chat.id,
                                    media=media_group,
                                    disable_notification=True,
                                    protect_content=Protect_Content_Switch_R,
                                    reply_to_message_id=message.message_id
                              )
                              stop_the_bot=1 # to stop any further checks on the rest of code
                              break  # Success - exit retry loop
                           except Exception as e:
                              if attempt == max_retries - 1:
                                    print(f"Failed after {max_retries} attempts: {str(e)}")
                                    stop_the_bot=1 # to stop any further checks on the rest of code
                                    break
                              else:
                                    print(f"Attempt {attempt+1} failed, retrying...")
                                    time.sleep(5 * (attempt + 1))
                                    stop_the_bot=1 # to stop any further checks on the rest of code
                                    break
                              
       # ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

       # WWWW W ############ Manuals and references ##########  

       # فحص اذا الرسالة تبدأ بكلمة "بوت"
       for element in trigger_BOT:  
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
              # اذا طلب كتيب  او دليل المالك
                if any(trigger in words for trigger in trigger_Wm if trigger):  
                  Model_found = False
                  # تشييك هل حدد الموديل او لا
                  for i, trigger_list in enumerate([trigger_W1, trigger_W2, trigger_W3, trigger_W4, trigger_W5,
                                                   trigger_W6, trigger_W7, trigger_W8, trigger_W9 ], start=1):
                     if any(trigger in words for trigger in trigger_list if trigger):
                        Wanted_Model_Year = Model_Year [i - 1] 
                        Model_found = True
                        # Construct the text file path
                        pdf_path = f"C:\\Users\\Engmu\\OneDrive\\Desktop\\ALL PARTS\\W - References\دليل المالك\\{Wanted_Model_Year}.pdf"                       

                        # Generate the response text
                        response_text = f"*{W}:*\n📘 دليل المالك (فيوجن {Wanted_Model_Year})\n\n"

                        #  if the PDF do not exists
                        if not os.path.exists(pdf_path):
                              bot.send_message(
                                    message.chat.id,
                                    text=f" الملف {X}",
                                    parse_mode='Markdown',
                                    disable_notification=True,
                                    protect_content=Protect_Content_Switch_W,
                                    reply_to_message_id=message.message_id )
                              stop_the_bot = 1
                        # Send the PDF file to the user
                        try:
                              with open(pdf_path, 'rb') as pdf_file:
                                 last_time=now
                                 bot.send_document(
                                    message.chat.id,
                                    document=pdf_file,
                                    caption=response_text,
                                    parse_mode='Markdown',
                                    disable_notification=True,
                                    protect_content=Protect_Content_Switch_W,
                                    reply_to_message_id=message.message_id )
                                 stop_the_bot = 1
                        except Exception as e:
                              with open(pdf_path, 'rb') as pdf_file:
                                 last_time=now
                                 bot.send_document(
                                    message.chat.id,
                                    document=pdf_file,
                                    caption="حدث خطأ أثناء إرسال الملف. يرجى المحاولة لاحقاً.",
                                    parse_mode='Markdown',
                                    disable_notification=True,
                                    protect_content=Protect_Content_Switch_W,
                                    reply_to_message_id=message.message_id )
                                 stop_the_bot = 1
                  #  اذا ماحدد الموديل لدليل المالك
                  if not Model_found and stop_the_bot != 1:
                     keyboard = types.InlineKeyboardMarkup()
                     W_ref = "W"
                     buttons = [types.InlineKeyboardButton(text=Wanted_Model_Year, callback_data=f'{W_ref}[{i}]') for i, Wanted_Model_Year in enumerate(Model_Year[:9])]
                     for i in range(0, len(buttons), 3):
                        keyboard.add(*buttons[i:i + 3])
                     last_time = now
                     bot.send_voice(message.chat.id,
                                    voice=open(f'{Sound_File_Location}{random.choice(pick_from_list)}.ogg', 'rb'),
                                    caption=f"*{W}*\n({W1}) {Pick_model}",
                                    disable_notification=True, protect_content=Protect_Content_Switch_W,
                                    reply_markup=keyboard,parse_mode='Markdown',
                                    reply_to_message_id=message.message_id)
                     stop_the_bot = 1
                     break


               # اذا طلب اي شي ثاني غير الكتيبات راح يكون تكوين خيارات داخل خيارات اوتوماتيك من الملفات
                if any(trigger in words for trigger in trigger_W if trigger)    and stop_the_bot != 1 :  
                     random_word = random.choice(words_list);  random_emoji = random.choice(emoji)
                     Random_wait_reply=random.choice(pick_from_list)
                     bottonC1 =types.InlineKeyboardButton(text= "نعم" ,callback_data='clickW')
                     bottonC2 =types.InlineKeyboardButton(text= "لا - الخروج من القائمة" ,callback_data='Exit')                     
                     # Send the voice message with the two button options
                     bot.send_voice(
                        message.chat.id,
                        voice=open(f'{Sound_File_Location}{random.choice(pick_from_list)}.ogg', 'rb'),
                        caption=f" *هل تقصد المراجع ؟*",
                        disable_notification=True,
                        protect_content=Protect_Content_Switch_W,
                        reply_markup=keyboard,
                        parse_mode='Markdown',
                        reply_to_message_id=message.message_id  )
                     last_time=now
                     stop_the_bot = 1
      #_________________________________________________________________________________________________


       # AAAA ############ PARTS STORES OPTIONS ##########  
        # اذا طلب ارقام المحلات بدون مايحدد المدينه
       
       # فحص اذا الرسالة تبدأ بكلمة "بوت"
       for element in trigger_BOT:  
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
              # فحص اذا تحتوي الرسالة على كلمة من المصفوفة المححده للطلب العام 
                if any(trigger in words for trigger in trigger_A if trigger):  
                  city_found = False
                  # قراءة المصفوفات كلها والتأكد هل تحتوي الرسالة على أي كلمة مرتبطة بالمصفوفات. وتحديد الكلمة في أي مصفوفة بالضبط لتحديد الطلب الخاص
                  for i, trigger_list in enumerate([trigger_A1, trigger_A2, trigger_A3, trigger_A4, trigger_A5,
                                                   trigger_A6, trigger_A7, trigger_A8, trigger_A9, trigger_A10,
                                                   trigger_A11, trigger_A12, trigger_A13, trigger_A14, trigger_A15], start=1):
                     if any(trigger in words for trigger in trigger_list if trigger):
                        print (trigger_list)
                        city = City[i - 1]  # Get the city name from the City list
                        print (i)
                        city_found = True
                        print (f"found city ?? {city_found}")
                        print (f"City is :{city}")
                        # Construct the text file path
                        file_path = f"C:\\Users\\Engmu\\OneDrive\\Desktop\\ALL PARTS\\A - Stores Num_Location\\{i}- {city}.txt"                       
                        # Generate the response text
                        response_text = f"\U0001F3E0 *محلات قطع غيار في {city}:*\n{Show_Location}\n\n"
                        groups = read_city_data(file_path)

                        for header, store_location_pairs in groups:
                           response_text += f"\n{header}\n"
                           for store, location in store_location_pairs:
                              # Escape Markdown characters
                              store = store.replace("[", "\\[").replace("]", "\\]").replace("*", "\\*").replace("_", "\\_")
                              response_text += f"📍 [{store}]({location})\n"
                        #print(response_text)

                        # Send the response with a photo (if available)
                        photo_path = f"C:\\Users\\Engmu\\OneDrive\\Desktop\\ALL PARTS\\A - Stores Num_Location\\{i}- Locations.png"
                        if os.path.exists(photo_path):
                           max_length = max_Caption_length  # Telegram's caption length limit

                           if len(response_text) > max_length:
                              # Split the text into 2 parts
                              midpoint = len(response_text) // 2  # Find the midpoint

                              # Search for the nearest header (emoji) to the midpoint
                              emojis = ["🟡", "🔴", "🟢", "🟣", "🟤", "🟠", "🔵"]
                              split_index = -1

                              # Search forward from midpoint for the first emoji line
                              for i in range(midpoint, len(response_text)):
                                    if any(response_text[i:].startswith(emoji) for emoji in emojis):
                                       split_index = i  # Split BEFORE this line
                                       break

                              # If no emoji found after midpoint, search backward
                              if split_index == -1:
                                    for i in range(midpoint, 0, -1):
                                       if any(response_text[i:].startswith(emoji) for emoji in emojis):
                                          split_index = i
                                          break

                              # Default to midpoint if no emoji found
                              if split_index == -1:
                                    split_index = midpoint

                              # Split the text into two parts
                              part1 = response_text[:split_index].strip()
                              part2 = response_text[split_index:].strip()
                              part2 +=f"{read_full_parts}"

                              # Send Part 1 with photo
                              bot.send_photo(
                                    message.chat.id,
                                    photo=open(photo_path, 'rb'),
                                    caption=part1,
                                    parse_mode='Markdown',
                                    disable_notification=True,
                                    protect_content=Protect_Content_Switch_A,
                                    reply_to_message_id=message.message_id
                              )

                              # Send Part 2 as follow-up message
                              bot.send_message(
                                    message.chat.id,
                                    text=part2,
                                    parse_mode='Markdown',
                                    disable_notification=True,
                                    protect_content=Protect_Content_Switch_A,
                                    reply_to_message_id=message.message_id
                              )
                           else:
                              # If the message is within the limit, send it as is
                              bot.send_photo(
                                    message.chat.id,
                                    photo=open(photo_path, 'rb'),
                                    caption=response_text,
                                    parse_mode='Markdown',
                                    disable_notification=True,
                                    protect_content=Protect_Content_Switch_A,
                                    reply_to_message_id=message.message_id
                              )
                        else:
                           print(f"Debug: Photo not found for city = {city}")
                           bot.send_message(
                              message.chat.id,
                              text=response_text,
                              parse_mode='Markdown',
                              disable_notification=True,
                              protect_content=Protect_Content_Switch_A,
                              reply_to_message_id=message.message_id
                           )

                        last_time = now
                        stop_the_bot = 1
                        break

                  if not city_found and stop_the_bot != 1:
                     keyboard = types.InlineKeyboardMarkup()
                     City_ref = "City"
                     buttons = [types.InlineKeyboardButton(text=city, callback_data=f'{City_ref}[{i}]') for i, city in enumerate(City[:15])]
                     keyboard.add(types.InlineKeyboardButton(text="موقع بيع عبر الانترنت", callback_data=f'{City_ref}[X]'))
                     for i in range(0, len(buttons), 3):
                        keyboard.add(*buttons[i:i + 3])
                     last_time = now
                     bot.send_voice(message.chat.id,
                                    voice=open(f'{Sound_File_Location}{random.choice(pick_from_list)}.ogg', 'rb'),
                                    caption=f"({A}) {Pick_City}",
                                    disable_notification=True, protect_content=Protect_Content_Switch_A,
                                    reply_markup=keyboard,
                                    reply_to_message_id=message.message_id)
                     stop_the_bot = 1
                     break


       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


       # OOOO ############  "أفضل الورش حسب المدينة" ##########       
       # ALL Cities

        # فحص اذا الرسالة تبدأ بكلمة "بوت"
       for element in trigger_BOT:
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
                # فحص اذا تحتوي الرسالة على كلمة من المصفوفة المححده للطلب العام
                if any(trigger in words for trigger in trigger_O if trigger):

                    # قراءة المصفوفات كلها والتأكد هل تحتوي الرسالة على أي كلمة مرتبطة بالمصفوفات. وتحديد الكلمة في أي مصفوفة بالضبط لتحديد الطلب الخاص
                    for i, trigger_list in enumerate([trigger_O1, trigger_O2, trigger_O3, trigger_O4, trigger_O5,
                                                    trigger_O6, trigger_O7, trigger_O8, trigger_O9, trigger_O10,
                                                    trigger_O11, trigger_O12, trigger_O13, trigger_O14, trigger_O15], start=1):
                        if any(trigger in words for trigger in trigger_list if trigger):
                            index = max(i - 1, 0)
                            refference1 = globals().get(f'Shop_Store____Group{index}', [])
                            refference2 = globals().get(f'Shop_Number___Group{index}', [])
                            refference3 = globals().get(f'Shop_Location_Group{index}', [])
                            refference4 = globals().get(f'Speciality____Group{index}', [])

                            response_text = f"🔧 *ورش صيانة في {City[index]}:*\n\n"
                            for j in range(len(refference1)):
                                if refference1[j]:
                                    response_text += f"🏢 *الورشة:*\n{refference1[j]}\n\n"
                                    response_text += f"🛠 *التخصص:*\n{refference4[j]}\n\n"
                                    response_text += f"📞 *رقم الهاتف:*\n{refference2[j]}\n\n"
                                    response_text += f"📍 *الموقع:*\n{refference3[j]}\n\n"
                                    response_text += "\n\n"  # Add space between each workshop info
                            last_time = now
                            bot.send_voice(message.chat.id,
                                        voice=open(f'{Sound_File_Location}{random.choice(Answer_replies_O)}.ogg', 'rb'),
                                        caption=response_text,protect_content=Protect_Content_Switch_O,
                                        parse_mode='Markdown',
                                        disable_notification=True)  # Disable notifications
                            stop_the_bot=1 # to stop any further checks on the rest of code
                            break

                    else:
                        keyboard = types.InlineKeyboardMarkup()
                        buttons = [types.InlineKeyboardButton(text=City[i], callback_data=f"FixShop[{i}]") for i in range(len(City))]
                        keyboard.add(*buttons[:3])
                        keyboard.add(*buttons[3:6])
                        keyboard.add(*buttons[6:9])
                        keyboard.add(*buttons[9:])
                        last_time = now
                        bot.send_voice(message.chat.id,
                                    voice=open(f'{Sound_File_Location}{random.choice(pick_from_list)}.ogg', 'rb'),
                                    caption=f"({O}) {Pick_City}",
                                    disable_notification=True,protect_content=Protect_Content_Switch_O,
                                    reply_markup=keyboard,
                                    reply_to_message_id=message.message_id)
                        stop_the_bot=1 # to stop any further checks on the rest of code
                        break
       # ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
       
       
              # هذا الكود فيه خلل انه يخرب الاكواد الي تحته لسبب او اخر تاكد انه اخر شي في الاكواد 
     # KKKK

        # Section A 
        # Step 1: Check for "بوت" trigger
       for element in trigger_BOT:
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
               
               # Check if message contains any general triggers
               for i, trigger_list in enumerate([trigger_Price, trigger_number, trigger_Location, trigger_Tutorial], start=1):
                     if any(trigger in words for trigger in trigger_list if trigger):
                        Answer_replies = random.choice(All_Answer_replies)
                        error_tone = random.choice(Click_Start_replies)
                        emojis = ["🌝", "🌚", "🙃", "😇", "😊", "🫡", "", ""]
                        found_part = None
                        group_type = None
                        response = {}

                        # Step 2: Identify part group (A-L) with conflict checking
                        matched_parts = []  # List to store all matched parts
                        conflict_groups = []  # List to store conflicting groups

                        # Collect all matched parts
                        for group_letter in "CJGHADEFKLB":               
                           for i in range(1, 60):
                                 group_name = f'Group_{group_letter}{i}'
                                 group = globals().get(group_name, [])
                                 if any(trigger in words for trigger in group if trigger):
                                    found_part_idx = i - 1
                                    matched_parts.append((group_letter, found_part_idx, group_name))

#________________________________________________________________
                        # Check for conflicts in similar groups
                        for similar_group in similar_groups:
                           group_matches = [gn for gl, fp, gn in matched_parts if gn in similar_group]
                           if len(group_matches) > 1:  # If more than one match in the same similar group
                                 conflict_groups.extend(similar_group)
                                 break  # Only need to detect conflict once

                        # Handle part conflicts
                        if conflict_groups:
                           # Collect requested info types
                           requested_info = []
                           if any(t in words for t in trigger_Price): requested_info.append("price")
                           if any(t in words for t in trigger_number): requested_info.append("number")
                           if any(t in words for t in trigger_Location): requested_info.append("location")
                           if any(t in words for t in trigger_Tutorial): requested_info.append("tutorial")
                           info_suffix = "_".join(requested_info)  # Format: price_number_location_tutorial

                           # Create conflict resolution keyboard
                           for gl, fp, gn in matched_parts:
                              if gn in conflict_groups:
                                 part_name = globals()[f'Parts_Group_{gl}'][fp]
                                 # Format: part_conflict_<group_letter>_<part_idx>_<info_types>
                                 callback_data = f"part_conflict_{gl}_{fp}_{','.join(requested_info)}" 
                                 keyboard.add(types.InlineKeyboardButton(part_name, callback_data=callback_data))

                           # Send single confirmation message
                           Pick_The_Exact = ["⚠️ يوجد عدة أجزاء متشابهة\n اختر الجزء الذي تريده:", "فيه قطع متشابهة لطلبك\n حدد اللي تبغاه بالضبط! 🧐", "⚠️ لاحظت تداخل خيارات \n عيّن لي القطعة المطلوبة!", "هذي القطع تتشابة تقريبًا\n قل لي ايش اللي تقصده! 🤔", "⚠️ فيه تشابه بين الخيارات\n دقّق الاختيار!", "⚠️ لاحظت تشابه في النتائج\n حدّد بالضبط وش اللي تبغى!", "الخيارات متشابهة\n خذ راحتك واختر بدقّة!", "قل لي ايش القطعة اللي تقصدها بالضبط! 🤨", "فيه خيارات متشابهة حدد المطلوب بالتحديد!", "⚠️ القطع هذي اختار منها المقصود بالضبط\n حدّد لي المطلوب!", "⚠️ الخيارات هذي كلها متشابهة\n دقّق الاختيار!", "فيه تداخل في القطع\n خذ لك وقتك وحدّد المطلوب! ⏳", "القطع متشابهة\n خبّرني بالضبط وش اللي تقصده! 🧐", "لاحظت تشابه في الخيارات\n حدّد اللي تبغاه بدقّة! 🔍", "القطع هذي فيها تشابة!\n قول لي وش اللي تقصده! 🤔", "⚠️ الخيارات متشابهة\n تأكّد من اختيارك!", "⚠️ لاحظت تداخل في النتائج\n حدّد القطعة المحددة!", "تمام، لكن القطع ذي كلها متشابهة.\n خبّرني بالضبط اي وحدة تقصد! 🤨", "اوك  لاحظت تشابه في الخيارات\n عطيني القطعة اللي تبغاها! 🧐", "طيب، فيه تداخل بالقطع\n دقّق واختر بدقّة! 🔍", "ولا يهمك لكن الخيارات هذي تشبه بعض!\n قل لي وش اللي تقصده! 🤔", "⚠️ حلو لكن، القطع متطابقة\n تأكّد من اختيارك عشان ما أغلط!", "⚠️ ثواني، لاحظت تشابه\n حدّد لي المطلوب بالضبط!", "ثواني، القطع هذي كلها متشابهة\n خبّرني وش تبغى! 🧐", "⚠️ ممتاز ولكن، فيه خيارات متقاربة\n اختر المطلوب عشان اكون دقيق!", "⚠️ تمام، لاحظت تداخل\n عيّن لي القطعة اللي تقصدها!", "فيه تداخل في القطع\n خذ لك وقتك وحدّد المطلوب! 🙃", "القطع متشابهة\n خبّرني بالضبط وش اللي تقصده! 🌚", "لاحظت تشابه في الخيارات\n حدّد اللي تبغاه بدقّة! 😇", "القطع هذي زي بعض!\n قل لي وش اللي تقصده! 😌", "فيه قطع نوعا ما متشابهه\n اختر اللي تبغاه بالضبط! 🌝"]
                           bot.send_message(
                                 message.chat.id, random.choice(Pick_The_Exact),
                                 reply_markup=keyboard,
                                 reply_to_message_id=message.message_id
                           )
                           stop_the_bot = 1  # Stop further processing
                           break  # Exit the loop after sending the confirmation message
#________________________________________________________________



                        # Step 3: Handle found part (no conflicts)
                        Is_price_Asked    = "No"
                        Is_number_Asked   = "No"
                        Is_tutorial_Asked = "No"
                        Is_location_Asked = "No"
                        

                        if matched_parts:  # If parts were found (no conflicts)
                           group_type, found_part, _ = matched_parts[0]  # Use the first matched part
                           mapped_group = group_mapping[group_type]  # Convert A-L to L1-L11
                           group_header_text = group_headers.get(mapped_group)  # Get the appropriate header
                           Random_answer_reply = random.choice(All_Answer_replies)

                           # --- Part Location Handling ---  
                           if any(trigger in words for trigger in trigger_Location if trigger):
                                 Is_location_Asked = "Yes"
                                 location = globals().get(f'Part_Location_group_{group_type}')[found_part]
                                 # Check if location is empty or invalid
                                 if not location:  # If location is empty or falsy
                                    response['location'] =("عذرا لا أمتلك الصورة ولكنني مازلت أتعلم")
                                 else:
                                    # Append the main response only if location is valid
                                    response['location'] =(f"* (تم إرسال الصورة)*")  #{globals().get(f'Parts_Group_{group_type}')[found_part]}
                                    
                           # --- Part Number Handling ---
                           if any(trigger in words for trigger in trigger_number if trigger):
                                 Is_number_Asked = "Yes"
                                 numbers = globals().get(f'Parts_numbers_group_{group_type}')[found_part]
                                 response['number'] = f"\n*🔢 رقم القطعة: *{numbers}" if is_valid_info(str(numbers)) else f"\n*🔢 رقم القطعة:*\n{X}\n"
                      
                           # --- Price Handling ---
                           if any(trigger in words for trigger in trigger_Price if trigger):
                                 Is_price_Asked = "Yes"
                                 prices = globals().get(f'Parts_prices_group_{group_type}')[found_part]
                                 response['price'] = f"\n*💰 الأسعار من عدة محلات:*\n{', '.join(map(str, prices))}" if is_valid_info(str(prices)) else f"\n*💰 الأسعار من عدة محلات:*\n{X}\n"

                           # --- Tutorial Handling ---
                           if any(trigger in words for trigger in trigger_Tutorial if trigger):
                                 Is_tutorial_Asked = "Yes"
                                 links = [globals().get(f'How_2_Change_{group_type}_Link{link_num}')[found_part] for link_num in range(1, 5)]
                                 links = [link for link in links if link and "http" in link]
                                 # Separate the (first 3 links) and (the fourth link) (if it exists)
                                 fourth_link = links[3] if len(links) > 3 else None  # Fourth link (if available)
                                 links = links[:3]  # This ensures only the first 3 links are kept
                                 # Combine the first 3 links into the response
                                 formatted_links = [
                                    f"[(فديو {i + 1})]({link})" for i, link in enumerate(links)  ]

                                 # Combine into the response
                                 response['tutorial'] = "\n*🎥 فديوهات لطريقة التغيير:*\n📎 " + "\n\n📎 ".join(formatted_links) if links else f"\n*🎥 فديوهات لطريقة التغيير:*\n{X}\n"
                                 if fourth_link:         # Add the fourth link with a different header (if it exists)
                                    response['tutorial'] += "\n\n*📌قم بإعادة الضبط  بعد التغيير:*\n📎 [(إضغط لعرض الطريقة)]({})".format(fourth_link)

                           # Construct final Response
                           if  (Is_price_Asked=="Yes")   and   (Is_number_Asked=="No")  and   (Is_tutorial_Asked=="No")  and  (Is_location_Asked=="No"):
                              if not any(isinstance(item, (int, float)) for item in prices):
                                 # If the list is empty or contains no numbers
                                 Random_answer_reply = random.choice(Click_Start_replies)
                              else: # If the list contains at least one number
                                 Random_answer_reply = random.choice(Answer_Fits_All)                             
                           if  (Is_price_Asked=="No")   and   (Is_number_Asked=="Yes")  and   (Is_tutorial_Asked=="No")  and  (Is_location_Asked=="No"):
                              if not numbers : # if empty or invalid
                                    Random_answer_reply = random.choice(Click_Start_replies)
                              else :          # if written
                                    Random_answer_reply = random.choice(Answer_Fits_All)
                           if  (Is_price_Asked=="No")   and   (Is_number_Asked=="No")  and   (Is_tutorial_Asked=="No")  and  (Is_location_Asked=="Yes"):
                              if not location : # if empty or invalid
                                    Random_answer_reply = random.choice(Click_Start_replies)
                              else :          # if written
                                    Random_answer_reply = random.choice(Answer_Fits_All)
                           if  (Is_price_Asked=="No")   and   (Is_number_Asked=="No")  and   (Is_tutorial_Asked=="Yes")  and  (Is_location_Asked=="No"):
                              if links:  # If the first link is not empty 
                                 Random_answer_reply = random.choice(Answer_Fits_All)
                              else:      # If the first link is empty 
                                 Random_answer_reply = random.choice(Click_Start_replies)

                           response_text = f" {car_header}\n*🔧 القطعة: {globals().get(f'Parts_Group_{group_type}')[found_part]}*\n"
                           response_text += "\n".join(response.values())                  
                           if Is_location_Asked== "Yes" :  #if location is asked
                              emojis = ["🌝", "🌚","🌝", "🌚", "🙃", "😇", "😊", "🫡", "", ""]
                              picture_path = f"{Pictures_File_Location}{location}.png"
                              try:
                                    with open(picture_path, 'rb') as photo:
                                       bot.send_photo( message.chat.id, photo,caption= response_text ,reply_to_message_id=message.message_id, parse_mode='Markdown', disable_notification=True, protect_content=Protect_Content_Switch_K)
                                       break
                              except FileNotFoundError: # Fallback to voice message if image missing
                                    bot.send_voice( message.chat.id, voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg', 'rb'), caption=response_text, parse_mode='Markdown', reply_to_message_id=message.message_id, disable_notification=True, protect_content=Protect_Content_Switch_K)
                                    break
                           else:  # Original voice handling for other modes
                                 bot.send_voice( message.chat.id, voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg', 'rb'), caption=response_text, parse_mode="Markdown",reply_to_message_id=message.message_id, disable_notification=True, protect_content=Protect_Content_Switch_K)
                                 break
                           stop_the_bot=1
                           last_time=now
#__________________________________________________________________



                        # If no part is found, show options
                        else:
                           if not matched_parts:  # If no parts were found
                                 # Check for ANY trigger in the message
                                 detected_trigger = None

                                 # Check all trigger categories
                                 for trigger in trigger_Price:
                                    if trigger in words:
                                       detected_trigger = "price"
                                       break
                                 if not detected_trigger:
                                    for trigger in trigger_number:
                                       if trigger in words:
                                             detected_trigger = "number"
                                             break
                                 if not detected_trigger:
                                    for trigger in trigger_Location:
                                       if trigger in words:
                                             detected_trigger = "location"
                                             break
                                 if not detected_trigger:
                                    for trigger in trigger_Tutorial:
                                       if trigger in words:
                                             detected_trigger = "tutorial"
                                             if ("زيت" or "الزيت") in words:
                                                detected_trigger = "oil_Options"
                                                Random_answer_reply = random.choice(Answer_AS_Lnik)
                                             break

                                 if detected_trigger:
                                    # Create inline keyboard
                                    keyboard = types.InlineKeyboardMarkup(row_width=2)

                                    # Create all buttons
                                    Button_Prices = types.InlineKeyboardButton("💰 أسعار القطع", callback_data="mode_pp")
                                    Button_numbers = types.InlineKeyboardButton("🔢 أرقام القطع", callback_data="mode_pn")
                                    Button_location = types.InlineKeyboardButton("📍 صور وموقع القطع", callback_data="mode_pl")
                                    Button_tutorial = types.InlineKeyboardButton("📺 فديو طريقة التغيير", callback_data="mode_ct")
                                    Engine = types.InlineKeyboardButton("زيت المكينة", callback_data="part_cp_L9_8")  #vvvv
                                    Trans = types.InlineKeyboardButton("زيت القير", callback_data="part_cp_L9_9") 
                                    Brakes = types.InlineKeyboardButton("زيت الفرامل", callback_data="part_cp_L9_10")

                                    # Add buttons with detected trigger first
                                    Pick_The_Exact1 = ["مو متأكد أي قطعة تقصد.. 🙃\n\nاستخدم الزر عشان أعرض لك الخيارات المتاحة:", "طيب، مافهمت بالضبط أي قطعة تقصد.. 🌚\n\nإضغط هنا عشان أظهر لك القطع:", "أي قطعة تقصد بالضبط.. 😌\n\nإضغط على الزر عشان أعرض لك التفاصيل:", "مو متأكد ايش القطعة اللي تبغاها.. 🙂‍↕️\n\nإضغط هنا عشان أقدّم لك الخيارات:", "مو واضح لي أي قطعة تقصد.. 🫨\n\nإختر من الزر عشان أظهر لك القطع المتاحة:", "لحظة.. مو متأكد بالضبط أي قطعة تقصد. 😮‍💨\n\nإضغط على الزر عشان أعرض لك الخيارات:", "غير متأكد أي قطعة تقصد بالضبط.. 🙃\n\nإضغط هنا عشان أظهر لك الخيارات المتوفرة:"]
                                    if detected_trigger == "price":
                                       keyboard.add(Button_Prices)
                                    elif detected_trigger == "number":
                                       keyboard.add(Button_numbers)
                                    elif detected_trigger == "location":
                                       keyboard.add(Button_location)
                                    elif detected_trigger == "tutorial":
                                       keyboard.add(Button_tutorial)
                                    elif detected_trigger == "oil_Options":
                                       Pick_The_Exact1 = ["مو متأكد أي زيت تقصد .. 🙃\n\nاضغط على اللي تبغاه:", "طيب، مافهمت أي زيت تقصد .. 🌚\n\nانقر على الزر اللي يعبّر عن قصدك:", "أي زيت تقصد بالضبط .. 😌\n\nاختر الزر اللي يوافق المقصود:", "مو متأكد ايش نوع الزيت اللي تبغاه .. 🙂\n\nاضغط على الزر اللي يناسب طلبك:", "مو واضح لي أي زيت تقصد .. 🫨\n\nانقر على الزر اللي يمثّل طلبك :", "لحظة.. مو متأكد أي زيت تقصد .. 😮‍💨\n\nاختر المقصود:", "غير متأكد أي زيت تقصد .. 🙃\n\nاضغط على الزيت المقصود:"]
                                       keyboard.add(Engine).add(Trans).add(Brakes)
                                    # Send response
                                    last_time = now
                                    bot.send_voice(
                                       message.chat.id,
                                       voice=open(f'{Sound_File_Location}{random.choice(pick_from_list)}.ogg', 'rb'),
                                       caption=random.choice(Pick_The_Exact1),
                                       reply_markup=keyboard,
                                       parse_mode='Markdown',
                                       disable_notification=True,
                                       reply_to_message_id=message.message_id
                                    )
                                    stop_the_bot = 1  # to stop any further checks on the rest of code
                                    break

       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
       #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


       if  ( "بوت قمع البنزين" in words     or"بوت قمع بنزين" in words   or"بوت صور قمع البنزين" in words     or"بوت صور قمع بنزين" in words) and (stop_the_bot==0):
            bot.reply_to(message,"جاري البحث...")  ; time.sleep(5)  
            bot.send_photo(message.chat.id, photo=open(f"{Pictures_File_Location}ALL PARTS\\fuel funnel.jpg", 'rb') , caption=None, disable_notification=True ,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id) ;  bot.delete_message(message.chat.id, message.message_id +1 )  ; last_time = now  
            stop_the_bot=1 # to stop any further checks on the rest of code
       if  ("بوت سير المكينة"== words   or "بوت سير المكينه"== words ) and (stop_the_bot==0):
            bot.reply_to(message,f"جاري البحث...")  ; time.sleep(5)  
            bot.send_photo(message.chat.id, photo=open(f"{Pictures_File_Location}ALL PARTS\\drivebelt drive belt engine belt ac belt.png", 'rb') , caption=None, disable_notification=True ,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id) ;  bot.delete_message(message.chat.id, message.message_id +1 )   ; last_time = now          
            stop_the_bot=1 # to stop any further checks on the rest of code 
         #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
       if  ("بوت Valve cover gasket"== words   or "بوت valve cover gasket"== words ) and (stop_the_bot==0):
            bot.reply_to(message,f"جاري البحث...") ;time.sleep(20) 
            bot.send_photo(message.chat.id, photo=open(f"{Pictures_File_Location}Valve cover Gasket.png", 'rb') , caption=None, disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)
            bot.send_photo(message.chat.id, photo=open(f"{Pictures_File_Location}Valve cover Gasket 2.png", 'rb') , caption="تم البحث..", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id) ; bot.delete_message(message.chat.id, message.message_id +1 ) ;last_time = now       
            stop_the_bot=1 # to stop any further checks on the rest of code
          #_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

       # التحقق من وجود "بوت تشخيص" أو "بوت شخص" في الرسالة
       #if "بوت تشخيص الاعطال" in words:
         #start_diagnosis(message)  # Trigger cooling system diagnosis
      


      # QQQQ  PinPoint Tests
       # فحص اذا الرسالة تبدأ بكلمة "بوت"
       for element in trigger_BOT:
            if (words.startswith(element)) and (element != "") and (stop_the_bot == 0):
                # فحص اذا تحتوي الرسالة على كلمة من المصفوفة المححده للطلب العام
                if any(trigger in words for trigger in trigger_Q if trigger):
                  keyboard = types.InlineKeyboardMarkup()
                  buttons = []
                  # بناء الأزرار بناءً على PinPoint_Test_Name اللي فيه قيم صالحة فقط
                  for i, name in enumerate(PinPoint_Test_Name):
                     if name:  # إذا كان الاسم مو فاضي
                        buttons.append(types.InlineKeyboardButton(text=name, callback_data=f"Q[{i}]"))
                  # توزيع الأزرار على شكل شبكة (كل صف فيه زرين)
                  for j in range(0, len(buttons), 2):
                     keyboard.add(*buttons[j:j+2])
                  last_time = now
                  bot.send_voice(
                     message.chat.id,
                     voice=open(f'{Sound_File_Location}{random.choice(Pick_any_Subject)}.ogg', 'rb'),
                     caption=f"({Q}) {Pick_one}",
                     disable_notification=True,
                     protect_content=Protect_Content_Switch_H,
                     reply_markup=keyboard,
                     reply_to_message_id=message.message_id   )
                  stop_the_bot = 1  # لإيقاف الفحص في بقية الكود


       if "بوت كم كود تعلمت" in words:
         total_codes, prefix_counts, invalid_codes = check_code_prefixes()
        
         # حساب عدد الأكواد بناءً على الحرف الثاني
         codes_with_0_second_list = [code for code in data.keys() if len(code) > 1 and code[1] == '0']
         codes_with_other_second_list = [code for code in data.keys() if len(code) > 1 and code[1] != '0']

         # Construct the response in Arabic with Markdown formatting
         response = (
            "📊 *إحصائيات الأكواد*:\n\n"
            f"• *عدد الأكواد الي تعلمتها حتى الآن*: `{total_codes}`\n"
            f"• `{len(codes_with_0_second_list)}` كود عام + `{len(codes_with_other_second_list)}` خاص بفورد\n..............\n"
            f"• `{prefix_counts['P']}` كود يبدأ بحرف (P)*\nوتمثل الأعطال التي تخص انظمة مولد القوة وتشمل المحرك والقير*\n\n"
            f"• `{prefix_counts['C']}` كود يبدأ بحرف (C)*\nوتمثل الأعطال التي تخص الشاصيه مثل ال ABS و نظام التعليق والبريك ونظام التوجية*\n\n"
            f"• `{prefix_counts['B']}` كود يبدأ بحرف (B)*\nوتمثل الأعطال التي تخص الأنظمة الموجودة في داخلية السيارة مثل التكييف والإضلائة والايرباق وغيرها*\n\n"
            f"• `{prefix_counts['U']}` كود يبدأ بحرف (U)*\nوتمثل الأعطال التي تخص كمبيوترات ووحدات التحكم بالسيارة والشبكة*\n\n _SuperSyn_"
         )
         
         if invalid_codes:
            response += "\n⚠️ *أكواد غير صالحة (لا تبدأ بـ P, C, B, أو U):*\n"
            for code in invalid_codes:
                  response += f"- `{code}`\n"
         
         # Assuming `bot` and `message` are defined elsewhere in your code
         bot.reply_to(message, response, parse_mode="Markdown")
         last_time=now



       # DTC  dtc  شرح اكواد الاعطال      vvvv
       text = normalize_input(message.text)
       # Debug: Print the normalized input text
       #print(f"Normalized input text: '{text}'")
      
       # Split the text into words
       words = text.split()
      
       # Debug: Print the list of words
       #print(f"Words: {words}")
      

       # Search for a valid code in the entire text
       code_match = re.search(r'\b[PUCBpucb][0-9A-Za-z]{4}\b', text)
      
       if code_match:
            code = code_match.group().upper()  # Convert to uppercase for consistency
            
            # Debug: Print the detected code
            #print(f"Detected code: {code}")
            
            # Load JSON data
            try:
               with open('dtc_data.json', 'r', encoding='utf-8') as f:
                  dtc_data = json.load(f)
            except FileNotFoundError:
               bot.reply_to(message, "❌ ملف البيانات غير موجود")
               return
            except json.JSONDecodeError:
               bot.reply_to(message, "❌ خطأ في تنسيق ملف البيانات")
               return
            
            dtc_info = dtc_data.get(code)
            
            if not dtc_info:
               bot.reply_to(message, f"❌ الكود {code}\n بحثت عنة لكنة غير موجود في قاعدة البيانات")
               return
            
            # Start building the response with the title (if it exists)
            response = ""
            if dtc_info.get('title'):
               response += f"<b>{dtc_info['title']}</b>\n\n"
            
            # Add description if it exists and is not empty
            if dtc_info.get('description'):
               response += f"<b>الوصف:</b>\n{dtc_info['description']}\n\n"
            
            # Add possible causes if they exist and are not empty
            if dtc_info.get('possible_causes'):
               response += "<b>الأسباب المحتملة:</b>\n" + "\n".join(f"• {cause}" for cause in dtc_info['possible_causes']) + "\n\n"
            
            # Add diagnostic aids if they exist and are not empty
            if dtc_info.get('diagnostic_aids'):
               response += "<b>الإرشادات التشخيصية:</b>\n" + "\n".join(f"• {aid}" for aid in dtc_info['diagnostic_aids']) + "\n\n"
            
            # If only the title exists and no other data is available
            if not any([dtc_info.get('description'), dtc_info.get('possible_causes'), dtc_info.get('diagnostic_aids')]):
               response += "ماعندي معلومات أكثر عن هذا الكود"
            #response+= "\n_SuperSun_"
            # Debug: Print the final response
            #print(f"Response: {response}")
            
            # Send the response
            bot.reply_to(message, response, parse_mode='HTML')
            last_time=now

#____________________________________________________________________________________


          #### LEVEL 5
         #### COOLING SYSTEM DIAG ####  
         #  تشخيص مشكله المراوح ماتدور NOW ONLY 2013-2016 2.5L
       if ("المممراوح ماتشتغل" in words    and message.from_user.id == 5308309193 ) :
          bot.send_message(message.chat.id, "لدي القدرة بتشخيص مشاكل مراوح الرديتر, قد لا أتمكن من حل المشكلة ولكن سأقرب لك السبب :)\nإذا كنت مستعد إكتب (بوت شخص المراوح)\nوإقرا التعليمات" , disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)        
       if ("بوت شخص المراوح" in words     and (message.from_user.id == 5308309193) ):
          bot.send_message(message.chat.id, COOLING_FAN_DIAG                                                                           , disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)   
       if (   ("1 1 1 1"== words)           and (message.from_user.id == 5308309193) ) :
          bot.send_message(message.chat.id, COOLING_FAN_RESULT1                                                                        , disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)   
       if (   ("1 1 1 0"== words)           and (message.from_user.id == 5308309193) ) :
          bot.send_photo(message.chat.id, photo=open(f'{Pictures_File_Location}fan test case1.png', 'rb') , caption=COOLING_FAN_RESULT2, disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)   
       if (   ("0 0 0 1"== words)           and (message.from_user.id == 5308309193) ) :
          bot.send_photo(message.chat.id, photo=open(f'{Pictures_File_Location}fan test case2.png', 'rb') , caption=COOLING_FAN_RESULT3, disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)
       if (   ("1 1 0 1"== words)           and (message.from_user.id == 5308309193) ) :
          bot.send_photo(message.chat.id, photo=open(f'{Pictures_File_Location}fan test case3.png', 'rb') , caption=COOLING_FAN_RESULT4, disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id) 
       if (   ("0 0 1 1"== words)           and (message.from_user.id == 5308309193) ) :
          bot.send_photo(message.chat.id, photo=open(f'{Pictures_File_Location}fan test case4.png', 'rb') , caption=COOLING_FAN_RESULT5, disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)   
       if (   ("0 0 1 0"== words)           and (message.from_user.id == 5308309193) ) :
          bot.send_message(message.chat.id, COOLING_FAN_RESULT6                                                                        , disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=message.message_id)   
         #________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

       #if (   ("بوت ايش تعلمت"== words)  and (message.from_user.id == 5308309193) ) : 
              #bot.send_message(message.chat.id, ALL_INO_LEARNED)


        #  اذا كان طلب البوت متكرر في المده المحدده راح يحذف الرسالة
    else:
      if ( (now - last_time) <= (Short_Pause_BeforeAnotherReply) )  and  (  f"{Signature}" not in words  )  and  (message.from_user.id  not in  Blocked )  and   ("بوت" == words   or  words.split()[0]=="بوت" )  : 
         bot.delete_message(message.chat.id, message.message_id ) 
         t = time.localtime(); current_time = time.strftime("%H:%M:%S", t); print(f'..................\n..................\n{current_time}\n❌ frequnt message deleted:\n   ({message.from_user.first_name}) ID:({message.from_user.id})')

# _______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________



# HERE WHAT HAPPEND WHEN A BUTTON IS CLICKED
@bot.callback_query_handler(func=lambda call:True)
def callback_data(call):

#______________________________________تخصيص خيارات لكل مستخدم لاتعمل الا له_____________________________________________xxxx
    # Get ownership info
   allowed_user_id = user_keyboard_ownership.get(
        (call.message.chat.id, call.message.message_id), 
        None
    )
   current_user_id = call.from_user.id
    
   # Debug: Print ownership info
   print(f"Allowed User: {allowed_user_id}, Current User: {current_user_id}")
    
   if allowed_user_id != current_user_id:
    try:
        # Get the original user's details
        original_user = bot.get_chat_member(call.message.chat.id, allowed_user_id).user
        name1 = original_user.first_name or ""
        name2 = original_user.last_name or ""
    except Exception as e:
        print(f"Error getting user info: {e}")
        name1 = "صاحب الطلب"
        name2 = ""
    
    bot.answer_callback_query(
        call.id, 
        f"❌ هذه الخيارات خاصة ب {name1} {name2}\nلا تخرب علية 🙃", 
        show_alert=True
    )
    return
#_____________________________________________________________________________________
        

   handle_query(call)
   # ALL definds
   data = call.data  
   Start="\n🟢 إضغط للتأكيد"
   name1=call.message.from_user.first_name ;   name2=call.message.from_user.last_name
   sleep_time1=25;  sleep_time2=20 ; sleep_time3=15 ; sleep_time4=10 ;  sleep_time5=5   ; sleep_time_A=15;      sleep_time_B=5;      sleep_time_C=7;      sleep_time_D=15;      sleep_time_E=15;      sleep_time_F=15;      sleep_time_G=15;      sleep_time_H=15;      sleep_time_J=15;       sleep_time_K=15;      sleep_time_L=15;      sleep_time_M=15;      sleep_time_N=15;      sleep_time_O=15;      sleep_time_R=15
   #  إتاحة وقت إنتظار بعد الضغط جتى يظهر الزر المضغوط  + حتى تحل مشكلة تكرار الضغط الي تسبب نوقف البوت وتسبب تكرار ردود البوت   
   Ckick_Sleep=1  # <<<  هذا الرقم الوحيد الي تلعب فيه وهو وقت الانتظار بعد الضغط
   global last_Click ; now = time.time()
   system_to_group = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E","6": "F",  "7": "G", "8": "H", "9": "J", "10": "K", "11": "L"}


    #  الازارير ماتستجيب الا بعد وقت معين  ولازم يكون غير محظور
   if (     (now - last_Click) > (Ckick_Sleep +1) )  and  (call.message.from_user.id  not in  Blocked ): 
       if (call.from_user.id == MY_ID)  :
          Level_of_Clicker=" 🎖🎖🎖🎖🎖"
       if (call.from_user.id != MY_ID) :
          Level_of_Clicker=""

       t = time.localtime(); current_time = time.strftime("%H:%M:%S", t); print(f'..................\n..................\n{current_time}\n🔴 Clicked By:({call.from_user.first_name})\n   ID:({call.from_user.id}) Level:{Level_of_Clicker}')
       last_Click = now ; time.sleep(Ckick_Sleep)  
       Pick_one=random.choice(Pick_one_1)
       Pick_City=random.choice(Pick_City_1)
       Pick_Engine=random.choice(Pick_Engine_1)
       Pick_model=random.choice(Pick_model_1)
       Pick_wheel_size=random.choice(Pick_wheel_size_1)
       Searching_Text=random.choice(Searching_Text_1)
       ALL_Learned=[ "Direct_Parts_Related",    "Parts_Group_A" ,"Parts_Group_B" ,"Parts_Group_C" ,"Parts_Group_D" , "Parts_Group_E" ,"Parts_Group_F" , "Parts_Group_G","Parts_Group_H" ,"Parts_Group_J" , "Parts_Group_K" , "Parts_Group_L"]
 
       # شرح البوت xxxx  use this   bot.answer_callback_query(call.id, f"({Z})\n\n https://t.me/fusion1/77876" , show_alert=True)
       if call.message:
          if call.data=="clickZ"  :
            Random_wait_reply = random.choice(wait_replies_Z) # هذي ردود العشوائية الي يقول فيها حسنا انتظر او داري البحث تم كتابتها فوق كل مازادت الردود ضيفها فوق و اوتوماتيك يختار واحد عشوائي 
            bot.delete_message(call.message.chat.id, ((call.message.message_id)) )
            bot.send_voice(chat_id=call.message.chat.id, voice=open(f'{Sound_File_Location}{Random_wait_reply}.ogg','rb'),   caption=f"({Z})\n\n [دليل إستخدام البوت](https://t.me/fusion1/77876)", disable_notification=True,parse_mode="Markdown", reply_to_message_id= (call.message.message_id) -1 )

################################################  Need fix down #######################################################################

#_______________________________________________________________________________________________________________________________________

# BBBB  (بحث معلومات المركبة)
       if call.message:            
          if call.data=="clickB"  :
             Random_wait_reply  = random.choice(wait_replies_B) # هذي ردود العشوائية الي يقول فيها حسنا انتظر او داري البحث تم كتابتها فوق كل مازادت الردود ضيفها فوق و اوتوماتيك يختار واحد عشوائي              
             Random_answer_reply= random.choice(Answer_AS_Lnik)  # تاكد الحرف الي هنا يتناسق مع القسم
             bot.delete_message(call.message.chat.id, ((call.message.message_id)) )
             #bot.send_voice(chat_id=call.message.chat.id, voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg','rb'),   caption=f"{Signature}\n({B})\n\n{REPLY_TEXT_VIN}\n\n{Put_At_End_Of_Message}", disable_notification=True, reply_to_message_id= (call.message.message_id) -1 )
             bot.send_photo(call.message.chat.id, photo=open(f'{Pictures_File_Location}VIN lovations.png', 'rb'), caption=f"{Signature}\n({B})\n\n{REPLY_TEXT_VIN}\n\n{Put_At_End_Of_Message}",  disable_notification=True,reply_to_message_id= (call.message.message_id) -1 )

#_______________________________________________________________________________________________________________________________________


# Amounts and Sizes إذا تم إختيار  كميات ومقاسات  الأزارير لجديدة تحت تمثل كل قسم 
       if call.message:
          if (call.data=='Amounts_and_Sizes'  or call.data=='Amounts_and_Sizes_return') :      
            last_Click = now
            keyboard = types.InlineKeyboardMarkup()
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bottonD=types.InlineKeyboardButton(text= D ,callback_data='clickD') # بحث مقاسات
            bottonJ=types.InlineKeyboardButton(text= J ,callback_data='clickJ') # كميات
            botton_Return=types.InlineKeyboardButton(text= Main_Return ,callback_data='botton_Return')
            keyboard.add(bottonD,bottonJ)#.add(botton_Return)
            bot.edit_message_caption(f"({Amounts_and_Sizes}){Pick_one}",call.message.chat.id, (call.message.message_id) , reply_markup=keyboard) 

      # DDDD إذا تم إختيار مقاسات   
       for element in  ClickD  :  # في حال تم ضغط اي زر راح يشيك في هذي القائمة ويطبق الكود اذا كان من ضمنها
           if   (element == call.data)  and  (element !="") :      
                Random_wait_reply  = random.choice(wait_replies_D) ; Random_answer_reply= random.choice(Answer_replies_D)
                if  call.data=="clickD" :    
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    bottonD1 =types.InlineKeyboardButton(text= D1 ,callback_data='clickD[0]') #(مقاس البطاريه)
                    bottonD2 =types.InlineKeyboardButton(text= D2 ,callback_data='clickD2') #(مقاس الكفرات)
                    bottonD3=types.InlineKeyboardButton(text= D3 ,callback_data='clickD[2]') #(مقاس المبات)
                    bottonD4 =types.InlineKeyboardButton(text= D4 ,callback_data='clickD[3]') #(مقاس المساحات)
                    bottonD5 =types.InlineKeyboardButton(text= D5 ,callback_data='clickD[4]') #"مقاس صواميل الكفر"
                    botton_Return=types.InlineKeyboardButton(text= "رجوع" ,callback_data='Amounts_and_Sizes_return')
                    keyboard.add(bottonD1,bottonD2).add(bottonD3,bottonD4).add(bottonD5)#.add(botton_Return)
                    bot.edit_message_caption( f"({D}){Pick_one}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard) 
                    break
                # D2  خيارات مقاسات الكفرات حسب الموديل
                if  call.data=="clickD2" :            
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    botton1=types.InlineKeyboardButton(text=' موديلات 2013-2019',callback_data='clickD[1]')
                    botton2=types.InlineKeyboardButton(text=' موديلات 2009-2012',callback_data='clickD[01]')
                    keyboard.add(botton1,botton2)  
                    bot.edit_message_caption( f"{D2}{Pick_model}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard) 
                    break
                if (call.data=="clickD[01]") : #2012-
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    botton31=types.InlineKeyboardButton(text='  جنط 16',callback_data='click31')
                    botton32=types.InlineKeyboardButton(text='  جنط 17',callback_data='click32')
                    botton33=types.InlineKeyboardButton(text='  جنط 18',callback_data='click33')
                    botton38=types.InlineKeyboardButton(text="لا أعلم - غير ذلك ",callback_data='click38')
                    Return  =types.InlineKeyboardButton(text="قائمة الموديلات",callback_data='clickD2')
                    keyboard.add(botton31,botton32,botton33).add(botton38).add(Return)
                    bot.edit_message_caption( f"{D2}\n{K00}{Pick_wheel_size}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard) 
                    break
                if (call.data=="clickD[1]") : #2013+ 
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    botton2013_2019=types.InlineKeyboardButton(text='2013_2019',callback_data='none')
                    botton35=types.InlineKeyboardButton(text=' جنط 16',callback_data='click35')
                    botton36=types.InlineKeyboardButton(text=' جنط 17',callback_data='click36')
                    botton37=types.InlineKeyboardButton(text=' جنط 18',callback_data='click37')
                    botton38=types.InlineKeyboardButton(text="لا أعلم - غير ذلك ",callback_data='click38')
                    Return  =types.InlineKeyboardButton(text="قائمة الموديلات",callback_data='clickD2')
                    keyboard.add(botton35,botton36,botton37).add(botton38).add(Return) 
                    bot.edit_message_caption( f"{D2}\n{K0}{Pick_wheel_size}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard) 
                    break
                # ردود مقاسات الكفرات
                if  call.data=="click31":
                    Search_text=f"🛞({D2})"      ; Send_Voice="Yes";      Voice_caption=f"{Search_text}{tire_size1}";            Send_Photo="No";     Photo_name=""                ;Photo_caption=""
                if  call.data=="click32":
                    Search_text=f"🛞({D2})"      ; Send_Voice="Yes";      Voice_caption=f"{Search_text}{tire_size2}";            Send_Photo="No";     Photo_name=""                ;Photo_caption=""
                if  call.data=="click33":
                    Search_text=f"🛞({D2})"      ; Send_Voice="Yes";      Voice_caption=f"{Search_text}{tire_size3}";            Send_Photo="No";     Photo_name=""                ;Photo_caption=""
                if  call.data=="click35":
                    Search_text=f"🛞({D2})"      ; Send_Voice="Yes";      Voice_caption=f"{Search_text}{tire_size4}";            Send_Photo="No";     Photo_name=""                ;Photo_caption=""
                if  call.data=="click36":
                    Search_text=f"🛞({D2})"      ; Send_Voice="Yes";      Voice_caption=f"{Search_text}{tire_size5}";            Send_Photo="No";     Photo_name=""                ;Photo_caption=""
                if  call.data=="click37":
                    Search_text=f"🛞({D2})"      ; Send_Voice="Yes";      Voice_caption=f"{Search_text}{tire_size6}";            Send_Photo="No";     Photo_name=""                ;Photo_caption=""
                if  call.data=="click38":
                    Search_text="إخترت (لا أعلم)"                  ; Send_Voice="No" ;      Voice_caption="";                   Send_Photo="Yes";     Photo_name="Door Label.png"  ;Photo_caption="الموديل وحجم الجنط:\nإخترت (لا أعلم) \n\n المعلومات  موجودة في الملصق عند مدخل باب السائق من الداخل"
                # ردود باقي الخيارات          
                if  call.data=="clickD[0]" :   #(مقاس البطاريه)     
                    Search_text=f"({D1})"                           ; Send_Voice="NO";       Voice_caption=f"{Search_text}{REPLY_TEXT_BATTERY}";    Send_Photo="Yes";    Photo_name="Battery.jpg"      ;Photo_caption=f"{Search_text}{REPLY_TEXT_BATTERY}"
                if  call.data=="clickD[2]"  or call.data=="clickD[02]" :   #(مقاس اللمبات)    
                    Search_text=f"\U0001f4a1({D3})"               ; Send_Voice="No";         Voice_caption=f"{Search_text}{LIGHTS_REPLY_TEXT}";     Send_Photo="Yes";    Photo_name= "headlights All bulbs lamps.png"      ;Photo_caption=f"{Search_text}{LIGHTS_REPLY_TEXT}"
                if  call.data=="clickD[3]"  or call.data=="clickD[03]" :   #(مقاس مساحات)     
                    Search_text=f"({D4})"                           ; Send_Voice="Yes";      Voice_caption=f"{Search_text}{REPLY_TEXT_WIPERS}";     Send_Photo="No";     Photo_name=""                 ;Photo_caption=""
                if  call.data=="clickD[4]" :   #(مقاس صواميل كفرات)     
                    Search_text=f"({D5})"                           ; Send_Voice="Yes";      Voice_caption=f"{Search_text}{REPLY_TEXT_LugNut}";     Send_Photo="No";     Photo_name=""                 ;Photo_caption=""
                bot.delete_message(call.message.chat.id, ((call.message.message_id)) )
                if Send_Voice=="Yes":
                   bot.send_voice(chat_id=call.message.chat.id, voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg','rb'),caption=f"{Voice_caption}\n\n{Put_At_End_Of_Message}" , disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id= (call.message.message_id) -1 )
                if Send_Photo=="Yes":
                   bot.send_photo(call.message.chat.id,      photo=open(f"{Pictures_File_Location}{Photo_name}", 'rb') ,           caption=f"{Photo_caption}\n\n{Put_At_End_Of_Message}" , disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id= (call.message.message_id) -1 )  
    
      
      
      
      # jjjj إذا تم إختيار كميات 
       for element in  ClickJ  :  # في حال تم ضغط اي زر راح يشيك في هذي القائمة ويطبق الكود اذا كان من ضمنها
           if   (element == call.data)  and  (element !="") :      
                Random_wait_reply  = random.choice(wait_replies_J) ; Random_answer_reply= random.choice(Answer_replies_J)
                # J جميع الكميات
                if call.data=="clickJ" or call.data=="Amounts_Return"  :
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    bottonJ1 =types.InlineKeyboardButton(text= J1 ,callback_data='clickE2')  # كمية زيت المكينة  المدخلات فوق جاهزه مايحتاج اضافه
                    bottonJ2 =types.InlineKeyboardButton(text= J2 ,callback_data='clickJ2')  
                    bottonJ3 =types.InlineKeyboardButton(text= J3 ,callback_data='clickJ[2]')  
                    bottonJ4 =types.InlineKeyboardButton(text= J4 ,callback_data='clickJ[3]')  
                    bottonJ5 =types.InlineKeyboardButton(text= J5 ,callback_data='clickJ[4]')  
                    botton_Return=types.InlineKeyboardButton(text= "رجوع" ,callback_data='Amounts_and_Sizes_return')
                    keyboard.add(bottonJ1,bottonJ2).add(bottonJ3,bottonJ4).add(bottonJ5)#.add(botton_Return)
                    bot.edit_message_caption( f"({J}){Pick_one}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard) 
                    break
                # J2 كميه زيت القير   #  غير مستخدم حاليا هذا اذا تبغى تخلي الرد اكثر تفصيلا
                if call.data=="clickJ2"   or call.data=="J_J2" :
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    botton2014=types.InlineKeyboardButton(text=' موديلات 2013-2019',callback_data='clickJ[1]')
                    botton2012=types.InlineKeyboardButton(text=' موديل 2012-2009',callback_data='clickJ[01]')
                    Return     =types.InlineKeyboardButton(text="العودة",callback_data= 'Amounts_Return')
                    keyboard.add(botton2012).add(botton2014)#.add(Return)
                    bot.edit_message_caption( f"({J2}){Pick_model}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard) 
                    break
               # E2 كمية زيت المكينه تحديد الموديل
                if call.data=="clickE2":
                  keyboard = types.InlineKeyboardMarkup()
                  bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                  botton1=types.InlineKeyboardButton(text='موديلات 2013-2019',callback_data='clickJ[0]')
                  botton2=types.InlineKeyboardButton(text='موديلات 2009-2012',callback_data='clickJ[00]')
                  keyboard.add(botton1).add(botton2)#.add(Return)
                  bot.edit_message_caption( f"({E2}){Pick_model}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard) 
                  break


                # اجوبه كميات زيت المكينه حسب المحرك والموديل  
                if call.data=="clickJ[0]" :   #(كمية زيت المكينة 2014)
                  Search_text=f"({E2})";     Send_Voice_1="No";  Voice_file_1=f"{random.choice(Eng_Amount_2013)}";       Voice_caption_1="";                                                                                                          Send_Voice_2="No";       Voice_file_2="";                             Voice_caption_2="";                                                                              Send_Photo="Yes"      ; Photo_name="Dipstick.png";     Photo_caption=f"{REPLY_TEXT_Engine_Oil_AMOUNT1}\n\n{oil_level}" 
                if call.data=="clickJ[00]":    #(كمية زيت لمكينه 2012)
                  Search_text=f"({E2})";     Send_Voice_1="No";  Voice_file_1=f"{random.choice(Eng_Amount_2012)}";       Voice_caption_1=Search_text;                                                                                                 Send_Voice_2="No";       Voice_file_2="";                             Voice_caption_2="";                                                                              Send_Photo="Yes"      ; Photo_name="Dipstick.png";     Photo_caption=f"{REPLY_TEXT_Engine_Oil_AMOUNT2}\n\n{oil_level}" 

                # ردود باقي الخيارات          
                if  call.data=="clickJ[1]" :   #(كمية زيت القير 2013)     
                    Search_text=f"({J2})"                            ; Send_Voice_1="Yes";    Voice_file_1=f"{random.choice(Aft_Amount_2013)}";        Voice_caption_1=REPLY_TEXT_ATF_AMOUNT_1;                       Send_Voice_2="No";       Voice_file_2="";                             Voice_caption_2="";                                              Send_Photo="No"            ; Photo_name="";                  Photo_caption=""
                if  call.data=="clickJ[01]" :  #(كمية زيت القير 2012 )    
                    Search_text=f"({J2})"                           ; Send_Voice_1="Yes";    Voice_file_1=f"{random.choice(Aft_Amount_2012)}";        Voice_caption_1=REPLY_TEXT_ATF_AMOUNT_2;                       Send_Voice_2="No";       Voice_file_2="";                             Voice_caption_2="";                                              Send_Photo="No"            ; Photo_name="";                  Photo_caption=""
                if  call.data=="clickJ[2]":    #2014(كمية سائل الفرامل)  
                    Search_text=f"({J3})"                                  ; Send_Voice_1="NO";    Voice_file_1=Random_answer_reply;                         Voice_caption_1=f"{REPLY_TEXT_BrakeFluid_AMOUNT}";             Send_Voice_2="No";       Voice_file_2="";                             Voice_caption_2="";                                              Send_Photo="No"            ; Photo_name="";                  Photo_caption=""
                if  call.data=="clickJ[02]":   #2012(كمية سائل الفرامل)     
                    Search_text=f"({J3})"                                  ; Send_Voice_1="NO";    Voice_file_1=Random_answer_reply ;                        Voice_caption_1=f"{REPLY_TEXT_BrakeFluid_AMOUNT}";              Send_Voice_2="No";       Voice_file_2="";                             Voice_caption_2="";                                              Send_Photo="No"            ; Photo_name="";                  Photo_caption=""
                if  call.data=="clickJ[3]" :   #2014(كمية سائل التبريد)    
                    Search_text=f"({J4})"                                  ; Send_Voice_1="NO";    Voice_file_1=Random_answer_reply;                         Voice_caption_1=f"{REPLY_TEXT_COOLANT_AMOUNT}";            Send_Voice_2="No";       Voice_file_2="";                             Voice_caption_2="";                                              Send_Photo="Yes"      ; Photo_name="Coolant water";            Photo_caption="REPLY_TEXT_COOLANT_AMOUNT"
                if  call.data=="clickJ[03]" :  #2012(كمية سائل التبريد)    
                    Search_text=f"({J4})"                                  ; Send_Voice_1="NO";    Voice_file_1=Random_answer_reply;                         Voice_caption_1=f"{X}";                                         Send_Voice_2="No";       Voice_file_2="";                             Voice_caption_2="";                                              Send_Photo="No"            ; Photo_name="";                  Photo_caption=""             
                if  call.data=="clickJ[4]" :   #2014 (كمية غاز الفريون)    
                    Search_text=f"({J5})"                                  ; Send_Voice_1="NO";    Voice_file_1=Random_answer_reply;                         Voice_caption_1=f"{REPLY_TEXT_FERON_AMOUNT}\n{X}";              Send_Voice_2="No";       Voice_file_2="";                             Voice_caption_2="";                                              Send_Photo="No"            ; Photo_name="";                  Photo_caption=""
                if  call.data=="clickJ[04]" :  #2012 (كمية غاز الفريون)    
                    Search_text=f"({J5})"                                  ; Send_Voice_1="NO";    Voice_file_1=f"Ring_Tone1" ;                              Voice_caption_1=f"{X}";                                         Send_Voice_2="No";       Voice_file_2="";                             Voice_caption_2="";                                              Send_Photo="No"            ; Photo_name="";                  Photo_caption=""


                if Send_Voice_1 == "NO":
                   bot.send_message( chat_id=call.message.chat.id, text=f"{Search_text}\n{Voice_caption_1}\n\n{Put_At_End_Of_Message}",  disable_notification=True,  protect_content=Protect_Content_Switch,parse_mode="Markdown",  reply_to_message_id=call.message.message_id - 1  )

                if Send_Voice_1=="Yes":
                   bot.send_voice(chat_id=call.message.chat.id, voice=open(f'{Sound_File_Location}{Voice_file_1}.ogg','rb')     ,caption=f"{Search_text}\n{Voice_caption_1}\n\n{Put_At_End_Of_Message}" , disable_notification=True,protect_content=Protect_Content_Switch,parse_mode="Markdown", reply_to_message_id= (call.message.message_id) -1 )
                if Send_Photo=="Yes":
                   time.sleep(0.3)
                   bot.send_photo(call.message.chat.id,      photo=open(f"{Pictures_File_Location}{Photo_name}", 'rb') ,         caption=f"{Search_text}\n{Photo_caption}\n\n{Put_At_End_Of_Message}" , disable_notification=True,protect_content=Protect_Content_Switch,parse_mode="Markdown", reply_to_message_id= (call.message.message_id) -1 )  
                bot.delete_message(call.message.chat.id, ((call.message.message_id)) )
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# GGGG إذا تم إختيار ( مشاكل شائعة) الازارير الجديدة تحت تمثل كل قسم  
       for element in ClickG:
            if element == call.data and element:
                Random_answer_reply = random.choice(Answer_replies_G)

                if call.data == "clickG":
                    City_ref = "G"
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    buttons = [types.InlineKeyboardButton(text=problem, callback_data=f'{City_ref}[{i}]') for i, problem in enumerate(Sections_G0[:20])]
                    for i in range(0, len(buttons), 3):
                        keyboard.add(*buttons[i:i + 3])
                    bot.edit_message_caption(f"({G}){Pick_one}", call.message.chat.id, call.message.message_id, reply_markup=keyboard)
                    break

                if call.data.startswith("G["):
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    index = int(call.data[2:-1])
                    refference1 = globals().get(f'Sections_G0', [])
                    refference2 = globals().get(f'Answer_By_Link1_G0', [])
                    refference3 = globals().get(f'Answer_By_Link2_G0', [])

                    response_text = f"🔧 *{G}\n  ({Sections_G0[index]}) *\n\n"
                    response_text += f"📎 [*إضغط هنا*]({refference2[index]})\n"
                    if refference3[index]:
                        response_text += f"📎 [*الرابط الثاني*]({refference3[index]})\n"
                    response_text += "\n\n"  # Add space between each other info

                    bot.send_voice(
                        chat_id=call.message.chat.id,
                        voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg', 'rb'),
                        caption=response_text, parse_mode="Markdown",
                        disable_notification=True,
                        protect_content=Protect_Content_Switch_G,
                        reply_to_message_id=call.message.message_id - 1)
                    break
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# RRRR إذا تم إختيار (الإستدعائات)الازارير الجديدة تحت تمثل كل قسم  
       if call.message:
          if call.data=="clickR" or   call.data=="R_1"  :
             last_Click = now
             time.sleep(Ckick_Sleep)
             Random_wait_reply = random.choice(wait_replies_R) # هذي ردود العشوائية الي يقول فيها حسنا انتظر او داري البحث تم كتابتها فوق كل مازادت الردود ضيفها فوق و اوتوماتيك يختار واحد عشوائي 
             bot.delete_message(call.message.chat.id, ((call.message.message_id)) )
             bot.send_voice(chat_id=call.message.chat.id, voice=open(f'{Sound_File_Location}Recalls_1.ogg','rb'), caption=f"تم البحث\U00002714\n\n[إضغط هنا لعرض إستدعائات فيوجن 2013-2016](https://t.me/fusion1/117878)\n......................\n\nفورد الناغي (للمنطقة الغربية والجنوبية)\n8001240218\n\nفورد توكيلات الجزيرة(المنطقة الشرقية والشمالية والرياض)\n920002999", disable_notification=True,protect_content=Protect_Content_Switch_R,parse_mode="Markdown", reply_to_message_id= (call.message.message_id) -1)

#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# HHHH إذا تم إختيار ( إعدادات - مود ) الازارير الجديدة تحت تمثل كل قسم  
       for element in ClickH:
            if element == call.data and element:
                Random_answer_reply = random.choice(Answer_replies_H)

                if call.data == "clickH":
                    City_ref = "H"
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    buttons = [types.InlineKeyboardButton(text=Sections_H0[i], callback_data=f"H[{i}]") for i in range(len(Sections_H0))]
                    keyboard.add(buttons[0], buttons[4])
                    keyboard.add(buttons[7], buttons[8])
                    keyboard.add(buttons[9], buttons[5])
                    keyboard.add(buttons[3], buttons[6])
                    keyboard.add(buttons[1], buttons[2])
                    bot.edit_message_caption(f"({H}){Pick_one}", call.message.chat.id, call.message.message_id, reply_markup=keyboard)
                    break

                if call.data.startswith("H["):

                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    index = int(call.data[2:-1])
                    refference1 = globals().get(f'Sections_H0', [])
                    refference2 = globals().get(f'Answer_By_Link1_H0', [])
                    refference3 = globals().get(f'Answer_By_Link2_H0', [])

                    response_text = f"⚙️ *{H}\n({Sections_H0[index]}):*\n\n"
                    response_text += f"📎 [*إضغط هنا*]({refference2[index]})\n\n"
                    if refference3[index]:
                        response_text += f"📎 [*الرابط الثاني*]({refference3[index]})\n\n"
                    response_text += "\n\n"  # Add space between each setting info

                    bot.send_voice(
                        chat_id=call.message.chat.id,
                        voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg', 'rb'),
                        caption=response_text, parse_mode="Markdown",
                        disable_notification=True,
                        protect_content=Protect_Content_Switch_H,
                        reply_to_message_id=call.message.message_id - 1)
                    break
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# QQQQ إذا تم إختيار ( إعدادات - مود ) الازارير الجديدة تحت تمثل كل قسم  
       for element in clickQ:
            if element == call.data and element:
                Random_answer_reply = random.choice(All_Answer_replies)
                if call.data == "clickQ":
                  City_ref = "Q"
                  keyboard = types.InlineKeyboardMarkup()
                  bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                  # بناء الأزرار بناءً على PinPoint_Test_Name اللي فيها أسماء صالحة فقط
                  buttons = []
                  for i, name in enumerate(PinPoint_Test_Name):
                     if name.strip():  # فقط الأسماء غير الفارغة
                           buttons.append(types.InlineKeyboardButton(text=name, callback_data=f"Q[{i}]"))
                  # توزيع الأزرار على شكل شبكة (كل صف فيه زرين)
                  for j in range(0, len(buttons), 2):
                     keyboard.add(*buttons[j:j+2])
                  bot.edit_message_caption(
                     caption=f"({Q}){Pick_one}", 
                     chat_id=call.message.chat.id, 
                     message_id=call.message.message_id, 
                     reply_markup=keyboard   )
                  break
                if call.data.startswith("Q["):
                  bot.delete_message(call.message.chat.id, call.message.message_id)
                  index = int(call.data[2:-1])
                  # Get references from your lists
                  refference1 = globals().get('PinPoint_Test_Name', [])
                  refference2 = globals().get('Text_File1_Name', [])
                  refference3 = globals().get('Text_File2_Name', [])
                  refference4 = globals().get('Text_File3_Name', [])

                  # Base directory path
                  base_dir = r"C:\\Users\\Engmu\\OneDrive\Desktop\ALL PARTS\\Pin PoinT checks"
                  # List of file references to process
                  file_references = [refference2, refference3, refference4]
                  # Track if it's the first file (to send with voice)
                  first_file = True
                  # Process each file
                  for ref in file_references:
                     if index < len(ref) and ref[index].strip():  # Check if the entry is not empty
                           file_path = os.path.join(base_dir, f"{ref[index]}.txt")
                           
                           if os.path.exists(file_path) and os.path.getsize(file_path) > 0:  # Check if file exists and is not empty
                              try:
                                 with open(file_path, 'r', encoding='utf-8') as file:
                                       content = file.read()
                                 
                                 # Send the first file (text only) as a reply
                                 if first_file:
                                    bot.send_message(
                                       chat_id=call.message.chat.id,
                                       text=content,  # File content as text
                                       disable_notification=True,
                                       protect_content=Protect_Content_Switch_O,
                                       reply_to_message_id=call.message.message_id - 1)
                                    
                                    first_file = False  # Mark first file as sent
                                 else:
                                    # Send subsequent files as plain text, replying to the previous message
                                    bot.send_message(
                                       chat_id=call.message.chat.id,
                                       text=content,
                                       disable_notification=True,
                                       protect_content=Protect_Content_Switch_O,
                                       reply_to_message_id=call.message.message_id - 1)
                                    

                              except Exception as e:
                                 # Log errors silently (no user-facing messages)
                                 bot.send_message(
                                       MY_ID,
                                       f"Error reading file: {file_path}\n {str(e)}",
                                       print(file_path) )
                           else:
                              # Log missing or empty files silently
                              bot.send_message(
                                 MY_ID,
                                 f"File missing or empty",
                                 print (file_path)     )
                  break

#_________________________________________________________________________________________________________________________




# Oooo إذا تم إختيار (افضل  الورش حسب المدينة)الازارير الجديدة تحت تمثل كل مدينه 

       for element in ClickO:
            if element == call.data and element:
                Random_answer_reply = random.choice(Answer_replies_O)

                if call.data == "clickO":
                    City_ref = "FixShop"
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    buttons = [types.InlineKeyboardButton(text=city, callback_data=f'{City_ref}[{i}]') for i, city in enumerate(City[:15])]
                    keyboard.add(*buttons[:3])
                    keyboard.add(*buttons[3:6])
                    keyboard.add(*buttons[6:9])
                    keyboard.add(*buttons[9:])
                    bot.edit_message_caption(f"({O}){Pick_City}", call.message.chat.id, call.message.message_id, reply_markup=keyboard)
                    break

                if call.data.startswith("FixShop["):
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    index = int(call.data[8:-1])
                    refference1 = globals().get(f'Shop_Store____Group{index}', [])
                    refference2 = globals().get(f'Shop_Number___Group{index}', [])
                    refference3 = globals().get(f'Shop_Location_Group{index}', [])
                    refference4 = globals().get(f'Speciality____Group{index}', [])

                    response_text = f"🔧 *ورش صيانة في {City[index]}:*\n\n"
                    for j in range(len(refference1)):
                        if refference1[j]:
                            response_text += f"🏢 *الورشة:*\n{refference1[j]}\n\n"
                            response_text += f"🛠 *التخصص:*\n{refference4[j]}\n\n"
                            response_text += f"📞 *رقم الهاتف:*\n{refference2[j]}\n\n"
                            response_text += f"📍 *الموقع:*\n{refference3[j]}\n\n"
                            response_text += "\n\n"  # Add space between each workshop info

                    bot.send_voice(
                        chat_id=call.message.chat.id,
                        voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg', 'rb'),
                        caption=response_text, parse_mode="Markdown",
                        disable_notification=True,
                        protect_content=Protect_Content_Switch_O,
                        reply_to_message_id=call.message.message_id - 1)
                    break

                
#____________________________________________________________________________________________________________


#AAAA
#  إذا تم إختيار محلات  قطع الغيار الأزارير لجديدة تحت تمثل كل قسم 
       for element in ClickA:
           if element == call.data and element:
                Random_answer_reply = random.choice(Answer_replies_A)

                if call.data == "clickA":
                    City_ref = "City"
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    buttons = [types.InlineKeyboardButton(text=city, callback_data=f'{City_ref}[{i}]') for i, city in enumerate(City[:15])]
                    keyboard.add(types.InlineKeyboardButton(text="موقع أونلاين", callback_data=f'{City_ref}[X]'))
                    for i in range(0, len(buttons), 3):
                        keyboard.add(*buttons[i:i+3])
                    bot.edit_message_caption(f"({A}){Pick_City}", call.message.chat.id, call.message.message_id, reply_markup=keyboard)
                    break
                #  إذا تم إختيار  محلات قطع الغيار.  الخيارات تحت تمثل كل قسم 
                if call.data.startswith("City["):
                  city_index = call.data.split("[")[1].split("]")[0]
                  if call.data == "City[X]":
                        print( "RRRRRRRERFFE")
                        # Handle the online location option
                        #bot.send_message(call.message.chat.id, "You selected the online location option.")
                        bot.answer_callback_query( call.id, f"{X}", show_alert=True  )

                  else:
                        city_index = int(city_index)
                        if 0 <= city_index < len(City):
                           city = City[city_index]
                           # Construct the text file path
                           file_path = f"C:\\Users\\Engmu\\OneDrive\\Desktop\\ALL PARTS\\A - Stores Num_Location\\{city_index + 1}- {city}.txt"
                           
                           # Check if the file exists
                           if not os.path.exists(file_path):
                              # If the file does not exist, send an alert to the user
                              bot.answer_callback_query(call.id, f"{X}", show_alert=True)
                              return  # Exit the function to prevent further execution
                                    
                           # Generate the response text
                           response_text = f"\U0001F3E0 *محلات قطع غيار في {city}:*\n{Show_Location}\n\n"
                           groups = read_city_data(file_path)
                           for header, store_location_pairs in groups:
                              response_text += f"\n{header}\n"
                              for store, location in store_location_pairs:
                                    # Escape Markdown characters
                                    store = store.replace("[", "\\[").replace("]", "\\]").replace("*", "\\*").replace("_", "\\_")
                                    response_text += f"📍 [{store}]({location})\n"
                           # Send the response with a photo (if available)
                           photo_path = f"C:\\Users\\Engmu\\OneDrive\\Desktop\\ALL PARTS\\A - Stores Num_Location\\{city_index + 1}- Locations.png"
                           if os.path.exists(photo_path):
                                 max_length = max_Caption_length  # Telegram's caption length limit
                                 if len(response_text) > max_length:
                                       # Split the text into 2 parts
                                       midpoint = len(response_text) // 2  # Find the midpoint
                                       # Search for the nearest header (emoji) to the midpoint
                                       emojis = ["🟡", "🔴", "🟢", "🟣", "🟤", "🟠", "🔵"]
                                       split_index = -1
                                       # Search forward from midpoint for the first emoji line
                                       for i in range(midpoint, len(response_text)):
                                          if any(response_text[i:].startswith(emoji) for emoji in emojis):
                                             split_index = i  # Split BEFORE this line
                                             break
                                       # If no emoji found after midpoint, search backward
                                       if split_index == -1:
                                          for i in range(midpoint, 0, -1):
                                             if any(response_text[i:].startswith(emoji) for emoji in emojis):
                                                   split_index = i
                                                   break
                                       # Default to midpoint if no emoji found
                                       if split_index == -1:
                                          split_index = midpoint
                                       # Split the text into two parts
                                       part1 = response_text[:split_index].strip()
                                       part2 = response_text[split_index:].strip()
                                       part2 +=f"{read_full_parts}"
                                       # Send Part 1 with photo
                                       bot.delete_message(call.message.chat.id, call.message.message_id)
                                       bot.send_photo(
                                          call.message.chat.id,
                                          photo=open(photo_path, 'rb'),
                                          caption=part1,
                                          parse_mode='Markdown',
                                          disable_notification=True,
                                          protect_content=Protect_Content_Switch_A,
                                          reply_to_message_id=call.message.message_id -1  )
                                       # Send Part 2 as follow-up message
                                       bot.send_message(
                                          call.message.chat.id,
                                          text=part2,
                                          parse_mode='Markdown',
                                          disable_notification=True,
                                          protect_content=Protect_Content_Switch_A,
                                          reply_to_message_id=call.message.message_id -1  )
                                 else:
                                       # If the message is within the limit, send it as is
                                       bot.delete_message(call.message.chat.id, call.message.message_id)
                                       bot.send_photo(
                                          call.message.chat.id,
                                          photo=open(photo_path, 'rb'),
                                          caption=response_text,
                                          parse_mode='Markdown',
                                          disable_notification=True,
                                          protect_content=Protect_Content_Switch_A,
                                          reply_to_message_id=call.message.message_id -1  )
                           else:
                              print(f"Debug: Photo not found for city = {city}")
                              bot.send_message(
                                    call.message.chat.id,
                                    text=response_text,
                                    parse_mode='Markdown',
                                    disable_notification=True,
                                    protect_content=Protect_Content_Switch_A,
                                    reply_to_message_id=call.message.message_id -1  )
                           last_time = now
                           stop_the_bot = 1
                           break



#____________________________________________________________________________________________________________



# Maintenance           
#  إذا تم إختيار محلات  قطع الغيار الأزارير لجديدة تحت تمثل كل قسم
         
# جزء الذي يعالج الضغطات
       if  call.data.startswith('maint_')  or (call.data== "MAINTENANCE")  :
        # ================== MAINTENANCE HANDLER ==================
         if call.data == "MAINTENANCE":
               try:
                  category = MAINTENANCE
                  config = MAINTENANCE_CONFIG[category]
                  header = config['header']
                  # إنشاء قائمة الأزرار
                  buttons = []
                  for part in config['items']:
                     sanitized_part = part.replace(" ", "_").replace("-", "").replace("(", "").replace(")", "")
                     btn = types.InlineKeyboardButton(
                           text=f"{config['items'][part]['emoji']} {part}",
                           callback_data=f"maint_{sanitized_part[:30]}"  # قص السلسلة لـ 30 حرف
                     )
                     buttons.append(btn)
                  # إنشاء لوحة مفاتيح مع تحديد عرض الصف 3 أزرار
                  keyboard = types.InlineKeyboardMarkup(row_width=3)
                  keyboard.add(*buttons)
                  
                  bot.edit_message_caption(
                     chat_id=call.message.chat.id,
                     message_id=call.message.message_id,
                     caption=config['header'],
                     parse_mode='HTML',
                     reply_markup=keyboard
                  )
                  
               except Exception as e:
                  print(f"MAINTENANCE MENU ERROR: {str(e)}")
                  bot.answer_callback_query(call.id, text="⚠️ فشل تحميل قائمة الصيانة")

         # ================== MAINTENANCE ITEM HANDLER ==================
         elif call.data.startswith('maint_'):
               try:
                  Random_answer_reply = random.choice(Answer_replies_A)
                  # Acknowledge the callback query
                  bot.answer_callback_query(call.id, text="جارٍ التحميل...")
                 
                  sanitized_part = '_'.join(call.data.split('_')[1:])  # Join all parts after 'maint_'
                  # Find the corresponding part from the configuration
                  part = None
                  for p in MAINTENANCE_CONFIG[MAINTENANCE]['items']:
                        sanitized_p = p.replace(" ", "_").replace("-", "").replace("(", "").replace(")", "")[:30]
                        if sanitized_p == sanitized_part:
                           part = p
                           break

                  if not part:
                     print("Part not found in configuration!")
                     bot.answer_callback_query(call.id, text="⚠️ الجزء غير موجود في القائمة")
                     return
                  # Retrieve part info from the configuration
                  part_info = MAINTENANCE_CONFIG[MAINTENANCE]['items'][part]





                  # Format and send the maintenance info with interval_km only   
                  full_caption = f"🔧 *({MAINTENANCE})*\n"
                  full_caption += f" *ل{part}*\n\n"

                  # Add part_number if not empty
                  part_number = part_info.get('part_number', '').strip()
                  if part_number:
                     full_caption += f"📚 *رقم القطعة:* {part_number}\n\n"

                  # Add video links if not empty
                  video_links = [url.strip() for url in part_info.get('video', []) if url.strip()]
                  if video_links:
                     LINK_TO_VID = ', '.join(video_links)
                     full_caption += f"🎥 *فديو للطريقة:*\n [*إضغط هنا*]({LINK_TO_VID})\n\n"

                  # Add interval_km if not empty
                  interval_km = part_info.get('interval_km', '').strip()
                  if interval_km:
                     full_caption += f"⏳ *ينصح بعملها:*\n {interval_km}\n\n"

                  # Add important_tips if not empty
                  important_tips = part_info.get('important_tips', '').strip()
                  if important_tips:
                     full_caption += f"💡 *نصائح مهمة:*\n {important_tips}\n\n"
            


                  #print  (', '.join(part_info['video']))
                  #full_caption += Signature
                  # ========== END OF YOUR CODE BLOCK ==========
         
                  bot.send_voice(
                     chat_id=call.message.chat.id,
                     voice=open(f'{Sound_File_Location}{random.choice(All_Answer_replies)}.ogg', 'rb'),
                     caption=full_caption,
                     parse_mode="Markdown",
                     disable_notification=True,
                     protect_content=Protect_Content_Switch_K,
                     reply_to_message_id=call.message.message_id
                  )
               except Exception as e:
                  print(f"MAINTENANCE ITEM ERROR: {str(e)}")
                  bot.answer_callback_query(call.id, text="⚠️ حدث خطأ أثناء معالجة الطلب")
               bot.delete_message(call.message.chat.id, ((call.message.message_id)) )


#____________________________________________________________________________________________________________

    #kkkk  ALL PARTS RELATED    
       for element in ClickK: 
            if element == call.data and element:
                Random_answer_reply = random.choice(All_Answer_replies)
                # here nothing happens

#________________________________________________________________  
            # Handle Conflict similar_parts options
            if call.data.startswith('part_conflict_'):
                  Is_price_Asked    = "No"
                  Is_number_Asked   = "No"
                  Is_tutorial_Asked = "No"
                  Is_location_Asked = "No"
                  Random_answer_reply = random.choice(All_Answer_replies) 
                  parts = call.data.split('_')
                  group_letter = parts[2]
                  part_idx = int(parts[3])
                  info_types = parts[4].split(',')
                  # Get part info
                  group_header = group_headers[group_mapping[group_letter]]
                  part_name = globals()[f'Parts_Group_{group_letter}'][part_idx]
                  # Build response
                  response_parts = []
                  emojis = ["🌝", "🌚", "🙃", "😇", "😊", "🫡", "", ""]
                
                  if 'location' in info_types: 
                     Is_location_Asked="Yes"
                     location = globals()[f'Part_Location_group_{group_letter}'][part_idx]
                     # Check if location is empty or invalid
                     if not location:  # If location is empty or falsy
                        response_parts.append("عذرا لا أمتلك الصورة ولكنني مازلت أتعلم")
                     else:
                        # Append the main response only if location is valid
                        response_parts.append(f"* (تم إرسال الصورة)*")  #{globals().get(f'Parts_Group_{group_letter}')[part_idx]}*")

                  if 'number' in info_types:
                     Is_number_Asked="Yes"
                     numbers = globals()[f'Parts_numbers_group_{group_letter}'][part_idx]
                     response_parts.append(f"*🔢 رقم القطعة:* {numbers if is_valid_info(str(numbers)) else X}")
                     Random_answer_reply = random.choice(All_Answer_replies)

                  if 'price' in info_types:
                     Is_price_Asked="Yes"
                     prices = globals()[f'Parts_prices_group_{group_letter}'][part_idx]
                     response_parts.append(f"*💰 الأسعار من عدة محلات:* \n{', '.join(map(str, prices)) if is_valid_info(str(prices)) else X}")
                     Random_answer_reply = random.choice(All_Answer_replies)                     

                  if 'tutorial' in info_types:  #vvvv
                     Is_tutorial_Asked="Yes"
                     links = [globals()[f'How_2_Change_{group_letter}_Link{ln}'][part_idx] for ln in range(1, 5)]
                     valid_links = [ln for ln in links if ln and "http" in ln]
                     Random_answer_reply = random.choice(Answer_AS_Lnik)
                     fourth_link = valid_links[3] if len(valid_links) > 3 else None  # Fourth link (if available)
                     # Limit the number of links to 3
                     valid_links = valid_links[:3]  # This ensures only the first 3 links are kept
                     # Format links as clickable text (فديو 1), (فديو 2), etc.
                     formatted_links = [
                        f"[(فديو {i + 1})]({link})" for i, link in enumerate(valid_links)  ]
                     # Combine into the response
                     response_parts.append( "*🎥 فديوهات لطريقة التغيير:*\n📎 " + "\n\n📎 ".join(formatted_links) if valid_links else f"*🎥 فديوهات لطريقة التغيير:*\n{X}"  )
                     # Add the fourth link with a different header (if it exists)
                     if fourth_link:
                        response_parts.append(  "*📌قم بإعادة الضبط  بعد التغيير:*\n📎 [(إضغط لعرض الطريقة)]({})".format(fourth_link) )

                  # Add random emoji (25% chance)
                  if random.random() < 0.25:
                     response_parts += f"{random.choice(emojis)}"

                  # Construct final response
                  if  (Is_price_Asked=="Yes")   and   (Is_number_Asked=="No")  and   (Is_tutorial_Asked=="No")  and  (Is_location_Asked=="No"):
                     if not any(isinstance(item, (int, float)) for item in prices):
                        # If the list is empty or contains no numbers
                        Random_answer_reply = random.choice(Click_Start_replies)
                     else: # If the list contains at least one number
                        Random_answer_reply = random.choice(Answer_Fits_All)                             
                  if  (Is_price_Asked=="No")   and   (Is_number_Asked=="Yes")  and   (Is_tutorial_Asked=="No")  and  (Is_location_Asked=="No"):
                     if not numbers : # if empty or invalid
                           Random_answer_reply = random.choice(Click_Start_replies)
                     else :          # if written
                           Random_answer_reply = random.choice(Answer_Fits_All)
                  if  (Is_price_Asked=="No")   and   (Is_number_Asked=="No")  and   (Is_tutorial_Asked=="No")  and  (Is_location_Asked=="Yes"):
                     if not location : # if empty or invalid
                           Random_answer_reply = random.choice(Click_Start_replies)
                     else :          # if written
                           Random_answer_reply = random.choice(Answer_Fits_All)
                  if  (Is_price_Asked=="No")   and   (Is_number_Asked=="No")  and   (Is_tutorial_Asked=="Yes")  and  (Is_location_Asked=="No"):
                     if links:  # If the first link is not empty 
                        Random_answer_reply = random.choice(Answer_Fits_All)
                     else:      # If the first link is empty 
                        Random_answer_reply = random.choice(Click_Start_replies)


                  Full_response_text =   f"*♻️ تم إعادة تأكيد القطعة\n إخترت: ({part_name})*\n{car_header}\n" + "\n\n".join(response_parts)
                  if 'location' in info_types:  # if location is asked
                     emojis = ["🌝", "🌚","🌝", "🌚", "🙃", "😇", "😊", "🫡", "", ""]
                     picture_path = f"{Pictures_File_Location}{location}.png"
                     try:
                           with open(picture_path, 'rb') as photo:
                              bot.send_photo(
                                 chat_id=call.message.chat.id,
                                 photo=photo,
                                 caption= Full_response_text ,
                                 parse_mode="Markdown",
                                 disable_notification=True,
                                 protect_content=Protect_Content_Switch_K,
                                 reply_to_message_id=call.message.message_id - 1)
                     except FileNotFoundError:
                           # Fallback to voice message if image missing
                           bot.send_voice(
                              voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg', 'rb'),
                              caption= f"{Full_response_text}",
                              chat_id=call.message.chat.id,
                              parse_mode="Markdown",
                              disable_notification=True,
                              protect_content=Protect_Content_Switch_K,
                              reply_to_message_id=call.message.message_id - 1)
                  else:  # Original voice handling for other modes
                        bot.send_voice( chat_id=call.message.chat.id,   voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg', 'rb'), 
                                       caption=Full_response_text, parse_mode="Markdown", disable_notification=True, protect_content=Protect_Content_Switch_K,
                                       reply_to_message_id=call.message.message_id - 1)
                        stop_the_bot=1
                  bot.delete_message(call.message.chat.id, call.message.message_id)                        
                  break
#________________________________________________________________   



            # Handle Parts_Related options
            if call.data == "Parts_Related":
                keyboard = types.InlineKeyboardMarkup(row_width=2)
                btn_pn = types.InlineKeyboardButton("🔢 أرقام القطع", callback_data="mode_pn")
                btn_pp = types.InlineKeyboardButton("💰 أسعار القطع", callback_data="mode_pp")
                btn_pl = types.InlineKeyboardButton("📍 صور وموقع القطع", callback_data="mode_pl")
                btn_ct = types.InlineKeyboardButton("📺 فديو طريقة التغيير", callback_data="mode_ct")
                keyboard.add(btn_pn, btn_pp).add(btn_pl, btn_ct)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=keyboard)
                bot.edit_message_caption(f"*🔧 قطع الغيار* {Pick_one}",        #_________________________
                                           call.message.chat.id, call.message.message_id,parse_mode="Markdown", reply_markup=keyboard)      
                bot.answer_callback_query(call.id)
                return

            # Handle mode selection (pn/pp/pl/ct)
            if call.data.startswith("mode_"):
                mode = call.data.split("_")[1]
                systems = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11]
                
                keyboard = types.InlineKeyboardMarkup()
                buttons = []
                for idx, system in enumerate(systems, 1):
                    buttons.append(types.InlineKeyboardButton(
                        text=system,
                        callback_data=f"system_{mode}_L{idx}"
                    ))

                # Fixed button_order with proper tuple syntax
                button_order = [
                    (1,),     # Single button row (L2)
                    (2,),      # Single button row (L8)
                    (0, 9),    # L1 & L10
                    (4, 3),    # L5 & L4
                    (5, 6),    # L6 & L7
                    (8, 7),    # L9 & L3
                    (10,)      # Single button row (L11)
                ]

                # Add buttons in custom order
                for row_indices in button_order:
                    row_buttons = []
                    for index in row_indices:  # Now iterable
                        try:
                            row_buttons.append(buttons[index])
                        except IndexError:
                            continue
                    if row_buttons:
                        keyboard.row(*row_buttons)

                bot.edit_message_caption(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    caption=f"*القطعة من أي قسم؟*🤔",parse_mode="Markdown",       #_________________________
                    reply_markup=keyboard
                )
                bot.answer_callback_query(call.id)
                return



            # Handle system selection (L1-L11)
            if call.data.startswith("system_"):
                _, mode, system = call.data.split("_")
                system_num = system[1:]
                group = system_to_group.get(system_num, "A")
                
                parts_group = globals()[f"Parts_Group_{group}"]
                keyboard = types.InlineKeyboardMarkup()
                
                # Create all possible buttons (up to 60)
                part_buttons = []
                for idx, part in enumerate(parts_group):
                    if part.strip() and idx < 60:  # Limit to first 30 parts
                        part_buttons.append(
                            types.InlineKeyboardButton(
                                text=part,
                                callback_data=f"part_{mode}_{system}_{idx}"
                            )
                        )

                # Automatically generate button_order with 2 buttons per row
                button_order = [(i, i + 1) for i in range(0, len(part_buttons), 2)]

                # Add buttons with auto-hiding    
                for row in button_order:
                    row_buttons = []
                    for btn_index in row:
                        if btn_index < len(part_buttons):  # Only add if exists
                           row_buttons.append(part_buttons[btn_index])
                    if row_buttons:  # Only add row if has buttons
                       keyboard.row(*row_buttons)
            

                bot.edit_message_caption(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    caption=f"*واخيرا..حددلي القطعة*😌",parse_mode="Markdown",       #__________________________________
                    reply_markup=keyboard
                )
                bot.answer_callback_query(call.id)
                return


            # Handle part selection     
            if call.data.startswith("part_"):
                #_____________________________________________________________________________________________________
                _, mode, system, idx = call.data.split("_")
                idx = int(idx)       # error here this line
                system_num = system[1:]
                group = system_to_group.get(system_num, "A")
                
                # Get headers and part name
                mapped_group = group_mapping.get(group, group)
                group_header_text = group_headers.get(mapped_group, "")
                part_name = globals()[f"Parts_Group_{group}"][idx]
                
                # Build response
                response_text = ""
                emojis = ["🌝", "🌚","🌝", "🌚", "🙃", "😇", "😊", "🫡", "", ""]
                
                if mode == "pn":
                    numbers = globals()[f"Parts_numbers_group_{group}"][idx]
                    response_text = f"*🔢 رقم القطعة:*\n{numbers if is_valid_info(str(numbers)) else X}\n"
                    Random_answer_reply = random.choice(All_Answer_replies)

                elif mode == "pp":
                    prices = globals()[f"Parts_prices_group_{group}"][idx]
                    response_text = f"*💰 الأسعار من عدة محلات:*\n{', '.join(map(str, prices)) if is_valid_info(str(prices)) else X}\n"
                    Random_answer_reply = random.choice(All_Answer_replies)

                elif mode == "pl":
                    location = globals()[f"Part_Location_group_{group}"][idx]
                    response_text = f"*📍 موقع القطعة:*\n{location if is_valid_info(str(location)) else X}\n"
                    Random_answer_reply = random.choice(All_Answer_replies)

                elif (mode == "ct") or ( call.data== "part_cp_L9_8")  or (call.data== "part_cp_L9_9")  or ( call.data==  "part_cp_L9_10" ) :   
                    links = [globals()[f"How_2_Change_{group}_Link{ln}"][idx] for ln in range(1,5)]
                    valid_links = [link for link in links if link and "http" in link]
                    Random_answer_reply = random.choice(Answer_AS_Lnik)
                    fourth_link = valid_links[3] if len(valid_links) > 3 else None  # Fourth link (if available)   vvvv
                    # Limit the number of links to 3
                    valid_links = valid_links[:3]  # This ensures only the first 3 links are kept
                    # Format links as clickable text (فديو 1), (فديو 2), etc.
                    formatted_links = [
                         f"[(فديو {i + 1})]({link})" for i, link in enumerate(valid_links)  ]
                    # Combine into the response
                    if valid_links:
                      response_text += "*🎥 فديوهات لطريقة التغيير:*\n📎 " + "\n\n📎 ".join(formatted_links) + "\n"
                    else:
                      response_text += f"*🎥 فديوهات لطريقة التغيير:*\n{X}"
                  
                    # Add the fourth link with a different header (if it exists)
                    if fourth_link:
                      response_text += "\n*📌قم بإعادة الضبط  بعد التغيير:*\n📎 [(إضغط لعرض الطريقة)]({})\n".format(fourth_link)








                # Add random emoji (25% chance)
                if random.random() < 0.25:
                    response_text += f"\n\n{random.choice(emojis)}"

                # Construct final caption
                full_caption = f"{car_header}\n.........................\n\n*🔧 القطعة: {part_name}*\n\n{response_text}"  
                if mode == "pl":  # if location is asked
                    emojis = ["🌝", "🌚","🌝", "🌚", "🙃", "😇", "😊", "🫡", "", ""]
                    picture_path = f"{Pictures_File_Location}{location}.png"
                    try:
                        with open(picture_path, 'rb') as photo:
                            bot.send_photo(
                                chat_id=call.message.chat.id,
                                photo=photo,
                                caption= f"{car_header}\n\n*هذا موقع وصورة القطعة* {random.choice(emojis)}"  ,
                                parse_mode="Markdown",
                                disable_notification=True,
                                protect_content=Protect_Content_Switch_K,
                                reply_to_message_id=call.message.message_id - 1)
                    except FileNotFoundError:
                        # Fallback to voice message if image missing
                        Random_answer_reply = random.choice(Click_Start_replies)
                        bot.send_voice(
                            voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg', 'rb'),
                            caption= f"{X}",
                            chat_id=call.message.chat.id,
                            parse_mode="Markdown",
                            disable_notification=True,
                            protect_content=Protect_Content_Switch_K,
                            reply_to_message_id=call.message.message_id - 1)
                else:  # Original voice handling for other modes
                     bot.send_voice( chat_id=call.message.chat.id,   voice=open(f'{Sound_File_Location}{Random_answer_reply}.ogg', 'rb'), 
                                     caption=full_caption, parse_mode="Markdown", disable_notification=True, protect_content=Protect_Content_Switch_K,
                                     reply_to_message_id=call.message.message_id - 1)
                     stop_the_bot=1
                bot.delete_message(call.message.chat.id, call.message.message_id)
                break
                
                    


# _______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# CCCC إذا تم إختيار (بحث الفيوز حسب الموديل)الازارير الجديدة تحت تمثل كل موديل 
       for element in  ClickC  :
           if   (element == call.data)  and  (element !="") :      
                Random_wait_reply  = random.choice(wait_replies_C) ; Random_answer_reply= random.choice(Answer_replies_C)
                if  call.data=="clickC" :     
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    bottonC1 =types.InlineKeyboardButton(text= C1 ,callback_data='clickC1')
                    bottonC2 =types.InlineKeyboardButton(text= C2 ,callback_data='clickC2')
                    bottonC3 =types.InlineKeyboardButton(text= C3 ,callback_data='clickC3')
                    bottonC4 =types.InlineKeyboardButton(text= C4 ,callback_data='clickC4')
                    bottonC5 =types.InlineKeyboardButton(text= C5 ,callback_data='clickC5')
                    bottonC6 =types.InlineKeyboardButton(text= C6 ,callback_data='clickC6')
                    bottonC7 =types.InlineKeyboardButton(text= C7 ,callback_data='clickC7')
                    bottonC8 =types.InlineKeyboardButton(text= C8 ,callback_data='clickC8')
                    bottonC9 =types.InlineKeyboardButton(text= C9 ,callback_data='clickC9')
                    botton_Return=types.InlineKeyboardButton(text= Main_Return ,callback_data='botton_Return')
                    keyboard.add(bottonC1,bottonC2,bottonC3).add(bottonC4,bottonC5,bottonC6).add(bottonC7,bottonC8,bottonC9)#.add(botton_Return)
                    bot.edit_message_caption(f"({C}){Pick_model}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard)        
                    break
                # C1 C2 C3 2010-2012 هنا خيارات فيوزات 
                if  call.data=="clickC1"  or  call.data=="clickC2"   or call.data=="clickC3" :
                    if call.data=="clickC1" : Model="2010" 
                    if call.data=="clickC2" : Model="2011"
                    if call.data=="clickC3" : Model="2012"  
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    bottonN5_55=types.InlineKeyboardButton(text="السلف",callback_data='clickN5_55')
                    bottonN9=types.InlineKeyboardButton(text="مساحات",callback_data='clickN9')
                    bottonN17=types.InlineKeyboardButton(text="الدنمو",callback_data='clickN17')
                    bottonN22=types.InlineKeyboardButton(text="مدخل طاقة 1",callback_data='clickN22')
                    bottonN25_43=types.InlineKeyboardButton(text="كومبرسر",callback_data='clickN25_43')
                    bottonN28=types.InlineKeyboardButton(text="مراوح رديتر",callback_data='clickN28')
                    bottonN29=types.InlineKeyboardButton(text="مدخل ولاعة",callback_data='clickN29')
                    bottonN31=types.InlineKeyboardButton(text="كرسي الراكب",callback_data='clickN31')
                    bottonN32=types.InlineKeyboardButton(text="كرسي السائق",callback_data='clickN32')
                    bottonN35_52=types.InlineKeyboardButton(text="مروحة مكيف",callback_data='clickN35_52')
                    bottonN36=types.InlineKeyboardButton(text="طرمبة البنزين",callback_data='clickN36')
                    bottonN41=types.InlineKeyboardButton(text="ريووس",callback_data='clickN41')
                    bottonN48=types.InlineKeyboardButton(text="كويلات",callback_data='clickN48')
                    bottonP1=types.InlineKeyboardButton(text="زجاج السائق",callback_data='clickP1')
                    bottonP2=types.InlineKeyboardButton(text="لمبة فرامل الوسط",callback_data='clickP2')
                    bottonP4=types.InlineKeyboardButton(text="زجاج الراكب",callback_data='clickP4')
                    bottonP6=types.InlineKeyboardButton(text="اشارة وفرامل",callback_data='clickP6')
                    bottonP7=types.InlineKeyboardButton(text="واطي يسار",callback_data='clickP7')
                    bottonP8=types.InlineKeyboardButton(text="واطي يمين",callback_data='clickP8')
                    bottonP9=types.InlineKeyboardButton(text="الشماسة",callback_data='clickP9')
                    bottonP10=types.InlineKeyboardButton(text="خلفية ومرايات",callback_data='clickP10')
                    bottonP12=types.InlineKeyboardButton(text="مرايات خارجية",callback_data='clickP12')
                    bottonP13=types.InlineKeyboardButton(text="نظام سينك",callback_data='clickP13')
                    bottonP14=types.InlineKeyboardButton(text="راديو وشاشة وازرار المكيف",callback_data='clickP14')
                    bottonP15=types.InlineKeyboardButton(text="نظام التكييف",callback_data='clickP15')
                    bottonP17=types.InlineKeyboardButton(text="قفل أبواب-شنطة",callback_data='clickP17')
                    bottonP21=types.InlineKeyboardButton(text="الضباب",callback_data='clickP21')
                    bottonP22=types.InlineKeyboardButton(text="نعاس ولوحة",callback_data='clickP22')
                    bottonP23=types.InlineKeyboardButton(text="العالي",callback_data='clickP23')
                    bottonP24=types.InlineKeyboardButton(text="البوري",callback_data='clickP24')
                    bottonP27=types.InlineKeyboardButton(text="سوتش مفتاح",callback_data='clickP27')
                    bottonP32=types.InlineKeyboardButton(text="الايرباق",callback_data='clickP32')
                    bottonP39=types.InlineKeyboardButton(text="الراديو",callback_data='clickP39')
                    bottonP41=types.InlineKeyboardButton(text="داخلية",callback_data='clickP41')
                    bottonP47=types.InlineKeyboardButton(text="نوافذ الزجاج",callback_data='clickP47')
                    bottonSECTION=types.InlineKeyboardButton(text="\U0001f4a1  \U00002B07 إضائة ولمبات \U00002B07  \U0001f4a1",callback_data='bottonSECTION')
                    Fuses_Return_Button=types.InlineKeyboardButton(text= Fuses_Return ,callback_data='clickC')
                    keyboard.add(Fuses_Return_Button).add(bottonN28,bottonN17,bottonN36).add(bottonN48,bottonP32,bottonN9).add(bottonN5_55,bottonP27,bottonP24).add(bottonN25_43,bottonN35_52,bottonP15).add(bottonN29,bottonN22,bottonP39).add(bottonP1,bottonP47,bottonP4).add(bottonN32,bottonP13,bottonN31).add(bottonP17,bottonP12).add(bottonP14).add(bottonSECTION).add(bottonP2,bottonP41).add(bottonP7,bottonP23,bottonP8).add(bottonP21,bottonN41,bottonP6).add(bottonP10,bottonP22,bottonP9)
                    bot.edit_message_caption( f"مواقع الفيوزات\nفيوجن {Model}{Pick_one}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard)       
                    break
                # C4   2014  هنا خيارات كل فيوزات
                if  call.data=="clickC4"  :
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    bottonX1=types.InlineKeyboardButton(text="مساحة يمين",callback_data='clickX1')
                    bottonX2_84=types.InlineKeyboardButton(text="السلف",callback_data='clickX2_84')
                    bottonX4_79=types.InlineKeyboardButton(text="مروحة مكيف",callback_data='clickX4_79')
                    bottonX5=types.InlineKeyboardButton(text="مدخل طاقة 2",callback_data='clickX5')
                    bottonX10=types.InlineKeyboardButton(text="مدخل ولاعة",callback_data='clickX10')
                    bottonX11=types.InlineKeyboardButton(text="كويلات",callback_data='clickX11')
                    bottonX12=types.InlineKeyboardButton(text="الشتر",callback_data='clickX12')
                    bottonX16=types.InlineKeyboardButton(text="مدخل طاقة 1",callback_data='clickX16')
                    bottonX22_33_12=types.InlineKeyboardButton(text="كومبروسر",callback_data='clickX22_33_12')
                    bottonX40_56=types.InlineKeyboardButton(text="طرمبة بنزين",callback_data='clickX40_56')
                    bottonX41_48=types.InlineKeyboardButton(text="البوري",callback_data='clickX41_48')
                    bottonX46=types.InlineKeyboardButton(text="الدنمو",callback_data='clickX46')
                    bottonX47=types.InlineKeyboardButton(text="لمبات فرامل",callback_data='clickX47')
                    bottonX68=types.InlineKeyboardButton(text="زجاج خلفي",callback_data='clickX68')
                    bottonX70=types.InlineKeyboardButton(text="كرسي الراكب",callback_data='clickX70')
                    bottonX74=types.InlineKeyboardButton(text="كرسي السائق",callback_data='clickX74')
                    bottonX83=types.InlineKeyboardButton(text="مساحة يسار",callback_data='clickX83')
                    bottonM1=types.InlineKeyboardButton(text="إضائة الداخلية",callback_data='clickM1')
                    bottonM3=types.InlineKeyboardButton(text="قفل باب يسار",callback_data='clickM3')
                    bottonM5=types.InlineKeyboardButton(text="مكبر الصوت",callback_data='clickM5')
                    bottonM10=types.InlineKeyboardButton(text="دخول بالرمز",callback_data='clickM10')
                    bottonM12=types.InlineKeyboardButton(text="لوحة الشاشة",callback_data='clickM12')
                    bottonM16=types.InlineKeyboardButton(text="قفل شنطة",callback_data='clickM16')
                    bottonM18=types.InlineKeyboardButton(text="سويتش مفتاح",callback_data='clickM18')
                    bottonM24=types.InlineKeyboardButton(text="قفل مركزي",callback_data='clickM24')
                    bottonM25=types.InlineKeyboardButton(text="تحكم باب السائق",callback_data='clickM25')
                    bottonM26=types.InlineKeyboardButton(text="تحكم باب الراكب",callback_data='clickM26')
                    bottonM29=types.InlineKeyboardButton(text="تحكم باب خلف يسار",callback_data='clickM29')
                    bottonM30=types.InlineKeyboardButton(text="تحكم باب خلف يمين",callback_data='clickM30')
                    bottonM32=types.InlineKeyboardButton(text="نظام الترفية",callback_data='clickM32')
                    bottonM33=types.InlineKeyboardButton(text="نظام الصوت",callback_data='clickM33')
                    bottonM35=types.InlineKeyboardButton(text="ايرباق",callback_data='clickM35')
                    Fuses_Return_Button=types.InlineKeyboardButton(text= Fuses_Return ,callback_data='clickC')
                    keyboard.add(Fuses_Return_Button).add(bottonX2_84,bottonX40_56,bottonX46).add(bottonX11,bottonX41_48,bottonX47).add(bottonX4_79,bottonX22_33_12,bottonX12).add(bottonX83,bottonX68,bottonX1).add(bottonX5,bottonX16,bottonX10).add(bottonM18,bottonM10,bottonM35).add(bottonM5,bottonM32,bottonM33).add(bottonM1,bottonM12).add(bottonX74,bottonX70).add(bottonM25,bottonM26).add(bottonM29,bottonM30).add(bottonM3,bottonM16,bottonM24)
                    bot.edit_message_caption( f"مواقع الفيوزات\n فيوجن 2014{Pick_one}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard)             
                    break
                # C5 C6 C7 C8 C9  هنا خيارات كل فيوزات 2015-2019
                if  call.data=="clickC5"  or call.data=="clickC6"  or  call.data=="clickC7"   or call.data=="clickC8"   or  call.data=="clickC9" :
                    if call.data=="clickC5" : Model="2015" 
                    if call.data=="clickC6" : Model="2016"
                    if call.data=="clickC7" : Model="2017"
                    if call.data=="clickC8" : Model="2018" 
                    if call.data=="clickC9" : Model="2019" 
                    keyboard = types.InlineKeyboardMarkup()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                    bottonX2_84=types.InlineKeyboardButton(text="السلف",callback_data='clickX2_84')
                    bottonX4_79=types.InlineKeyboardButton(text="مروحة مكيف",callback_data='clickX4_79')
                    bottonX5=types.InlineKeyboardButton(text="مدخل طاقة 2",callback_data='clickX5')
                    bottonX10=types.InlineKeyboardButton(text="مدخل ولاعة",callback_data='clickX10')
                    bottonX11=types.InlineKeyboardButton(text="كويلات",callback_data='clickX11')
                    bottonX12=types.InlineKeyboardButton(text="الشتر",callback_data='clickX12')
                    bottonX16=types.InlineKeyboardButton(text="مدخل طاقة 1",callback_data='clickX16')
                    bottonX22_33_12=types.InlineKeyboardButton(text="كومبروسر",callback_data='clickX22_33_12')
                    bottonX42_58=types.InlineKeyboardButton(text="طرمبة بنزين",callback_data='clickX42_58')
                    bottonX40_50=types.InlineKeyboardButton(text="البوري",callback_data='clickX40_50')
                    bottonX54=types.InlineKeyboardButton(text="لمبات فرامل",callback_data='clickX54')
                    bottonX68=types.InlineKeyboardButton(text="زجاج خلفي",callback_data='clickX68')
                    bottonX70=types.InlineKeyboardButton(text="كرسي الراكب",callback_data='clickX70')
                    bottonX74=types.InlineKeyboardButton(text="كرسي السائق",callback_data='clickX74')
                    bottonX75=types.InlineKeyboardButton(text="مساحة يسار",callback_data='clickX75')
                    bottonX80=types.InlineKeyboardButton(text="مساحة يمين",callback_data='clickX80')
                    bottonM1=types.InlineKeyboardButton(text="إضائة الداخلية",callback_data='clickM1')
                    bottonM3=types.InlineKeyboardButton(text="قفل باب يسار",callback_data='clickM3')
                    bottonM5=types.InlineKeyboardButton(text="مكبر الصوت",callback_data='clickM5')
                    bottonM10=types.InlineKeyboardButton(text="دخول بالرمز",callback_data='clickM10')
                    bottonM12=types.InlineKeyboardButton(text="لوحة الشاشة",callback_data='clickM12')
                    bottonM16=types.InlineKeyboardButton(text="قفل شنطة",callback_data='clickM16')
                    bottonM18=types.InlineKeyboardButton(text="سويتش مفتاح",callback_data='clickM18')
                    bottonM24_2015=types.InlineKeyboardButton(text="قفل مركزي",callback_data='clickM24_2015')
                    bottonM25=types.InlineKeyboardButton(text="تحكم باب السائق",callback_data='clickM25')
                    bottonM26=types.InlineKeyboardButton(text="تحكم باب الراكب",callback_data='clickM26')
                    bottonM29=types.InlineKeyboardButton(text="تحكم باب خلف يسار",callback_data='clickM29')
                    bottonM30=types.InlineKeyboardButton(text="تحكم باب خلف يمين",callback_data='clickM30')
                    bottonM32=types.InlineKeyboardButton(text="نظام الترفية",callback_data='clickM32')
                    bottonM33=types.InlineKeyboardButton(text="نظام الصوت",callback_data='clickM33')
                    bottonM35=types.InlineKeyboardButton(text="ايرباق",callback_data='clickM35')
                    Fuses_Return_Button=types.InlineKeyboardButton(text= Fuses_Return ,callback_data='clickC')
                    keyboard.add(Fuses_Return_Button).add(bottonX2_84,bottonX42_58).add(bottonX11,bottonX40_50,bottonX54).add(bottonX4_79,bottonX22_33_12,bottonX12).add(bottonX75,bottonX68,bottonX80).add(bottonX5,bottonX16,bottonX10).add(bottonM18,bottonM10,bottonM35).add(bottonM5,bottonM32,bottonM33).add(bottonM1,bottonM12).add(bottonX74,bottonX70).add(bottonM25,bottonM26).add(bottonM29,bottonM30).add(bottonM3,bottonM16,bottonM24_2015)
                    bot.edit_message_caption( f"مواقع الفيوزات\nفيوجن {Model}{Pick_one}",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard) 
                    break
                # هنا الردود لكل فيوز
                #  مواقع الفيوزات 2014-2020 
                if call.data=="clickX1":
                   ref_f="X1.png"            ; Model_f="2013-2019"; fuse="المساحة اليمين"
                if call.data=="clickX2_84":
                   ref_f="X2_84.png"         ; Model_f="2013-2019"; fuse="السلف"
                if call.data=="clickX4_79":
                   ref_f="X4_79.png"         ; Model_f="2013-2019"; fuse="مروحة المكيف"
                if call.data=="clickX5":
                   ref_f="X5.png"            ; Model_f="2013-2019"; fuse="مدخل الطاقة 2"
                if call.data=="clickX10":
                   ref_f="X10.png"           ; Model_f="2013-2019"; fuse="مدخل الولاعة"
                if call.data=="clickX11":
                   ref_f="X11.png"           ; Model_f="2013-2019"; fuse="الكويلات"
                if call.data=="clickX12":
                   ref_f="X12.png"           ; Model_f="2013-2019"; fuse="الشتر"
                if call.data=="clickX16":
                   ref_f="X16.png"           ; Model_f="2013-2019"; fuse="مدخل الطاقة 1"
                if call.data=="clickX22_33_12":
                   ref_f="X22_33_12.png"     ; Model_f="2013-2019"; fuse="الكومبروسر"
                if call.data=="clickX40_56":
                   ref_f="40_56.png"         ; Model_f="2013-2019"; fuse="طرمبة البنزين"
                if call.data=="clickX41_48":
                   ref_f="X41_48.png"        ; Model_f="2013-2019"; fuse="البوري"
                if call.data=="clickX46":
                   ref_f="X46.png"           ; Model_f="2013-2019"; fuse="الدنمو"
                if call.data=="clickX47":
                   ref_f="X47.png"           ; Model_f="2013-2019"; fuse="لمبات الفرامل"
                if call.data=="clickX68":
                   ref_f="X68.png"           ; Model_f="2013-2019"; fuse="الزجاج الخلفي"
                if call.data=="clickX70":
                   ref_f="X70.png"           ; Model_f="2013-2019"; fuse="كرسي الراكب"
                if call.data=="clickX74":
                   ref_f="X74.png"           ; Model_f="2013-2019"; fuse="كرسي السائق"
                if call.data=="clickX83":
                   ref_f="X83.png"           ; Model_f="2013-2019"; fuse="المساحة اليسار"
                # internal fuse box                                   #
                if call.data=="clickM1":
                   ref_f="M1.png"            ; Model_f="2013-2019"; fuse="إضائة الداخلية"
                if call.data=="clickM3":
                   ref_f="M3.png"            ; Model_f="2013-2019"; fuse="قفل الباب اليسار"
                if call.data=="clickM5":
                   ref_f="M5.png"            ; Model_f="2013-2019"; fuse="مكبر الصوت"
                if call.data=="clickM10":
                   ref_f="M10.png"           ; Model_f="2013-2019"; fuse="دخول بالرمز"
                if call.data=="clickM12":
                   ref_f="M12.png"           ; Model_f="2013-2019"; fuse="لوحة الشاشة"
                if call.data=="clickM16":
                   ref_f="M16.png"           ; Model_f="2013-2019"; fuse="قفل الشنطة"
                if call.data=="clickM18":
                   ref_f="M18.png"           ; Model_f="2013-2019"; fuse="سويتش المفتاح"
                if call.data=="clickM24":
                   ref_f="M24.png"           ; Model_f="2013-2019"; fuse="القفل المركزي"
                if call.data=="clickM25":
                   ref_f="M25.png"           ; Model_f="2013-2019"; fuse="وحدة تحكم باب السائق"
                if call.data=="clickM26":
                   ref_f="M26.png"           ; Model_f="2013-2019"; fuse="وحدة تحكم باب الراكب"
                if call.data=="clickM29":
                   ref_f="M29.png"           ; Model_f="2013-2019"; fuse="وحدة تحكم باب خلف يسار"
                if call.data=="clickM30":
                   ref_f="M30.png"           ; Model_f="2013-2019"; fuse="وحدة تحكم باب خلف يمين"
                if call.data=="clickM32":
                   ref_f="M32.png"           ; Model_f="2013-2019"; fuse="نظام الترفية"
                if call.data=="clickM33":
                   ref_f="M33.png"           ; Model_f="2013-2019"; fuse="نظام الصوت"
                if call.data=="clickM35":
                   ref_f="M35.png"           ; Model_f="2013-2019"; fuse="نظام الإيرباق"
                #those who are different between models                                  #
                if call.data=="clickX42_58":
                   ref_f="X42.png"           ; Model_f="2015-2019"; fuse="طرمبة البنزين"
                if call.data=="clickX54":      #"لمبات فرامل"
                   ref_f="X54.png"           ; Model_f="2015-2019"; fuse="لمبات الفرامل"
                if call.data=="clickX40_50":   # البوري
                   ref_f="X40_50.png"        ; Model_f="2015-2019"; fuse="البوري"
                if call.data=="clickM24_2015": #"قفل مركزي"
                   ref_f="M24_2015.png"      ; Model_f="2015-2019"; fuse="القفل المركزي"
         
                # ANSWER FOR 2010-2012                                                    #
                if call.data=="clickN5_55":
                   ref_f="N5_55.png"         ; Model_f="2009-2012"; fuse="السلف"
                if call.data=="clickN9":
                   ref_f="N9.png"            ; Model_f="2009-2012"; fuse="مساحات"
                if call.data=="clickN17":
                   ref_f="N17.png"           ; Model_f="2009-2012"; fuse="الدنمو"
                if call.data=="clickN22": 
                   ref_f="N22.png"           ; Model_f="2009-2012"; fuse="مدخل طاقة 1"
                if call.data=="clickN25_43":
                   ref_f="N25_43.png"        ; Model_f="2009-2012"; fuse="كومبرسر"
                if call.data=="clickN28":
                   ref_f="N28.png"           ; Model_f="2009-2012"; fuse="مراوح رديتر"
                if call.data=="clickN29":
                   ref_f="N29.png"           ; Model_f="2009-2012"; fuse="مدخل ولاعة"
                if call.data=="clickN31":
                   ref_f="N31.png"           ; Model_f="2009-2012"; fuse="كرسي الراكب"
                if call.data=="clickN32":
                   ref_f="N32.png"           ; Model_f="2009-2012"; fuse="كرسي السائق"
                if call.data=="clickN35_52":
                   ref_f="N35_52.png"        ; Model_f="2009-2012"; fuse="مروحة مكيف"
                if call.data=="clickN36":
                   ref_f="N36.png"           ; Model_f="2009-2012"; fuse="طرمبة البنزين"
                if call.data=="clickN41":
                   ref_f="N41.png"           ; Model_f="2009-2012"; fuse="ريووس"
                if call.data=="clickN48":
                   ref_f="N48.png"           ; Model_f="2009-2012"; fuse="كويلات"
                if call.data=="clickP1":
                   ref_f="P1.png"            ; Model_f="2009-2012"; fuse="زجاج السائق"
                if call.data=="clickP2":
                   ref_f="P2.png"            ; Model_f="2009-2012"; fuse="لمبة فرامل الوسط"
                if call.data=="clickP4":
                   ref_f="P4.png"            ; Model_f="2009-2012"; fuse="زجاج الراكب"
                if call.data=="clickP6":
                   ref_f="P6.png"            ; Model_f="2009-2012"; fuse="اشارة وفرامل"
                if call.data=="clickP7":
                   ref_f="P7.png"            ; Model_f="2009-2012"; fuse="واطي يسار"
                if call.data=="clickP8":
                   ref_f="P8.png"            ; Model_f="2009-2012"; fuse="واطي يمين"
                if call.data=="clickP9":
                   ref_f="P9.png"            ; Model_f="2009-2012"; fuse="الشماسة"
                if call.data=="clickP10":
                   ref_f="P10.png"           ; Model_f="2009-2012"; fuse="خلفية ومرايات"
                if call.data=="clickP12":
                   ref_f="P12.png"           ; Model_f="2009-2012"; fuse="مرايات خارجية"
                if call.data=="clickP13":
                   ref_f="P13.png"           ; Model_f="2009-2012"; fuse="نظام سينك"
                if call.data=="clickP14":
                   ref_f="P14.png"           ; Model_f="2009-2012"; fuse="راديو وشاشة وازرار المكيف"
                if call.data=="clickP15":
                   ref_f="P15.png"           ; Model_f="2009-2012"; fuse="نظام التكييف"
                if call.data=="clickP17":
                   ref_f="P17.png"           ; Model_f="2009-2012"; fuse="قفل أبواب-شنطة"
                if call.data=="clickP21":
                   ref_f="P21.png"           ; Model_f="2009-2012"; fuse="الضباب"
                if call.data=="clickP22":
                   ref_f="P22.png"           ; Model_f="2009-2012"; fuse="نعاس ولوحة"
                if call.data=="clickP23":
                   ref_f="P23.png"           ; Model_f="2009-2012"; fuse="العالي"
                if call.data=="clickP24":
                   ref_f="P24.png"           ; Model_f="2009-2012"; fuse="البوري"
                if call.data=="clickP27":
                   ref_f="P27.png"           ; Model_f="2009-2012"; fuse="سوتش مفتاح"
                if call.data=="clickP32":
                   ref_f="P32.png"           ; Model_f="2009-2012"; fuse="الايرباق"
                if call.data=="clickP39":
                   ref_f="P39.png"           ; Model_f="2009-2012"; fuse="الراديو"
                if call.data=="clickP41":
                   ref_f="P41.png"           ; Model_f="2009-2012"; fuse="داخلية"
                if call.data=="clickP47":
                   ref_f="P47.png"           ; Model_f="2009-2012"; fuse="نوافذ الزجاج" 
                bot.delete_message(call.message.chat.id, ((call.message.message_id)) )
                bot.send_photo(call.message.chat.id, photo=open(f'{Pictures_File_Location}{ref_f}', 'rb'),   caption=f"{Fuse_finder_reply}\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch_Fuses, reply_to_message_id= (call.message.message_id) -1 )


#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


 #  ALL SPECIFICATIONS  "مواصفات فنية وصيانة"
       if call.message:
          if call.data=="clickU": 
             last_Click = now
             time.sleep(Ckick_Sleep)
             keyboard = types.InlineKeyboardMarkup()
             bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
             bottonU1 =types.InlineKeyboardButton(text= U1 ,callback_data='clickU1') #"لمحرك"
             bottonU2 =types.InlineKeyboardButton(text= U2 ,callback_data='clickU2') #"القير"
             bottonU3 =types.InlineKeyboardButton(text= U3 ,callback_data='clickU3') #"الفرامل"
             bottonU4 =types.InlineKeyboardButton(text= U4 ,callback_data='clickU4') #"بطارية - مولد" 
             bottonU5 =types.InlineKeyboardButton(text= U5 ,callback_data='clickU5') #"نظام التكييف"
             bottonU6 =types.InlineKeyboardButton(text= U6 ,callback_data='clickU6') #"نظام التبرييد"
             bottonU7 =types.InlineKeyboardButton(text= U7 ,callback_data='clickU7') #"نظام الوقود"
             bottonU8 =types.InlineKeyboardButton(text= U8 ,callback_data='clickU8') #"نظام التشغيل"
             bottonU9 =types.InlineKeyboardButton(text= U9 ,callback_data='clickU9') #"نظام التعليق"
             bottonU10=types.InlineKeyboardButton(text= U10,callback_data='clickU10') #"بواجي"
             bottonU11=types.InlineKeyboardButton(text= U11,callback_data='clickU11') #"Lug nut torqe"
             bottonU12=types.InlineKeyboardButton(text= U12,callback_data='clickU12') #"Relays - testing"
             botton_Return=types.InlineKeyboardButton(text= Main_Return ,callback_data='botton_Return')
             keyboard.add(bottonU1,bottonU2,bottonU3).add(bottonU4,bottonU5,bottonU6).add(bottonU7,bottonU8,bottonU9).add(bottonU10).add(bottonU11,bottonU12)#.add(botton_Return)
             bot.edit_message_caption(f"({U})\n\n...",call.message.chat.id, (call.message.message_id ), reply_markup=keyboard) 
          if call.data=="clickU1":  #لمحرك
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\Specifications - Engine - engine oil.pdf", 'rb'), caption= f"{Signature}\n\n({U})-({U1})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
          if call.data=="clickU2":  #القير
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\Specifications - Automatic Transmission.pdf", 'rb'), caption= f"{Signature}\n\n({U})-({U2})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
          if call.data=="clickU3":  #الفرامل
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\Specifications - Brake System.pdf", 'rb'), caption= f"{Signature}\n\n({U})-({U3})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
          if call.data=="clickU4":  ##"بطارية - مولد"
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\Alternator Specifications.png", 'rb'), caption= f"{Signature}\n\n({U})-({U4})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
          if call.data=="clickU5":  #نظام التكييف"
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\Specifications - Climate Control System.pdf", 'rb'), caption= f"{Signature}\n\n({U})-({U5})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
          if call.data=="clickU6":  #نظام التبرييد"
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\Specifications - Cooling system.pdf", 'rb'), caption= f"{Signature}\n\n({U})-({U6})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
          if call.data=="clickU7":  #نظام الوقود"
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\Fuel System - specifications - 2.5L Duratec  125kW -170PS.pdf", 'rb'), caption= f"{Signature}\n\n({U})-({U7})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
          if call.data=="clickU8":  #"نظام التشغيل"
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\Specifications - Starting System.pdf", 'rb'), caption= f"{Signature}\n\n({U})-({U8})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
          if call.data=="clickU9":  #نظام التعليق"
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\Specifications - suspension.pdf", 'rb'), caption= f"{Signature}\n\n({U})-({U9})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
          if call.data=="clickU10":  #بواجي
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\Specifications - Ignition.pdf", 'rb'), caption= f"{Signature}\n\n({U})-({U10})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
          if call.data=="clickU11":  #"Lug nut torqe"
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.edit_message_caption(f"{Signature}\n\n({U}) - ({U11})\U00002714\n......................\n 135 Nm\n100 ft ibs\n\n{Put_At_End_Of_Message}",call.message.chat.id, ((call.message.message_id)))
          if call.data=="clickU12":  #"Relays - testing"
             last_Click = now
             time.sleep(Ckick_Sleep)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\relay test 1.png", 'rb'), caption= f"{Signature}\n\n({U})-({U12})\U00002714\n......................\n\n{Put_At_End_Of_Message}", disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\relay test 2.png", 'rb'), caption=None , disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)
             bot.send_photo(call.message.chat.id, photo=open("C:\\Users\\Engmu\\OneDrive\Desktop\\ALL PARTS\\relay test 3.png", 'rb'), caption=None , disable_notification=True,protect_content=Protect_Content_Switch, reply_to_message_id=call.message.message_id -1)

               # add later Protect_Content_Switch_U
#_________________________________________________________________________________________________________


# WWWW Manuals and references
      # Handle folder and PDF navigation if "clickW" is pressed
     
      # Decode the callback_data to get the full path
    # Combine all conditions into a single if statement
    
          if call.data == 'clickW':

            if call.data == 'clickW':
               path = START_FOLDER_PATH  # Start from the predefined folder path
            else:
               try:
                     # Decode the path from the callback data
                     path = decode_path(call.data)
               except:
                     bot.send_message(call.message.chat.id, "Invalid selection.")
                     return

            # Check if it's a directory or a PDF file
            if os.path.isdir(path):
               items = list_folders(path) + list_files(path)
               
               if items:
                     keyboard = create_keyboard(items, path)
                     bot.edit_message_reply_markup(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        reply_markup=keyboard
                     )
               else:
                     bot.send_message(call.message.chat.id, "No items found in this folder.")
            elif os.path.isfile(path) and path.endswith('.pdf'):
               with open(path, 'rb') as pdf_file:
                     bot.send_document(call.message.chat.id, pdf_file)

#____________________________________________________________________________________________________________



#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________




#server()
bot.infinity_polling(timeout=30, long_polling_timeout = 30)

# python main.py  
