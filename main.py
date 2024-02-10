pics = [] 
pic_template = "http://www.kaitorimax.com/signkai/{}/img/{}.jpg" 
page_template = "http://www.kaitorimax.com/signkai/{}/{}.html" 
pic_info = [ 
  ("2023/0416_", "hanayagi_anna", 11), 
  ("2023/0723_", "hoshino_natsuki", 28), 
  ("2023/1022_", "hoshino_natsuki", 40), 
  ("2022/1217_", "kikuchi_maya", 35), 
  ("2023/0128_", "ikuta_machi", 40), 
  ("2014/0614_", "shiraishi_marina", 20), 
  ("2018/1013_14_", "mitoma_umi", 28), 
  ("2019/0901_", "shinozaki_kanna", 20), 
  ("2023/0422_", "fujita_kozue", 21), 
  ("2023/0918_", "fujita_kozue", 21), 
  ("2023/0402_", "akari_nonoka", 35), 
  ("2023/0701_", "suzune_kyouka", 38), 
  ("2021/1128_", "yoshine_yuria", 30), 
  ("2023/0506_", "tsukada_shiori", 40), 
  ("2023/0225_", "yumi_shion", 14) 
] 

for date_prefix, name, cnt in pic_info: 
  pics.extend(pic_template.format(date_prefix + name, i) for i in range(1, cnt + 1)) 
  page_url = page_template.format(date_prefix + name, name) 
  pics.append(page_url) 
  pics.append( "\r\n") 

s = "\r\n".join(pics) 
print(s) 
