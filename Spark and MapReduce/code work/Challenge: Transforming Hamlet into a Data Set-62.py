## 2. Extract Line Numbers ##

raw_hamlet = sc.textFile("hamlet.txt")
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)

def new_list(line):
    first = line[0]
    id_hamlet = first.split('@')[1]
    line[0] = id_hamlet
    return line
        
hamlet_with_ids = split_hamlet.map(new_list)   
hamlet_with_ids.take(5)

## 3. Remove Blank Values ##

hamlet_with_ids.take(5)

real_text = hamlet_with_ids.filter(lambda line: len(line) > 1)
hamlet_text_only = real_text.map(lambda line: [l for l in line if l != ''])
hamlet_text_only.take(10)

## 4. Remove Pipe Characters ##

hamlet_text_only.take(10)
def fix_pipe(line):
    results = list()
    for l in line:
        if l == '|':
            pass
        elif '|' in l:
            fmtd = l.replace("|", "")
            results.append(fmtd)
        else:
            results.append(l)
    return results

clean_hamlet = hamlet_text_only.map(lambda line: fix_pipe(line))