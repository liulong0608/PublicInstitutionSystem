# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         personnelAdd_page.py  
# @version          v0.2
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
import time

import selenium.common.exceptions

from config import globalparam
from public.common.base_page import BasePage
from public.pages import *

TYSHXYID = '9153262422416699BG'


class PersonnelAddPage(BasePage):

    def preposition(self, grassrootsUnitsID = TYSHXYID):
        self.open('http://192.168.2.194/console/home')  # 打开控制台
        time.sleep(1)
        self.click(glbBtn_loc)  # 点击管理版
        self.hover_and_click(ywshBtn_loc, ywzd_jcBtn_loc)  # 悬停业务审核,点击业务指导基层
        time.sleep(3)
        self.click_linkText(grassrootsUnitsID)  # 进入指定基层单位
        time.sleep(2)
        self.into_new_window()  # 切换到新窗口
        time.sleep(2)
        self.hover_and_click(xzjsBtn_loc, ryxzBtn_lco)  # 悬停人员新增减少菜单,点击新增按钮
        # time.sleep(1)

    # 新增事业管理人员
    def add_manager_page(self, dentityPersonne, salaryDate, name, gender, nationality, idCard, politicalStatus,
                         initialPersonnelIdentity, personnelSource, entryUnitTime, enterDate, personnelFinanceCode,
                         education, graduationTime,
                         position, positionTime, actualPost, rankOfStaff, rankOffStaff_time, postWage, actualPostTime,
                         payScale, payScaleTime, birthplace, address,
                         internalMechanism, remarks, degree,
                         localRankSequence, periodOfStudy, socialSecurityNumber,
                         surveyStandard, primaryAndHighSchoolTeacher, nurse, tg10wage,
                         specialEducation, jbt, jx
                         ):
        """
        :param jx: 绩效
        :param jbt: 津补贴额度
        :param socialSecurityNumber: 社会保障号
        :param personnelFinanceCode: 人员财政编码
        :param dentityPersonne: 人员身份
        :param salaryDate:起薪时间
        :param name:人员姓名
        :param gender:性别
        :param nationality:民族
        :param idCard:身份证号码
        :param politicalStatus:政治面貌
        :param initialPersonnelIdentity:初始人员身份
        :param personnelSource:人员来源
        :param entryUnitTime:进入本单位时间
        :param enterDate:参加工作时间
        :param education:学历
        :param graduationTime:毕业时间
        :param position:现任职务
        :param positionTime:现任职务时间
        :param actualPost:实际岗位
        :param rankOfStaff:职员等级
        :param rankOffStaff_time:现任职员等级时间
        :param postWage:基本工资对应岗位
        :param actualPostTime:任现岗位时间
        :param payScale:薪级
        :param payScaleTime:薪级起考年限
        :param internalMechanism:内设机构
        :param remarks:备注
        :param birthplace:籍贯
        :param address:住址
        :param degree:学位
        :param localRankSequence:地方职级序列
        :param periodOfStudy:学段
        :param surveyStandard:地勘标准
        :param primaryAndHighSchoolTeacher:是否中小学教师
        :param nurse:是否护士
        :param tg10wage:是否提高10%
        :param specialEducation:是否特殊教育
        :return:
        """
        self.preposition()
        self.htmlSelect(rysf_loc, dentityPersonne)  # 选择人员身份
        self.clear_type(qxsj_loc, salaryDate)  # 输入起薪时间
        self.send_keys(name_loc, name)  # 输入人员姓名
        self.htmlSelect(gender_loc, gender)  # 选择性别
        self.htmlSelect(mz_loc, nationality)  # 选择民族
        self.send_keys(idNumber_loc, idCard)  # 输入身份证号码
        self.clear_type(birthday_loc, idCard[6:14])  # 输入出生日期
        self.htmlSelect(zzmm_loc, politicalStatus)  # 选择政治面貌
        if initialPersonnelIdentity is not None:
            self.htmlSelect(csrysf_loc, initialPersonnelIdentity)  # 选择初始人员身份
        else:
            pass
        if birthplace is not None:
            self.send_keys(jg_loc, birthplace)  # 输入籍贯
        else:
            pass
        if address is not None:
            self.send_keys(address_loc, address)  # 输入住址
        else:
            pass
        self.htmlSelect(ryly_loc, personnelSource)  # 选择人员来源
        self.clear_type(jrdwDate_loc, entryUnitTime)  # 输入进入本单位时间
        if internalMechanism is not None:
            try:
                self.htmlSelect(nsjg_loc, internalMechanism)  # 选择所属机构
            except:
                pass
        else:
            pass
        if remarks is not None:
            self.send_keys(rybz_loc, remarks)  # 输入人员备注
        else:
            pass
        self.clear_type(cjgzDate_loc, enterDate)  # 输入参加工作时间
        if personnelFinanceCode is not None:
            self.send_keys(ryczCode_loc, personnelFinanceCode)  # 输入人员财政编码
        else:
            pass
        self.htmlSelect(xl_loc, education)  # 选择学历
        if degree is not None:
            self.htmlSelect(xw_loc, degree)  # 选择学位
        else:
            pass
        self.clear_type(byDate_loc, graduationTime)  # 输入毕业时间
        try:
            if self.get_element(dfzjxl_loc):  # 地方职级序列
                self.htmlSelect(dfzjxl_loc, localRankSequence)
            else:
                pass
        except:
            pass
        try:
            if self.get_element(xd_loc) and periodOfStudy is not None:  # 学段
                self.htmlSelect(xd_loc, periodOfStudy)
            else:
                pass
        except:
            pass
        if socialSecurityNumber is not None:
            self.send_keys(shbzh_loc, socialSecurityNumber)  # 社会保障号
        else:
            pass
        self.click(gzxxBtn_loc)  # 点击工资信息按钮
        try:  # 是否地勘
            if surveyStandard is not None:
                self.htmlSelect(dk_loc, surveyStandard)
            else:
                pass
        except:
            pass
        self.send_keys(xrzw_loc, position)  # 输入现任职务
        self.clear_type(xrwzDate_loc, positionTime)  # 输入现任职务时间
        self.htmlSelect(sjgw_loc, actualPost)  # 选择实际岗位
        try:
            if self.get_element(zydj_loc) and rankOffStaff_time is not None:
                self.htmlSelect(zydj_loc, rankOfStaff)  # 职员等级
                self.clear_type(rzydjDate_loc, rankOffStaff_time)  # 任职员等级时间
            else:
                pass
        except:
            pass
        self.htmlSelect(jbgzdygw_loc, postWage)  # 选择基本工资对应岗位
        self.clear_type(rxgwDate_loc, actualPostTime)  # 输入任现岗位/职员等级时间
        isPayScale = {
            '实际岗位': actualPost,
            '基本工资对应岗位': postWage
        }
        if isPayScale.get('实际岗位') and isPayScale.get('基本工资对应岗位') != '事业管理人员试用期':
            time.sleep(1)
            self.htmlSelect(xj_loc, payScale)  # 选择薪级
            self.clear_type(xjqknx_loc, payScaleTime)  # 输入薪级起考年限
        else:
            pass
        if primaryAndHighSchoolTeacher == '是':
            self.htmlSelect(zxxjs_loc, primaryAndHighSchoolTeacher)  # 是否中小学教师
        else:
            pass
        if nurse == '是':
            self.htmlSelect(hs_loc, nurse)  # 是否护士
        else:
            pass
        if tg10wage == '是' and (primaryAndHighSchoolTeacher == '是' or nurse == '是'):
            try:
                self.htmlSelect(tg10wage_loc, tg10wage)  # 是否提高10%
            except:
                pass
        else:
            pass
        if specialEducation == '是':
            self.htmlSelect(tsjy_loc, specialEducation)  # 是否特殊教育
        else:
            pass
        # 输入津补贴
        try:
            if jbt is not None:
                jbtxm = self.get_elements(jbtxmInputs_loc)
                if jbtxm:  # 如果津补贴存在
                    for jbt_input in jbtxm:
                        jbt_input.send_keys(int(jbt))
            else:
                pass
        except:
            pass
        # 输入绩效项
        try:
            if jx is not None:
                jxxm = self.get_elements(jxxmInputs_loc)
                if jxxm:
                    for jx_input in jxxm:
                        jx_input.send_keys(int(jx))
                else:
                    pass
        except:
            pass

        self.click(gzfjBtn_loc)  # 点击工资报审附件按钮
        time.sleep(0.7)
        self.upload_winFile(upload_file_loc, globalparam.file_path + '附件示例.png')  # 上传附件
        self.click(qdfj_file_loc)  # 点击上传附件确定窗口按钮
        time.sleep(0.5)
        self.click(ndkhBtn_loc)  # 点击年度考核
        try:
            self.click(sureNdkhBtn_loc)  # 点击确认年度考核
        except:
            pass
        self.click(sureBtn_loc)  # 点击保存按钮
        self.fuzzy_assert('录入人员成功', add_msg_loc)  # 断言人员录入成功
        time.sleep(1.5)

    # 新增专业技术人员
    def add_professionalSkill_page(self, dentityPersonne, salaryDate, name, gender, nationality, idCard,
                                   politicalStatus,
                                   initialPersonnelIdentity, personnelSource, entryUnitTime, enterDate,
                                   personnelFinanceCode,
                                   education, graduationTime, compulsoryEducation,
                                   position, positionTime, actualPost, postWage,
                                   actualPostTime,
                                   payScale, payScaleTime, birthplace, address,
                                   internalMechanism, remarks, degree,
                                   full_time, periodOfStudy, socialSecurityNumber,
                                   surveyStandard, primaryAndHighSchoolTeacher, nurse, tg10wage,
                                   specialEducation, jbt, jx):
        """
        :param compulsoryEducation: 是否义务教育教师
        :param jx: 绩效
        :param jbt: 津补贴额度
        :param socialSecurityNumber: 社会保障号
        :param personnelFinanceCode: 人员财政编码
        :param dentityPersonne: 人员身份
        :param salaryDate:起薪时间
        :param name:人员姓名
        :param gender:性别
        :param nationality:民族
        :param idCard:身份证号码
        :param politicalStatus:政治面貌
        :param initialPersonnelIdentity:初始人员身份
        :param personnelSource:人员来源
        :param entryUnitTime:进入本单位时间
        :param enterDate:参加工作时间
        :param education:学历
        :param graduationTime:毕业时间
        :param position:现任职务
        :param positionTime:现任职务时间
        :param actualPost:实际岗位
        :param postWage:基本工资对应岗位
        :param actualPostTime:任现岗位时间
        :param payScale:薪级
        :param payScaleTime:薪级起考年限
        :param internalMechanism:内设机构
        :param remarks:备注
        :param birthplace:籍贯
        :param address:住址
        :param degree:学位
        :param full_time:专职情况
        :param periodOfStudy:学段
        :param surveyStandard:地勘标准
        :param primaryAndHighSchoolTeacher:是否中小学教师
        :param nurse:是否护士
        :param tg10wage:是否提高10%
        :param specialEducation:是否特殊教育
        :return:
        """
        self.preposition()
        self.htmlSelect(rysf_loc, dentityPersonne)  # 选择人员身份
        self.clear_type(qxsj_loc, salaryDate)  # 输入起薪时间
        self.send_keys(name_loc, name)  # 输入人员姓名
        self.htmlSelect(gender_loc, gender)  # 选择性别
        self.htmlSelect(mz_loc, nationality)  # 选择民族
        self.send_keys(idNumber_loc, idCard)  # 输入身份证号码
        self.clear_type(birthday_loc, idCard[6:14])  # 输入出生日期
        self.htmlSelect(zzmm_loc, politicalStatus)  # 选择政治面貌
        if initialPersonnelIdentity is not None:
            self.htmlSelect(csrysf_loc, initialPersonnelIdentity)  # 选择初始人员身份
        else:
            pass
        if birthplace is not None:
            self.send_keys(jg_loc, birthplace)  # 输入籍贯
        else:
            pass
        if address is not None:
            self.send_keys(address_loc, address)  # 输入住址
        else:
            pass
        self.htmlSelect(ryly_loc, personnelSource)  # 选择人员来源
        self.clear_type(jrdwDate_loc, entryUnitTime)  # 输入进入本单位时间
        if internalMechanism is not None:
            try:
                self.htmlSelect(nsjg_loc, internalMechanism)  # 选择所属机构
            except:
                pass
        else:
            pass
        if remarks is not None:
            self.send_keys(rybz_loc, remarks)  # 输入人员备注
        else:
            pass
        self.clear_type(cjgzDate_loc, enterDate)  # 输入参加工作时间
        if personnelFinanceCode is not None:
            self.send_keys(ryczCode_loc, personnelFinanceCode)  # 输入人员财政编码
        else:
            pass
        self.htmlSelect(xl_loc, education)  # 选择学历
        if degree is not None:
            self.htmlSelect(xw_loc, degree)  # 选择学位
        else:
            pass
        self.clear_type(byDate_loc, graduationTime)  # 输入毕业时间
        try:
            if self.get_element(zzqk_loc) and full_time is not None:  # 专职情况
                self.htmlSelect(zzqk_loc, full_time)
            else:
                pass
        except:
            pass
        try:
            if xd_loc and periodOfStudy is not None:  # 学段
                self.htmlSelect(xd_loc, periodOfStudy)
            else:
                pass
        except:
            pass
        if socialSecurityNumber is not None:
            self.send_keys(shbzh_loc, socialSecurityNumber)  # 社会保障号
        else:
            pass
        self.click(gzxxBtn_loc)  # 点击工资信息按钮

        if surveyStandard is not None:
            try:  # 是否地勘
                self.htmlSelect(dk_loc, surveyStandard)
            except:
                pass
        else:
            pass
        self.htmlSelect(ywjyjs_loc, compulsoryEducation)  # 是否义务教育教师
        self.send_keys(xrzw_loc, position)  # 输入现任职务
        self.clear_type(xrwzDate_loc, positionTime)  # 输入现任职务时间
        self.htmlSelect(sjgw_loc, actualPost)  # 选择实际岗位
        self.htmlSelect(jbgzdygw_loc, postWage)  # 选择基本工资对应岗位
        self.clear_type(rxgwDate_loc, actualPostTime)  # 输入任现岗位/职员等级时间
        isPayScale = {
            '实际岗位': actualPost,
            '基本工资对应岗位': postWage
        }
        if isPayScale.get('实际岗位') and isPayScale.get('基本工资对应岗位') != '事业专业技术人员试用期':
            self.htmlSelect(xj_loc, payScale)  # 选择薪级
            self.clear_type(xjqknx_loc, payScaleTime)  # 输入薪级起考年限
        else:
            pass
        if compulsoryEducation == '否':
            if primaryAndHighSchoolTeacher == '是':
                self.htmlSelect(zxxjs_loc,
                                primaryAndHighSchoolTeacher)  # 是否中小学教师
            else:
                pass
            if nurse == '是':
                self.htmlSelect(hs_loc, nurse)  # 是否护士
            else:
                pass
            if tg10wage == '是' and (primaryAndHighSchoolTeacher == '是' or nurse == '是'):
                try:
                    self.htmlSelect(tg10wage_loc, tg10wage)  # 是否提高10%
                except:
                    pass
            else:
                pass
        else:
            pass
        if specialEducation == '是':
            self.htmlSelect(tsjy_loc, specialEducation)  # 是否特殊教育
        else:
            pass
        # 输入津补贴
        try:
            if jbt is not None:
                jbtxm = self.get_elements(jbtxmInputs_loc)
                if jbtxm:  # 如果津补贴存在
                    for jbt_input in jbtxm:
                        jbt_input.send_keys(int(jbt))
            else:
                pass
        except:
            pass
        # 输入绩效项
        try:
            if jx is not None:
                jxxm = self.get_elements(jxxmInputs_loc)
                if jxxm:
                    for jx_input in jxxm:
                        jx_input.send_keys(int(jx))
                else:
                    pass
        except:
            pass

        self.click(gzfjBtn_loc)  # 点击工资报审附件按钮
        self.upload_winFile(upload_file_loc, globalparam.file_path + '附件示例.png')  # 上传附件
        self.click(qdfj_file_loc)  # 点击上传附件确定窗口按钮
        time.sleep(0.5)
        self.click(ndkhBtn_loc)  # 点击年度考核
        try:
            self.click(sureNdkhBtn_loc)  # 点击确认年度考核
        except:
            pass
        self.click(sureBtn_loc)  # 点击保存按钮
        self.fuzzy_assert('录入人员成功', add_msg_loc)  # 断言人员录入成功
        time.sleep(1.5)

    # 新增事业技术工人
    def add_skilledWorker_page(self, dentityPersonne, salaryDate, name, gender, nationality, idCard,
                               politicalStatus,
                               initialPersonnelIdentity, personnelSource, entryUnitTime, enterDate,
                               personnelFinanceCode,
                               education, graduationTime, technicalCertificate,
                               position, positionTime, actualPost, postWage,
                               actualPostTime,
                               payScale, payScaleTime, birthplace, address,
                               internalMechanism, remarks, degree,
                               periodOfStudy, socialSecurityNumber,
                               surveyStandard,
                               specialEducation, jbt, jx):
        """
        :param technicalCertificate: 是否取得技术证书
        :param jx: 绩效
        :param jbt: 津补贴额度
        :param socialSecurityNumber: 社会保障号
        :param personnelFinanceCode: 人员财政编码
        :param dentityPersonne: 人员身份
        :param salaryDate:起薪时间
        :param name:人员姓名
        :param gender:性别
        :param nationality:民族
        :param idCard:身份证号码
        :param politicalStatus:政治面貌
        :param initialPersonnelIdentity:初始人员身份
        :param personnelSource:人员来源
        :param entryUnitTime:进入本单位时间
        :param enterDate:参加工作时间
        :param education:学历
        :param graduationTime:毕业时间
        :param position:现任职务
        :param positionTime:现任职务时间
        :param actualPost:实际岗位
        :param postWage:基本工资对应岗位
        :param actualPostTime:任现岗位时间
        :param payScale:薪级
        :param payScaleTime:薪级起考年限
        :param internalMechanism:内设机构
        :param remarks:备注
        :param birthplace:籍贯
        :param address:住址
        :param degree:学位
        :param periodOfStudy:学段
        :param surveyStandard:地勘标准
        :param specialEducation:是否特殊教育
        :return:
        """
        self.preposition()
        self.htmlSelect(rysf_loc, dentityPersonne)  # 选择人员身份
        self.clear_type(qxsj_loc, salaryDate)  # 输入起薪时间
        self.send_keys(name_loc, name)  # 输入人员姓名
        self.htmlSelect(gender_loc, gender)  # 选择性别
        self.htmlSelect(mz_loc, nationality)  # 选择民族
        self.send_keys(idNumber_loc, idCard)  # 输入身份证号码
        self.clear_type(birthday_loc, idCard[6:14])  # 输入出生日期
        self.htmlSelect(zzmm_loc, politicalStatus)  # 选择政治面貌
        if initialPersonnelIdentity is not None:
            self.htmlSelect(csrysf_loc, initialPersonnelIdentity)  # 选择初始人员身份
        else:
            pass
        if birthplace is not None:
            self.send_keys(jg_loc, birthplace)  # 输入籍贯
        else:
            pass
        if address is not None:
            self.send_keys(address_loc, address)  # 输入住址
        else:
            pass
        self.htmlSelect(ryly_loc, personnelSource)  # 选择人员来源
        self.clear_type(jrdwDate_loc, entryUnitTime)  # 输入进入本单位时间
        if internalMechanism is not None:
            try:
                self.htmlSelect(nsjg_loc, internalMechanism)  # 选择所属机构
            except:
                pass
        else:
            pass
        if remarks is not None:
            self.send_keys(rybz_loc, remarks)  # 输入人员备注
        else:
            pass
        self.clear_type(cjgzDate_loc, enterDate)  # 输入参加工作时间
        if personnelFinanceCode is not None:
            self.send_keys(ryczCode_loc, personnelFinanceCode)  # 输入人员财政编码
        else:
            pass
        self.htmlSelect(xl_loc, education)  # 选择学历
        if degree is not None:
            self.htmlSelect(xw_loc, degree)  # 选择学位
        else:
            pass
        self.clear_type(byDate_loc, graduationTime)  # 输入毕业时间
        try:
            if jszs_loc and technicalCertificate is not None:  # 是否取得技术证书
                self.htmlSelect(zzqk_loc, jszs_loc)
            else:
                pass
        except:
            pass
        try:
            if xd_loc and periodOfStudy is not None:  # 学段
                self.htmlSelect(xd_loc, periodOfStudy)
            else:
                pass
        except:
            pass
        if socialSecurityNumber is not None:
            self.send_keys(shbzh_loc, socialSecurityNumber)  # 社会保障号
        else:
            pass
        self.click(gzxxBtn_loc)  # 点击工资信息按钮

        if surveyStandard is not None:
            try:  # 是否地勘
                self.htmlSelect(dk_loc, surveyStandard)
            except:
                pass
        else:
            pass
        self.send_keys(xrzw_loc, position)  # 输入现任职务
        self.clear_type(xrwzDate_loc, positionTime)  # 输入现任职务时间
        self.htmlSelect(sjgw_loc, actualPost)  # 选择实际岗位
        self.htmlSelect(jbgzdygw_loc, postWage)  # 选择基本工资对应岗位
        self.clear_type(rxgwDate_loc, actualPostTime)  # 输入任现岗位/职员等级时间
        isPayScale = {
            '实际岗位': actualPost,
            '基本工资对应岗位': postWage
        }
        if isPayScale.get('实际岗位') and isPayScale.get(
                '基本工资对应岗位') != '事业技术工人学徒期' or '事业技术工人熟练期':
            self.htmlSelect(xj_loc, payScale)  # 选择薪级
            self.clear_type(xjqknx_loc, payScaleTime)  # 输入薪级起考年限
        else:
            pass
        if specialEducation == '是':
            self.htmlSelect(tsjy_loc, specialEducation)  # 是否特殊教育
        else:
            pass
        # 输入津补贴
        try:
            if jbt is not None:
                jbtxm = self.get_elements(jbtxmInputs_loc)
                if jbtxm:  # 如果津补贴存在
                    for jbt_input in jbtxm:
                        jbt_input.send_keys(int(jbt))
            else:
                pass
        except:
            pass
        # 输入绩效项
        try:
            if jx is not None:
                jxxm = self.get_elements(jxxmInputs_loc)
                if jxxm:
                    for jx_input in jxxm:
                        jx_input.send_keys(int(jx))
                else:
                    pass
        except:
            pass

        self.click(gzfjBtn_loc)  # 点击工资报审附件按钮
        self.upload_winFile(upload_file_loc, globalparam.file_path + '附件示例.png')  # 上传附件
        self.click(qdfj_file_loc)  # 点击上传附件确定窗口按钮
        time.sleep(0.5)
        self.click(ndkhBtn_loc)  # 点击年度考核
        try:
            self.click(sureNdkhBtn_loc)  # 点击确认年度考核
        except:
            pass
        self.click(sureBtn_loc)  # 点击保存按钮
        self.fuzzy_assert('录入人员成功', add_msg_loc)  # 断言人员录入成功
        time.sleep(1.5)

    # 新增事业普通工人
    def add_ordinaryWorker_page(self, dentityPersonne, salaryDate, name, gender, nationality, idCard,
                                politicalStatus,
                                initialPersonnelIdentity, personnelSource, entryUnitTime, enterDate,
                                personnelFinanceCode,
                                education, graduationTime,
                                position, positionTime, actualPost, postWage,
                                actualPostTime,
                                payScale, payScaleTime, birthplace, address,
                                internalMechanism, remarks, degree,
                                periodOfStudy, socialSecurityNumber,
                                surveyStandard,
                                specialEducation, jbt, jx):
        """
        :param jx: 绩效
        :param jbt: 津补贴额度
        :param socialSecurityNumber: 社会保障号
        :param personnelFinanceCode: 人员财政编码
        :param dentityPersonne: 人员身份
        :param salaryDate:起薪时间
        :param name:人员姓名
        :param gender:性别
        :param nationality:民族
        :param idCard:身份证号码
        :param politicalStatus:政治面貌
        :param initialPersonnelIdentity:初始人员身份
        :param personnelSource:人员来源
        :param entryUnitTime:进入本单位时间
        :param enterDate:参加工作时间
        :param education:学历
        :param graduationTime:毕业时间
        :param position:现任职务
        :param positionTime:现任职务时间
        :param actualPost:实际岗位
        :param postWage:基本工资对应岗位
        :param actualPostTime:任现岗位时间
        :param payScale:薪级
        :param payScaleTime:薪级起考年限
        :param internalMechanism:内设机构
        :param remarks:备注
        :param birthplace:籍贯
        :param address:住址
        :param degree:学位
        :param periodOfStudy:学段
        :param surveyStandard:地勘标准
        :param specialEducation:是否特殊教育
        :return:
        """
        self.preposition()
        self.htmlSelect(rysf_loc, dentityPersonne)  # 选择人员身份
        self.clear_type(qxsj_loc, salaryDate)  # 输入起薪时间
        self.send_keys(name_loc, name)  # 输入人员姓名
        self.htmlSelect(gender_loc, gender)  # 选择性别
        self.htmlSelect(mz_loc, nationality)  # 选择民族
        self.send_keys(idNumber_loc, idCard)  # 输入身份证号码
        self.clear_type(birthday_loc, idCard[6:14])  # 输入出生日期
        self.htmlSelect(zzmm_loc, politicalStatus)  # 选择政治面貌
        if initialPersonnelIdentity is not None:
            self.htmlSelect(csrysf_loc, initialPersonnelIdentity)  # 选择初始人员身份
        else:
            pass
        if birthplace is not None:
            self.send_keys(jg_loc, birthplace)  # 输入籍贯
        else:
            pass
        if address is not None:
            self.send_keys(address_loc, address)  # 输入住址
        else:
            pass
        self.htmlSelect(ryly_loc, personnelSource)  # 选择人员来源
        self.clear_type(jrdwDate_loc, entryUnitTime)  # 输入进入本单位时间
        if internalMechanism is not None:
            try:
                self.htmlSelect(nsjg_loc, internalMechanism)  # 选择所属机构
            except:
                pass
        else:
            pass
        if remarks is not None:
            self.send_keys(rybz_loc, remarks)  # 输入人员备注
        else:
            pass
        self.clear_type(cjgzDate_loc, enterDate)  # 输入参加工作时间
        if personnelFinanceCode is not None:
            self.send_keys(ryczCode_loc, personnelFinanceCode)  # 输入人员财政编码
        else:
            pass
        self.htmlSelect(xl_loc, education)  # 选择学历
        if degree is not None:
            self.htmlSelect(xw_loc, degree)  # 选择学位
        else:
            pass
        self.clear_type(byDate_loc, graduationTime)  # 输入毕业时间
        try:
            if xd_loc and periodOfStudy is not None:  # 学段
                self.htmlSelect(xd_loc, periodOfStudy)
            else:
                pass
        except:
            pass
        if socialSecurityNumber is not None:
            self.send_keys(shbzh_loc, socialSecurityNumber)  # 社会保障号
        else:
            pass
        self.click(gzxxBtn_loc)  # 点击工资信息按钮

        if surveyStandard is not None:
            try:  # 是否地勘
                self.htmlSelect(dk_loc, surveyStandard)
            except:
                pass
        else:
            pass
        self.send_keys(xrzw_loc, position)  # 输入现任职务
        self.clear_type(xrwzDate_loc, positionTime)  # 输入现任职务时间
        self.htmlSelect(sjgw_loc, actualPost)  # 选择实际岗位
        self.htmlSelect(jbgzdygw_loc, postWage)  # 选择基本工资对应岗位
        self.clear_type(rxgwDate_loc, actualPostTime)  # 输入任现岗位/职员等级时间
        isPayScale = {
            '实际岗位': actualPost,
            '基本工资对应岗位': postWage
        }
        if isPayScale.get('实际岗位') and isPayScale.get(
                '基本工资对应岗位') != '事业普通工人学徒期' or '事业普通工人熟练期':
            self.htmlSelect(xj_loc, payScale)  # 选择薪级
            self.clear_type(xjqknx_loc, payScaleTime)  # 输入薪级起考年限
        else:
            pass
        if specialEducation == '是':
            self.htmlSelect(tsjy_loc, specialEducation)  # 是否特殊教育
        else:
            pass
        # 输入津补贴
        try:
            if jbt is not None:
                jbtxm = self.get_elements(jbtxmInputs_loc)
                if jbtxm:  # 如果津补贴存在
                    for jbt_input in jbtxm:
                        jbt_input.send_keys(int(jbt))
            else:
                pass
        except:
            pass
        # 输入绩效项
        try:
            if jx is not None:
                jxxm = self.get_elements(jxxmInputs_loc)
                if jxxm:
                    for jx_input in jxxm:
                        jx_input.send_keys(int(jx))
                else:
                    pass
        except:
            pass

        self.click(gzfjBtn_loc)  # 点击工资报审附件按钮
        self.upload_winFile(upload_file_loc, globalparam.file_path + '附件示例.png')  # 上传附件
        self.click(qdfj_file_loc)  # 点击上传附件确定窗口按钮
        time.sleep(0.5)
        self.click(ndkhBtn_loc)  # 点击年度考核
        try:
            self.click(sureNdkhBtn_loc)  # 点击确认年度考核
        except:
            pass
        self.click(sureBtn_loc)  # 点击保存按钮
        self.fuzzy_assert('录入人员成功', add_msg_loc)  # 断言人员录入成功
        time.sleep(1.5)

    # 新增运动员
    def add_sportsman_page(self, dentityPersonne, salaryDate, name, gender, nationality, idCard,
                           politicalStatus,
                           initialPersonnelIdentity, personnelSource, entryUnitTime, enterDate,
                           personnelFinanceCode,
                           education, graduationTime, birthplace, address,
                           internalMechanism, calledTime, whetherMain, remarks, degree, socialSecurityNumber,
                           trueProRankId,
                           formerSalaryMappingProRankId, formerSalaryRank, formerSalaryGrade, rankingDate, jbt, jx):
        """
        :param rankingDate: 成绩津贴名次取得时间
        :param formerSalaryGrade: 成绩津贴名次
        :param formerSalaryRank: 成绩津贴层次
        :param formerSalaryMappingProRankId: 基本工资对应基础津贴档次
        :param trueProRankId: 实际基础津贴档次
        :param whetherMain: 是否主力
        :param calledTime: 选招时间
        :param jx: 绩效
        :param jbt: 津补贴额度
        :param socialSecurityNumber: 社会保障号
        :param personnelFinanceCode: 人员财政编码
        :param dentityPersonne: 人员身份
        :param salaryDate:起薪时间
        :param name:人员姓名
        :param gender:性别
        :param nationality:民族
        :param idCard:身份证号码
        :param politicalStatus:政治面貌
        :param initialPersonnelIdentity:初始人员身份
        :param personnelSource:人员来源
        :param entryUnitTime:进入本单位时间
        :param enterDate:参加工作时间
        :param education:学历
        :param graduationTime:毕业时间
        :param internalMechanism:内设机构
        :param remarks:备注
        :param birthplace:籍贯
        :param address:住址
        :param degree:学位
        :return:
        """
        self.preposition()
        self.htmlSelect(rysf_loc, dentityPersonne)  # 选择人员身份
        self.clear_type(qxsj_loc, salaryDate)  # 输入起薪时间
        self.send_keys(name_loc, name)  # 输入人员姓名
        self.htmlSelect(gender_loc, gender)  # 选择性别
        self.htmlSelect(mz_loc, nationality)  # 选择民族
        self.send_keys(idNumber_loc, idCard)  # 输入身份证号码
        self.clear_type(birthday_loc, idCard[6:14])  # 输入出生日期
        self.htmlSelect(zzmm_loc, politicalStatus)  # 选择政治面貌
        if initialPersonnelIdentity is not None:
            self.htmlSelect(csrysf_loc, initialPersonnelIdentity)  # 选择初始人员身份
        else:
            pass
        if birthplace is not None:
            self.send_keys(jg_loc, birthplace)  # 输入籍贯
        else:
            pass
        if address is not None:
            self.send_keys(address_loc, address)  # 输入住址
        else:
            pass
        self.htmlSelect(ryly_loc, personnelSource)  # 选择人员来源
        self.clear_type(jrdwDate_loc, entryUnitTime)  # 输入进入本单位时间
        if internalMechanism is not None:
            try:
                self.htmlSelect(nsjg_loc, internalMechanism)  # 选择所属机构
            except:
                pass
        else:
            pass
        self.clear_type(xzDate_loc, calledTime)  # 选招时间
        if whetherMain == '是':  # 是否主力
            self.click(isMain_loc)
        else:
            self.click(noMain_loc)
        if remarks is not None:
            self.send_keys(rybz_loc, remarks)  # 输入人员备注
        else:
            pass
        self.clear_type(cjgzDate_loc, enterDate)  # 输入入队时间
        if personnelFinanceCode is not None:
            self.send_keys(ryczCode_loc, personnelFinanceCode)  # 输入人员财政编码
        else:
            pass
        self.htmlSelect(xl_loc, education)  # 选择学历
        if degree is not None:
            self.htmlSelect(xw_loc, degree)  # 选择学位
        else:
            pass
        self.clear_type(byDate_loc, graduationTime)  # 输入毕业时间
        if socialSecurityNumber is not None:
            self.send_keys(shbzh_loc, socialSecurityNumber)  # 社会保障号
        else:
            pass
        self.click(gzxxBtn_loc)  # 点击工资信息按钮

        self.htmlSelect(sjjcjtdc_loc, trueProRankId)  # 选择实际基础津贴档次
        self.htmlSelect(jbgzdyjcjtdc_loc,
                        formerSalaryMappingProRankId)  # 选择基本工资对应基础津贴档次
        self.htmlSelect(cjjtcc_loc, formerSalaryRank)  # 选择成绩津贴层次
        self.htmlSelect(cjjtmc_loc, formerSalaryGrade)  # 选择成绩津贴名次
        self.clear_type(cjmcDate_loc, rankingDate)  # 输入成绩津贴名次取得时间

        # 输入津补贴
        try:
            if jbt is not None:
                jbtxm = self.get_elements(jbtxmInputs_loc)
                if jbtxm:  # 如果津补贴存在
                    for jbt_input in jbtxm:
                        jbt_input.send_keys(int(jbt))
            else:
                pass
        except:
            pass
        # 输入绩效项
        try:
            if jx is not None:
                jxxm = self.get_elements(jxxmInputs_loc)
                if jxxm:
                    for jx_input in jxxm:
                        jx_input.send_keys(int(jx))
                else:
                    pass
        except:
            pass

        self.click(gzfjBtn_loc)  # 点击工资报审附件按钮
        self.upload_winFile(upload_file_loc, globalparam.file_path + '附件示例.png')  # 上传附件
        self.click(qdfj_file_loc)  # 点击上传附件确定窗口按钮
        time.sleep(0.5)
        self.click(ndkhBtn_loc)  # 点击年度考核
        try:
            self.click(sureNdkhBtn_loc)  # 点击确认年度考核
        except:
            pass
        self.click(sureBtn_loc)  # 点击保存按钮
        self.fuzzy_assert('录入人员成功', add_msg_loc)  # 断言人员录入成功
        time.sleep(1.5)
