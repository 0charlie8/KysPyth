def main(x):

dir4 = {1965 : 0, 1990 : 1, 1961 : 2 }
dir1 = {2006 : 3, 1989 : 4}
dir3 = {'ASP' : dir4[x[4]], 'MASK' : dir1[x[1]], 'RUST' : 5}
dir1_d = {2006 : 6, 1989 : 7}
dir1_dd = {2006 : 8, 1989 : 9}
dir3_d = {'ASP' : dir1_d[x[1]], 'MASK' : dir1_dd[x[1]], 'RUST' : 10}
dir0 = {'APL' : dir3[x[3]], 'P4' : dir3_d[x[1]], 'DYLAN' : 11}
dir2 = {'XSLT' : dir0[x[0]], 'GOSU' : 12}
return dir2[x[2]]

print(main(['P4', 2006, 'GOSU', 'RUST', 1961]))
