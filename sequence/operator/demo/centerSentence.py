# coding=utf-8
# create by chengfan on 2017/1/13 下午2:29

# 以正确的宽度在剧中的盒子内打印一个句子
# add & multiply 综合练习

sentence = raw_input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 20
left_margin = (screen_width - box_width) // 2
left_padding = (box_width - text_width - 2) // 2

print
print ' ' * left_margin                  + '+'  + '-' * (box_width) + '+'
print ' ' * (left_margin + left_padding) + '| ' + ' ' * text_width    + ' |'
print ' ' * (left_margin + left_padding) + '| ' +      sentence       + ' |'
print ' ' * (left_margin + left_padding) + '| ' + ' ' * text_width    + ' |'
print ' ' * left_margin                  + '+'  + '-' * (box_width) + '+'
print


