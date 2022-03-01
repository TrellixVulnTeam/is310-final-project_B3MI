
tool = {
    'python' : {
        '2015' : 9, 
        '2016' : 22, 
        '2017' : 27, 
        '2018' : 32,
        '2019' : 35
    }, 
    'javascript' : {
        '2015' : 8, 
        '2016' : 18, 
        '2017' : 12, 
        '2018' : 6,
        '2019' : 15
    }, 
    'twitter' : {
        '2015' : 10, 
        '2016' : 18, 
        '2017' : 26, 
        '2018' : 16,
        '2019' : 12
    },
    'github' : { 
        '2015' : 2, 
        '2016' : 6, 
        '2017' : 17, 
        '2018' : 5,
        '2019' : 10
    },
    'gephi' : { 
        '2015' : 11, 
        '2016' : 16, 
        '2017' : 14, 
        '2018' : 10,
        '2019' : 9
    },
    'geonames' : { 
        '2015' : 2, 
        '2016' : 4, 
        '2017' : 3,
        '2018' : 1,
        '2019' : 8
    },
    'transkribus' : { 
        '2015' : 0, 
        '2016' : 1, 
        '2017' : 2, 
        '2018' : 1,
        '2019' : 8
    },
    'excel' : { 
        '2015' : 5, 
        '2016' : 9, 
        '2017' : 3, 
        '2018' : 6,
        '2019' : 7
    },
    'mysql' : { 
        '2015' : 0, 
        '2016' : 6, 
        '2017' : 9, 
        '2018' : 5,
        '2019' : 7
    },
}

#print(tool)
#print(tool['python']['2015'])
#print(tool['python']['2015'] + tool['python']['2016']
# + tool['python']['2017'] + tool['python']['2018'] + tool['python']['2019'])
for key, value in tool.items() : 
    print('tool:', key)
    print('tool value in 2015', value['2015'])
    print('tool value in 2019', value['2019'])
    print('total popularity count', value['2015'] + value['2016'] + value['2017']
    + value['2018'] + value['2019'])