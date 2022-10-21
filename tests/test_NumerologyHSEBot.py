import unittest

import telebot

from NumerologyHSEBot import find_num
from NumerologyHSEBot import check_date
from NumerologyHSEBot import start
from NumerologyHSEBot import number_fate
from NumerologyHSEBot import number_soul
from NumerologyHSEBot import number_year
from NumerologyHSEBot import zodiac
from NumerologyHSEBot import get_text_messages

class user:
        id = 487495212
        is_bot = False
        first_name ='Анастасия'
        username = 'aniiisimovaaa'
        last_name = None
        language_code = 'ru'
        can_join_groups = None
        can_read_all_group_messages = None
        supports_inline_queries = None
        is_premium = None
        added_to_attachment_menu = None

class chat:
        id = 487495212
        type = 'private'
        title = None
        username = 'aniiisimovaaa'
        first_name = 'Анастасия'
        last_name = None
        photo = None
        bio = None
        join_to_send_messages = None
        join_by_request = None
        has_private_forwards = None
        has_restricted_voice_and_video_messages = None
        description = None
        invite_link = None
        pinned_message = None
        permissions = None
        slow_mode_delay = None
        message_auto_delete_time = None
        has_protected_content = None
        sticker_set_name = None
        can_set_sticker_set = None
        linked_chat_id = None
        location = None

message = telebot.types.Message(0, user, 0, chat, '', [], '')

