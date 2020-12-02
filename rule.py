import csv

def price1(row):
    if (int)(row[11]) < 10000000:
        return True
    return False

def price2(row):
    if (int)(row[11]) >= 10000000 and (int)(row[11]) < 15000000:
        return True
    return False

def price3(row):
    if (int)(row[11]) >= 15000000 and (int)(row[11]) < 20000000:
        return True
    return False

def price4(row):
    if (int)(row[11]) >= 20000000 and (int)(row[11]) < 25000000:
        return True
    return False

def price5(row):
    if (int)(row[11]) >= 25000000 and (int)(row[11]) < 30000000:
        return True
    return False

def price6(row):
    if (int)(row[11]) >= 30000000:
        return True
    return False

def tmp1(row):
    if row[5].startswith('NVIDIA GeForce RTX') or row[5].startswith('NVIDIA GeForce GTX'):
        return True
    return False

def tmp2(row):
    if row[5].startswith('NVIDIA GeForce GTX') and (row[3].startswith('Intel Core i5') or row[3].startswith('Intel Core i7') or row[3].startswith('Ryzen 5') or row[3].startswith('Ryzen 7')) and (row[6].__contains__('GB') or row[6].__contains__('+')) and (row[4] == '8GB' or row[4] == '16GB'):
        return True
    return False

def tmp3(row):
    if (float)(row[9]) < 2:
        return True
    return False

def tmp4(row):
    if (row[4] == '8GB' or row[4] == '16GB') and (row[3].startswith('Intel Core i5') or row[3].startswith('Intel Core i7') or row[3].startswith('Ryzen 5') or row[3].startswith('Ryzen 7')):
        return True
    return False

def tmp5(row):
    if (float)(row[7]) < 17.3 and (row[2] == 'Bạc' or row[2] == 'Xanh'or row[3] == 'Trắng' or row[3] == 'Vàng') and tmp3(row):
        return True
    return False

def tmp6(row):
    if tmp3(row) and (row[4] == '4GB' or row[4] == '8GB') and (row[3].startswith('Intel Core i3') or row[3].startswith('Intel Core i5') or row[3].startswith('Ryzen 3') or row[3].startswith('Ryzen 5')):
        return True
    return False

def tmp7(row):
    if row[8] == '3-CELL' or row[8] == '4-CELL' or row[8] == '6-CELL':
        return True
    return False


def list_result(rule):
    result = []
    with open('D:\COURSES\Project AI\Thongsokithuat.csv', 'r+', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        if rule == 'l1':
            for row in csv_reader:
                if tmp1(row) and price3(row):
                    result.append(row)
            return result
    
        elif rule == 'l2':
            for row in csv_reader:
                if tmp1(row) and price4(row):
                    result.append(row)
            return result
    
        elif rule == 'l3':
            for row in csv_reader:
                if tmp1(row) and price5(row):
                    result.append(row)
            return result
    
        elif rule == 'l4':
            for row in csv_reader:
                if tmp1(row) and price6(row):
                    result.append(row)
            return result
    
        elif rule == 'l5':
            for row in csv_reader:
                if tmp2(row) and price3(row):
                    result.append(row)
            return result
        
        elif rule == 'l6':
            for row in csv_reader:
                if tmp2(row) and price4(row):
                    result.append(row)
            return result

        elif rule == 'l7':
            for row in csv_reader:
                if tmp2(row) and price5(row):
                    result.append(row)
            return result
        
        elif rule == 'l8':
            for row in csv_reader:
                if tmp2(row) and price6(row):
                    result.append(row)
            return result

        elif rule == 'l9':
            for row in csv_reader:
                if tmp3(row) and price1(row):
                    result.append(row)
            return result
        
        elif rule == 'l10':
            for row in csv_reader:
                if tmp3(row) and price2(row):
                    result.append(row)
            return result

        elif rule == 'l11':
            for row in csv_reader:
                if tmp3(row) and price3(row):
                    result.append(row)
            return result

        elif rule == 'l12':
            for row in csv_reader:
                if tmp3(row) and price4(row):
                    result.append(row)
            return result

        elif rule == 'l13':
            for row in csv_reader:
                if tmp3(row) and price5(row):
                    result.append(row)
            return result

        elif rule == 'l14':
            for row in csv_reader:
                if tmp3(row) and price6(row):
                    result.append(row)
            return result
        
        elif rule == 'l15':
            for row in csv_reader:
                if tmp3(row) and (price5(row) or price6(row)) and (row[3].startswith('Intel Core i5') or row[3].startswith('Intel Core i7')):
                    result.append(row)
            return result
        
        elif rule == 'l16':
            for row in csv_reader:
                if tmp4(row) and price2(row):
                    result.append(row)
            return result
        
        elif rule == 'l17':
            for row in csv_reader:
                if tmp4(row) and price3(row):
                    result.append(row)
            return result
        
        elif rule == 'l18':
            for row in csv_reader:
                if tmp4(row) and price4(row):
                    result.append(row)
            return result
        
        elif rule == 'l19':
            for row in csv_reader:
                if tmp4(row) and price5(row):
                    result.append(row)
            return result

        elif rule == 'l20':
            for row in csv_reader:
                if tmp4(row) and price6(row):
                    result.append(row)
            return result
        elif rule == 'l21':
            for row in csv_reader:
                if tmp5(row) and price1(row):
                    result.append(row)
            return result
        
        elif rule == 'l22':
            for row in csv_reader:
                if tmp5(row) and price2(row):
                    result.append(row)
            return result
        
        elif rule == 'l23':
            for row in csv_reader:
                if tmp5(row) and price3(row):
                    result.append(row)
            return result
        
        elif rule == 'l24':
            for row in csv_reader:
                if tmp5(row) and price4(row):
                    result.append(row)
            return result
        
        elif rule == 'l25':
            for row in csv_reader:
                if tmp5(row) and price5(row):
                    result.append(row)
            return result
        
        elif rule == 'l26':
            for row in csv_reader:
                if tmp5(row) and price6(row):
                    result.append(row)
            return result
        
        elif rule == 'l27':
            for row in csv_reader:
                if tmp6(row) and price1(row):
                    result.append(row)
            return result
        
        elif rule == 'l28':
            for row in csv_reader:
                if tmp6(row) and price2(row):
                    result.append(row)
            return result

        elif rule == 'l29':
            for row in csv_reader:
                if tmp6(row) and price3(row):
                    result.append(row)
            return result

        elif rule == 'l30':
            for row in csv_reader:
                if tmp6(row) and price4(row):
                    result.append(row)
            return result
        
        elif rule == 'l31':
            for row in csv_reader:
                if tmp6(row) and price5(row):
                    result.append(row)
            return result
        
        elif rule == 'l32':
            for row in csv_reader:
                if tmp6(row) and price6(row):
                    result.append(row)
            return result
        
        elif rule == 'l33':
            for row in csv_reader:
                if tmp7(row) and price2(row):
                    result.append(row)
            return result
        
        elif rule == 'l34':
            for row in csv_reader:
                if tmp7(row) and price3(row):
                    result.append(row)
            return result
        
        elif rule == 'l35':
            for row in csv_reader:
                if tmp7(row) and price4(row):
                    result.append(row)
            return result
        
        elif rule == 'l36':
            for row in csv_reader:
                if tmp7(row) and price5(row):
                    result.append(row)
            return result
        
        elif rule == 'l37':
            for row in csv_reader:
                if tmp7(row) and price6(row):
                    result.append(row)
            return result

        elif rule == 'l38':
            for row in csv_reader:
                if price1(row) or price2(row) or price3(row):
                    result.append(row)
            return result
        
        else:
            return result
