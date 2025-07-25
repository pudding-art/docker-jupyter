#!/bin/bash

# JupyterHub 快速测试脚本

set -e

JUPYTERHUB_URL="${JUPYTERHUB_URL:-http://localhost:8000}"
TEST_USER="${TEST_USER:-testuser}"

echo "🚀 开始测试 JupyterHub: $JUPYTERHUB_URL"
echo "=" * 50

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 测试函数
test_endpoint() {
    local url=$1
    local name=$2
    local expected_code=${3:-200}
    
    echo -n "测试 $name... "
    
    if curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$url" | grep -q "$expected_code"; then
        echo -e "${GREEN}✅ 通过${NC}"
        return 0
    else
        echo -e "${RED}❌ 失败${NC}"
        return 1
    fi
}

# 检查 JupyterHub 是否运行
echo "🔍 检查服务状态..."
if ! curl -s --max-time 5 "$JUPYTERHUB_URL" > /dev/null; then
    echo -e "${RED}❌ 无法连接到 JupyterHub: $JUPYTERHUB_URL${NC}"
    echo "请确保 JupyterHub 正在运行并且地址正确"
    exit 1
fi

# 运行基本测试
echo -e "\n📋 运行基本测试..."

PASSED=0
TOTAL=0

# 测试主页
((TOTAL++))
if test_endpoint "$JUPYTERHUB_URL" "主页"; then
    ((PASSED++))
fi

# 测试登录页面
((TOTAL++))
if test_endpoint "$JUPYTERHUB_URL/hub/login" "登录页面"; then
    ((PASSED++))
fi

# 测试 API
((TOTAL++))
if test_endpoint "$JUPYTERHUB_URL/hub/api/" "Hub API" "40[13]"; then  # 401 或 403 都是正常的
    ((PASSED++))
fi

# 测试健康检查（如果有）
((TOTAL++))
if test_endpoint "$JUPYTERHUB_URL/hub/health" "健康检查" "20[0-9]"; then
    ((PASSED++))
fi

echo ""
echo "=" * 50
echo "测试结果: $PASSED/$TOTAL 项通过"

if [ $PASSED -eq $TOTAL ]; then
    echo -e "${GREEN}🎉 基本测试全部通过！${NC}"
    echo ""
    echo -e "${YELLOW}📝 手动测试建议:${NC}"
    echo "1. 打开浏览器访问: $JUPYTERHUB_URL"
    echo "2. 使用任意用户名登录（如: $TEST_USER）"
    echo "3. 检查是否能启动 Jupyter Notebook"
    echo "4. 测试创建和运行笔记本"
    exit 0
else
    echo -e "${RED}⚠️ 部分测试失败，请检查 JupyterHub 配置${NC}"
    exit 1
fi