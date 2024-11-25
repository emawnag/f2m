# Read the contents of the airportRunwayLength.html file as text
file_path = 'C:/Users/ai/Documents/andy/code/ftm/airportRunwayLength.html'

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

#print(html_content)

# Split the HTML content by <br> tag
data_array = html_content.split('<br>')

# Print the resulting array
#print(data_array)

# Filter out elements that contain '<' or '>'
filtered_data_array = [x for x in data_array if '<' not in x and '>' not in x]

# Print the filtered array
#print(len(filtered_data_array))

a = filtered_data_array[0:int(len(filtered_data_array)/4)-1]
b = filtered_data_array[int(len(filtered_data_array)/4):int(len(filtered_data_array)/4*2)-1]
c = filtered_data_array[int(len(filtered_data_array)/4*2):int(len(filtered_data_array)/4*3)-1]
d = filtered_data_array[int(len(filtered_data_array)/4*3):len(filtered_data_array)]

# print(a)
# print(b)
# print(c)
# print(d)

varStr = ""
for i in range(len(a)):
    e = c[i].split('(')[0].replace('ft', '').strip()
    f = c[i].split('(')[1].replace('m', '').replace(')', '').strip()
    varStr += "<tr><td>" + a[i] + "</td><td>" + b[i] + "</td><td>" + e + "</td><td>"+ f + "</td><td>" + d[i] + "</td></tr>"

print(varStr)