
RUN :  python expensesharing.py

INPUT FORMAT : 
1. EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL
2. EXPENSE u1 1250 2 u2 u3 EXACT 370 880
3. EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20
4. SHOW
5. SHOW u1
```
C:\machine_coding\expense_sharing>python expensesharing.py
Enter expense : EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20
Enter expense : EXPENSE u1 1250 2 u2 u3 EXACT 370 880
Enter expense : EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL
```

OUTPUT : 
```
Enter expense : SHOW
u1 owes u4 : 230
u2 owes u4 : 240
u3 owes u4 : 240
u2 owes u1 : 620
u3 owes u1 : 1130
```
Problem Link : https://workat.tech/machine-coding/practice/splitwise-problem-0kp2yneec2q2
