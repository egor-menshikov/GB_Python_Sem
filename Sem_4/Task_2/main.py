
# sentence = ('She sells sea shells on the sea shore The shells that she sells are sea' \
#            ' shells Im sure So if she sells sea shells on the sea shore Im sure that' \
#            ' the shells are sea shore shells')
#
#
# print(len(set(sentence.lower().split())))

text = "She sells sea shells on the sea shore The shells that she sells are sea shells Im sure So if she sells sea shells on the sea shore Im sure that the shells are sea shore shells"
text = text.lower()
text = text.split()
text = set(text)
text.discard(' ')
text.discard('.')
text.discard('"')
print(text)
print(len(text))