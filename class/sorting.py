def sorting(m):
    s = m[0]
    for i in range(1,len(m)):
        s = m.pop(i)
        position = i
        if s< m[i-1]:
           d = (m[i-1] - s)**2
           for j in range(i):
               if s<m[j]:
                   dis = (m[j]-s)**2
                   if dis<d:
                      position = j
                      d = dis
        m.insert(position,s)
    return m   
