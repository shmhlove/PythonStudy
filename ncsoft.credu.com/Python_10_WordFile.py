#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

from pyautomate import office

doc = office.Word('turing.docx');
print(doc.paragraphs[0].text);
print(doc.paragraphs[2].text);

content = doc.extract_text();
print(content);

for line in doc.paragraphs:
    print(line.text);

table = doc.extract_tables(0);
print(table);

doc = office.Word('turing.docx');
tables = doc.extract_tables();
print(tables[0]);
print(tables[1]);

doc.tables_to_excel('newExcel.xlsx');

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

doc = office.Word();
doc.add_paragraph("write in python program");
doc.save('writedoc.docx');

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

doc = office.Word('writedoc.docx');
p = doc.add_paragraph("edit in python program");
p.style = 'List Number';
doc.add_heading('Test Main Title', 0);
doc.add_heading('Test Sub Title 1', 1);
doc.add_heading('Test Sub Title 2', 1);
p = doc.add_heading('Test Sub Title 3', 1);
print(p);
doc.add_picture('includeword.jpg', width=5, height=5);
doc.save('writedoc.docx');

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------
