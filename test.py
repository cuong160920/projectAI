import readUser1
import readUser2
import rule

gt = ['n4']
kl = readUser1.conclude(gt)
re = rule.list_result(kl)
for i in re:
    print(i)
