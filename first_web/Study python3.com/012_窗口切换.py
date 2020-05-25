from selenium import webdriver
wd = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wd.implicitly_wait(5)

wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')

# 点击打开新窗口链接

link = wd.find_element_by_tag_name("a")
link.click()

#切换前保存当前窗口值
mainWdindow = wd.current_window_handle

for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break

print(wd.title)

wd.find_element_by_id('sb_form_q').send_keys('白夜黑羽\n')

wd.switch_to.window(mainWdindow)

wd.find_element_by_id('outerbutton').click()

input('')

#wb.quit()

