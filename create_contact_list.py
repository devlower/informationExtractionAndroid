import re
from datetime import datetime
from pathlib import Path
import os

def createContactList(path):

  index = 0
  device_data = []
  file_content = []

  file = open(path, 'r')
  file_read = file.read()
  file.close()

  pattern_name_contact = r'display_name=(.*?),.*?data1=[0|+]?(\w+),.*?creation_time=(\w+),'

  matches = re.findall(pattern_name_contact, file_read)
  list_contacts = sorted(set(matches))

  while index != len(list_contacts):
    if index + 1 < len(list_contacts):
      if list_contacts[index][0] == list_contacts[index+1][0]:
        list_contacts.pop(index)
    index += 1

  for index in range(0, len(list_contacts)):
    temp = list(list_contacts[index])
    timestamp = list_contacts[index][2]
    if timestamp != '0':
      dt_object = datetime.fromtimestamp(int(timestamp)/1000).strftime("%d-%m-%Y %H:%M:%S")
      temp[2] = str(dt_object)
      device_data.append(temp)
    else:
      temp[2] = 'Nenhum registro encontrado'
      device_data.append(temp)

    colunm0 = ' ' * (4 - len(str(index)))
    colunm1 = ' ' * (35 - len(temp[0]))
    colunm2 = ' ' * (20 - len(temp[1]))
    colunm3 = ' ' * (30 - len(temp[2])) 

    outputFormat = f' {index}{colunm0}|  {temp[0]}{colunm1}|       {temp[1]}{colunm2}|    {temp[2]}{colunm3}|\n{"-"*5}+{"-"*37}+{"-"*27}+{"-"*34}+\n'
    file_content.append(outputFormat)

  path = Path(f'{path}')

  basename = os.path.basename(path)
  file_name = os.path.splitext(basename)[0]
  file_name = f'{file_name}_Contatos_Tratados'

  fileOutput = open(f"{path.parent}\\{file_name}.txt", "w")
  fileOutput.writelines(file_content)
  fileOutput.close()

  return device_data
  