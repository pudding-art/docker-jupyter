#!/usr/bin/env python3
"""
JupyterHub 问题诊断和修复建议脚本
专门用于诊断 XSRF、认证等常见问题
"""

import requests
import sys
import logging
from urllib.parse import urljoin
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class JupyterHubDiagnostic:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        
    def diagnose_xsrf_protection(self):
        """诊断 XSRF 保护状态"""
        logger.info("🔍 诊断 XSRF 保护状态...")
        
        try:
            login_url = urljoin(self.base_url, "/hub/login")
            response = self.session.get(login_url)
            
            if response.status_code != 200:
                logger.error(f"❌ 无法访问登录页面: {response.status_code}")
                return False
            
            # 检查页面中是否有 XSRF token
            xsrf_in_form = '_xsrf' in response.text
            xsrf_in_meta = 'name="_xsrf"' in response.text or 'name="csrf-token"' in response.text
            
            # 检查 cookies 中是否有 XSRF token
            xsrf_cookie = any(cookie.name == '_xsrf' for cookie in self.session.cookies)
            
            logger.info(f"📋 XSRF 检查结果:")
            logger.info(f"  - 表单中包含 _xsrf 字段: {'✅' if xsrf_in_form else '❌'}")
            logger.info(f"  - Meta 标签中包含 XSRF: {'✅' if xsrf_in_meta else '❌'}")
            logger.info(f"  - Cookies 中包含 _xsrf: {'✅' if xsrf_cookie else '❌'}")
            
            if xsrf_in_form or xsrf_in_meta or xsrf_cookie:
                logger.info("✅ XSRF 保护已启用")
                return True
            else:
                logger.warning("⚠️ 未检测到 XSRF 保护")
                return False
                
        except Exception as e:
            logger.error(f"❌ XSRF 检查失败: {e}")
            return False
    
    def test_login_without_xsrf(self):
        """测试不带 XSRF token 的登录"""
        logger.info("🧪 测试不带 XSRF token 的登录...")
        
        try:
            login_url = urljoin(self.base_url, "/hub/login")
            
            # 直接提交登录表单，不包含 XSRF token
            login_data = {
                "username": "testuser",
                "password": "dummy"
            }
            
            response = self.session.post(login_url, data=login_data, allow_redirects=False)
            
            if response.status_code == 403:
                logger.info("✅ 正常：服务器正确拒绝了没有 XSRF token 的请求")
                return True
            elif response.status_code in [200, 302]:
                logger.warning("⚠️ 异常：服务器接受了没有 XSRF token 的请求（XSRF 保护可能已禁用）")
                return False
            else:
                logger.error(f"❌ 意外的响应码: {response.status_code}")
                return False
                
        except Exception as e:
            logger.error(f"❌ 登录测试失败: {e}")
            return False
    
    def suggest_fixes(self):
        """提供修复建议"""
        logger.info("\n🔧 修复建议:")
        
        print("""
═══════════════════════════════════════════════════════════════
                         修复建议
═══════════════════════════════════════════════════════════════

🔐 方案1: 禁用 XSRF 保护（仅用于测试环境）
───────────────────────────────────────────────────────────────
在 jupyterhub_config.py 中添加：

    # 禁用 XSRF 保护（仅用于测试）
    c.JupyterHub.xsrf_cookies = False
    
⚠️  警告：这会降低安全性，仅建议在隔离的测试环境中使用

🔧 方案2: 更新测试脚本（推荐）
───────────────────────────────────────────────────────────────
测试脚本已更新以正确处理 XSRF token，请使用最新版本的测试脚本。

🌐 方案3: 配置反向代理
───────────────────────────────────────────────────────────────
如果使用 nginx 等反向代理，确保正确转发所有头信息：

    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $host;

📊 方案4: 检查认证器配置
───────────────────────────────────────────────────────────────
确认 DummyAuthenticator 配置正确：

    c.JupyterHub.authenticator_class = "jupyterhub.auth.DummyAuthenticator"
    c.Authenticator.allow_all = True

🐳 方案5: Docker 网络配置
───────────────────────────────────────────────────────────────
确保容器间网络通信正常：

    # 检查网络
    docker network ls
    docker network inspect jupyterhub-network
    
    # 确保容器在同一网络
    docker ps --format "table {{.Names}}\\t{{.Networks}}"

🔍 方案6: 调试模式
───────────────────────────────────────────────────────────────
启用 JupyterHub 调试模式获取更多信息：

    c.JupyterHub.log_level = 'DEBUG'
    c.Application.log_level = 'DEBUG'

═══════════════════════════════════════════════════════════════
""")
    
    def run_diagnosis(self):
        """运行完整诊断"""
        logger.info("🏥 开始 JupyterHub 问题诊断...")
        logger.info("=" * 60)
        
        # 检查服务器可达性
        try:
            response = self.session.get(self.base_url, timeout=10)
            if response.status_code == 200:
                logger.info("✅ JupyterHub 服务器可访问")
            else:
                logger.error(f"❌ 服务器返回状态码: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"❌ 无法连接到服务器: {e}")
            return False
        
        # 诊断 XSRF 保护
        xsrf_enabled = self.diagnose_xsrf_protection()
        
        # 测试无 XSRF token 的行为
        if xsrf_enabled:
            self.test_login_without_xsrf()
        
        # 提供修复建议
        self.suggest_fixes()
        
        return True

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="JupyterHub 问题诊断脚本")
    parser.add_argument("--url", default="http://localhost:8000", 
                       help="JupyterHub 服务地址")
    
    args = parser.parse_args()
    
    diagnostic = JupyterHubDiagnostic(args.url)
    diagnostic.run_diagnosis()

if __name__ == "__main__":
    main()