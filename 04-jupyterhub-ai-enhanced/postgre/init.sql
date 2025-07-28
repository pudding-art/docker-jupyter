CREATE DATABASE jupyterhub_db;

\c jupyterhub_db

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- -- 创建 JupyterHub 数据库（如果不存在）
-- -- 注意：POSTGRES_DB 环境变量已经创建了主数据库，这里主要是确保配置正确

-- -- 设置数据库编码和排序规则
-- ALTER DATABASE jupyterhub SET timezone TO 'UTC';

-- -- 创建扩展（如果需要）
-- CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- -- 创建用户会话表的索引（JupyterHub 会自动创建表，这里预先优化）
-- -- 注意：这些表会由 JupyterHub 自动创建，这里只是预设一些优化

-- -- 日志记录
-- \echo 'PostgreSQL 数据库初始化完成'
-- \echo '数据库名称: jupyterhub'
-- \echo '字符编码: UTF-8'
-- \echo '时区: UTC'
-- \echo 'UUID 扩展: 已启用'
