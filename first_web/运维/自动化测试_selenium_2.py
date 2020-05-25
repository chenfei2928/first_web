from selenium import webdriver
b = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
b.implicitly_wait(5)
b.get('https://study.163.com/provider/470451/index.htm?_trace_c_p_k2_=6e2344184d0b4b8299d134fe3c02f049')


b.find_element_by_link_text()


