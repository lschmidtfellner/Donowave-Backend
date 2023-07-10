CREATE DATABASE campaigns;

CREATE USER campaigns_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE campaigns TO campaigns_admin;