# -*- coding: utf-8 -*-

#####################################################################################################

text_ascii = u"Je suis allez a Paris"
text_with_accent = "Je suis allez à Paris"
text_unicode = u"Je suis allez à Paris"

print text_ascii, len(text_ascii) # len = 21
print text_with_accent, len(text_with_accent) # len = 21 +1
print text_unicode, len(text_unicode) # len = 21

text = u'|'.join(u'(%u)%s' % (i, x) for i, x in enumerate(text_unicode))
print text

#####################################################################################################
#
# End
#
#####################################################################################################
