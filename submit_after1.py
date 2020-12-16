def filter(readuser1):
    result = []
    laptops = readuser1
    for attr in laptops:
        for j in range(0, 10):
            if j == 0:
                if attr[j] == 'DELL':
                    shortcut = 'm1'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'ASUS':
                    shortcut = 'm2'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'ACER':
                    shortcut = 'm3'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'HP':
                    shortcut = 'm4'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'LG':
                    shortcut = 'm5'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'APPLE':
                    shortcut = 'm6'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'LENOVO':
                    shortcut = 'm7'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'MICROSOFT':
                    shortcut = 'm8'
                    if shortcut not in result:
                        result.append(shortcut)
                else:
                    shortcut = 'm9'
                    if shortcut not in result:
                        result.append(shortcut)
            
            elif j == 1:
                continue
            
            elif j == 2:
                if attr[j] == 'Xám':
                    shortcut = 'c1'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'Đen':
                    shortcut = 'c2'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'Bạc':
                    shortcut = 'c3'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'Vàng':
                    shortcut = 'c4'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'Xanh':
                    shortcut = 'c5'
                    if shortcut not in result:
                        result.append(shortcut)
                else:
                    shortcut = 'c6'
                    if shortcut not in result:
                        result.append(shortcut)       
            
            elif j == 3:
                if attr[j].startswith('Intel Core i3'):
                    shortcut = 'ch1'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j].startswith('Intel Core i5'):
                    shortcut = 'ch2'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j].startswith('Intel Core i7'):
                    shortcut = 'ch3'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j].startswith('Ryzen 3'):
                    shortcut = 'ch4'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j].startswith('Ryzen 5'):
                    shortcut = 'ch5'
                    if shortcut not in result:
                        result.append(shortcut)
                else:
                    shortcut = 'ch6'
                    if shortcut not in result:
                        result.append(shortcut)
            
            elif j == 4:
                if attr[j] == '4GB':
                    shortcut = 'ra1'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == '8GB':
                    shortcut = 'ra2'
                    if shortcut not in result:
                        result.append(shortcut)
                else:
                    shortcut = 'ra3'
                    if shortcut not in result:
                        result.append(shortcut)
            
            elif j == 5:
                if attr[j].__contains__('Graphics'):
                    shortcut = 'ca1'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j].__contains__('NVIDIA'):
                    shortcut = 'ca2'
                    if shortcut not in result:
                        result.append(shortcut)
                else:
                    shortcut = 'ca3'
                    if shortcut not in result:
                        result.append(shortcut)
            
            elif j == 6:
                if attr[j] == 'SSD':
                    shortcut = 'h1'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == 'HDD':
                    shortcut = 'h2'
                    if shortcut not in result:
                        result.append(shortcut)
                else:
                    shortcut = 'h3'
                    if shortcut not in result:
                        result.append(shortcut)
            
            elif j == 7:
                if (float)(attr[j]) < 14:
                    shortcut = 'mo1'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == '14':
                    shortcut = 'mo2'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == '15.6':
                    shortcut == 'mo3'
                    if shortcut not in result:
                        result.append(shortcut)
                else:
                    shortcut = 'mo4'
                    if shortcut not in result:
                        result.append(shortcut)
            
            elif j == 8:
                if attr[j] == '2-CELL':
                    shortcut = 'b1'
                    if shortcut not in result:
                        result.append(shortcut)
                elif attr[j] == '3-CELL':
                    shortcut = 'b2'
                    if shortcut not in result:
                        result.append(shortcut) 
                elif attr[j] == '4-CELL':
                    shortcut = 'b3'
                    if shortcut not in result:
                        result.append(shortcut) 
                else:
                    shortcut = 'b4'
                    if shortcut not in result:
                        result.append(shortcut) 
            else:
                if (float)(attr[j]) < 1.5:
                    shortcut = 'w1'
                    if shortcut not in result:
                        result.append(shortcut)
                elif (float)(attr[j])>=1.5 and (float)(attr[j]) < 2:
                    shortcut = 'w2'
                    if shortcut not in result:
                        result.append(shortcut)
                else:
                    shortcut = 'w3'
                    if shortcut not in result:
                        result.append(shortcut)
    return result