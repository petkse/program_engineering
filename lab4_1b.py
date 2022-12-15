students =
{
"Dasha": ["troechnic", "woman"], "Masha": ["horoshist", "woman"], "Pasha": ["otlichnic", "man"], "Misha":["troechnic",
   "man"]}
for i
in students.keys ():
  if (students[i][0] == "horoshist" or students[i][0] == "otlichnic")
  :
    print (i, "molodets!");
for i
in students.keys ():
  if ((students[i][0] == "horoshist" or students[i][0] ==
       "otlichnic") and students[i][1] == "man")
  :
    print (i, "malchik i molodets!");
