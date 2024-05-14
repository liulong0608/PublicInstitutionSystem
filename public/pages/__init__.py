# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         __init__.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
# 登录


# 新建单位
supervisor_yes = 'xpath->//div[@title="是"]'  # 是主管
supervisor_no = 'xpath->//div[@title="否"]'  # 否主管
closs_btn = 'xpath->//div[@class="unit_add_head__fNOk6"]/button[2]'  # 关闭
qwwh_btn = 'xpath->//div[@class="ant-modal-confirm-btns"]/button[2]'  # 前往维护

# 新增人员元素
glbBtn_loc = 'css->.ant-card:nth-child(4) .home_auto_btn__LBhkK:nth-child(2)'  # 管理版按钮
ywshBtn_loc = "xpath->//span[contains(.,'业务审核')]"
ywzd_jcBtn_loc = 'xpath->//*[@class="cdk-overlay-pane"]/div/ul/li[3]/a'
xzjsBtn_loc = 'xpath->//ul[@class="menu-root"]/li[4]/div'
ryxzBtn_lco = 'xpath->//div[@class="menu-sub ng-star-inserted"]/ul/li[1]/a'
rysf_loc = 'xpath->//nz-select[@formcontrolname="personalIdentityId"]'

# 新增管理人员
qxsj_loc = 'xpath->//input[@placeholder="请选择起薪时间"]'
name_loc = 'xpath->//input[@placeholder="请输入姓名"]'
gender_loc = 'xpath->//nz-select[@formcontrolname="gender"]'
mz_loc = 'xpath->//nz-select[@nzplaceholder="请选择民族"]'
idNumber_loc = 'xpath->//input[@placeholder="请输入身份证号"]'
birthday_loc = 'xpath->//lib-date-input[@formcontrolname="birthDate"]/div/nz-input-group/input'
zzmm_loc = 'xpath->//nz-select[@nzplaceholder="请选择政治面貌"]'
csrysf_loc = 'xpath->//nz-select[@formcontrolname="initialPersonalIdentityId"]'
jg_loc = 'xpath->//input[@formcontrolname="nativePlace"]'
address_loc = 'xpath->//textarea[@formcontrolname="address"]'
ryly_loc = 'xpath->//nz-select[@nzplaceholder="请选择人员来源"]'
jrdwDate_loc = 'xpath->//lib-date-input[@formcontrolname="joinDate"]/div/nz-input-group/input'
nsjg_loc = 'xpath->//nz-select[@formcontrolname="departmentId"]'
rybz_loc = 'xpath->//textarea[@formcontrolname="staffRemark"]'
cjgzDate_loc = 'xpath->//lib-date-input[@formcontrolname="enterDate"]/div/nz-input-group/input'
ryczCode_loc = 'xpath->//input[@formcontrolname="financialCode"]'
xl_loc = 'xpath->//nz-select[@nzplaceholder="请选择学历"]'
xw_loc = 'xpath->//nz-select[@formcontrolname="degreeTypeId"]'
byDate_loc = 'xpath->//lib-date-input[@formcontrolname="graduateDate"]/div/nz-input-group/input'
shbzh_loc = 'xpath->//input[@formcontrolname="socialismCode"]'
dfzjxl_loc = 'xpath->//nz-select[@formcontrolname="localRankOrg"]'
xd_loc = 'xpath->//nz-select[@formcontrolname="academicSection"]'
gzxxBtn_loc = 'xpath->//div[@class="ant-tabs-nav-list"]/div[2]'
dk_loc = 'xpath->//nz-select[@formcontrolname="surveyStandard"]'
xrzw_loc = 'xpath->//input[@placeholder="请输入职务"]'
xrwzDate_loc = 'xpath->//lib-date-input[@formcontrolname="presentOccupationDate"]/div/nz-input-group/input'
sjgw_loc = 'xpath->//nz-select[@formcontrolname="trueProRankId"]'
zydj_loc = 'xpath->//nz-select[@formcontrolname="levelProRankId"]'
rzydjDate_loc = 'xpath->//input[@placeholder="请选择任职员等级时间"]'
jbgzdygw_loc = 'xpath->//nz-select[@formcontrolname="salaryMappingProRankId"]'
rxgwDate_loc = 'xpath->//lib-date-input[@formcontrolname="jobNowDate"]/div/nz-input-group/input'
xj_loc = 'xpath->//nz-select[@formcontrolname="formerSalaryGrade"]'
xjqknx_loc = 'xpath->//input[@placeholder="请输入薪级起考年限"]'
zxxjs_loc = 'xpath->//nz-select[@formcontrolname="primaryAndHighSchoolTeacher"]'
hs_loc = 'xpath->//nz-select[@formcontrolname="nurse"]'
tg10wage_loc = 'xpath->//nz-select[@formcontrolname="tg10wage"]'
tsjy_loc = 'xpath->//nz-select[@formcontrolname="specialEducation"]'
jbtxmInputs_loc = 'xpath->//tbody[@class="ant-table-tbody ng-star-inserted"]/tr/td/input'
jxxmInputs_loc = 'xpath->//div[@class="ng-star-inserted"]/lib-add-performance/div/nz-table/nz-spin/div/div/nz-table-inner-scroll/div[2]/table/tbody/tr/td/input'
ndkhBtn_loc = 'xpath->//div[@class="ant-tabs-extra-content ng-star-inserted"]/nz-space/nz-space-item[1]/nz-button-group/button[4]'  # 年度考核按钮
ndkhMsg_loc = 'xpath->/html/body/div/div[2]/div/nz-message-container/div/nz-message/div/div/div/span'
sureNdkhBtn_loc = 'css->div.ant-modal-footer button.ant-btn-primary'
gzfjBtn_loc = 'xpath->//div[@class="staff-head-warp"]/lib-staff-head/form/nz-form-item[5]/nz-form-label/label/button'
upload_file_loc = 'css->lib-accessory-action > nz-space > nz-space-item:nth-child(1) > lib-accessory-upload-group > nz-list > nz-list-header > div > div:nth-child(2) > nz-space > nz-space-item:nth-child(1) > lib-accessory-upload > nz-upload > div > div > input[type=files]'
qdfj_file_loc = 'css->div.ant-modal-footer button.ant-btn-primary'
sureBtn_loc = 'xpath->//div[@class="staff-head-warp"]/lib-staff-head/button'
add_msg_loc = 'xpath->/html/body/div/div[2]/div/nz-message-container/div/nz-message/div/div/div/span'

