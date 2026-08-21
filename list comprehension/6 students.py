students = {
"Rahul": 75,
"Anil": 32,
"Priya": 56,
"Sneha": 28
}
d={i:"pass" if students[i]>35 else "fail" for i in students}
print(d,end=" ")