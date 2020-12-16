import readUser1
import readUser2
import rule
import submit_after1

gt = ['n3', 'p3']
kl = readUser1.conclude(gt)
re = rule.list_result(kl)
thuoctinh = submit_after1.filter(re)

for i in thuoctinh:
    print(i)
