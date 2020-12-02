def conclude(gt):
     used_rule = []
     td = gt
     f = open('D:\\rule1.txt', 'r+')
     content = f.read()
     rules = content.split('\n')
     while(True):
          for rule in rules:
               temp1 = rule.split(' ')
               if temp1[0] in used_rule:
                    continue

               temp2 = temp1[1].split('>')
               rule_tmp = temp2[0].split('&')
               check = True
               for i in rule_tmp:
                    if i not in td:
                         check = False
                         break
               if check == True:
                    if temp2[1].__contains__('l'):
                         return temp2[1]
                    td.append(temp2[1])
                    used_rule.append(temp1[0])      


           

           








