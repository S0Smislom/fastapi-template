from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "abstractusermodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(120) NOT NULL,
    "password" VARCHAR(200) NOT NULL
);;
        CREATE TABLE IF NOT EXISTS "timestampmixin" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(120) NOT NULL,
    "password" VARCHAR(200) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_staff" BOOL NOT NULL  DEFAULT False,
    "is_superuser" BOOL NOT NULL  DEFAULT False,
    "is_active" BOOL NOT NULL  DEFAULT True
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "abstractusermodel";
        DROP TABLE IF EXISTS "timestampmixin";
        DROP TABLE IF EXISTS "user";"""
