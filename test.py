from bar_tab import Tab

table1 = Tab()
# print(table1) # <bar_tab.Tab object at 0x000001e6aeaef040>


print(table1.add('chicken'))
print(table1.add('desert'))
print(table1.add('veggie'))
print(table1.print_bill(10,10))

# None
# None
# None
# None
# soft_drink €2
# chicken €10
# desert €6
# veggie €12
# Total: €36.00
# None

# using CMD also work fine, doesnt show None

# >>> from bar_tab import Tab
# >>> table2 = Tab()
# >>> table2
# <bar_tab.Tab object at 0x0000019811dba100>      
# >>> table2.add('beef')
# >>> table2.add('wine')
# >>> table2.print_bill(10,10)
# beef                 €15
# wine                 €5
# 'Total: €24.00'
# >>>