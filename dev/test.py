# import codecs
#
# rabbit1 = "a, b, c"
# rabbit2 = "й, ў, ї"
#
# rabbit = rabbit2
#
# if type(rabbit) is not str:
#     raise TypeError(f"Non-string value was found in {rabbit}")
#
# # UnicodeDecodeError check
# assert type(rabbit.encode(encoding='utf-8')) is bytes, f"The string {rabbit} failed the"
# assert type(codecs.encode(rabbit, 'latin1', errors='strict')) is bytes
#
# # TypeError check
# assert type(rabbit + "normal_string") is str


#
# from checks import encoding_check
# import codecs
# rabbit = "й, ў, ї"
#
# # assert type(codecs.encode(rabbit, 'latin1', errors='strict')) is bytes, f"The string {rabbit} failed the "
# encoding_check(rabbit=rabbit)

from lib import InputArmor

InputArmor.advanced_check(rabbit="й, ў, ї")