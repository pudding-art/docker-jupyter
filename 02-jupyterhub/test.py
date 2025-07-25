#!/usr/bin/env python3
"""
JupyterHub 测试脚本
测试 JupyterHub 服务的各项功能是否正常
"""

import requests
import time
import json
import sys
import os
from urllib.parse import urljoin
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class JupyterHubTester:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.username = "testuser"
        
    def test_server_status(self):
        """测试服务器是否可访问"""
        logger.info("测试 JupyterHub 服务器状态...")
        try:
            response = self.session.get(self.base_url, timeout=10)
            if response.status_code == 200:
                logger.info("✅ JupyterHub 服务器可访问")
                return True
            else:
                logger.error(f"❌ 服务器返回状态码: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ 无法连接到服务器: {e}")
            return False
    
    def test_hub_api(self):
        """测试 Hub API"""
        logger.info("测试 Hub API...")
        try:
            api_url = urljoin(self.base_url, "/hub/api/")
            response = self.session.get(api_url, timeout=10)
            if response.status_code in [200, 401, 403]:  # API 存在但可能需要认证
                logger.info("✅ Hub API 可访问")
                return True
            else:
                logger.error(f"❌ API 状态码: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ API 请求失败: {e}")
            return False
    
    def test_login_page(self):
        """测试登录页面"""
        logger.info("测试登录页面...")
        try:
            login_url = urljoin(self.base_url, "/hub/login")
            response = self.session.get(login_url, timeout=10)
            if response.status_code == 200:
                if "login" in response.text.lower() or "username" in response.text.lower():
                    logger.info("✅ 登录页面正常")
                    return True
                else:
                    logger.warning("⚠️ 登录页面内容异常")
                    return False
            else:
                logger.error(f"❌ 登录页面状态码: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ 登录页面请求失败: {e}")
            return False
    
    def get_fresh_xsrf_token(self, url=None):
        """获取最新的 XSRF token"""
        if url is None:
            url = urljoin(self.base_url, "/hub/")
        
        try:
            # 获取页面以刷新 XSRF token
            response = self.session.get(url, timeout=10)
            if response.status_code != 200:
                logger.warning(f"无法获取页面刷新 XSRF: {response.status_code}")
                return None
            
            # 从页面中提取 XSRF token
            from html.parser import HTMLParser
            
            class XSRFParser(HTMLParser):
                def __init__(self):
                    super().__init__()
                    self.xsrf_token = None
                
                def handle_starttag(self, tag, attrs):
                    if tag == "input":
                        attr_dict = dict(attrs)
                        if attr_dict.get("name") == "_xsrf":
                            self.xsrf_token = attr_dict.get("value")
            
            parser = XSRFParser()
            parser.feed(response.text)
            
            if parser.xsrf_token:
                return parser.xsrf_token
            
            # 如果页面中没有，尝试从 cookies 获取
            for cookie in self.session.cookies:
                if cookie.name == "_xsrf":
                    return cookie.value
            
            return None
            
        except Exception as e:
            logger.warning(f"获取 XSRF token 失败: {e}")
            return None
    def test_dummy_auth_login(self):
        """测试 DummyAuthenticator 登录"""
        logger.info("测试用户登录...")
        try:
            # 获取登录页面
            login_url = urljoin(self.base_url, "/hub/login")
            response = self.session.get(login_url)
            
            if response.status_code != 200:
                logger.error(f"❌ 无法获取登录页面: {response.status_code}")
                return False
            
            # 获取最新的 XSRF token
            xsrf_token = self.get_fresh_xsrf_token(login_url)
            
            # 准备登录数据
            login_data = {
                "username": self.username,
                "password": "dummy"  # DummyAuthenticator 允许任何密码
            }
            
            if xsrf_token:
                login_data["_xsrf"] = xsrf_token
                logger.info("✅ 已获取 XSRF token")
            else:
                logger.warning("⚠️ 未获取到 XSRF token，继续尝试登录")
            
            # 尝试登录
            response = self.session.post(login_url, data=login_data, allow_redirects=False)
            
            if response.status_code in [302, 303]:  # 重定向表示登录成功
                logger.info("✅ 用户登录成功")
                return True
            elif response.status_code == 200:
                if "dashboard" in response.text.lower() or "spawn" in response.text.lower():
                    logger.info("✅ 用户登录成功（已在用户页面）")
                    return True
                else:
                    logger.error("❌ 登录失败，仍在登录页面")
                    if "invalid" in response.text.lower() or "expired" in response.text.lower():
                        logger.error("提示：可能是 XSRF token 问题")
                    return False
            else:
                logger.error(f"❌ 登录请求状态码: {response.status_code}")
                if response.status_code == 403:
                    logger.error("提示：403 错误通常是 XSRF token 缺失或无效")
                return False
        except Exception as e:
            logger.error(f"❌ 登录请求失败: {e}")
            return False
    
    def test_user_server_spawn(self):
        """测试用户服务器启动"""
        logger.info("测试用户服务器启动...")
        try:
            spawn_url = urljoin(self.base_url, f"/hub/spawn/{self.username}")
            user_url = urljoin(self.base_url, f"/user/{self.username}")
            
            # 首先检查是否已有服务器运行
            response = self.session.get(user_url, allow_redirects=False, timeout=5)
            if response.status_code == 200:
                logger.info("✅ 用户服务器已运行")
                return True
            
            # 检查用户是否已登录并有权限启动服务器
            hub_url = urljoin(self.base_url, "/hub/")
            response = self.session.get(hub_url, allow_redirects=False, timeout=10)
            
            if response.status_code == 302 and 'login' in response.headers.get('Location', ''):
                logger.error("❌ 用户未登录，无法启动服务器")
                return False
            
            # 获取spawn页面以确保有最新的session状态
            logger.info("获取 spawn 页面...")
            response = self.session.get(spawn_url, timeout=10)
            
            if response.status_code == 302:
                # 如果被重定向，检查重定向地址
                location = response.headers.get('Location', '')
                if f'/user/{self.username}' in location:
                    logger.info("✅ 用户服务器已启动（重定向检测）")
                    return True
                elif 'login' in location:
                    logger.error("❌ 被重定向到登录页面，用户可能未认证")
                    return False
            
            # 获取最新的 XSRF token（关键修复）
            xsrf_token = self.get_fresh_xsrf_token(spawn_url)
            
            # 准备启动数据
            spawn_data = {}
            if xsrf_token:
                spawn_data["_xsrf"] = xsrf_token
                logger.info("✅ 已获取启动页面的最新 XSRF token")
            else:
                logger.warning("⚠️ 未获取到 XSRF token，尝试继续")
            
            # 尝试启动服务器
            logger.info("发送服务器启动请求...")
            response = self.session.post(spawn_url, data=spawn_data, allow_redirects=False, timeout=60)
            
            if response.status_code == 403:
                logger.error("❌ 启动请求被拒绝（403）")
                logger.error("可能原因：XSRF token不匹配或权限不足")
                
                # 尝试重新获取token并再试一次
                logger.info("尝试重新获取 XSRF token...")
                time.sleep(1)
                fresh_token = self.get_fresh_xsrf_token(spawn_url)
                if fresh_token and fresh_token != xsrf_token:
                    logger.info("获取到新的 XSRF token，重试启动...")
                    spawn_data["_xsrf"] = fresh_token
                    response = self.session.post(spawn_url, data=spawn_data, allow_redirects=False, timeout=60)
                
                if response.status_code == 403:
                    logger.error("❌ 重试后仍然被拒绝，可能存在配置问题")
                    return False
            
            if response.status_code in [200, 202]:
                logger.info("✅ 启动请求已接受，等待容器启动...")
            elif response.status_code == 302:
                location = response.headers.get('Location', '')
                if f'/user/{self.username}' in location:
                    logger.info("✅ 启动成功，已重定向到用户服务器")
                    return True
                else:
                    logger.info(f"收到重定向到: {location}")
            elif response.status_code != 403:  # 403已经在上面处理过了
                logger.warning(f"⚠️ 启动请求状态码: {response.status_code}")
            
            # 等待服务器启动完成
            logger.info("等待用户服务器启动完成...")
            for i in range(10):  # 最多等待60秒
                time.sleep(1)
                try:
                    response = self.session.get(user_url, allow_redirects=False, timeout=5)
                    if response.status_code == 200:
                        logger.info("✅ 用户服务器启动成功")
                        return True
                    elif response.status_code == 503:
                        # 服务器正在启动中
                        if i % 10 == 0:
                            logger.info(f"服务器启动中... ({i+1}/60秒)")
                    elif response.status_code == 302:
                        # 检查重定向目标
                        location = response.headers.get('Location', '')
                        if 'spawn' in location:
                            if i % 10 == 0:
                                logger.info(f"等待容器创建... ({i+1}/60秒)")
                        else:
                            logger.info(f"收到重定向: {location}")
                    else:
                        if i % 10 == 0:
                            logger.info(f"等待启动，状态码: {response.status_code} ({i+1}/60秒)")
                except Exception as e:
                    if i % 10 == 0:
                        logger.info(f"等待服务器响应... ({i+1}/60秒)")
            
            logger.error("❌ 用户服务器启动超时（60秒）")
            return False
                
        except Exception as e:
            logger.error(f"❌ 服务器启动测试失败: {e}")
            return False
    
    def test_notebook_interface(self):
        """测试 Notebook 界面"""
        logger.info("测试 Notebook 界面...")
        try:
            user_url = urljoin(self.base_url, f"/user/{self.username}")
            response = self.session.get(user_url, timeout=10)
            
            if response.status_code == 200:
                content = response.text.lower()
                if any(keyword in content for keyword in ["jupyter", "notebook", "tree", "lab"]):
                    logger.info("✅ Notebook 界面正常")
                    return True
                else:
                    logger.warning("⚠️ Notebook 界面内容异常")
                    return False
            else:
                logger.error(f"❌ Notebook 界面状态码: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Notebook 界面测试失败: {e}")
            return False
    
    def test_user_authentication_status(self):
        """测试用户认证状态"""
        logger.info("检查用户认证状态...")
        try:
            # 检查是否已登录
            hub_url = urljoin(self.base_url, "/hub/")
            response = self.session.get(hub_url, allow_redirects=False, timeout=10)
            
            if response.status_code == 302:
                location = response.headers.get('Location', '')
                if 'login' in location:
                    logger.info("⚠️ 用户未登录，将被重定向到登录页面")
                    return False
                else:
                    logger.info("✅ 用户已登录")
                    return True
            elif response.status_code == 200:
                if "logout" in response.text.lower() or "spawn" in response.text.lower():
                    logger.info("✅ 用户已登录")
                    return True
                else:
                    logger.info("⚠️ 用户认证状态不明确")
                    return False
            else:
                logger.error(f"❌ Hub 页面状态码: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"❌ 认证状态检查失败: {e}")
            return False
    def test_api_user_status(self):
        """测试用户状态 API"""
        logger.info("测试用户状态 API...")
        try:
            api_url = urljoin(self.base_url, f"/hub/api/users/{self.username}")
            response = self.session.get(api_url, timeout=10)
            
            if response.status_code == 200:
                user_info = response.json()
                logger.info(f"✅ 用户状态: {user_info.get('name', 'unknown')}")
                if user_info.get('server'):
                    logger.info("✅ 用户服务器信息正常")
                else:
                    logger.warning("⚠️ 用户服务器信息不完整")
                return True
            elif response.status_code == 401:
                logger.warning("⚠️ API 需要认证（用户未登录）")
                return False
            elif response.status_code == 403:
                logger.warning("⚠️ API 访问被拒绝（可能是权限问题）")
                return False
            else:
                logger.error(f"❌ API 状态码: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"❌ API 请求失败: {e}")
            return False
    
    def run_all_tests(self):
        """运行所有测试"""
        logger.info("开始 JupyterHub 功能测试...")
        logger.info("=" * 50)
        
        tests = [
            ("服务器状态", self.test_server_status),
            ("Hub API", self.test_hub_api),
            ("登录页面", self.test_login_page),
            ("用户登录", self.test_dummy_auth_login),
            ("认证状态", self.test_user_authentication_status),
             # ("服务器启动", self.test_user_server_spawn),
            ("Notebook 界面", self.test_notebook_interface),
            ("用户状态 API", self.test_api_user_status),
        ]
        
        results = {}
        login_success = False
        
        for test_name, test_func in tests:
            logger.info(f"\n--- 测试: {test_name} ---")
            try:
                # 如果登录失败，跳过需要认证的测试
                if test_name in ["服务器启动", "用户状态 API"] and not login_success:
                    logger.warning(f"⚠️ 跳过 {test_name} 测试（用户未登录）")
                    results[test_name] = False
                    continue
                
                result = test_func()
                results[test_name] = result
                
                # 记录登录状态
                if test_name == "用户登录" and result:
                    login_success = True
                elif test_name == "认证状态" and not result:
                    login_success = False
                    
            except Exception as e:
                logger.error(f"❌ 测试 {test_name} 出现异常: {e}")
                results[test_name] = False
            time.sleep(1)  # 测试间隔
        
        # 输出测试结果
        logger.info("\n" + "=" * 50)
        logger.info("测试结果汇总:")
        logger.info("=" * 50)
        
        passed = 0
        total = len(results)
        
        for test_name, result in results.items():
            status = "✅ 通过" if result else "❌ 失败"
            logger.info(f"{test_name}: {status}")
            if result:
                passed += 1
        
        logger.info("=" * 50)
        logger.info(f"总计: {passed}/{total} 项测试通过")
        
        # 提供故障排除建议
        if not login_success:
            logger.warning("\n🔧 故障排除建议:")
            logger.warning("1. 检查 JupyterHub 配置中的认证器设置")
            logger.warning("2. 确认 DummyAuthenticator 已正确配置")
            logger.warning("3. 检查 XSRF 保护设置")
            logger.warning("4. 查看 JupyterHub 日志获取详细错误信息")
        
        if passed == total:
            logger.info("🎉 所有测试通过！JupyterHub 运行正常")
            return True
        else:
            logger.warning(f"⚠️ {total - passed} 项测试失败，请检查配置")
            return False

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="JupyterHub 功能测试脚本")
    parser.add_argument("--url", default="http://localhost:8000", 
                       help="JupyterHub 服务地址 (默认: http://localhost:8000)")
    parser.add_argument("--username", default="testuser",
                       help="测试用户名 (默认: testuser)")
    
    args = parser.parse_args()
    
    tester = JupyterHubTester(args.url)
    tester.username = args.username
    
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()