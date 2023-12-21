from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.options.android import UiAutomator2Options
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
import time
import sys, os

class CheckHW():
    EXECUTOR = 'http://127.0.0.1:4723'          # appium 버전 2.X
    def __init__(self, appLocation):
        options = UiAutomator2Options()
        options.app = appLocation
        options.platform_name = 'Android'
        options.automation_name = 'flutter'  # flutter
        options.allow_test_packages = True
        options.enforce_app_install = True
        options.uiautomator2_server_install_timeout = 20000
        options.adb_exec_timeout = 20000
        options.language = 'en'
        options.locale = 'US'
        options.auto_grant_permissions = True
        
        self.driver = webdriver.Remote(
            self.EXECUTOR, options=options
        )
        self.driver.implicitly_wait(10)
        self.finder = FlutterFinder()
 
 
    def uninstall_app(self):
        pkg = self.driver.current_package
        print(pkg)
        self.driver.remove_app(pkg)


    def press_home(self):
        self.driver.press_keycode(3) # keycode HOME
        
        
    def press_back(self):
        self.driver.press_keycode(4) # keycode Back
        
        
    def find_widget(self, id_str):
        try:
            w = self.driver.find_element(AppiumBy.ID, id_str)
        except:
            w = f'ID가 {id_str}인 위젯을 찾을 수 없음'
        return w
    
    def check_list_items(self, items, recyclerview, tvID):
        try:
            elements = recyclerview.find_elements(AppiumBy.ID, tvID)
            e_text = [e.text for e in elements]
            items_len = len(items)
            result = set(items[:items_len]) == set(e_text[:items_len])
            if result == False:
                return False, f'Repository 가져온 결과가 다름 {items}, {e_text}'
            else:
                return True, 'OK'
        except:
            return False, f'ID {tvID}인 위젯을 찾을 수 없음'


    def test_lab(self, item_num):
        item_key = f"list_item{item_num}"
        f = self.finder.by_descendant(self.finder.by_value_key(item_key), self.finder.by_type('Text'), True, True)  # list_item1 키를 갖는 위젯의 자식 중 type이 Text인 것 중 처음 나오는 자식
        t2 = FlutterElement(self.driver, f)
        
        print(t2.text)
        o_title = t2.text
        
        list_item1 = FlutterElement(self.driver, self.finder.by_value_key(item_key))
        list_item1.click()
        
        time.sleep(1)

        title = FlutterElement(self.driver, self.finder.by_value_key('title'))
        if title.text == o_title:
            return 'OK'
        else:
            return 'Error'
        

if __name__ == '__main__':
    # 테스트할 APK 파일의 위치
    DEF_APP_LOCATION = r'C:\Users\ohyuj\Downloads\app-debug.apk'
    
    print('''
    1. Appium 서버는 실행 했나요?
    2. 에뮬레이터를 실행 했나요?
    3. 에뮬레이터는 정상적으로 동작 중인가요? 에뮬레이터가 멈춰있다면 cold boot하세요.
    4. DEF_APP_LOCATION은 본인의 app-debug.apk를 제대로 가리키고 있나요?
    ''')

    chw = CheckHW(DEF_APP_LOCATION)
    r = chw.test_lab(3)  # 테스트용 입력을 바꿔가면서 해볼 것. 

    if r == 'OK':
        score = 100
    else:
        score = 0
    print(score, r)