class MyTestCase(unittest.TestCase):
    def test_number_fate(self):
        self.assertEqual(number_fate(message, "01.01.2133"), "Неспроста двойка символизирует противоречие противоположностей — обладателям этого числа жизненного пути регулярно приходится бороться с перепадами настроения и даже депрессией, но в то же время вы добры и сердечны. Несмотря на разносторонние таланты, семейные ценности и забота о близких всегда будут для вас в приоритете. Вы умеете смекалисто и быстро разрешать конфликты, а в работе — справляться с любыми трудностями. Поскольку вам свойственно залипать на чужих интересах, почаще вспоминайте, что заботиться надо и о себе.")
        self.assertEqual(number_fate(message, "01.01.2000"), "Четверка воплощает собой целостность — недаром квадрат имеет четыре угла, а знаки зодиака делятся на четыре стихии. Люди с этим числом жизненного пути обладают проницательным умом, впечатляющим даром организатора и неизменно полагаются на логику. Из-за пунктуальности, методичности и прямой манеры высказываться вас часто воспринимают как персонажа с жестким характером, но внутренняя гармония и спокойный нрав обеспечивают вам верных друзей и стабильные отношения.")
        self.assertEqual(number_fate(message, "01.10.2010"),"Вы — выдающийся оратор, умеете расположить к себе любого собеседника или мотивировать команду. Вам присущи гибкость в общении, открытость, доброжелательность. Обладатели числа жизненного пути 5 любят свободу и обожают приключения, стараясь по возможности игнорировать повседневную рутину и долгосрочные обязательства. Очевидные для вас приоритеты усложняют отношения с родственниками, партнерами и коллегами, но на такого харизматика, как вы, просто невозможно долго обижаться.")
        self.assertEqual(number_fate(message, "01.10.2200"),"Шестерка символизирует устойчивость и истину. Если вам выпало это число жизненного пути, вы — перфекционист, вдохновляемый гармонией и красотой, творческая, мечтательная личность с обостренным чувством справедливости и большими амбициями. Вам хватает такта угадать ситуацию, где требуется ваша помощь, ни в коем случае не вмешиваясь в чужие дела без повода. Скорее всего, вы раскроетесь в творческой профессии, а в отношениях — как однолюб/-ка, потому что партнер просто обязан соответствовать вашим высоким стандартам.")

    def test_number_soul(self):
        self.assertEqual(number_soul(message, "01.01.2133"), "2 - символ человека спокойного в поведении и действиях, мягкого, тактичного, с умение м находить компромиссы, способного держать себя в руках. Вы – человек с противоборством двух равносильных начал действующих в противоположные друг от друга стороны. За счет этих противоборств внутри вас сохраняется равновесие и спокойствие. Вы легко подчиняемы, пассивны и мягки. Вам ближе роль советчика или проектировщика, нежели чем исполнителя.")
        self.assertEqual(number_soul(message, "01.01.2000"), "4 - это число, символизирующее четыре стихии, четыре времени года и четыре периода жизни. Люди с числом души 4 трудолюбивы, уравновешены и рассудительны. Всё чего они хотят добиться добиваются сами. В обсуждениях занимают противоположную позицию и очень редко дают волю эмоциям. «В штыки» воспринимают правила и инструкции, их тянет к реформам. «Четверка» означает успех в технических областях.")
        self.assertEqual(number_soul(message, "01.10.2010"),"5 - символ человека, не сидящего на одном месте, стремящегося к самосовершенствованию, поиску и приобретению опыта. Вы – натура, переполненная энтузиазма, нуждающаяся в приключениях и риске. Решение действовать приходить спонтанно и внезапно. В жизни вами правят позитивный настрой, находчивость, остроумие и жизнерадостность. Вы направленны только вперед и думаете только о положительном исходе всего, за чтобы не взялись. Как правило люди с числом жизни 5 нервны, авантюрны и очень подвижны.")
        self.assertEqual(number_soul(message, "01.10.2200"),"6 - число творческой личности, символ семьи и воссоединения мужчины и женщины для создания новой жизни. Число шесть так же символизирует связь между Богом и Человеком. Люди с числом жизни 6 надежны, честны и способны добиться уважения и улучшения не только собственных условий жизни, но и окружающих. Терпеливы и обладают природным внутренним магнетизмом, однако в осуществлении своих планов жестки и настойчивы. Очень романтичны и любят искусство, не выносят ревность и всяческие раздоры. Легко находят общий язык абсолютно со всеми. Обладают большой способностью заводить друзей и повышенное чувство долга. Вы – домосед, счастливы в кругу родных и близких.")

    def test_number_year(self):
        self.assertEqual(number_year(message, "01.01.2133"), "Тем, кто получил 2, поможет харизма и выдающие коммуникативные навыки. Вы весь год будете прокладывать себе дорогу через общение, приятные встречи, новые знакомства. Дар красноречия и врожденное обаяние помогут вам приручить Голубого Водяного Тигра и добиться желаемого по-хорошему. Особенное покровительство достанется тем, кто работает в творческой сфере — музыкантам, певцам, скульпторам, художникам, поэтами и писателям.")
        self.assertEqual(number_year(message, "01.01.2000"), "4 говорит о том, что год получится напряженный и тяжелый. Уже к началу лета вы будете измотаны в край плохими новостями и проблемами на работе. Если не возьмете отпуск и хорошенько не отдохнете, то начнутся сложности еще и со здоровьем. Зато в плане путешествий вам повезет гораздо больше других. Любая ваша поездка пройдет удачно и будет полностью безопасной. Одна проблема — скорее всего, это будут командировки, и придется не только гулять, но и работать.")
        self.assertEqual(number_year(message, "01.10.2010"),"Тем, у кого вышла твердая 5, придется разрушить старые устои и создать новые. Если не переродиться, то можно застрять в прошлом и навсегда свернуть с предначертанного пути, а делать этого никак нельзя. Поэтому, как бы ни было сложно, стойко примите любые перемены. Помните: все, что происходит в вашей жизни, принесет пользу и ради этого стоит немножечко потерпеть. Зато вам повезет в любви. Одиночки встретят вторую половинку, а те, кто уже связан отношениями, будут счастливы вместе.")
        self.assertEqual(number_year(message, "01.10.2200"),"6 — число коварное и это значит, что всегда нужно быть настороже. Перепроверяйте информацию, не доверяйте новым знакомствам, всегда подстилайте соломку. В вашем случае лучше подстраховаться, чем потом зализывать душевные раны. Во второй половине года, наоборот, уделяйте больше времени общению с друзьями и близкими, займитесь хобби. Ваше новое увлечение может перерасти в дело всей жизни и принести вам нежданное богатство.")

    def test_zodiac(self):
        self.assertEqual(zodiac(message, "01.01.2133"), f'<b>{message.from_user.first_name}</b>, Твой знак зодиака Козерог')
        self.assertEqual(zodiac(message, "23.04.2223"), f'<b>{message.from_user.first_name}</b>, Твой знак зодиака Телец')
        self.assertEqual(zodiac(message, "05.09.3333"), f'<b>{message.from_user.first_name}</b>, Твой знак зодиака Дева')
        self.assertEqual(zodiac(message, "16.05.2133"), f'<b>{message.from_user.first_name}</b>, Твой знак зодиака Телец')
        self.assertEqual(zodiac(message, "20.03.2003"), f'<b>{message.from_user.first_name}</b>, Твой знак зодиака Рыбы')
        self.assertEqual(zodiac(message, "30.05.2003"), f'<b>{message.from_user.first_name}</b>, Твой знак зодиака Близнецы')
        self.assertEqual(zodiac(message, "11.11.1978"), f'<b>{message.from_user.first_name}</b>, Твой знак зодиака Скорпион')

    def test_start(self):
        message.from_user.first_name = "Test"
        self.assertEqual(start(message), f'<b>Привет! {message.from_user.first_name}!</b> Что ты хочешь узнать о себе? Для начала установи дату.')
        message.from_user.first_name = "Me"
        self.assertEqual(start(message), f'<b>Привет! {message.from_user.first_name}!</b> Что ты хочешь узнать о себе? Для начала установи дату.')
        message.from_user.first_name = "No"
        self.assertEqual(start(message), f'<b>Привет! {message.from_user.first_name}!</b> Что ты хочешь узнать о себе? Для начала установи дату.')

    def test_find_num(self):
        self.assertEqual(find_num("123"), '6')
        self.assertEqual(find_num("000"), '0')
        self.assertEqual(find_num("1111"), '4')
        self.assertEqual(find_num("9993"), '3')
        self.assertEqual(find_num("12023000"), '8')

    def test_check_date(self):
        self.assertEqual(check_date(message,"01.01.2133"), True)
        self.assertEqual(check_date(message,""), False)
        self.assertEqual(check_date(message, "sdf"), False)
        self.assertEqual(check_date(message, "12,02,3000"), False)
        self.assertEqual(check_date(message, "12.02,3000"), False)
        self.assertEqual(check_date(message, "12.02,3000"), False)
        self.assertEqual(check_date(message, "11.11.1111"), True)
        self.assertEqual(check_date(message, "12,02.3000"), False)
        self.assertEqual(check_date(message, "12.023000"), False)
        self.assertEqual(check_date(message, "12023000"), False)
        self.assertEqual(check_date(message, "11.09.1222"), True)
        self.assertEqual(check_date(message, "32.02.3000"), False)
        self.assertEqual(check_date(message, "31.13.3000"), False)
        self.assertEqual(check_date(message, "3d02.3000"), False)

    def test_get_text_messages(self):
        message.text = "dd"
        self.assertEqual(get_text_messages(message), "Команда не распознана")
        message.text = "Установить дату"
        self.assertEqual(get_text_messages(message), "Установить дату")
        message.text = "Знак зодиака"
        self.assertEqual(get_text_messages(message), "Знак зодиака")
        message.text = "Число года"
        self.assertEqual(get_text_messages(message), "Число года")
        message.text = "Число судьбы"
        self.assertEqual(get_text_messages(message), "Число судьбы")
        message.text = "Число души"
        self.assertEqual(get_text_messages(message), "Число души")
        message.text = "Числssсудьбы"
        self.assertEqual(get_text_messages(message), "Команда не распознана")
        message.text = "12134"
        self.assertEqual(get_text_messages(message), "Команда не распознана")

if __name__ == '__main__':
    unittest.main()
