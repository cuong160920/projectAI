def criteria(shortcut, result):
    array_result = []
    if shortcut == 'm1':
        for laptop in result:
            if laptop[0] == 'DELL':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'm2':
        for laptop in result:
            if laptop[0] == 'ASUS':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'm3':
        for laptop in result:
            if laptop[0] == 'ACER':
                array_result.append(laptop)
        return array_result

    elif shortcut == 'm4':
        for laptop in result:
            if laptop[0] == 'HP':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'm5':
        for laptop in result:
            if laptop[0] == 'LG':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'm6':
        for laptop in result:
            if laptop[0] == 'APPLE':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'm7':
        for laptop in result:
            if laptop[0] == 'LENOVO':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'm8':
        for laptop in result:
            if laptop[0] == 'MICROSOFT':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'm9':
        for laptop in result:
            if laptop[0] == 'MSI':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'c1':
        for laptop in result:
            if laptop[2] == 'Xám':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'c2':
        for laptop in result:
            if laptop[2] == 'Đen':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'c3':
        for laptop in result:
            if laptop[2] == 'Bạc':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'c4':
        for laptop in result:
            if laptop[2] == 'Vàng':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'c5':
        for laptop in result:
            if laptop[2] == 'Xanh':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'c6':
        for laptop in result:
            if laptop[2] == 'Trắng':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ch1':
        for laptop in result:
            if laptop[3].__contains__('Intel Core i3'):
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ch2':
        for laptop in result:
            if laptop[3].__contains__('Intel Core i5'):
                array_result.append(laptop)
        return array_result

    elif shortcut == 'ch3':
        for laptop in result:
            if laptop[3].__contains__('Intel Core i7'):
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ch4':
        for laptop in result:
            if laptop[3].__contains__('Ryzen 3'):
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ch5':
        for laptop in result:
            if laptop[3].__contains__('Ryzen 5'):
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ch6':
        for laptop in result:
            if laptop[3].__contains__('Ryzen 7'):
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ra1':
        for laptop in result:
            if laptop[4] == '4GB':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ra2':
        for laptop in result:
            if laptop[4] == '8GB':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ra3':
        for laptop in result:
            if laptop[4] == '16GB':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ca1':
        for laptop in result:
            if laptop[5].__contains__('Graphics'):
                array_result.append(laptop)
        return array_result

    elif shortcut == 'ca2':
        for laptop in result:
            if laptop[5].__contains__('NVIDIA'):
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ca3':
        for laptop in result:
            if laptop[5].__contains__('Radeon'):
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ca4':
        for laptop in result:
            if laptop[5].__contains__('NVIDIA GeForce RTX'):
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'ca5':
        for laptop in result:
            if laptop[5].__contains__('NVIDIA GeForce GTX'):
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'h1':
        for laptop in result:
            if laptop[6].__contains__('GB'):
                array_result.append(laptop)
        return array_result

    elif shortcut == 'h2':
        for laptop in result:
            if laptop[6] == 'HDD':
                array_result.append(laptop)
        return array_result

    elif shortcut == 'h3':
        for laptop in result:
            if laptop[6] == 'HDD + SSD':
                array_result.append(laptop)
        return array_result

    elif shortcut == 'mo1':
        for laptop in result:
            if (float)(laptop[7]) < 14:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'mo2':
        for laptop in result:
            if (float)(laptop[7]) == 14:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'mo3':
        for laptop in result:
            if (float)(laptop[7]) == 15.6:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'mo4':
        for laptop in result:
            if (float)(laptop[7]) == 17.3:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'b1':
        for laptop in result:
            if laptop[8] == '2-CELL':
                array_result.append(laptop)
        return array_result
    elif shortcut == 'b2':
        for laptop in result:
            if laptop[8] == '3-CELL':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'b3':
        for laptop in result:
            if laptop[8] == '4-CELL':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'b4':
        for laptop in result:
            if laptop[8] == '6-CELL':
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'w1':
        for laptop in result:
            if (float)(laptop[9]) < 1.5:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'w2':
        for laptop in result:
            if (float)(laptop[9]) >= 1.5 and (float)(laptop[9]) < 2:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'w3':
        for laptop in result:
            if (float)(laptop[9]) >= 2:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'p1':
        for laptop in result:
            if (int)(laptop[11]) < 10000000:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'p2':
        for laptop in result:
            if (int)(laptop[11]) >= 10000000 and (int)(laptop[11]) < 15000000:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'p3':
        for laptop in result:
            if (int)(laptop[11]) >= 15000000 and (int)(laptop[11]) < 20000000:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'p4':
        for laptop in result:
            if (int)(laptop[11]) >= 20000000 and (int)(laptop[11]) < 25000000:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'p5':
        for laptop in result:
            if (int)(laptop[11]) >= 25000000 and (int)(laptop[11]) < 30000000:
                array_result.append(laptop)
        return array_result
    
    elif shortcut == 'p6':
        for laptop in result:
            if (int)(laptop[11]) >= 30000000:
                array_result.append(laptop)
        return array_result

    else:
        return result
    

    


    
    
    


        
    

        