# 新增专业技术人员
zzqk_loc = 'xpath->nz-select[@formcontrolname="professionalConditionInst"]'
ywjyjs_loc = 'xpath->//nz-select[formcontrolname="compulsoryEducation"]'

# 新增事业技术工人
jszs_loc = 'xpath->//nz-select[@formcontrolname="technicalCertificate"]'

# 新增事业普通工人

# 新增运动员
xzDate_loc = 'xpath->//lib-date-input[@formcontrolname="calledTime"]/div/nz-input-group/input'
isMain_loc = 'xpath->//nz-radio-group[@formcontrolname="main"]/label[1]/span/input'
noMain_loc = 'xpath->//nz-radio-group[@formcontrolname="main"]/label[2]/span/input'
sjjcjtdc_loc = 'xpath->//nz-select[@formcontrolname="trueProRankId"]'
jbgzdyjcjtdc_loc = 'xpath->//nz-select[formcontrolname="formerSalaryMappingProRankId"]'
cjjtcc_loc = 'xpath->//nz-select[@formcontrolname="formerSalaryRank"]'
cjjtmc_loc = 'xpath->//nz-select[@formcontrolname="formerSalaryGrade"]'
cjmcDate_loc = 'xpath->//lib-date-input[@formcontrolname="rankingDate"]/div/nz-input-group/input'
# 新增参公人员

# 新增机关技术工人

# 新增机关普通工人

