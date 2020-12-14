from selenium.webdriver.common.by import By
from base.basepage import BasePage

class ManagerListPage(BasePage):
    """封装设置-账号设置页面元素、操作"""
    # <<<<<<<<<<<<<<<<<元素>>>>>>>>>>>>>>>>>>>>>>>>>
    # 创建帐号
    manager_add_loc = (By.LINK_TEXT, '创建帐号')
    # 角色
    manager_role_loc = (By.NAME, 'role')
    # 姓名
    manager_inputname_loc = (By.ID, 'inputName')
    # 手机号码
    manager_inputphone_loc = (By.ID, 'inputPhone')
    # 管理权限
    manager_userright_loc = (By.XPATH, "//input[@type='checkbox']/..")
    # 选择区域
    manager_shopselector_lco = (By.CSS_SELECTOR, "div.wss-result")
    # 门店
    manager_shopname_loc = (By.XPATH, "//li[@class='shop']/label")
    # 确定
    # manager_sure_loc = (By.XPATH, "//button[contains(text(),'确定')]")
    manager_sure_loc = (By.XPATH,
                        "//a[@class='btn btn-primary submit']"
                        )
    # 取消
    manager_cancle_loc = (By.XPATH,
                          "//a[@class='btn btn-default cancel']"
                          )
    # 保存
    manager_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")
    # 返回
    manager_return_loc = (By.XPATH, "//button[contains(text(),'返回')]")
    # 记录条数
    manager_account_loc = (By.XPATH,
                           "//p[@class='pull-right']/b")
    # 禁用
    manager_remove_loc = (By.XPATH, "//a[@data-url='/manager/remove']")
    # 确认
    manager_ok_loc = (By.XPATH, "//button[contains(text(),'确认')]")
    # <<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def click_add(self):
        """点击创建帐号"""
        self.click_button('创建帐号', *(self.manager_add_loc))

    def select_role(self, role):
        """选择角色"""
        self.select_list(*(self.manager_role_loc))\
            .select_by_index(role)

    def input_name(self, inputName):
        """输入姓名"""
        self.clear_input_text(*(self.manager_inputname_loc))
        self.input_text(inputName, '姓名',
                        *(self.manager_inputname_loc)
                        )

    def input_phone(self, inputPhone):
        """输入手机号码"""
        self.clear_input_text(*(self.manager_inputphone_loc))
        self.input_text(inputPhone, '手机号码',
                        *(self.manager_inputphone_loc)
                        )
    def select_userright(self, userRight):
        """选择管理权限"""
        self.click_btn_index('管理权限', userRight,
                             *(self.manager_userright_loc)
                             )

    def select_shopselector_and_shopname(self):
        """选择区域和门店"""
        self.click_button('选择区域', *(self.manager_shopselector_lco))
        self.click_button('门店', *(self.manager_shopname_loc))

    def click_sure(self):
        """点击确定"""
        self.click_button('', *(self.manager_sure_loc))

    def click_cancle(self):
        """点击取消"""
        self.click_button('取消', *(self.manager_cancle_loc))

    def click_save(self):
        """点击保存"""
        self.click_button('保存', *(self.manager_save_loc))

    def click_return(self):
        """点击返回"""
        self.click_button('返回', *(self.manager_save_loc))

    def get_name(self):
        """获取保存成功后的账号"""
        count = self.get_tag_text('text', *(self.manager_account_loc))
        self.get_image
        return count

    def  assertTrue(self, old_num, new_num):
        old_num = int(old_num)
        new_num = int(new_num)
        if old_num + 1 == new_num:
            return True

    def click_remove(self):
        """点击禁用"""
        self.click_button('禁用', *(self.manager_remove_loc))

    def click_ok(self):
        """点击确认禁用"""
        self.click_button('确认', *(self.manager_ok_loc))